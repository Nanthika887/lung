import streamlit as st
import pandas as pd
import joblib

model = joblib.load("lung_cancer_model.pkl")

st.title("Lung Cancer Prediction App")

age = st.number_input("Age", 1, 120, 50)

if st.button("Test"):
    st.success("Model Loaded Successfully")