<script setup>
import { reactive, watchEffect } from "vue";
import { useApplicationStore } from "../stores/application";

const applicationStore = useApplicationStore();

const formData = reactive({});

const handleSubmit = () => {
  applicationStore.editCandidate(formData);
};

watchEffect(() => {
  const data = { ...applicationStore.person };
  Object.assign(formData, data);
});
</script>

<template>
  <article>
    <form class="flex flex-col gap-4" @submit.prevent="handleSubmit">
      <div>
        <h4 class="mb-2 font-bold tracking-wider">Firstname:</h4>
        <input
          type="text"
          placeholder="Surasak"
          class="w-full input input-bordered"
          v-model="formData.firstname"
        />
      </div>
      <div>
        <h4 class="mb-2 font-bold tracking-wider">Lastname:</h4>
        <input
          type="text"
          placeholder="Montri"
          class="w-full input input-bordered"
          v-model="formData.lastname"
        />
      </div>
      <div>
        <h4 class="mb-2 font-bold tracking-wider">Address:</h4>
        <input
          type="text"
          placeholder="38 Hogward street"
          class="w-full input input-bordered"
          v-model="formData.address"
        />
      </div>
      <div>
        <h4 class="mb-2 font-bold tracking-wider">Expected Salary:</h4>
        <input
          type="number"
          placeholder="123456"
          class="w-full input input-bordered"
          v-model="formData.expected_salary"
        />
      </div>
      <div>
        <h4 class="mb-2 font-bold tracking-wider">Others:</h4>
        <textarea
          class="w-full textarea textarea-bordered"
          placeholder="Bio"
          v-model="formData.other"
        ></textarea>
      </div>
      <div>
        <button type="submit" class="w-full btn btn-neutral">Edit</button>
      </div>
    </form>
  </article>
</template>
