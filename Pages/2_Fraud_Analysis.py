import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("Data/synthetic_fraud_dataset1.csv")

fraud_df = df[df["Fraud_Label"] == 1]

st.title("🚨 Fraud Analysis")
location_filter = st.sidebar.multiselect(
    "Location",
    df["Location"].unique(),
    default=df["Location"].unique()
)

fraud_df = fraud_df[
    fraud_df["Location"].isin(location_filter)
]

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Fraud Cases",
    len(fraud_df)
)

col2.metric(
    "Fraud Amount",
    f"${fraud_df['Transaction_Amount'].sum():,.0f}"
)

col3.metric(
    "Affected Users",
    fraud_df["User_ID"].nunique()
)

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:

    merchant_chart = px.bar(
        fraud_df.groupby("Merchant_Category")
        ["Fraud_Label"]
        .count()
        .reset_index(),
        x="Merchant_Category",
        y="Fraud_Label",
        title="Fraud by Merchant Category",
        color="Fraud_Label"
    )

    st.plotly_chart(
        merchant_chart,
        use_container_width=True
    )

with col2:

    card_chart = px.pie(
        fraud_df,
        names="Card_Type",
        title="Fraud by Card Type"
    )

    st.plotly_chart(
        card_chart,
        use_container_width=True
    )

st.subheader("Fraud Transactions")

top_fraud = fraud_df.sort_values(
    by="Transaction_Amount",
    ascending=False
).head(20)

st.dataframe(
    top_fraud,
    use_container_width=True
)
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

fraud_trend = (
    fraud_df.groupby("Date")
    .size()
    .reset_index(name="Fraud Count")
)

fig_trend = px.line(
    fraud_trend,
    x="Date",
    y="Fraud Count",
    title="Fraud Trend Over Time"
)

st.plotly_chart(
    fig_trend,
    use_container_width=True
)