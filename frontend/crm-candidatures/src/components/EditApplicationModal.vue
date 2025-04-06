<template>
    <div v-if="visible" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
      <div class="bg-white rounded-lg p-6 w-full max-w-md shadow-lg relative">
        <button class="absolute top-2 right-3 text-gray-500" @click="handleClose">✖</button>
  
        <h2 class="text-lg font-semibold mb-4">Modifier la candidature</h2>
  
        <form @submit.prevent="submitForm" class="space-y-3 text-sm">
          <input v-model="form.job_title" type="text" placeholder="Poste" class="w-full border p-2 rounded" required />
          <input v-model="form.company" type="text" placeholder="Entreprise" class="w-full border p-2 rounded" required />
          <input v-model="form.link" type="url" placeholder="Lien" class="w-full border p-2 rounded" />
          <input v-model="form.contact_email" type="email" placeholder="Email" class="w-full border p-2 rounded" />
          <textarea v-model="form.notes" placeholder="Notes" class="w-full border p-2 rounded"></textarea>
  
          <select v-model="form.status" class="w-full border p-2 rounded">
            <option value="todo">À postuler</option>
            <option value="applied">Candidature envoyée</option>
            <option value="interview">Entretien/Test</option>
            <option value="waiting">En attente</option>
            <option value="rejected">Refus</option>
            <option value="offer">Offre reçue</option>
          </select>
  
          <div class="flex justify-end gap-2 pt-2">
            <button type="button" @click="handleClose" class="bg-gray-300 text-gray-800 px-4 py-2 rounded hover:bg-gray-400">
              Annuler
            </button>
            <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
              Enregistrer
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive, watchEffect } from 'vue'
  import api from '../api'
  
  const props = defineProps({
    visible: Boolean,
    app: Object
  })
  
  const emit = defineEmits(['close', 'updated'])
  
  const form = reactive({
    job_title: '',
    company: '',
    link: '',
    contact_email: '',
    notes: '',
    status: 'todo',
  })
  
  function resetForm() {
    Object.assign(form, {
      job_title: '',
      company: '',
      link: '',
      contact_email: '',
      notes: '',
      status: 'todo',
    })
  }
  
  // ✅ Pré-remplissage fiable dès que props.app est dispo
  watchEffect(() => {
    if (props.visible && props.app) {
      Object.assign(form, {
        job_title: props.app.job_title || '',
        company: props.app.company || '',
        link: props.app.link || '',
        contact_email: props.app.contact_email || '',
        notes: props.app.notes || 'This is ok',
        status: props.app.status || 'todo',
      })
    }
  })
  
  function handleClose() {
    resetForm()
    emit('close')
  }
  
  async function submitForm() {
    await api.updateApplication(props.app.id, { ...form })
    emit('updated')
    handleClose()
  }
  </script>