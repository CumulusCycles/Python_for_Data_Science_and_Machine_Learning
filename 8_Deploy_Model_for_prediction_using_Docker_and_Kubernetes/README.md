# Pima Diabetes Predictor - Kubernetes Deployment

A machine learning application deployed on Kubernetes that predicts diabetes risk using the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database). The application consists of a FastAPI backend service and a Flask web frontend, containerized and orchestrated with Kubernetes.

## Architecture

- **FastAPI Backend**: Serves ML predictions via REST API (port 8081)
- **Flask Frontend**: Web interface for user interaction (port 5001)
- **Kubernetes Orchestration**: Deployed using Docker Desktop Kubernetes
- **Machine Learning Model**: Logistic Regression trained on Pima diabetes dataset

## Prerequisites

- [Docker Desktop](https://www.docker.com/) with Kubernetes enabled
- Trained ML model file: `pima_diabetes_lr_predicter.joblib` (generated from `demo.ipynb`)

## Quick Start

### 1. Train the Model

Execute the `demo.ipynb` notebook to train and export the model:

```bash
jupyter notebook demo.ipynb
```

This creates the required `pima_diabetes_lr_predictor.joblib` file.

### 2. Build and Deploy

```bash
# Build Docker images and deploy to Kubernetes
./build-and-prepare.sh

# Deploy to Kubernetes
kubectl apply -k k8s/

# Access the application
kubectl port-forward service/pima-diabetes-predictor-app 5001:80 -n diabetes-predictor
```

### 3. Use the Application

Open your browser to: http://localhost:5001

Enter patient data to get diabetes risk predictions powered by the ML model.

## Project Structure

```
├── api.py                     # FastAPI backend service
├── app.py                     # Flask frontend application
├── demo.ipynb                 # Model training notebook
├── pima_diabetes_lr_predicter.joblib  # Trained ML model
├── apiDockerfile              # API container definition
├── appDockerfile              # App container definition
├── build-and-prepare.sh       # Build and deployment script
├── k8s/                       # Kubernetes manifests
│   ├── api-deployment.yaml    # API service deployment
│   ├── app-deployment.yaml    # Frontend deployment
│   ├── namespace.yaml         # Kubernetes namespace
│   └── kustomization.yaml     # Kustomize configuration
└── templates/
    └── index.html             # Web interface template
```

## Detailed Documentation

- **[Kubernetes Deployment Guide](KUBERNETES_DEPLOYMENT.md)** - Complete deployment instructions
- **[K8s README](k8s/README.md)** - Kubernetes-specific documentation

## API Endpoints

- `GET /` - Health check
- `POST /predict` - Diabetes prediction endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)

## Clean Up

To remove the deployed resources:

```bash
./teardown.sh
```

### Validate Cleanup

```bash
kubectl get all -n diabetes-predictor
kubectl get namespaces

docker ps -a
docker images | grep pima
```
