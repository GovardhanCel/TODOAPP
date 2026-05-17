# Quick Start Guide - TODO App Full Stack

## 📋 Project Overview

This is an **advanced production-ready TODO application** with:
- ✅ Real-time collaboration features
- ✅ Team management & permissions
- ✅ Containerized deployment (Docker)
- ✅ Kubernetes orchestration (Azure AKS)
- ✅ Continuous Integration/Continuous Deployment (GitHub Actions)
- ✅ Infrastructure as Code (Azure Bicep)
- ✅ Comprehensive monitoring & autoscaling

---

## 🚀 Getting Started - Local Development

### Prerequisites
- **Node.js 18+** (from nodejs.org)
- **Docker & Docker Compose** (from docker.com)
- **Git** (from git-scm.com)
- **Azure CLI** (optional, for Azure deployment)

### Step 1: Clone & Setup

```bash
# Navigate to project root
cd /Users/admin/TODOAPP

# Copy environment file
cp .env.example .env

# Start all services (PostgreSQL, Backend, Frontend)
docker compose up -d

# Wait for services to start (about 30-60 seconds)
```

### Step 2: Access the Application

Once services are running:

| Service | URL |
|---------|-----|
| **Frontend** (React App) | http://localhost:3000 |
| **Backend API** | http://localhost:5000 |
| **Database** | localhost:5432 |
| **Health Check** | http://localhost:5000/health |

### Step 3: Verify Services

```bash
# Check all containers are running
docker ps

# View logs
docker logs todoapp-backend
docker logs todoapp-frontend
docker logs todoapp-postgres

# Test API
curl http://localhost:5000/health
```

### Step 4: Stop Services

```bash
docker compose down

# Remove volumes too (resets database)
docker compose down -v
```

---

## 📁 Project Structure

```
todo-app/
├── frontend/                      # React 18 TypeScript frontend
│   ├── src/
│   │   ├── pages/                 # Page components
│   │   ├── components/            # Reusable components
│   │   ├── App.tsx                # Root component
│   │   └── index.tsx              # Entry point
│   ├── public/
│   ├── Dockerfile                 # Production container
│   ├── nginx.conf                 # Nginx config for production
│   ├── tailwind.config.js         # Tailwind CSS config
│   └── package.json
│
├── backend/                        # Node.js/Express backend
│   ├── src/
│   │   ├── index.ts               # Server entry point
│   │   ├── routes/                # API route definitions
│   │   ├── controllers/           # Business logic
│   │   ├── models/                # Data models
│   │   ├── middleware/            # Express middleware
│   │   ├── database/              # DB connections
│   │   └── utils/authentication   # Auth utilities
│   ├── prisma/
│   │   └── schema.prisma          # Database schema
│   ├── Dockerfile                 # Production container
│   ├── tsconfig.json              # TypeScript config
│   └── package.json
│
├── k8s/                            # Kubernetes manifests for AKS
│   ├── 01-namespace.yaml          # Cluster namespace
│   ├── 02-secrets-configmap.yaml  # Secrets & configuration
│   ├── 03-postgres-deployment.yaml # Database
│   ├── 04-backend-deployment.yaml  # Backend API
│   ├── 05-frontend-deployment.yaml # Frontend
│   ├── 06-ingress.yaml            # Ingress controller
│   ├── 07-hpa.yaml                # Autoscaling rules
│   └── README.md                   # K8s deployment guide
│
├── infrastructure/                 # Azure Infrastructure as Code
│   ├── main.bicep                 # ACR, Key Vault, Database
│   ├── aks.bicep                  # AKS cluster setup
│   ├── deploy.sh                  # Deployment automation
│   ├── build-push-images.sh       # Docker build & push
│   └── README.md                   # Infrastructure guide
│
├── .github/
│   └── workflows/                 # GitHub Actions CI/CD
│       ├── deploy.yaml            # Build, test, deploy
│       └── security.yaml          # Vulnerability scanning
│
├── docker-compose.yml             # Local development setup
├── .env.example                   # Environment template
├── README.md                       # Main documentation
├── CICD.md                        # CI/CD pipeline guide
└── CONTRIBUTING.md                # Contributing guidelines
```

---

