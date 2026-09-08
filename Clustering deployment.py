import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load saved files
# -----------------------------
model = joblib.load("clustering_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Country Clustering",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Global Development Clustering")
st.write(
    "This application assigns a country to a development cluster "
    "using the trained clustering model."
)

st.divider()


# -----------------------------
# User Inputs
# -----------------------------
st.subheader("Enter Country Indicators")

input_data = {}

for feature in features:
    input_data[feature] = st.number_input(
        f"{feature}",
        value=0.0
    )


# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Cluster"):

    input_df = pd.DataFrame([input_data])

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict cluster
    cluster = model.predict(input_scaled)[0]

    st.success(f"Predicted Cluster: {cluster}")


    # -------------------------
    # Cluster interpretation
    # -------------------------

    cluster_meanings = {
        0: "Low development / higher risk group",
        1: "Moderate development group",
        2: "High development / lower risk group"
    }

    interpretation = cluster_meanings.get(
        cluster,
        "Cluster interpretation not defined."
    )

    st.info(f"Cluster Interpretation: {interpretation}")