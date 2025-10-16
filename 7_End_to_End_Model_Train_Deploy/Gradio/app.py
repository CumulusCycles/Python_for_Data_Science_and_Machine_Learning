import gradio as gr
import joblib
import numpy as np
import pandas as pd
import os
import sys

# Add parent directory to path to access the model
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(parent_dir, 'pima_diabetes_lr_predicter.joblib')

# Load the trained model
try:
    model = joblib.load(model_path)
    print(f"Model loaded successfully from {model_path}")
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)

# Define prediction function
def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, 
                    insulin, bmi, diabetes_pedigree_function, age):
    """
    Predict diabetes based on patient features
    """
    try:
        # Create input array
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                               insulin, bmi, diabetes_pedigree_function, age]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Get prediction probabilities if available
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]
            prob_no_diabetes = probabilities[0]
            prob_diabetes = probabilities[1]
        else:
            prob_no_diabetes = 1 - prediction
            prob_diabetes = prediction
        
        # Determine result
        result = "🔴 High Risk - Diabetic" if prediction == 1 else "🟢 Low Risk - Not Diabetic"
        confidence = prob_diabetes if prediction == 1 else prob_no_diabetes
        
        # Create detailed output
        output = f"""
## Prediction Result: {result}
        
**Confidence:** {confidence:.2%}

### Probability Breakdown:
- **Not Diabetic:** {prob_no_diabetes:.2%}
- **Diabetic:** {prob_diabetes:.2%}

### Input Summary:
- Pregnancies: {pregnancies}
- Glucose: {glucose} mg/dl
- Blood Pressure: {blood_pressure} mm Hg
- Skin Thickness: {skin_thickness} mm
- Insulin: {insulin} mu U/ml
- BMI: {bmi:.1f}
- Diabetes Pedigree Function: {diabetes_pedigree_function:.3f}
- Age: {age} years

---
*This is a machine learning prediction for educational purposes only. 
Please consult healthcare professionals for medical advice.*
        """
        
        return output
        
    except Exception as e:
        return f"Error making prediction: {str(e)}"

# Define sample data function
def load_sample_data(sample_type):
    """Load predefined sample data"""
    if sample_type == "High Risk Sample":
        return (8, 155, 85, 40, 210, 35.2, 0.745, 45)
    elif sample_type == "Low Risk Sample":
        return (2, 75, 70, 30, 50, 25.0, 0.500, 22)
    else:  # Average values
        return (3, 120, 70, 23, 79, 27.0, 0.400, 33)

