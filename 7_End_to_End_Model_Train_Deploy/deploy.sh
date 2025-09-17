#!/bin/zsh
# Create a Docker network
NETWORK_NAME=appnet
FASTAPI_IMAGE=pima-diabetes-predictor-api
FLASK_IMAGE=pima-diabetes-predictor-app

# Create network (ignore error if exists)
docker network create $NETWORK_NAME || true

# Build Docker images
docker build -f apiDockerfile -t pima-diabetes-predictor-api .
docker build -f appDockerfile -t pima-diabetes-predictor-app .

# Run FastAPI app container (replace with your built image name)
docker run --network $NETWORK_NAME --name $FASTAPI_IMAGE -p 8081:8081 -d $FASTAPI_IMAGE

# Run Flask app container (replace with your built image name)
docker run --network $NETWORK_NAME --name $FLASK_IMAGE -p 5001:5000 -d $FLASK_IMAGE

echo "FastAPI app running at http://127.0.0.1:8081"
echo "Flask app running at http://127.0.0.1:5001"
echo "FastAPI can access Flask at http://pima-diabetes-predictor-api:8081/predict from inside the network"
