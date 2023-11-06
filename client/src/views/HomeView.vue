<script setup>
import { onMounted } from "vue";
import Table from "../components/Table.vue";
import Modal from "../components/Modal.vue";
import { useApplicationStore } from "../stores/application";
import { useEventStore } from "../stores/event";

const applicationStore = useApplicationStore();
const eventStore = useEventStore();

onMounted(async () => {
  try {
    await applicationStore.getApplication();
  } catch (error) {
    console.log("error", error);
  }
});
</script>

<template>
  <section class="flex flex-col items-center w-full gap-4 mx-auto max-w-7xl">
    <h1 class="text-2xl font-bold tracking-wider">Job Application List</h1>
    <div class="w-full max-w-5xl mx-auto text-right">
      <button
        class="mr-4 btn btn-ghost btn-link text-accent btn-xs"
        @click="applicationStore.exportCSV()"
      >
        Export to csv
      </button>
      <button class="px-12 btn btn-primary" @click="eventStore.createModal">
        Create
      </button>
    </div>
    <Table :list="applicationStore.list" />
    <Modal />
  </section>
</template>
