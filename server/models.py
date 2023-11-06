from sqlalchemy import Column,Integer,String
from database import Base

class Applicant(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    expected_salary = Column(Integer)
    other = Column(String)