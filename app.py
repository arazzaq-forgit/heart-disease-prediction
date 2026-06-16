import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Load Model and Scaler
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title
st.title("❤️ Heart Disease Prediction")
st.markdown("### Enter the patient's medical details below")

# Input Fields
age = st.number_input("Age", min_value=20, max_value=100, value=50)

sex = st.selectbox(
    "Sex",
    options=[0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

cp = st.selectbox(
    "Chest Pain Type",
    options=[0, 1, 2, 3]
)

trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Cholesterol (mg/dl)",
    min_value=100,
    max_value=600,
    value=200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

restecg = st.selectbox(
    "Resting ECG",
    options=[0, 1, 2]
)

thalach = st.number_input(
    "Maximum Heart Rate Achieved",
    min_value=60,
    max_value=220,
    value=150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

oldpeak = st.number_input(
    "Oldpeak",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope = st.selectbox(
    "Slope",
    options=[0, 1, 2]
)

ca = st.selectbox(
    "Number of Major Vessels (CA)",
    options=[0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thal",
    options=[0, 1, 2, 3]
)

# Prediction Button
if st.button("Predict"):

    input_data = pd.DataFrame([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]], columns=[
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal"
    ])

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.error("⚠️ The model predicts a high likelihood of Heart Disease.")
    else:
        st.success("✅ The model predicts a low likelihood of Heart Disease.")

st.markdown("---")
st.caption("Built with ❤️ using Python, Scikit-learn and Streamlit")