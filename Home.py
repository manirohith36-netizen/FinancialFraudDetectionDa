import streamlit as st

st.set_page_config(
    page_title="Financial Fraud Detection System",
    page_icon="🚨",
    layout="wide"
)

# Custom Style
st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #374151;
}
</style>
""", unsafe_allow_html=True)

st.title("🚨 Financial Fraud Detection System")

st.markdown("""
## 📌 Project Overview

This project analyzes financial transactions and identifies fraudulent activities using interactive dashboards and Machine Learning.

### 🎯 Objectives
- Detect fraudulent transactions
- Analyze customer behavior
- Identify risky locations
- Evaluate transaction patterns
- Predict fraud using Machine Learning

### 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Plotly
- Scikit-Learn

### 📊 Dashboards Included
✅ Executive Summary

✅ Fraud Analysis

✅ Transaction Analysis

✅ Location Insights

✅ Customer Risk Analysis

✅ ML Prediction
""")

st.info("Use the left sidebar to navigate between dashboards.")