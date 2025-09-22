# Kubernetes Deployment Guide

## Overview

This project deploys a Pima Diabetes Prediction application using Kubernetes. The application consists of:

- **API Service**: FastAPI backend serving ML predictions (port 8081)
- **Web Application**: Flask frontend for user interaction (port 5001)

## Prerequisites

- Docker Desktop installed and running with Kubernetes enabled
- kubectl configured to access your Docker Desktop Kubernetes cluster

## Quick Start

### 1. Build Docker Images

```bash
# Build the API image
docker build -f apiDockerfile -t pima-diabetes-api:latest .

# Build the app image
docker build -f appDockerfile -t pima-diabetes-app:latest .
```

### 2. Deploy to Kubernetes

```bash
# Apply all configurations
kubectl apply -k k8s/

# Or apply individually
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/app-deployment.yaml
```

### 3. Access the Application

```bash
# Check service status
kubectl get services -n diabetes-predictor

# Option 1: Port forward the LoadBalancer service (recommended)
kubectl port-forward service/pima-diabetes-predictor-app 5001:80 -n diabetes-predictor

# Option 2: Use the NodePort service directly
kubectl port-forward service/pima-diabetes-predictor-app-nodeport 5001:5001 -n diabetes-predictor
```

Then open your browser to: http://localhost:5001

**Note**: With Docker Desktop Kubernetes, LoadBalancer services are automatically accessible on localhost.

## Architecture

```
┌─────────────────┐    ┌─────────────────┐
│   Web Browser   │    │      kubectl    │
│  (localhost:5001)│    │                 │
└─────────┬───────┘    └─────────────────┘
          │
          ▼
┌─────────────────┐
│  LoadBalancer   │
│   Service       │
│  (port 5001)    │
└─────────┬───────┘
          │
          ▼
┌─────────────────┐    ┌─────────────────┐
│   Flask App     │───▶│   FastAPI       │
│   Container     │    │   Container     │
│   (port 5001)   │    │   (port 8081)   │
└─────────────────┘    └─────────────────┘
│                      │
│  pima-diabetes-      │  pima-diabetes-
│  predictor-app       │  predictor-api
│  service             │  service
└─────────────────────┘
```

## Services

### API Service (`pima-diabetes-predictor-api`)

- **Type**: ClusterIP (internal only)
- **Port**: 8081
- **Endpoints**:
  - `GET /` - Health check
  - `POST /predict` - Diabetes prediction

### App Service (`pima-diabetes-predictor-app`)

- **Type**: LoadBalancer (external access)
- **Port**: 5001
- **Purpose**: Web interface for predictions

## Configuration Details

### Environment Variables

- API service uses the ML model file `pima_diabetes_lr_predicter.joblib`
- App service connects to API via Kubernetes DNS: `pima-diabetes-predictor-api:8081`

### Resource Limits

- **API**: 500m CPU, 512Mi memory
- **App**: 200m CPU, 256Mi memory

## Troubleshooting

### Check Pod Status

```bash
kubectl get pods -n diabetes-predictor
kubectl describe pod <pod-name> -n diabetes-predictor
```

### View Logs

```bash
kubectl logs -f deployment/pima-diabetes-predictor-api -n diabetes-predictor
kubectl logs -f deployment/pima-diabetes-predictor-app -n diabetes-predictor
```

### Test API Connectivity

```bash
# Port forward API service
kubectl port-forward service/pima-diabetes-predictor-api 8081:8081 -n diabetes-predictor

# Test API endpoint
curl http://localhost:8081/
```

### Clean Up

```bash
# Delete all resources
kubectl delete -k k8s/

# Or delete namespace (removes everything)
kubectl delete namespace diabetes-predictor
```

### Development

### Docker Desktop Kubernetes Setup

If you need to enable Kubernetes in Docker Desktop:

1. Open Docker Desktop preferences
2. Go to Kubernetes tab
3. Check "Enable Kubernetes"
4. Click "Apply & Restart"

### Image Updates

After code changes:

1. Rebuild Docker images with new tags
2. Update image tags in `k8s/kustomization.yaml`
3. Apply changes: `kubectl apply -k k8s/`
