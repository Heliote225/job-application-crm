<template>
    <div class="p-4">
      <!-- Formulaire d'ajout de candidature -->
      <AddApplicationForm @refresh="reloadKey++" />
  
      <!-- Colonnes du kanban -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <KanbanColumn
          v-for="column in columns"
          :key="column.status + '-' + reloadKey"
          :title="column.title"
          :status="column.status"
        />
      </div>
  
      <!-- Toast global -->
      <Toast v-if="toast.message" :message="toast.message" :type="toast.type" />
    </div>
  </template>
  
  <script setup>
  import { ref, provide } from 'vue'
  import AddApplicationForm from './components/AddApplicationForm.vue'
  import KanbanColumn from './components/KanbanColumn.vue'
  import Toast from './components/Toast.vue'
  
  // Déclencheur de reload (quand on ajoute/modifie)
  const reloadKey = ref(0)
  
  // Colonnes de statut
  const columns = [
    { title: 'À postuler', status: 'todo' },
    { title: 'Candidature envoyée', status: 'applied' },
    { title: 'Entretien / Test', status: 'interview' },
    { title: 'En attente de réponse', status: 'waiting' },
    { title: 'Refus', status: 'rejected' },
    { title: 'Offre reçue', status: 'offer' },
  ]
  
  // Toast global
  const toast = ref({ message: '', type: 'success' })
  
  function showToast(message, type = 'success') {
    toast.value = { message, type }
    setTimeout(() => (toast.value.message = ''), 3000)
  }
  
  provide('showToast', showToast)
  </script>