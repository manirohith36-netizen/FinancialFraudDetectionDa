import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Fraud Command Center",
    page_icon="🚨",
    layout="wide"
)

# Load Data
df = pd.read_csv("Data/synthetic_fraud_dataset1.csv")

# KPI Values
total_transactions = len(df)
fraud_cases = int(df["Fraud_Label"].sum())

fraud_rate = round(
    (fraud_cases / total_transactions) * 100,
    2
)

fraud_amount = df[df["Fraud_Label"] == 1][
    "Transaction_Amount"
].sum()

# Custom CSS
st.markdown("""
<style>

.stApp {
    background-color: #081420;
}

h1,h2,h3,p,li {
    color:white;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg,#0f2d4a,#123b63);
    padding:20px;
    border-radius:15px;
    border:1px solid #1f5f8b;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🚨 Financial Fraud Command Center")

st.success(
    "✅ System Status : ONLINE | Fraud Monitoring Active"
)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Transactions",
    f"{total_transactions:,}"
)

col2.metric(
    "Fraud Cases",
    fraud_cases
)

col3.metric(
    "Fraud Rate",
    f"{fraud_rate}%"
)

col4.metric(
    "Fraud Amount",
    f"${fraud_amount:,.0f}"
)

st.divider()

st.subheader("🎯 Dashboard Modules")

st.markdown("""
✅ Executive Summary

✅ Fraud Analysis

✅ Transaction Analysis

✅ Location Insights

✅ Customer Risk Analysis

✅ Machine Learning Prediction
""")

st.info(
    "Use the left sidebar to navigate between dashboards."
)
