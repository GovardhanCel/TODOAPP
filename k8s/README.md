# Kubernetes Deployment Guide

## Prerequisites

- Azure AKS cluster created
- `kubectl` configured
- Azure Container Registry (ACR) set up
- Docker images pushed to ACR

## Deployment Steps

### 1. Create Namespace and Secrets

```bash
kubectl apply -f 01-namespace.yaml
kubectl apply -f 02-secrets-configmap.yaml
```

### 2. Deploy Database

```bash
kubectl apply -f 03-postgres-deployment.yaml
```

### 3. Deploy Backend API

Before applying, update the ACR URL in `04-backend-deployment.yaml`:

```bash
sed -i 's/<ACR_URL>/your-acr-name.azurecr.io/g' 04-backend-deployment.yaml
kubectl apply -f 04-backend-deployment.yaml
```

### 4. Deploy Frontend

```bash
sed -i 's/<ACR_URL>/your-acr-name.azurecr.io/g' 05-frontend-deployment.yaml
kubectl apply -f 05-frontend-deployment.yaml
```

### 5. Configure Ingress

```bash
kubectl apply -f 06-ingress.yaml
```

### 6. Set Up Autoscaling

```bash
kubectl apply -f 07-hpa.yaml
```

## Verify Deployment

```bash
# Check pods
kubectl get pods -n todoapp

# Check services
kubectl get svc -n todoapp

# Check logs
kubectl logs -n todoapp deployment/todoapp-backend

# Port forward to test
kubectl port-forward -n todoapp svc/todoapp-backend 5000:5000
```

## Update Deployments

```bash
# Update image
kubectl set image deployment/todoapp-backend \
  backend=<ACR_URL>/todoapp-backend:new-tag \
  -n todoapp

# Rollback
kubectl rollout undo deployment/todoapp-backend -n todoapp
```
