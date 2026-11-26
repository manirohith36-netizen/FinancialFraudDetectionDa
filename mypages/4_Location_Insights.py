import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("Data/synthetic_fraud_dataset1.csv")

st.title("🌍 Location Insights")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Locations",
    df["Location"].nunique()
)

highest_location = (
    df.groupby("Location")["Fraud_Label"]
    .sum()
    .idxmax()
)

col2.metric(
    "Highest Fraud Location",
    highest_location
)

col3.metric(
    "Total Fraud Cases",
    int(df["Fraud_Label"].sum())
)

st.divider()

# Row 1
col1, col2 = st.columns(2)

with col1:

    fraud_location = (
        df.groupby("Location")
        ["Fraud_Label"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        fraud_location,
        x="Location",
        y="Fraud_Label",
        color="Fraud_Label",
        title="Fraud Cases by Location"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:

    amount_location = (
        df.groupby("Location")
        ["Transaction_Amount"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        amount_location,
        names="Location",
        values="Transaction_Amount",
        title="Transaction Amount by Location"
    )

    st.plotly_chart(fig2, use_container_width=True)

# Row 2
location_count = (
    df.groupby("Location")
    .size()
    .reset_index(name="Transactions")
)

fig3 = px.bar(
    location_count,
    x="Location",
    y="Transactions",
    title="Total Transactions by Location",
    color="Transactions"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Location Summary")

location_summary = (
    df.groupby("Location")
    .agg({
        "Transaction_Amount":"sum",
        "Fraud_Label":"sum"
    })
    .reset_index()
)

st.dataframe(
    location_summary,
    use_container_width=True
)