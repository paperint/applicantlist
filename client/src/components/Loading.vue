<script setup>
import { useApplicationStore } from "../stores/application";
const applicationStore = useApplicationStore();
</script>
<template>
  <div
    v-if="applicationStore.isLoading"
    class="absolute inset-0 top-0 left-0 z-[1000] inline-flex items-center justify-center w-full min-h-screen gap-4 bg-opacity-50 bg-neutral"
  >
    <span class="loading loading-spinner loading-lg"></span>
    <span class="text-xl tracking-wider">Loading</span>
    <span class="loading loading-dots"></span>
  </div>
</template>
