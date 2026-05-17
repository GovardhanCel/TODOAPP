#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

RESOURCE_GROUP_NAME="${RESOURCE_GROUP_NAME:-todoapp-rg}"
ACR_REGISTRY_NAME="${ACR_REGISTRY_NAME:-todoappregistry}"

echo -e "${YELLOW}=== Building and Pushing Docker Images ===${NC}"

# Get ACR login server
ACR_LOGIN_SERVER=$(az acr show \
  --resource-group "$RESOURCE_GROUP_NAME" \
  --name "$ACR_REGISTRY_NAME" \
  --query loginServer -o tsv)

echo "ACR Login Server: $ACR_LOGIN_SERVER"

# Create service principal for CI/CD (if needed)
echo -e "${YELLOW}Creating service principal for GitHub Actions...${NC}"
SERVICE_PRINCIPAL=$(az ad sp create-for-rbac \
  --name="${ACR_REGISTRY_NAME}-sp" \
  --scope="/subscriptions/$(az account show --query id -o tsv)/resourceGroups/$RESOURCE_GROUP_NAME" \
  --role="Contributor" \
  --output json)

echo -e "${GREEN}Service Principal Created${NC}"
echo "Add the following to GitHub Secrets:"
echo "ACR_URL: $ACR_LOGIN_SERVER"
echo "ACR_USERNAME: $(echo $SERVICE_PRINCIPAL | jq -r '.appId')"
echo "ACR_PASSWORD: $(echo $SERVICE_PRINCIPAL | jq -r '.password')"
echo "AZURE_CREDENTIALS: $SERVICE_PRINCIPAL"
echo "AZURE_RESOURCE_GROUP: $RESOURCE_GROUP_NAME"

# Build and push images
echo -e "${YELLOW}Building backend image...${NC}"
az acr build \
  --registry "$ACR_REGISTRY_NAME" \
  --image "todoapp-backend:latest" \
  --file ../backend/Dockerfile \
  ../backend

echo -e "${YELLOW}Building frontend image...${NC}"
az acr build \
  --registry "$ACR_REGISTRY_NAME" \
  --image "todoapp-frontend:latest" \
  --file ../frontend/Dockerfile \
  ../frontend

echo -e "${GREEN}Images pushed to ACR successfully!${NC}"
