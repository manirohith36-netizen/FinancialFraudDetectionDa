import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("Data/synthetic_fraud_dataset1.csv")

st.title("👤 Customer Risk Analysis")

# KPIs
col1, col2, col3 = st.columns(3)

high_risk_users = df[df["Previous_Fraudulent_Activity"] == 1]

col1.metric(
    "High Risk Users",
    high_risk_users["User_ID"].nunique()
)

col2.metric(
    "Users with Previous Fraud",
    int(df["Previous_Fraudulent_Activity"].sum())
)

col3.metric(
    "Total Customers",
    df["User_ID"].nunique()
)

st.divider()

# Previous Fraud Activity
col1, col2 = st.columns(2)

with col1:

    prev_fraud = (
        df.groupby("Previous_Fraudulent_Activity")
        .size()
        .reset_index(name="Customers")
    )

    fig1 = px.pie(
        prev_fraud,
        names="Previous_Fraudulent_Activity",
        values="Customers",
        title="Previous Fraud Activity"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:

    card_age = px.box(
        df,
        x="Fraud_Label",
        y="Card_Age",
        title="Card Age vs Fraud"
    )

    st.plotly_chart(card_age, use_container_width=True)

# Daily Transaction Analysis

daily_txn = (
    df.groupby("Daily_Transaction_Count")
    ["Fraud_Label"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    daily_txn,
    x="Daily_Transaction_Count",
    y="Fraud_Label",
    title="Fraud by Daily Transaction Count",
    color="Fraud_Label"
)

st.plotly_chart(fig2, use_container_width=True)

# High Risk Customers

st.subheader("High Risk Customer Records")

risk_table = df[
    df["Previous_Fraudulent_Activity"] == 1
]

st.dataframe(
    risk_table.head(20),
    use_container_width=True
)
