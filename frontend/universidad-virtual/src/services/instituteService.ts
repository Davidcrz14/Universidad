import axios from 'axios';
import { Institute, Publication } from '../interfaces/institute';

const API_URL = 'http://localhost:8000/api';

export const instituteService = {
    getAllInstitutes: async (): Promise<Institute[]> => {
        const response = await axios.get(`${API_URL}/institutes/`);
        return response.data;
    },

    getInstituteById: async (id: number): Promise<Institute> => {
        const response = await axios.get(`${API_URL}/institutes/${id}/`);
        return response.data;
    },

    getPublications: async (instituteId?: number): Promise<Publication[]> => {
        const url = instituteId
            ? `${API_URL}/publications/?institute=${instituteId}`
            : `${API_URL}/publications/`;
        const response = await axios.get(url);
        return response.data;
    }
};
