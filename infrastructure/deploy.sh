#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
RESOURCE_GROUP_NAME="${RESOURCE_GROUP_NAME:-todoapp-rg}"
LOCATION="${LOCATION:-eastus}"
ACR_REGISTRY_NAME="${ACR_REGISTRY_NAME:-todoappregistry}"
AKS_CLUSTER_NAME="${AKS_CLUSTER_NAME:-todoapp-aks}"
SUBSCRIPTION_ID="$(az account show --query id -o tsv)"

echo -e "${YELLOW}=== TODO App Azure Deployment ===${NC}"
echo "Resource Group: $RESOURCE_GROUP_NAME"
echo "Location: $LOCATION"
echo "Subscription: $SUBSCRIPTION_ID"
echo ""

# Create resource group
echo -e "${YELLOW}Creating resource group...${NC}"
az group create \
  --name "$RESOURCE_GROUP_NAME" \
  --location "$LOCATION"

# Deploy infrastructure
echo -e "${YELLOW}Deploying infrastructure with Bicep...${NC}"
az deployment group create \
  --resource-group "$RESOURCE_GROUP_NAME" \
  --template-file main.bicep \
  --parameters location="$LOCATION" projectName="todoapp"

# Deploy AKS
echo -e "${YELLOW}Deploying AKS cluster...${NC}"
az deployment group create \
  --resource-group "$RESOURCE_GROUP_NAME" \
  --template-file aks.bicep \
  --parameters location="$LOCATION" projectName="todoapp"

# Get credentials
echo -e "${YELLOW}Configuring kubectl...${NC}"
az aks get-credentials \
  --resource-group "$RESOURCE_GROUP_NAME" \
  --name "$AKS_CLUSTER_NAME" \
  --overwrite-existing

# Get ACR details
echo -e "${YELLOW}Getting Azure Container Registry details...${NC}"
ACR_LOGIN_SERVER=$(az acr show \
  --resource-group "$RESOURCE_GROUP_NAME" \
  --name "$ACR_REGISTRY_NAME" \
  --query loginServer -o tsv)

echo ""
echo -e "${GREEN}=== Deployment Complete ===${NC}"
echo -e "${GREEN}ACR Login Server: $ACR_LOGIN_SERVER${NC}"
echo -e "${GREEN}AKS Cluster: $AKS_CLUSTER_NAME${NC}"
echo ""
echo "Next steps:"
echo "1. Build and push Docker images to ACR"
echo "2. Deploy to AKS using kubectl apply -f k8s/"
echo "3. Configure DNS and SSL certificates"
