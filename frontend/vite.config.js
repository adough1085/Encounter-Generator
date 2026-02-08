import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import basicSsl from '@vitejs/plugin-basic-ssl';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), basicSsl()],
  server: {
    host: '0.0.0.0', // This makes Vite listen on all network interfaces
    port: 5173, // Optional: specify the port (default is 5173)
    // Optional: for HMR to work correctly in some Docker/WSL setups
    hmr: {
      host: 'localhost', 
      protocol: 'ws',
    },
  },
})
