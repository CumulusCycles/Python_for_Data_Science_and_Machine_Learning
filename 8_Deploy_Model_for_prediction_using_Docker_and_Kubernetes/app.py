from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Configuration
# API_BASE_URL = "http://127.0.0.1:8081"  # FastAPI server URL, localhost
API_BASE_URL = "http://pima-diabetes-predictor-api:8081" # Containerized FastAPI server URL


@app.route('/', methods=['GET', 'POST'])
def index():
    """Single page that handles everything"""
    patient_data = None
    prediction_result = None
    error_message = None
    health_result = None
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'get_patient_data':
            # Get patient data
            diabetic_flag = request.form.get('diabetic_type')
            try:
                response = requests.get(f"{API_BASE_URL}/patient_data?diabetic={diabetic_flag}")
                if response.status_code == 200:
                    patient_data = response.json()
                else:
                    error_message = f"Failed to get patient data. Status code: {response.status_code}"
            except requests.exceptions.RequestException as e:
                error_message = f"Error connecting to API: {str(e)}"
        
        elif action == 'check_health':
            # Check API health
            try:
                response = requests.get(f"{API_BASE_URL}/health")
                if response.status_code == 200:
                    health_result = {
                        "status": "✅ API is reachable and healthy",
                        "api_response": response.json(),
                        "status_code": response.status_code,
                        "success": True
                    }
                else:
                    health_result = {
                        "status": "⚠️ API responded with error",
                        "status_code": response.status_code,
                        "success": False
                    }
            except requests.exceptions.RequestException as e:
                health_result = {
                    "status": "❌ API is unreachable",
                    "error": str(e),
                    "success": False
                }
        
        elif action == 'predict':
            # Make prediction
            try:
                prediction_data = {
                    "pregnancies": int(request.form['pregnancies']),
                    "glucose": int(request.form['glucose']),
                    "blood_pressure": int(request.form['blood_pressure']),
                    "skin_thickness": int(request.form['skin_thickness']),
                    "insulin": int(request.form['insulin']),
                    "bmi": float(request.form['bmi']),
                    "diabetes_pedigree_function": float(request.form['diabetes_pedigree_function']),
                    "age": int(request.form['age'])
                }
                
                response = requests.post(f"{API_BASE_URL}/predict", 
                                       json=prediction_data,
                                       headers={'Content-Type': 'application/json'})
                
                if response.status_code == 200:
                    prediction_result = response.json()
                else:
                    error_message = f"Prediction failed. Status code: {response.status_code}"
                    
            except ValueError as e:
                error_message = f"Invalid input data: {str(e)}"
            except requests.exceptions.RequestException as e:
                error_message = f"Error connecting to API: {str(e)}"
    
    return render_template('index.html', 
                         patient_data=patient_data,
                         prediction_result=prediction_result,
                         error_message=error_message,
                         health_result=health_result)


if __name__ == '__main__':
    # app.run(debug=True, port=5001) # Localhost
    app.run(debug=True, host='0.0.0.0', port=5001) # Containerized
