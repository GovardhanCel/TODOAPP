#!/bin/bash

# Quick start script for local development
# Run this script to set up the entire development environment

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}=== TODO App Local Development Setup ===${NC}"

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"

command -v node >/dev/null 2>&1 || { echo -e "${RED}Node.js is not installed${NC}"; exit 1; }
command -v npm >/dev/null 2>&1 || { echo -e "${RED}npm is not installed${NC}"; exit 1; }
command -v docker >/dev/null 2>&1 || { echo -e "${RED}Docker is not installed${NC}"; exit 1; }
command -v git >/dev/null 2>&1 || { echo -e "${RED}Git is not installed${NC}"; exit 1; }

echo -e "${GREEN}All prerequisites found${NC}"

# Copy environment files
echo -e "${YELLOW}Setting up environment files...${NC}"
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}.env file created${NC}"
fi

# Install dependencies
echo -e "${YELLOW}Installing backend dependencies...${NC}"
cd backend
npm install
cd ..

echo -e "${YELLOW}Installing frontend dependencies...${NC}"
cd frontend
npm install
cd ..

# Start services with Docker Compose
echo -e "${YELLOW}Starting services with Docker Compose...${NC}"
docker-compose up -d

# Wait for services to be ready
echo -e "${YELLOW}Waiting for services to be ready...${NC}"
sleep 10

# Check health
echo -e "${YELLOW}Checking service health...${NC}"
curl http://localhost:5000/health || echo "Backend not ready yet"

echo -e "${GREEN}=== Setup Complete ===${NC}"
echo ""
echo "Frontend: http://localhost:3000"
echo "Backend:  http://localhost:5000"
echo "Database: localhost:5432"
echo ""
echo "To stop services: docker-compose down"
echo "To view logs: docker-compose logs -f"
