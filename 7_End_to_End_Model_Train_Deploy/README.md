## Deploy a ML Model and make Predictions against the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

Notes:

- Requires execution of `demo.ipynb` Notebook to train and export the Model to a `pima_diabetes_lr_predictor.joblib` file.

- Requires [Docker](https://www.docker.com/) to be installed and running locally.

## Local App Execution

Note: Set the `FASTAPI_URL` variable in `app.py` to "http://127.0.0.1:8081/predict" for local execution.

```bash
pip install -r requirements.txt
pip install flask requests
```

### Launch FastAPI Server

```bash
uvicorn api:app --host 0.0.0.0 --port 8081
```

[http://127.0.0.1:8081/health](http://127.0.0.1:8081/health)

[http://127.0.0.1:8081/docs](http://127.0.0.1:8081/docs)

### Launch Flask App

```bash
python app.py
```

[http://127.0.0.1:5001](http://127.0.0.1:5001)

## Docker Execution

### FastAPI

#### Build FastAPI Docker Image

```bash
docker build -f apiDockerfile -t pima-diabetes-predictor-api .
```

#### Run FastAPI Docker Container

```bash
docker run -p 8081:8081 --name pima-diabetes-predictor-api pima-diabetes-predictor-api:latest
```

[http://127.0.0.1:8081/health](http://127.0.0.1:8081/health)

[http://127.0.0.1:8081/docs](http://127.0.0.1:8081/docs)

### Flask App

#### Build Flask App Docker Image

```bash
docker build -f appDockerfile -t pima-diabetes-predictor-app .
```

#### Run Flask App Docker Container

```bash
docker run -p 5001:5001 --name pima-diabetes-predictor-app pima-diabetes-predictor-app:latest
```

[http://127.0.0.1:5001](http://127.0.0.1:5001)

## Docker Compose - up

Note: Note: Set the `FASTAPI_URL` variable in `app.py` to "http://pima-diabetes-predictor-api:8081/predict" for Docker Network execution.

```bash
docker-compose up --build
```

[http://127.0.0.1:5001](http://127.0.0.1:5001)

## Docker Compose - down

```bash
docker-compose down
```

## Deploy Docker Network and Containers - script

```bash
./deploy.sh
```

[http://127.0.0.1:5001](http://127.0.0.1:5001)

## Destroy Docker Network and Containers - script

```bash
./destroy.sh
```
