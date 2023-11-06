import { defineStore } from "pinia";

export const useEventStore = defineStore("event", {
  state: () => ({
    modalOpen: false,
    pageAction: "view",
  }),
  actions: {
    closeModal() {
      this.modalOpen = false;
    },
    viewModal() {
      this.pageAction = "view";
      this.modalOpen = true;
    },
    createModal() {
      this.pageAction = "create";
      this.modalOpen = true;
    },
    editModal() {
      this.pageAction = "edit";
      this.modalOpen = true;
    },
  },
});
