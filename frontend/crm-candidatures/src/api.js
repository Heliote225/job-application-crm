import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
})

export default {
  async getApplications() {
    const res = await api.get('applications/')
    return res.data
  },

  async updateApplication(id, data) {
    return await api.patch(`applications/${id}/`, data)
  },

  async createApplication(data) {
    return await api.post('applications/', data)
  },

  async updateApplication(id, data) {
    return await api.patch(`applications/${id}/`, data)
  },

  async deleteApplication(id) {
    return await api.delete(`applications/${id}/`)
  },
}