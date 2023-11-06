<template>
  <div class="drawer drawer-open">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
    <div class="flex flex-col items-center justify-center drawer-content">
      <!-- Page content here -->
      <slot></slot>
    </div>
    <div class="drawer-side">
      <ul class="min-h-full p-4 menu w-80 bg-base-200 text-base-content">
        <!-- Sidebar content here -->
        <h2 class="mb-12 text-4xl font-bold tracking-wider text-center">
          Dashboard
        </h2>
        <li class="w-full text-lg">
          <a class="active">Job application list</a>
        </li>
      </ul>
    </div>
  </div>
</template>
