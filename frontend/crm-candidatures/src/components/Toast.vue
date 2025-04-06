<template>
    <transition name="fade">
      <div
        v-if="visible"
        :class="[
          'fixed bottom-4 right-4 text-white px-4 py-2 rounded shadow-lg z-50',
          bgColor
        ]"
      >
        {{ message }}
      </div>
    </transition>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  
  const props = defineProps({
    message: String,
    type: {
      type: String,
      default: 'success', // success, error, info, warning
    }
  })
  
  const visible = ref(true)
  
  const bgColor = computed(() => {
    return {
      success: 'bg-green-600',
      error: 'bg-red-600',
      info: 'bg-blue-600',
      warning: 'bg-yellow-600'
    }[props.type] || 'bg-gray-800'
  })
  
  setTimeout(() => {
    visible.value = false
  }, 3000)
  </script>
  
  <style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.3s;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  </style>