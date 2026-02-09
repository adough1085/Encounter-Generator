import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import basicSsl from '@vitejs/plugin-basic-ssl';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), basicSsl()],
  build: {
    outDir: 'build',
    emptyOutDir: true,
  },
  server: {
    //host: '0.0.0.0', // This makes Vite listen on all network interfaces
    host: '0.0.0.0', // 
    port: 5173, // Optional: specify the port (default is 5173)
  },
})
