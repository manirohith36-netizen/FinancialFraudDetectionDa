import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Fraud Command Center",
    page_icon="🚨",
    layout="wide"
)

# Load Data
df = pd.read_csv("Data/synthetic_fraud_dataset1.csv")

# KPIs
total_transactions = len(df)
fraud_cases = int(df["Fraud_Label"].sum())

fraud_rate = round(
    (fraud_cases / total_transactions) * 100,
    2
)

fraud_amount = (
    df[df["Fraud_Label"] == 1]["Transaction_Amount"]
    .sum()
)

# Theme
st.markdown("""
<style>

.stApp{
    background-color:#071A2E;
}

h1,h2,h3,h4{
    color:#FFFFFF !important;
}

p,li,span{
    color:#D6E4F0 !important;
}

section[data-testid="stSidebar"]{
    background-color:#102A43;
}

[data-testid="stMetric"]{
    background-color:#123B63;
    border:1px solid #1F6AA5;
    padding:18px;
    border-radius:15px;
}

hr{
    border-color:#1F6AA5;
}

</style>
""", unsafe_allow_html=True)

# Header
st.title("🚨 Financial Fraud Command Center")

st.markdown("""
<div style="
background:#0F3A2D;
padding:15px;
border-radius:10px;
color:white;
font-weight:bold;
margin-bottom:10px;">
✅ System Status : ONLINE | Fraud Monitoring Active
</div>
""", unsafe_allow_html=True)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Transactions",
        f"{total_transactions:,}"
    )

with col2:
    st.metric(
        "Fraud Cases",
        f"{fraud_cases:,}"
    )

with col3:
    st.metric(
        "Fraud Rate",
        f"{fraud_rate}%"
    )

with col4:
    st.metric(
        "Fraud Amount",
        f"${fraud_amount:,.0f}"
    )

st.divider()

st.subheader("📊 Dashboard Modules")

st.markdown("""
✅ Executive Summary

✅ Fraud Analysis

✅ Transaction Analysis

✅ Location Insights

✅ Customer Risk Analysis

✅ Machine Learning Prediction
""")

st.divider()

st.subheader("🎯 Project Objective")

st.write(
"""
This Financial Fraud Detection System analyzes transactional data,
identifies fraud patterns, evaluates customer risk, and provides
machine learning based fraud prediction through interactive dashboards.
"""
)

st.info(
    "Use the left sidebar to navigate through all dashboards."
)