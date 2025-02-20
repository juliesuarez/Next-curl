# Architecture Overview

The Next-curl project is organized as a monorepo with the following 
components:

1. **Frontend:** Next.js with PWA support, built using React.
2. **Backend API:** Django-based service for core RESTful endpoints.
3. **Realtime Service:** Node.js server handling WebSocket communications.
4. **AI/VR Services:** 
   - **AI Service:** Python-based module for adaptive learning.
   - **VR Service:** Node.js module for immersive simulations.
5. **Databases:** Configuration for PostgreSQL, MongoDB, and Redis.

Each component is isolated in its own folder for clarity and scalability.
