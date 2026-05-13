import axios from 'axios'

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
        'Content-Type': 'application/json'
    }
})

export const login = async (data: {email: string; password:string;}) => {
    return api.post('/api/users/login/', data)
}

export const register = async (data: {email: string; password:string; full_name:string;}) => {
    return api.post('/api/users/register/', data)
}

export const getBooks = async() => api.get('api/books/')