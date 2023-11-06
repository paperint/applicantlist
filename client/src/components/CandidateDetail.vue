<script setup>
import { useApplicationStore } from "../stores/application";
import { useEventStore } from "../stores/event";

const applicationStore = useApplicationStore();
const eventStore = useEventStore();
</script>

<template>
  <article class="flex flex-col gap-4">
    <div>
      <h4 class="font-bold tracking-wider">Firstname:</h4>
      <p class="font-light">{{ applicationStore.person.firstname }}</p>
    </div>
    <div>
      <h4 class="font-bold tracking-wider">Lastname:</h4>
      <p class="font-light">{{ applicationStore.person.lastname }}</p>
    </div>
    <div>
      <h4 class="font-bold tracking-wider">Address:</h4>
      <p class="font-light">{{ applicationStore.person.address }}</p>
    </div>
    <div>
      <h4 class="font-bold tracking-wider">Expected Salary:</h4>
      <p class="font-light">
        {{ eventStore.formatNumber(applicationStore.person.expected_salary) }}
      </p>
    </div>
    <div class="font-bold tracking-wider">
      <h4>Others:</h4>
      <p class="font-light">{{ applicationStore.person.other }}</p>
    </div>
    <div>
      <button
        class="p-0 btn-link text-primary underline-offset-2"
        @click="applicationStore.exportCSVperson(applicationStore.person.id)"
      >
        Export to csv
      </button>
    </div>
  </article>
</template>