## 🏗️ Architecture Overview

### Local Development (Docker Compose)
```
┌──────────────────┐
│  React Frontend  │
│  (Port 3000)     │
└────────┬─────────┘
         │ HTTP/WebSocket
         ▼
┌──────────────────┐        ┌──────────────────┐
│ Express Backend  │◄──────►│   PostgreSQL DB  │
│  (Port 5000)     │        │  (Port 5432)     │
└──────────────────┘        └──────────────────┘
```

### Production (Azure AKS)
```
┌─────────────────────────────────────────────┐
│         Azure Kubernetes Service (AKS)       │
│  ┌────────────────────────────────────────┐ │
│  │  Ingress Controller (nginx)            │ │
│  └───────────────┬────────────────────────┘ │
│                  │                           │
│  ┌──────────────┴───────────────┐           │
│  │                              │           │
│  ▼ (Frontend)           ▼ (Backend)        │
│ ┌────────────────┐    ┌──────────────────┐ │
│ │ 3x Frontend    │    │ 3x Backend       │ │
│ │ (HPA: 2-5)     │    │ (HPA: 2-10)      │ │
│ └────────────────┘    └────────┬─────────┘ │
│                                 │           │
│                                 ▼           │
│                    ┌──────────────────────┐ │
│                    │ PostgreSQL (Managed) │ │
│                    └──────────────────────┘ │
└─────────────────────────────────────────────┘
       │
       ▼
┌──────────────────────┐  ┌──────────────────────┐
│ Azure Container      │  │ Azure Monitor        │
│ Registry (ACR)       │  │ - App Insights       │
│ - Image storage      │  │ - Log Analytics      │
│ - Version tracking   │  │ - Diagnostics        │
└──────────────────────┘  └──────────────────────┘
```

---

## 📚 Technology Stack

### Frontend
- **React 18** - User interface
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **React Router** - Page navigation
- **Axios** - HTTP client
- **WebSocket** - Real-time updates
- **Zustand** - State management

### Backend
- **Node.js 18** - Runtime
- **Express.js** - Web framework
- **TypeScript** - Type safety
- **Prisma ORM** - Database access
- **JWT** - Authentication
- **WebSocket (ws)** - Real-time communication
- **PostgreSQL** - Primary database

### Infrastructure & DevOps
- **Docker** - Containerization
- **Kubernetes (AKS)** - Orchestration
- **Azure Bicep** - Infrastructure as Code
- **GitHub Actions** - CI/CD pipeline
- **Azure Container Registry** - Image registry
- **Azure Database for PostgreSQL** - Managed DB
- **Azure Key Vault** - Secrets management
- **Azure Monitor** - Observability

---

## 🔐 Database Schema

**Key Tables:**
- **users** - User accounts with roles (ADMIN/USER)
- **teams** - Collaborative teams
- **team_members** - Team membership with roles
- **todos** - Tasks with priority & due dates
- **todo_tags** - Task categorization
- **todo_assignees** - Task assignment to team members

**Features:**
- Cascading deletes (delete user → deletes their todos)
- Unique constraints (prevents duplicate assignments)
- Automatic timestamps (createdAt, updatedAt)

---

## 🚀 Deployment - Azure AKS

### Phase 1: Set Up Infrastructure (One-time)

```bash
cd infrastructure

# 1. Set environment variables
export RESOURCE_GROUP_NAME="todoapp-rg"
export LOCATION="eastus"

# 2. Deploy Azure resources (ACR, AKS, Database, Key Vault)
./deploy.sh

# 3. Build and push Docker images to Azure Container Registry
./build-push-images.sh

# This outputs secrets for GitHub Actions configuration
```

### Phase 2: Configure GitHub Actions

Add secrets to GitHub repository:
1. Go to **Settings > Secrets and variables > Actions**
2. Add the secrets output from the script above:
   - `ACR_URL`
   - `ACR_USERNAME`
   - `ACR_PASSWORD`
   - `AZURE_CREDENTIALS`
   - `AZURE_RESOURCE_GROUP`
   - `AKS_CLUSTER_NAME`

### Phase 3: Deploy to AKS

