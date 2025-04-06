<template>
    <div v-if="visible" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div class="bg-white rounded-lg p-6 w-full max-w-md shadow-lg relative">
        <button class="absolute top-2 right-3 text-gray-500" @click="close">✖</button>
        
        <h2 class="text-xl font-semibold mb-2">Détails de la candidature</h2>
  
        <div class="text-sm space-y-2 mb-4">
          <p><strong>Poste :</strong> {{ app.job_title }}</p>
          <p><strong>Entreprise :</strong> {{ app.company }}</p>
          <p><strong>Statut :</strong> {{ app.status }}</p>
          <p><strong>Contact :</strong> {{ app.contact_email || '—' }}</p>
          <p><strong>Lien :</strong> <a :href="app.link" target="_blank" class="text-blue-600 underline">{{ app.link }}</a></p>
          <p><strong>Notes :</strong> {{ app.notes || '—' }}</p>
        </div>
  
        <div class="flex justify-end gap-2">
          <button @click="edit" class="bg-yellow-500 text-white px-3 py-1 rounded">Modifier</button>
          <button @click="deleteItem" class="bg-red-600 text-white px-3 py-1 rounded">Supprimer</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps(['app', 'visible'])
  const emit = defineEmits(['close', 'delete', 'edit'])
  
  function close() {
    emit('close')
  }
  
  function deleteItem() {
    if (confirm('Supprimer cette candidature ?')) {
      emit('delete', props.app.id)
      close()
    }
  }
  
  function edit() {
    emit('edit', props.app)
    close()
  }
  </script>