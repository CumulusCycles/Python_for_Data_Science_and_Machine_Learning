# Diabetes Predictor Kubernetes Deployment

This directory contains Kubernetes manifests for deploying the Pima Diabetes Predictor application.

## Architecture

- **API Service**: FastAPI-based prediction service running on port 8081
- **Web App**: Flask-based web interface running on port 5001
- **Namespace**: `diabetes-predictor` for resource isolation

## Prerequisites

1. **Docker Images**: Build the required images first:

   ```bash
   # Build API image
   docker build -f apiDockerfile -t pima-diabetes-api:latest .

   # Build App image
   docker build -f appDockerfile -t pima-diabetes-app:latest .
   ```

2. **Kubernetes Cluster**: Ensure you have a running Kubernetes cluster (Docker Desktop with Kubernetes enabled)

## Deployment

### Option 1: Using kubectl directly

```bash
# Apply all manifests
kubectl apply -f k8s/

# Or apply individually
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/app-deployment.yaml
```

### Option 2: Using kustomize

```bash
kubectl apply -k k8s/
```

## Accessing the Application

### Docker Desktop Kubernetes

```bash
# Option 1: Port forward the LoadBalancer service
kubectl port-forward -n diabetes-predictor service/pima-diabetes-predictor-app 8080:80

# Option 2: Direct port forward to pod
kubectl port-forward -n diabetes-predictor deployment/pima-diabetes-predictor-app 8080:5001
```

### Cloud Deployment

If running on a cloud provider with LoadBalancer support:

```bash
# Get external IP
kubectl get service pima-diabetes-predictor-app -n diabetes-predictor
```

## Monitoring

Check deployment status:

```bash
# Check all resources
kubectl get all -n diabetes-predictor

# Check pod logs
kubectl logs -n diabetes-predictor -l app=pima-diabetes-predictor-api
kubectl logs -n diabetes-predictor -l app=pima-diabetes-predictor-app

# Check service endpoints
kubectl get endpoints -n diabetes-predictor
```

## Cleanup

```bash
# Remove all resources
kubectl delete -f k8s/
```

## Configuration

- **API Service**: Exposed internally on `pima-diabetes-predictor-api:8081`
- **Web App Service**: Exposed externally via LoadBalancer on port 80 and NodePort on 30001
- **Resource Limits**: Both services have CPU/memory limits configured
- **Health Checks**: Liveness and readiness probes are configured for both services
- **Replicas**: Both services run with 2 replicas for high availability
