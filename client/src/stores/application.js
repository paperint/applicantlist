import axios from "axios";
import { defineStore } from "pinia";
import { useEventStore } from "./event";

const API = "http://127.0.0.1:8000";

export const useApplicationStore = defineStore("application", {
  state: () => ({
    list: [],
    person: {},
    isLoading: false,
  }),
  actions: {
    async getApplication() {
      try {
        this.isLoading = true;
        const response = await axios.get(`${API}/applicant`);
        this.list = response.data;
        this.isLoading = false;
      } catch (error) {
        console.log(error);
      }
    },
    async viewByPerson(candidateId, action) {
      const eventStore = useEventStore();
      try {
        this.isLoading = true;
        const response = await axios.get(`${API}/applicant/${candidateId}`);
        this.person = response.data;
        if (action === "view") {
          eventStore.viewModal();
          this.isLoading = false;
        } else if (action === "edit") {
          eventStore.editModal();
          this.isLoading = false;
        }
      } catch (error) {
        console.log("error", error);
      }
    },
    async createCandidate(data) {
      const eventStore = useEventStore();
      try {
        this.isLoading = true;
        await axios.post(`${API}/create`, data);
        await this.getApplication();
        eventStore.closeModal();
        this.isLoading = false;
      } catch (error) {
        console.log("error", error);
      }
    },
    async editCandidate(data) {
      const eventStore = useEventStore();
      try {
        this.isLoading = true;
        await axios.put(`${API}/applicant/${data.id}`, data);
        await this.getApplication();
        eventStore.closeModal();
        this.isLoading = false;
      } catch (error) {
        console.log("error", error);
      }
    },
    async deleteCandidate(candidateId) {
      try {
        this.isLoading = true;
        await axios.delete(`${API}/applicant/${candidateId}`);
        await this.getApplication();
        this.isLoading = false;
      } catch (error) {
        console.log("error", error);
      }
    },
    async exportCSV() {
      try {
        this.isLoading = true;
        const a = document.createElement("a");
        a.href = `${API}/export/applicants`;
        a.click();
        this.isLoading = false;
      } catch (error) {
        console.log("error", error);
      }
    },
    async exportCSVperson(id) {
      try {
        this.isLoading = true;
        const a = document.createElement("a");
        a.href = `${API}/export/applicants/${id}`;
        a.click();
        this.isLoading = false;
      } catch (error) {
        console.log("error", error);
      }
    },
  },
});
