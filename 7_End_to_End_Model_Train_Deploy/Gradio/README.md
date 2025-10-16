# 🏥 Pima Indians Diabetes Prediction - Gradio UI

This is a user-friendly Gradio web interface for the Pima Indians Diabetes prediction model built with [Gradio](https://gradio.app). The interface allows users to input patient data and get real-time diabetes risk predictions.

## ✨ Features

- **Interactive Web Interface**: Clean, intuitive Gradio-based UI
- **Real-time Predictions**: Instant diabetes risk assessment
- **Probability Scores**: Shows confidence levels for predictions
- **Sample Data**: Pre-loaded examples for quick testing
- **Responsive Design**: Works on desktop and mobile devices
- **Educational Focus**: Clear explanations and medical disclaimers

## 🏗️ Model Information

- **Model Type**: Logistic Regression
- **Dataset**: Pima Indians Diabetes Dataset
- **Features**: 8 diagnostic measurements
- **Output**: Binary classification (Diabetic/Not Diabetic) with probabilities

### Input Features:

1. **Pregnancies**: Number of times pregnant
2. **Glucose**: Plasma glucose concentration (mg/dl)
3. **Blood Pressure**: Diastolic blood pressure (mm Hg)
4. **Skin Thickness**: Triceps skin fold thickness (mm)
5. **Insulin**: 2-Hour serum insulin (mu U/ml)
6. **BMI**: Body mass index (weight in kg/(height in m)^2)
7. **Diabetes Pedigree Function**: Genetic likelihood score
8. **Age**: Age in years

## 🚀 Quick Start

```bash
# Install requirements
pip install -r requirements.txt

# Run the app
python app.py
```

## 📱 Using the Interface

1. **Open your browser** and go to `http://localhost:7860`
2. **Enter patient data** using the sliders on the left
3. **Try sample data** using the quick test buttons:
   - **High Risk Sample**: Example of a diabetic patient
   - **Low Risk Sample**: Example of a non-diabetic patient
   - **Average Values**: Typical baseline values
4. **Click "Predict Diabetes Risk"** to get the prediction
5. **Review results** including confidence scores and probability breakdown

## 🎯 Sample Test Cases

### High Risk Example:

- Pregnancies: 8
- Glucose: 155 mg/dl
- Blood Pressure: 85 mm Hg
- Skin Thickness: 40 mm
- Insulin: 210 mu U/ml
- BMI: 35.2
- Diabetes Pedigree: 0.745
- Age: 45 years

### Low Risk Example:

- Pregnancies: 2
- Glucose: 75 mg/dl
- Blood Pressure: 70 mm Hg
- Skin Thickness: 30 mm
- Insulin: 50 mu U/ml
- BMI: 25.0
- Diabetes Pedigree: 0.500
- Age: 22 years

## 🔧 Configuration

The app runs on:

- **Host**: `0.0.0.0` (accessible from any network interface)
- **Port**: `7860`
- **Share**: `False` (local only - set to `True` in code for public sharing)

## 📊 Understanding the Results

The model provides:

- **Binary Prediction**: Diabetic or Not Diabetic
- **Confidence Score**: How certain the model is about its prediction
- **Probability Breakdown**: Separate probabilities for each class
- **Risk Level Indicators**: Color-coded results (🟢 Low Risk / 🔴 High Risk)

## ⚠️ Important Disclaimers

- **Educational Use Only**: This tool is for learning and demonstration purposes
- **Not for Medical Diagnosis**: Never use for actual medical decisions
- **Consult Professionals**: Always seek professional medical advice
- **Model Limitations**: Based on historical data and may not reflect individual cases

## 🛠️ Technical Details

- **Framework**: Gradio 4.0+
- **Model Format**: Joblib (.joblib)
- **Backend**: scikit-learn Logistic Regression
- **UI Theme**: Gradio Soft theme with custom CSS
- **Dependencies**: See `requirements.txt`

## 📁 File Structure

```
Gradio/
├── app.py              # Main Gradio application
├── launch.py           # Launcher script with auto-install
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🐛 Troubleshooting

### Common Issues:

1. **Model not found error**:

   - Ensure the `pima_diabetes_lr_predicter.joblib` file exists in the parent directory
   - Check file permissions

2. **Import errors**:

   - Run `pip install -r requirements.txt`
   - Ensure you're using Python 3.8+

3. **Port already in use**:

   - Change the port in `app.py` (line with `server_port=7860`)
   - Or stop other processes using port 7860

4. **Browser doesn't open automatically**:
   - Manually visit `http://localhost:7860`
   - Check firewall settings

---

_Built with ❤️ using Gradio and scikit-learn_
