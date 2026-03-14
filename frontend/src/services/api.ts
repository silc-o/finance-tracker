import axios from "axios"
// * axios handles all the HTTP requests to the backend API, including authentication and transaction management.

const BASE_URL = 'http://localhost:8000'

const api = axios.create({
  baseURL: BASE_URL,
})

// * intercepts every request
// *
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`
  }
  return config
})

export const authService = {
    login: async (username: string, password: string) => {
        const formData = new FormData()
        formData.append('username', username)
        formData.append('password', password)
        const response = await api.post('/auth/login', formData)
        return response.data
    },

    register: async (username: string, email: string, password: string) => {
        const response = await api.post('/auth/register', {
            email,
            username,
            password,
        })
        return response.data
    },
}

export const transactionService = {
    getAll: async () => {
        const response = await api.get('/transactions')
        return response.data
    },

    create: async (data: { amount: number; description?: string; type: "income" | "expense" }) => {
        const response = await api.post('/transactions/', data)
        return response.data
    },

    delete: async (id: number) => {
        const response = await api.delete(`/transactions/${id}`)
        return response.data
    },
}

export default api