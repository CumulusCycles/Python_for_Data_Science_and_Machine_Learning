#!/bin/zsh

docker ps -a
docker stop pima-diabetes-predictor-api && docker rm pima-diabetes-predictor-api
docker stop pima-diabetes-predictor-app && docker rm pima-diabetes-predictor-app

docker images | grep pima
docker rmi pima-diabetes-predictor-api && docker rmi pima-diabetes-predictor-app

docker network ls
docker network rm appnet