import axios from 'axios';

// Create an instance of axios with a default base URL
const instance = axios.create({
  baseURL: 'http://localhost:8000/stats/api/', // Your base URL here
});

export default instance;