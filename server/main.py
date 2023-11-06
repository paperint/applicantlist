from fastapi import FastAPI,Depends, HTTPException, Response,Depends
from pydantic import BaseModel,Field
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import csv
import io

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://yourfrontendapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Applicant(BaseModel):
    firstname:str = Field(min_length=1)
    lastname:str = Field(min_length=1)
    address:str = Field(min_length=1)
    expected_salary:int = Field(gt=0)
    other:str

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get All Application
@app.get("/applicant")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Applicant).all()

# Get 1 Application
@app.get("/applicant/{applicant_id}")
def get_application (applicant_id:int, db:Session = Depends(get_db)):
    applicant_model = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    
    if applicant_model is None:
        raise HTTPException(
            status_code = 404,
            detail= f"ID {applicant_id} : Does not exist."
        )
    
    return applicant_model

# Create
@app.post("/create")
def create_application(applicant: Applicant,db: Session = Depends(get_db)):
    applicant_model = models.Applicant()
    applicant_model.firstname = applicant.firstname
    applicant_model.lastname = applicant.lastname
    applicant_model.address = applicant.address
    applicant_model.expected_salary = applicant.expected_salary
    applicant_model.other = applicant.other
    
    db.add(applicant_model)
    db.commit()

# Edit  
@app.put("/applicant/{applicant_id}")
def update_application(applicant_id:int, applicant:Applicant,db:Session = Depends(get_db)):
    applicant_model = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    
    if applicant_model is None:
        raise HTTPException(status_code=404,detail=f"{applicant_id} : Does not exit.")
    
    applicant_model.firstname = applicant.firstname
    applicant_model.lastname = applicant.lastname
    applicant_model.address = applicant.address
    applicant_model.expected_salary = applicant.expected_salary
    applicant_model.other = applicant.other
    
    db.add(applicant_model)
    db.commit()
    
    return applicant

# Delete
@app.delete("/applicant/{applicant_id}")
def delete_application (applicant_id:int, db:Session = Depends(get_db)):
    applicant_model = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    
    if applicant_model is None:
        raise HTTPException(
            status_code = 404,
            detail= f"ID {applicant_id} : Does not exist."
        )
    
    db.query(models.Applicant).filter(models.Applicant.id == applicant_id).delete()
    db.commit()

# Export all applications
@app.get("/export/applicants")
def export_applicants(db: Session = Depends(get_db)):
    applicant_model = db.query(models.Applicant).all()

    output = io.StringIO()
    writer = csv.writer(output)

    # Header
    writer.writerow(["id", "firstname", "lastname", "address", "expected_salary", "other"])

    # Loop all data
    for applicant in applicant_model:
        writer.writerow([applicant.id, applicant.firstname, applicant.lastname, applicant.address, applicant.expected_salary, applicant.other])

    csv_data = output.getvalue()

    response = Response(content=csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=applicants.csv"
    response.headers["Content-Type"] = "text/csv"

    return response

# Export 1 application
@app.get("/export/applicants/{applicant_id}")
def export_applicants_id(applicant_id:int, db:Session = Depends(get_db)):
    applicant_model = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    
    if applicant_model is None:
        raise HTTPException(
            status_code = 404,
            detail= f"ID {applicant_id} : Does not exist."
        )

    output = io.StringIO()
    writer = csv.writer(output)

    # Header
    writer.writerow(["id", "firstname", "lastname", "address", "expected_salary", "other"])
    writer.writerow([applicant_model.id, applicant_model.firstname, applicant_model.lastname, applicant_model.address, applicant_model.expected_salary, applicant_model.other])

    csv_data = output.getvalue()

    response = Response(content=csv_data)
    response.headers["Content-Disposition"] = f"attachment; filename={applicant_model.firstname}.csv"
    response.headers["Content-Type"] = "text/csv"

    return response