# Developer Guide

## Project Structure

- **frontend/**: Next.js application with PWA support.
  - Contains React components, pages, styles, and utility functions.
- **backend/api/**: Django REST API service.
  - Contains Django project files and a basic app structure.
- **backend/realtime/**: Node.js service for real-time communication.
  - A simple WebSocket server.
- **backend/ai_vr/**: Services for AI processing and VR simulations.
  - AI service is written in Python.
  - VR service is written in Node.js.
- **databases/**: Configuration files and instructions for PostgreSQL, 
MongoDB, and Redis.
- **docs/**: Project documentation including architecture, getting 
started, and FAQs.
- **.github/**: GitHub-specific configurations including issue/P.R. 
templates and CI workflows.

## Coding Standards

- **Frontend:** Use React and Next.js best practices. Follow the style 
guides provided in the documentation.
- **Backend (Django):** Follow standard Django conventions and PEP8 for 
Python code.
- **Realtime & VR:** Adhere to Node.js coding standards and best 
practices.
- **Testing:** Write unit tests for new features. Frontend tests run with 
Jest.

## Docker & Deployment

Each service includes its own Dockerfile. Use Docker Compose to run the 
entire stack locally. Review the Dockerfiles for details on how each 
service is built.
