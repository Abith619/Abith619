import axios from 'axios';

const ODOO_URL = 'https://rrr-mobile.binarywavesolutions.com';

const api = axios.create({
  baseURL: ODOO_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getProducts = async () => {
  try {
    const response = await api.get('/api/products');
    return response.data;
  } catch (error) {
    console.error('Error fetching products:', error);
    throw error;
  }
};

export default api;
