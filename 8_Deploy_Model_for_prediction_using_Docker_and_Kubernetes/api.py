from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import joblib
import numpy as np

# Example patient data collections
patient_data = {
    "diabetic": {
        "pregnancies": 8,
        "glucose": 155,
        "blood_pressure": 85,
        "skin_thickness": 40,
        "insulin": 210,
        "bmi": 35.2,
        "diabetes_pedigree_function": 0.745,
        "age": 45
    },
    "non_diabetic": {
        "pregnancies": 2,
        "glucose": 75,
        "blood_pressure": 70,
        "skin_thickness": 30,
        "insulin": 50,
        "bmi": 25.0,
        "diabetes_pedigree_function": 0.5,
        "age": 22
    }
}

# Create FastAPI instance
app = FastAPI(title="Pima Diabetes Logistic Regression Prediction API")


# Load the model from the file
lr_loaded = joblib.load('pima_diabetes_lr_predicter.joblib')


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


@app.get("/patient_data")
def get_patient_data(diabetic: int = 1):
    if diabetic == 1:
        data = patient_data["diabetic"]
    else:
        data = patient_data["non_diabetic"]
    return JSONResponse(content=data)


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


