import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

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
# Load Data
df = pd.read_csv("Data/synthetic_fraud_dataset1.csv")

# KPIs
total_transactions = len(df)
fraud_transactions = df["Fraud_Label"].sum()
fraud_rate = round((fraud_transactions / total_transactions) * 100, 2)
total_fraud_amount = df[df["Fraud_Label"] == 1]["Transaction_Amount"].sum()

st.title("🏠 Executive Summary")

st.markdown("### Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Transactions",
    f"{total_transactions:,}"
)

col2.metric(
    "Fraud Transactions",
    f"{fraud_transactions:,}"
)

col3.metric(
    "Fraud Rate",
    f"{fraud_rate}%"
)

col4.metric(
    "Fraud Amount",
    f"${total_fraud_amount:,.0f}"
)
st.divider()


st.subheader("Fraud vs Legitimate Transactions")

fraud_counts = df["Fraud_Label"].value_counts()

fig = px.pie(
    values=fraud_counts.values,
    names=["Legitimate", "Fraud"]
)

st.plotly_chart(fig, use_container_width=True)
st.divider()

st.subheader("Top 10 High Risk Transactions")

top_transactions = df.sort_values(
    by="Transaction_Amount",
    ascending=False
).head(10)

st.dataframe(
    top_transactions,
    use_container_width=True
)

col1, col2 = st.columns(2)

# Fraud by Location
with col1:

    location_fraud = (
        df.groupby("Location")
        ["Fraud_Label"]
        .sum()
        .reset_index()
    )

    fig_location = px.bar(
        location_fraud,
        x="Location",
        y="Fraud_Label",
        title="Fraud by Location",
        color="Fraud_Label"
    )

    st.plotly_chart(
        fig_location,
        use_container_width=True
    )

# Fraud by Device
with col2:

    device_fraud = (
        df.groupby("Device_Type")
        ["Fraud_Label"]
        .sum()
        .reset_index()
    )

    fig_device = px.bar(
        device_fraud,
        x="Device_Type",
        y="Fraud_Label",
        title="Fraud by Device Type",
        color="Fraud_Label"
    )

    st.plotly_chart(
        fig_device,
        use_container_width=True
    )
    st.subheader("Fraud by Transaction Type")

transaction_fraud = (
    df.groupby("Transaction_Type")
    ["Fraud_Label"]
    .sum()
    .reset_index()
)

fig_trans = px.bar(
    transaction_fraud,
    x="Transaction_Type",
    y="Fraud_Label",
    color="Fraud_Label",
    title="Fraud by Transaction Type"
)
st.plotly_chart(fig_trans, use_container_width=True)


