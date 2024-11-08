import axios from 'axios';
import { LoginCredentials, RegisterCredentials, AuthResponse } from '../interfaces/auth';

const API_URL = 'http://localhost:8000/api/auth';

// Configuración global de axios
axios.defaults.headers.post['Content-Type'] = 'application/json';

export const authService = {
    login: async (credentials: LoginCredentials): Promise<AuthResponse> => {
        try {
            const response = await axios.post(`${API_URL}/login/`, credentials);
            if (response.data.access) {
                localStorage.setItem('token', response.data.access);
                localStorage.setItem('refreshToken', response.data.refresh);
            }
            return response.data;
        } catch (error: any) {
            if (error.response) {
                throw new Error(error.response.data.error || 'Error en la autenticación');
            }
            throw new Error('Error de conexión con el servidor');
        }
    },

    register: async (userData: Omit<RegisterCredentials, 'role'>): Promise<AuthResponse> => {
        try {
            // Siempre establecemos el rol como 'student'
            const credentials: RegisterCredentials = {
                ...userData,
                role: 'student'
            };

            const response = await axios.post(`${API_URL}/register/`, credentials);
            if (response.data.access) {
                localStorage.setItem('token', response.data.access);
                localStorage.setItem('refreshToken', response.data.refresh);
            }
            return response.data;
        } catch (error: any) {
            if (error.response) {
                throw new Error(error.response.data.error || 'Error en el registro');
            }
            throw new Error('Error de conexión con el servidor');
        }
    },

    logout: async (): Promise<void> => {
        try {
            const refreshToken = localStorage.getItem('refreshToken');
            if (refreshToken) {
                await axios.post(`${API_URL}/logout/`, { refresh: refreshToken });
            }
        } catch (error) {
            console.error('Error en logout:', error);
        } finally {
            localStorage.removeItem('token');
            localStorage.removeItem('refreshToken');
        }
    },

    refreshToken: async (): Promise<string> => {
        const refreshToken = localStorage.getItem('refreshToken');
        if (!refreshToken) throw new Error('No refresh token available');

        try {
            const response = await axios.post(`${API_URL}/refresh/`, {
                refresh: refreshToken
            });
            localStorage.setItem('token', response.data.access);
            return response.data.access;
        } catch (error) {
            localStorage.removeItem('token');
            localStorage.removeItem('refreshToken');
            throw error;
        }
    }
};
