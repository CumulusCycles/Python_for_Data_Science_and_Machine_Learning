# FAST API file for pima_diabetes_svmc_predicter

# pip install fastapi uvicorn joblib numpy pydantic
# To run the app: uvicorn api:app --host 0.0.0.0 --port 8081
# Access the docs at: http://127.0.0.1:8081/docs

"""
Test Data 

Diabetic Patient:
{
    "pregnancies": 8,
    "glucose": 155,
    "blood_pressure": 85,
    "skin_thickness": 40,
    "insulin": 210,
    "bmi": 35.2,
    "diabetes_pedigree_function": 0.745,
    "age": 45
}

Non-Diabetic Patient:
{
    "pregnancies": 2,
    "glucose": 75,
    "blood_pressure": 70,
    "skin_thickness": 30,
    "insulin": 50,
    "bmi": 25.0,
    "diabetes_pedigree_function": 0.5,
    "age": 22
}
"""

# Import necessary libraries
from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel


# Load the model from the file
lr_loaded = joblib.load('pima_diabetes_lr_predicter.joblib')

# Create FastAPI instance
app = FastAPI(title="Pima Diabetes Logistic Regression Prediction API")

# Define the input data model
class PatientData(BaseModel):
    pregnancies: int
    glucose: int
    blood_pressure: int
    skin_thickness: int
    insulin: int
    bmi: float
    diabetes_pedigree_function: float
    age: int

@app.get("/health")
def health_check():
    return {"status": "API is healthy"}

@app.post("/predict")
def make_prediction(data: PatientData):
    
    # Preprocess the input data
    input_data = np.array([[data.pregnancies, data.glucose, data.blood_pressure,
                             data.skin_thickness, data.insulin, data.bmi,
                             data.diabetes_pedigree_function, data.age]])
    
    # Make a prediction using the loaded model
    prediction = lr_loaded.predict(input_data)
    verbose_result = {
        "input_data": input_data.tolist(),
        "raw_prediction": int(prediction[0]),
        "prediction_label": "Diabetic" if prediction[0] == 1 else "Not Diabetic"
    }
    
    # If model supports probability, add it
    if hasattr(lr_loaded, "predict_proba"):
        try:
            proba = lr_loaded.predict_proba(input_data)[0]
            verbose_result["probabilities"] = {
                "Not Diabetic": float(proba[0]),
                "Diabetic": float(proba[1])
            }
        except Exception as e:
            verbose_result["probabilities_error"] = str(e)
    
    return verbose_result
