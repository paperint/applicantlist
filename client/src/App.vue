<script setup>
import { RouterView } from "vue-router";
import Loading from "./components/Loading.vue";
import DashboardLayout from "./layout/DashboardLayout.vue";
</script>

<template>
  <main class="flex flex-col items-center justify-center w-full min-h-screen">
    <Loading />
    <DashboardLayout>
      <RouterView />
    </DashboardLayout>
  </main>
</template>
