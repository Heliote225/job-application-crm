<template>
  <div class="bg-white rounded-lg shadow p-2 min-h-[300px]">
    <h2 class="text-lg font-semibold mb-2">{{ title }}</h2>
    
    <draggable
      v-model="columnItems"
      group="candidatures"
      item-key="id"
      @end="onDrop"
    >
      <template #item="{ element }">
        <div
          @click="openDetails(element)"
          class="bg-gray-100 p-2 mb-2 rounded shadow-sm cursor-pointer hover:bg-gray-200 transition"
        >
          <p class="font-bold">{{ element.job_title }}</p>
          <p class="text-sm">{{ element.company }}</p>
        </div>
      </template>
    </draggable>

    <!-- Modal de détails -->
    <ApplicationModal
      v-if="selectedApp"
      :app="selectedApp"
      :visible="!!selectedApp"
      @close="selectedApp = null"
      @delete="handleDelete"
      @edit="startEdit"
    />

    <!-- Modal d'édition -->
    <EditApplicationModal
      :visible="!!editingApp"
      :app="editingApp"
      @close="editingApp = null"
      @updated="fetchItems"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, watch, inject } from 'vue'
import draggable from 'vuedraggable'
import api from '../api'
import ApplicationModal from './ApplicationModal.vue'
import EditApplicationModal from './EditApplicationModal.vue'

const props = defineProps(['title', 'status'])

const columnItems = ref([])
const selectedApp = ref(null)
const editingApp = ref(null)

// Toast global injecté depuis App.vue
const showToast = inject('showToast')

onMounted(fetchItems)
watch(() => props.status, fetchItems)

async function fetchItems() {
  const all = await api.getApplications()
  columnItems.value = all.filter(app => app.status === props.status)
}

async function onDrop(evt) {
  const movedItem = columnItems.value[evt.newIndex]
  if (movedItem && movedItem.status !== props.status) {
    movedItem.status = props.status
    await api.updateApplication(movedItem.id, { status: props.status })
    showToast('Statut mis à jour', 'success')
  }
}

function openDetails(app) {
  selectedApp.value = app
}

async function handleDelete(id) {
  await api.deleteApplication(id)
  showToast('Candidature supprimée', 'success')
  fetchItems()
}

function startEdit(app) {
  editingApp.value = app
  console.log('Editing app:', app)
}
</script>