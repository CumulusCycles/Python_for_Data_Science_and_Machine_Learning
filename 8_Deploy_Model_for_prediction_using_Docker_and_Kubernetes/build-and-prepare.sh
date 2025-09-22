#!/bin/bash

# Build Docker images
echo "Building Docker images..."

# Build API image
echo "Building API image..."
docker build -f apiDockerfile -t pima-diabetes-api:latest .

# Build App image
echo "Building App image..."
docker build -f appDockerfile -t pima-diabetes-app:latest .

echo "Docker images built successfully!"

echo "Ready for Kubernetes deployment!"
echo "Run: kubectl apply -k k8s/ to deploy the application"
