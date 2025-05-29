import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# App title and description
st.set_page_config(page_title="Diabetes Predictor", layout="centered")
st.title("🩺 Diabetes Prediction App")
st.markdown("This app predicts whether a person is **diabetic or not** based on health parameters.")

# Sidebar for inputs
st.sidebar.header("🧾 Enter Patient Details")

preg = st.sidebar.number_input("Pregnancies", min_value=0, step=1)
glucose = st.sidebar.number_input("Glucose", min_value=0)
bp = st.sidebar.number_input("Blood Pressure", min_value=0)
skin = st.sidebar.number_input("Skin Thickness", min_value=0)
insulin = st.sidebar.number_input("Insulin", min_value=0)
bmi = st.sidebar.number_input("BMI", min_value=0.0, format="%.1f")
dpf = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.sidebar.number_input("Age", min_value=0)

# Prediction button
if st.sidebar.button("🧠 Predict Diabetes"):
    with st.spinner("Analyzing input and predicting..."):
        # Prepare and scale input
        input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
        input_scaled = scaler.transform(input_data)

        # Make prediction
        result = model.predict(input_scaled)[0]

        st.subheader("🔍 Prediction Result")
        if result == 1:
            st.error("🚨 The model predicts: **Diabetes Positive**")
        else:
            st.success("✅ The model predicts: **Diabetes Negative**")

# Footer
st.markdown("---")
st.markdown("Made with using Streamlit | [GitHub](https://github.com/SathishB-1)")
