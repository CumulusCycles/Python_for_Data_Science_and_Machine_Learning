## Deploy a ML Model and make Predictions against the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) using Docker

Notes:

- Requires execution of `demo.ipynb` Notebook to train and export the Model to a `pima_diabetes_lr_predictor.joblib` file.

- Requires [Docker](https://www.docker.com/) to be installed and running locally.

## Local App Execution

Note: Set the `API_BASE_URL` variable and app.run() command in `app.py` for localhost deployment.

ex:

```python

# Configuration
API_BASE_URL = "http://127.0.0.1:8081"  # FastAPI server URL, localhost
# API_BASE_URL = "http://pima-diabetes-predictor-api:8081" # Containerized FastAPI server URL

# ...

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Localhost
    # app.run(debug=True, host='0.0.0.0', port=5001) # Containerized
```

### Install Dependencies

```bash
pip install -r api-requirements.txt
pip install -r app-requirements.txt
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

Note: Note: Set the `API_BASE_URL` variable and app.run() command in `app.py` for Docker Network deployment.

ex:

```python

# Configuration
# API_BASE_URL = "http://127.0.0.1:8081"  # FastAPI server URL, localhost
API_BASE_URL = "http://pima-diabetes-predictor-api:8081" # Containerized FastAPI server URL

# ...

if __name__ == '__main__':
    # app.run(debug=True, port=5001) # Localhost
    app.run(debug=True, host='0.0.0.0', port=5001) # Containerized
```

## Docker Compose - up

```bash
docker-compose up
```

[http://127.0.0.1:5001](http://127.0.0.1:5001)

## Docker Compose - down

```bash
docker-compose down
```
