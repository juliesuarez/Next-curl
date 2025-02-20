# Getting Started

## Prerequisites
- Docker & Docker Compose installed
- (Optional) Node.js and npm for local development without Docker
- (Optional) Python for running Django locally

## Using Docker Compose
1. Clone the repository.
2. Navigate to the project directory.
3. Run the following command to build and start all services:
   \`\`\`
   docker-compose up --build
   \`\`\`
4. Access the services:
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - API: [http://localhost:8000](http://localhost:8000)
   - Realtime: WebSocket at ws://localhost:4000
   - AI Service: [http://localhost:5000](http://localhost:5000)
   - VR Service: [http://localhost:5001](http://localhost:5001)

## Running Services Individually
- **Frontend:** 
  \`\`\`
  cd frontend
  npm install
  npm run dev
  \`\`\`
- **API:** 
  \`\`\`
  cd backend/api
  pip install -r requirements.txt
  python manage.py runserver
  \`\`\`
- **Realtime:** 
  \`\`\`
  cd backend/realtime
  npm install
  npm start
  \`\`\`
- **AI Service:** 
  \`\`\`
  cd backend/ai_vr
  pip install -r requirements.txt
  python ai_service.py
  \`\`\`
- **VR Service:** 
  \`\`\`
  cd backend/ai_vr
  node vr_service.js
  \`\`\`