# Define the Gradio interface
def create_interface():
    with gr.Blocks(
        title="Pima Indians Diabetes Prediction",
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {
            font-family: 'Arial', sans-serif;
        }
        .output-markdown {
            font-size: 16px;
        }
        """
    ) as demo:
        
        gr.Markdown("""
        # 🏥 Pima Indians Diabetes Prediction System
        
        This machine learning model predicts the likelihood of diabetes based on diagnostic measurements.
        The model was trained on the famous Pima Indians Diabetes Dataset.
        
        ## How to use:
        1. Enter patient information in the form below
        2. Or use the sample data buttons for quick testing
        3. Click "Predict Diabetes Risk" to get the prediction
        
        ---
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📋 Patient Information")
                
                # Input components
                pregnancies = gr.Slider(
                    minimum=0, maximum=20, value=3, step=1,
                    label="Number of Pregnancies",
                    info="Number of times pregnant"
                )
                
                glucose = gr.Slider(
                    minimum=0, maximum=200, value=120, step=1,
                    label="Glucose Level (mg/dl)",
                    info="Plasma glucose concentration a 2 hours in an oral glucose tolerance test"
                )
                
                blood_pressure = gr.Slider(
                    minimum=0, maximum=150, value=70, step=1,
                    label="Blood Pressure (mm Hg)",
                    info="Diastolic blood pressure"
                )
                
                skin_thickness = gr.Slider(
                    minimum=0, maximum=100, value=23, step=1,
                    label="Skin Thickness (mm)",
                    info="Triceps skin fold thickness"
                )
                
                insulin = gr.Slider(
                    minimum=0, maximum=900, value=79, step=1,
                    label="Insulin (mu U/ml)",
                    info="2-Hour serum insulin"
                )
                
                bmi = gr.Slider(
                    minimum=0.0, maximum=70.0, value=27.0, step=0.1,
                    label="BMI (Body Mass Index)",
                    info="Weight in kg/(height in m)^2"
                )
                
                diabetes_pedigree = gr.Slider(
                    minimum=0.0, maximum=3.0, value=0.4, step=0.001,
                    label="Diabetes Pedigree Function",
                    info="A function which scores likelihood of diabetes based on family history"
                )
                
                age = gr.Slider(
                    minimum=21, maximum=100, value=33, step=1,
                    label="Age (years)",
                    info="Age in years"
                )
                
                # Sample data buttons
                gr.Markdown("### 🎯 Quick Test Samples")
                with gr.Row():
                    high_risk_btn = gr.Button("High Risk Sample", variant="secondary")
                    low_risk_btn = gr.Button("Low Risk Sample", variant="secondary")
                    average_btn = gr.Button("Average Values", variant="secondary")
                
                # Prediction button
                predict_btn = gr.Button("🔍 Predict Diabetes Risk", variant="primary", size="lg")
            
            with gr.Column(scale=1):
                gr.Markdown("### 📊 Prediction Results")
                output = gr.Markdown(
                    """
                    ### Welcome! 👋
                    
                    Enter patient information on the left and click 
                    **"Predict Diabetes Risk"** to get started.
                    
                    You can also try the sample data buttons for quick testing.
                    """,
                    elem_classes=["output-markdown"]
                )
        
        # Event handlers
        predict_btn.click(
            fn=predict_diabetes,
            inputs=[pregnancies, glucose, blood_pressure, skin_thickness,
                   insulin, bmi, diabetes_pedigree, age],
            outputs=output
        )
        
        # Sample data button handlers
        def update_high_risk():
            return load_sample_data("High Risk Sample")
        
        def update_low_risk():
            return load_sample_data("Low Risk Sample")
        
        def update_average():
            return load_sample_data("Average Values")
        
        high_risk_btn.click(
            fn=update_high_risk,
            outputs=[pregnancies, glucose, blood_pressure, skin_thickness,
                    insulin, bmi, diabetes_pedigree, age]
        )
        
        low_risk_btn.click(
            fn=update_low_risk,
            outputs=[pregnancies, glucose, blood_pressure, skin_thickness,
                    insulin, bmi, diabetes_pedigree, age]
        )
        
        average_btn.click(
            fn=update_average,
            outputs=[pregnancies, glucose, blood_pressure, skin_thickness,
                    insulin, bmi, diabetes_pedigree, age]
        )
        
        # Footer
        gr.Markdown("""
        ---
        ### ℹ️ About This Model
        
        This logistic regression model was trained on the Pima Indians Diabetes Dataset, 
        which contains diagnostic measurements for predicting diabetes onset.
        
        **Features used:**
        - Pregnancies, Glucose, Blood Pressure, Skin Thickness
        - Insulin, BMI, Diabetes Pedigree Function, Age
        
        **Important:** This tool is for educational purposes only and should not be used 
        for actual medical diagnosis. Always consult healthcare professionals for medical advice.
        
        ---
        *Built with ❤️ using Gradio and scikit-learn*
        """)
    
    return demo

# Main execution
if __name__ == "__main__":
    # Create and launch the interface
    demo = create_interface()
    demo.launch(
        share=False,  # Set to True if you want to create a public link
        server_name="0.0.0.0",  # Allow external connections
        server_port=7860,
        show_error=True
    )