```bash
# Update image references in k8s manifests
cd k8s
sed -i 's/<ACR_URL>/your-acr-name.azurecr.io/g' *.yaml

# Apply all Kubernetes manifests
kubectl apply -f 01-namespace.yaml
kubectl apply -f 02-secrets-configmap.yaml
kubectl apply -f 03-postgres-deployment.yaml
kubectl apply -f 04-backend-deployment.yaml
kubectl apply -f 05-frontend-deployment.yaml
kubectl apply -f 06-ingress.yaml
kubectl apply -f 07-hpa.yaml

# Verify deployment
kubectl get pods -n todoapp
kubectl get svc -n todoapp
```

### Phase 4: Monitor & Scale

```bash
# View application logs
kubectl logs -f deployment/todoapp-backend -n todoapp

# Check autoscaling status
kubectl get hpa -n todoapp

# Update deployment (automatic on code push to main)
# GitHub Actions pipeline handles building, pushing, and deploying
```

---

## 📊 CI/CD Pipeline

The GitHub Actions pipeline automatically:

1. **Test** (on all pushes & PRs)
   - Install dependencies
   - Run unit tests
   - Run linting

2. **Build** (on main/develop pushes)
   - Build Docker images
   - Push to Azure Container Registry

3. **Deploy** (on main branch pushes)
   - Get AKS credentials
   - Apply Kubernetes manifests
   - Update running deployments
   - Verify rollout

4. **Security** (daily + on pushes)
   - Scan file systems for vulnerabilities
   - Check npm dependencies for security issues
   - Generate security reports

---

## 📈 Monitoring & Observability

### Application Insights
- **Performance metrics** - Response times, throughput
- **Error tracking** - Exceptions and failures
- **Custom events** - Business metrics

### Log Analytics
- **Container logs** - Pod output
- **Kubernetes events** - Cluster activities
- **Custom logs** - Application-specific data

### Dashboards
- Navigate to Azure Portal
- Resource Group > Application Insights
- Build custom dashboards for real-time monitoring

---

## 🐛 Troubleshooting

### Local Development

| Issue | Solution |
|-------|----------|
| `docker: command not found` | Install Docker Desktop for Mac |
| `Cannot connect to Docker daemon` | Start Docker Desktop application |
| `Port 5000 already in use` | Change PORT in .env or stop other services |
| `Database connection refused` | Wait 30 seconds for PostgreSQL to start |

### Azure Deployment

| Issue | Solution |
|-------|----------|
| `AKS cluster not found` | Verify cluster name and resource group |
| `Images not in ACR` | Run `./build-push-images.sh` first |
| `Pod CrashLoopBackOff` | Check: `kubectl logs pod-name -n todoapp` |
| `No external IP for service` | Wait for load balancer to provision (2-3 min) |

### GitHub Actions

| Issue | Solution |
|-------|----------|
| `ACR login failed` | Verify credentials in GitHub secrets |
| `Build timeout` | Increase timeout in workflow file |
| `Deployment fails` | Check AKS cluster status in Azure Portal |

---

## 📖 Documentation

- **[Architecture & Features](README.md)** - Project overview
- **[Backend Setup](backend/README.md)** - API documentation
- **[Frontend Setup](frontend/README.md)** - UI components
- **[Kubernetes Deployment](k8s/README.md)** - K8s manifests
- **[Azure Infrastructure](infrastructure/README.md)** - IaC setup
- **[CI/CD Pipeline](CICD.md)** - Pipeline details
- **[Contributing Guide](CONTRIBUTING.md)** - Development workflow

---

## 💡 Next Steps

1. ✅ **Understand the architecture** - Read architecture diagrams
2. ✅ **Run locally** - Start with `docker compose up`
3. ✅ **Explore the code** - Review backend & frontend structure
4. ✅ **Set up Azure resources** - Run infrastructure deployment
5. ✅ **Configure CI/CD** - Add GitHub secrets
6. ✅ **Deploy to production** - Push to main branch

---

## 📞 Support & Issues

- Check [Troubleshooting](#troubleshooting) section
- Review logs: `docker logs`, `kubectl logs`
- Open GitHub issues for bugs
- See CONTRIBUTING.md for development guidelines

---

## 📄 License

MIT License - See LICENSE file for details

---

**Happy coding! 🎉**
