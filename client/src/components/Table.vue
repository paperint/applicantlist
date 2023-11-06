<script setup>
import { defineProps, computed, ref } from "vue";
import { useEventStore } from "../stores/event";
import { useApplicationStore } from "../stores/application";

defineProps({
  list: Array,
});

const key = ref([
  "firstname",
  "lastname",
  "address",
  "expected_salary",
  "other",
]);

const applicationStore = useApplicationStore();
const eventStore = useEventStore();

const firstLetterUppercase = (name) => {
  const splitName = name.split("_");
  const newName = splitName
    .map((item) => item.charAt(0).toUpperCase() + item.slice(1))
    .join(" ");
  return newName;
};

const handleView = (id) => {
  applicationStore.viewByPerson(id, "view");
};
const handleEdit = (id) => {
  applicationStore.viewByPerson(id, "edit");
};
const handleDelete = (id) => {
  applicationStore.deleteCandidate(id);
};
</script>

<template>
  <div
    class="w-full max-w-5xl mx-auto overflow-x-auto h-[555px] scrollbar-hide"
  >
    <table class="table bg-neutral table-pin-rows">
      <thead>
        <tr>
          <th></th>
          <th v-for="item in key">{{ firstLetterUppercase(item) }}</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(item, index) in list"
          class="cursor-pointer hover"
          @click="handleView(item.id)"
        >
          <th>{{ index + 1 }}</th>
          <td>{{ firstLetterUppercase(item.firstname) }}</td>
          <td>{{ firstLetterUppercase(item.lastname) }}</td>
          <td>{{ item.address }}</td>
          <td>{{ eventStore.formatNumber(item.expected_salary) }}</td>
          <td>{{ item.other }}</td>
          <td>
            <button
              class="btn btn-active btn-secondary btn-sm hover:bg-primary"
              @click="handleEdit(item.id)"
              @click.stop
            >
              Edit
            </button>
            <button
              class="ml-4 btn btn-outline btn-error btn-sm"
              @click="handleDelete(item.id)"
              @click.stop
            >
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  /* display: none; */
  width: 2px;
}

.scrollbar-hide::-webkit-scrollbar-thumb {
  background: #61848c;
  border-radius: 50px;
}
</style>
