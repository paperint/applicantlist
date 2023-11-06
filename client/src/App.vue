<script setup>
import { RouterLink, RouterView } from "vue-router";
import Loading from "./components/Loading.vue";
</script>

<template>
  <main class="flex flex-col items-center justify-center w-full min-h-screen">
    <Loading />
    <RouterView />
  </main>
</template>
