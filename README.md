# Advanced TODO App - Full Stack with Azure AKS Deployment

A production-ready TODO application built with React, Node.js/Express, PostgreSQL, Docker, Kubernetes, and GitHub Actions CI/CD pipeline.

## Project Structure

```
todo-app-full-stack/
├── frontend/              # React TypeScript application
├── backend/               # Node.js/Express API server
├── k8s/                   # Kubernetes manifests for AKS
├── infrastructure/        # Azure Infrastructure as Code (Bicep)
├── .github/workflows/     # CI/CD pipelines (GitHub Actions)
└── docker/                # Docker configuration files
```

## Features

### Frontend
- React 18 with TypeScript
- Real-time WebSocket support
- Team collaboration
- Advanced task management
- Responsive UI with Tailwind CSS

### Backend
- Express.js with TypeScript
- JWT Authentication
- WebSocket support for real-time updates
- Role-based access control (RBAC)
- PostgreSQL database with Prisma ORM
- RESTful API design

### Infrastructure
- Azure Container Registry
- Azure Kubernetes Service (AKS)
- Azure Database for PostgreSQL
- Azure Key Vault for secrets
- Infrastructure as Code (Bicep)

### CI/CD
- GitHub Actions for automation
- Automated testing
- Docker image builds and push to ACR
- Automated Kubernetes deployment
- Multi-stage build process

## Prerequisites

- Node.js 18+
- Docker & Docker Compose
- Azure CLI
- kubectl
- Git

## Getting Started

### Local Development

```bash
# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies
cd ../backend
npm install

# Create .env files
cp .env.example .env

# Start PostgreSQL (Docker)
docker-compose up -d postgres

# Run migrations
npm run migrate

# Start backend server
npm run dev

# In another terminal, start frontend
cd frontend
npm start
```

### Docker Build & Run

```bash
# Build images
docker-compose build

# Run containers
docker-compose up
```

## Azure Deployment

### Prerequisites
- Azure subscription
- Azure Container Registry
- AKS cluster configured

### Deploy Steps

1. **Build and push Docker images**
```bash
az acr build -r <registry-name> -t todoapp-backend:latest ./backend
az acr build -r <registry-name> -t todoapp-frontend:latest ./frontend
```

2. **Deploy to AKS**
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/ingress.yaml
```

## Documentation

- [Backend Setup](./backend/README.md)
- [Frontend Setup](./frontend/README.md)
- [Kubernetes Deployment](./k8s/README.md)
- [Azure Infrastructure Setup](./infrastructure/README.md)
- [CI/CD Pipeline](./CICD.md)

## Environment Variables

Create `.env` files in backend and frontend directories with required configurations.

## Testing

```bash
# Backend tests
cd backend
npm test

# Frontend tests
cd frontend
npm test
```

## Contributing

Follow the branching strategy defined in CONTRIBUTING.md

## License

MIT
