import axios from 'axios';

const api = axios.create({
  baseURL: 'https://rrr-mobile.binarywavesolutions.com',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

export default api;
