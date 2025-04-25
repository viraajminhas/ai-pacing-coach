
import streamlit as st
import requests

st.title("AI-Powered Pacing Coach")
mile_pr = st.number_input("Enter your mile PR (in seconds):", min_value=200.0, max_value=500.0)

if st.button("Predict Splits"):
    response = requests.post("http://localhost:8000/predict", json={"mile_pr": mile_pr})
    if response.status_code == 200:
        splits = response.json()["recommended_splits"]
        st.write("Predicted Lap Splits (sec):", splits)
    else:
        st.write("Error:", response.text)
