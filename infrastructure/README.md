# Azure Infrastructure as Code Setup

## Prerequisites

- Azure CLI installed
- Logged into Azure (`az login`)
- kubectl installed (for AKS)
- jq installed (for JSON parsing)

## Infrastructure Components

This setup creates:

1. **Azure Container Registry (ACR)** - For storing Docker images
2. **Azure Kubernetes Service (AKS)** - Kubernetes cluster for running containers
3. **Azure Database for PostgreSQL** - Managed database service
4. **Azure Key Vault** - Secrets management
5. **Log Analytics & Application Insights** - Monitoring and diagnostics
6. **Virtual Network** - Network isolation and security

## Deployment Steps

### 1. Set Environment Variables

```bash
export RESOURCE_GROUP_NAME="todoapp-rg"
export LOCATION="eastus"
export ACR_REGISTRY_NAME="todoappregistry"
export AKS_CLUSTER_NAME="todoapp-aks"
```

### 2. Run Infrastructure Deployment

```bash
chmod +x deploy.sh
./deploy.sh
```

This will:
- Create Azure resource group
- Deploy all infrastructure resources via Bicep
- Configure kubectl to access the AKS cluster

### 3. Build and Push Docker Images

```bash
chmod +x build-push-images.sh
./build-push-images.sh
```

This will:
- Build Docker images using Azure Container Registry
- Push images to ACR
- Create service principal for CI/CD
- Output secrets needed for GitHub Actions

### 4. Configure GitHub Secrets

Add the following secrets to your GitHub repository:
- `ACR_URL` - Azure Container Registry URL
- `ACR_USERNAME` - Service principal app ID
- `ACR_PASSWORD` - Service principal password
- `AZURE_CREDENTIALS` - Full service principal JSON
- `AZURE_RESOURCE_GROUP` - Resource group name
- `AKS_CLUSTER_NAME` - AKS cluster name

### 5. Deploy to Kubernetes

Update the ACR URL in k8s manifests and deploy:

```bash
cd ../k8s
sed -i 's/<ACR_URL>/<your-acr-url>/g' *.yaml
kubectl apply -f 01-namespace.yaml
kubectl apply -f 02-secrets-configmap.yaml
kubectl apply -f 03-postgres-deployment.yaml
kubectl apply -f 04-backend-deployment.yaml
kubectl apply -f 05-frontend-deployment.yaml
kubectl apply -f 06-ingress.yaml
kubectl apply -f 07-hpa.yaml
```

## Monitoring

View logs and metrics:

```bash
# Check pod status
kubectl get pods -n todoapp

# View deployment logs
kubectl logs -n todoapp deployment/todoapp-backend

# Watch deployments
kubectl rollout status deployment/todoapp-backend -n todoapp
```

## Cleanup

To delete all resources:

```bash
az group delete --name "$RESOURCE_GROUP_NAME" --yes
```

## Costs

Azure resources have associated costs. Estimated monthly costs:
- AKS Cluster: ~$70-150
- PostgreSQL: ~$50-100
- Container Registry: ~$5
- Other services: ~$10-20

Total: ~$135-275/month (can vary based on usage)
