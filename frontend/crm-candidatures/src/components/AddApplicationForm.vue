<template>
    <form @submit.prevent="submitForm" class="bg-white p-4 rounded shadow mb-4 grid gap-2">
      <h2 class="text-lg font-semibold">Nouvelle candidature</h2>
  
      <input v-model="form.job_title" type="text" placeholder="Poste" class="border p-2 rounded" required />
      <input v-model="form.company" type="text" placeholder="Entreprise" class="border p-2 rounded" required />
      <input v-model="form.link" type="url" placeholder="Lien de l'offre" class="border p-2 rounded" />
      <input v-model="form.contact_email" type="email" placeholder="Email contact (optionnel)" class="border p-2 rounded" />
      <textarea v-model="form.notes" placeholder="Notes" class="border p-2 rounded"></textarea>
  
      <select v-model="form.status" class="border p-2 rounded">
        <option value="todo">À postuler</option>
        <option value="applied">Candidature envoyée</option>
        <option value="interview">Entretien/Test</option>
        <option value="waiting">En attente</option>
        <option value="rejected">Refus</option>
        <option value="offer">Offre reçue</option>
      </select>
  
      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        Ajouter
      </button>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import api from '../api'
  
  const emit = defineEmits(['refresh'])
  
  const form = ref({
    job_title: '',
    company: '',
    link: '',
    contact_email: '',
    notes: '',
    status: 'todo',
  })
  
  async function submitForm() {
    await api.createApplication(form.value)
    emit('refresh') // pour dire au parent de recharger les colonnes
    Object.keys(form.value).forEach(key => form.value[key] = key === 'status' ? 'todo' : '') // reset
  }
  </script>