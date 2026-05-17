# CI/CD Pipeline Documentation

## GitHub Actions Workflow

The project uses GitHub Actions for automated testing, building, and deployment.

### Workflows

#### 1. **deploy.yaml** - Main CI/CD Pipeline

Triggers on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

**Jobs:**

1. **test** - Runs on all triggers
   - Installs dependencies
   - Runs unit tests
   - Runs linting

2. **build** - Runs on push events (after test)
   - Sets up Docker Buildx
   - Logs into Azure Container Registry
   - Builds and pushes backend image with tags:
     - `latest`
     - Git SHA (specific commit)
     - Branch name
   - Builds and pushes frontend image (same tags)

3. **deploy** - Runs on main branch push (after build)
   - Authenticates with Azure
   - Gets AKS credentials
   - Updates image references in K8s manifests
   - Applies all K8s manifests
   - Waits for rollout completion
   - Outputs service endpoints

#### 2. **security.yaml** - Continuous Security Scanning

Triggers:
- On push to main/develop
- On pull requests
- Daily schedule (2 AM UTC)

**Scans:**
- File system vulnerabilities (Trivy)
- Docker image vulnerabilities
- npm package vulnerabilities

## Required Secrets

Add these to GitHub repository settings (Settings > Secrets and variables > Actions):

```
ACR_URL=myregistry.azurecr.io
ACR_USERNAME=service-principal-id
ACR_PASSWORD=service-principal-password
AZURE_CREDENTIALS={"clientId":"...","clientSecret":"...","subscriptionId":"...","tenantId":"..."}
AZURE_RESOURCE_GROUP=todoapp-rg
AKS_CLUSTER_NAME=todoapp-aks
```

## Getting Azure Credentials

### 1. Create Service Principal

```bash
az ad sp create-for-rbac \
  --name "github-actions" \
  --role "Contributor" \
  --scopes "/subscriptions/{subscription-id}" \
  --output json
```

### 2. Get ACR Details

```bash
az acr show \
  --resource-group todoapp-rg \
  --name todoappregistry \
  --query loginServer -o tsv
```

```bash
az acr credential show \
  --resource-group todoapp-rg \
  --name todoappregistry \
  --query '[username,passwords[0].value]' -o tsv
```

## Deployment Strategy

### Branch Strategy

- **main** - Production
  - Code is tested and deployed to AKS
  - Tagged with version numbers
  
- **develop** - Staging
  - Code is tested but deployment is optional
  - Used for integration testing

### Image Tagging

Images are tagged with:
- `latest` - Most recent build
- `{git-sha}` - Specific commit identifier
- `{branch-name}` - Branch name for tracking origin

### Rollout Strategy

- Uses Kubernetes Deployments with rolling updates
- Waits for all new pods to be ready
- Can auto-rollback on failure

## Manual Git Operations Behind the Pipeline

### Example: Deploy a specific commit

```bash
# Get the image SHA
git log --oneline | head -1
# e.g., "abc1234 Fix login bug"

# Update deployment to use specific image
kubectl set image deployment/todoapp-backend \
  backend=myregistry.azurecr.io/todoapp-backend:abc1234 \
  -n todoapp
```

### Example: Rollback to previous version

```bash
kubectl rollout undo deployment/todoapp-backend -n todoapp
kubectl rollout history deployment/todoapp-backend -n todoapp
```

## Monitoring Pipeline Status

### GitHub Actions Dashboard
- Visit Actions tab in your repository
- See all workflow runs and their status
- View detailed logs for each job

### AKS Monitoring

```bash
# Check current deployments
kubectl get deployments -n todoapp

# View pod status
kubectl get pods -n todoapp

# Stream logs from backend
kubectl logs -f deployment/todoapp-backend -n todoapp
```

### Application Insights
- View in Azure Portal under your resource group
- Monitor performance metrics
- Set up alerts for failures

## Troubleshooting

### Build Fails

1. Check GitHub Actions logs for error messages
2. Verify Docker files are valid:
   ```bash
   docker build -f backend/Dockerfile backend/
   docker build -f frontend/Dockerfile frontend/
   ```

### Deployment Fails

1. Check AKS cluster status:
   ```bash
   az aks show --name todoapp-aks -g todoapp-rg
   ```

2. Check pod status:
   ```bash
   kubectl describe pod <pod-name> -n todoapp
   ```

3. Check image availability in ACR:
   ```bash
   az acr repository list --name todoappregistry
   ```

### ACR Login Issues

```bash
# Re-authenticate with ACR
az acr login --name todoappregistry

# Verify credentials
az acr credential show --name todoappregistry
```

## Performance Tips

1. **Use layer caching** - Docker builds cache layers
2. **Parallel jobs** - GitHub Actions can run jobs in parallel
3. **Scheduled runs** - Use cron for off-peak hours
4. **Artifact caching** - Cache npm dependencies:
   ```yaml
   - uses: actions/setup-node@v4
     with:
       cache: 'npm'
   ```

## Next Steps

1. Set up branch protection rules
2. Configure status checks to require passing builds
3. Set up automated rollback on health check failures
4. Configure Azure Application Insights alerts
5. Set up log aggregation with Azure Monitor
