import axios from 'axios';

// Create an instance of axios with the base URL
const api = axios.create({
    baseURL: "https://3.137.101.123" // baseURL required for deployment
    //baseURL: "http://localhost:8000" // baseURL required for testing
})

// Export the Axios instance
export default api;