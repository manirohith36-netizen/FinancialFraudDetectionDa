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
df = pd.read_csv("Data/synthetic_fraud_dataset1.csv")

st.title("💰 Transaction Analysis")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Transaction Amount",
    f"${df['Transaction_Amount'].sum():,.0f}"
)

col2.metric(
    "Average Transaction",
    f"${df['Transaction_Amount'].mean():,.2f}"
)

col3.metric(
    "Maximum Transaction",
    f"${df['Transaction_Amount'].max():,.2f}"
)

st.divider()

# Charts Row 1
col1, col2 = st.columns(2)

with col1:

    fig_amount = px.histogram(
        df,
        x="Transaction_Amount",
        nbins=30,
        title="Transaction Amount Distribution"
    )

    st.plotly_chart(
        fig_amount,
        use_container_width=True
    )

with col2:

    trans_type = (
        df.groupby("Transaction_Type")
        ["Transaction_Amount"]
        .sum()
        .reset_index()
    )

    fig_type = px.bar(
        trans_type,
        x="Transaction_Type",
        y="Transaction_Amount",
        title="Transaction Amount by Type",
        color="Transaction_Amount"
    )

    st.plotly_chart(
        fig_type,
        use_container_width=True
    )

# Charts Row 2
col1, col2 = st.columns(2)

with col1:

    location_amount = (
        df.groupby("Location")
        ["Transaction_Amount"]
        .sum()
        .reset_index()
    )

    fig_location = px.pie(
        location_amount,
        names="Location",
        values="Transaction_Amount",
        title="Transaction Amount by Location"
    )

    st.plotly_chart(
        fig_location,
        use_container_width=True
    )

with col2:

    device_amount = (
        df.groupby("Device_Type")
        ["Transaction_Amount"]
        .sum()
        .reset_index()
    )

    fig_device = px.bar(
        device_amount,
        x="Device_Type",
        y="Transaction_Amount",
        title="Transaction Amount by Device Type",
        color="Transaction_Amount"
    )

    st.plotly_chart(
        fig_device,
        use_container_width=True
    )

st.subheader("Top 20 Transactions")

top_transactions = df.sort_values(
    by="Transaction_Amount",
    ascending=False
).head(20)

st.dataframe(
    top_transactions,
    use_container_width=True
)