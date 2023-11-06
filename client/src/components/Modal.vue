<script setup>
import { useEventStore } from "../stores/event";
import { useApplicationStore } from "../stores/application";
import CandidateDetail from "./CandidateDetail.vue";
import CreateForm from "./CreateForm.vue";
import EditForm from "./EditForm.vue";

const eventStore = useEventStore();
const applicationStore = useApplicationStore();
</script>

<template>
  <dialog class="modal" :class="eventStore.modalOpen ? 'modal-open' : ''">
    <div class="modal-box">
      <button
        @click="eventStore.closeModal()"
        class="absolute btn btn-sm btn-circle btn-ghost right-2 top-2"
      >
        ✕
      </button>
      <CandidateDetail v-if="eventStore.pageAction === 'view'" />
      <CreateForm v-if="eventStore.pageAction === 'create'" />
      <EditForm v-if="eventStore.pageAction === 'edit'" />
    </div>
  </dialog>
</template>
