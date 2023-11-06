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
    formatNumber(amount) {
      if (amount == null) {
        return "Invalid amount";
      }

      const newAmount =
        typeof amount === "string" ? parseFloat(amount) : amount;

      if (isNaN(newAmount)) {
        return "Invalid input";
      }

      const formattedAmount = newAmount.toLocaleString("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2,
      });

      return formattedAmount;
    },
  },
});
