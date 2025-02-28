import axios from 'axios';

// URL del backend
const API_URL = "http://127.0.0.1:8000/api";

export const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});