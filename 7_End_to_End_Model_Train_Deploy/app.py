# pip install flask requests

# A simple Flask web app to interact with the FastAPI model prediction endpoint
# To run the App, run: python app.py
# Access the app at: http://127.0.0.1:5001

# Note:FastAPI server (api.py) must be running on 127.0.0.1:8081

# Import necessary libraries
from flask import Flask, render_template, request
import requests

# Initialize the Flask application
app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8081/predict"
# FASTAPI_URL = "http://pima-diabetes-predictor-api:8081/predict"

# Home route to display the form and handle submissions
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    # Handle form submission
    if request.method == 'POST':
        try:
            # Collect form data
            data = {
                "pregnancies": int(request.form['pregnancies']),
                "glucose": int(request.form['glucose']),
                "blood_pressure": int(request.form['blood_pressure']),
                "skin_thickness": int(request.form['skin_thickness']),
                "insulin": int(request.form['insulin']),
                "bmi": float(request.form['bmi']),
                "diabetes_pedigree_function": float(request.form['diabetes_pedigree_function']),
                "age": int(request.form['age'])
            }
            # Send data to FastAPI for prediction
            response = requests.post(FASTAPI_URL, json=data)
            if response.status_code == 200:
                result = response.json()
            else:
                error = f"FastAPI error: {response.text}"
        except Exception as e:
            error = str(e)
    
    # Render the form with results or errors
    return render_template('index.html', result=result, error=error)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
