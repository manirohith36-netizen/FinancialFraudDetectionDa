import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

st.set_page_config(layout="wide")

st.title("🤖 ML Fraud Prediction")

# Load Data
df = pd.read_csv("Data/synthetic_fraud_dataset1.csv")

# Encoding
data = df.copy()

categorical_cols = [
    "Transaction_Type",
    "Device_Type",
    "Location",
    "Merchant_Category",
    "Card_Type"
]

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le

# Features
X = data[
    [
        "Transaction_Amount",
        "Transaction_Type",
        "Device_Type",
        "Location",
        "Merchant_Category",
        "Previous_Fraudulent_Activity",
        "Daily_Transaction_Count",
        "Card_Age"
    ]
]

y = data["Fraud_Label"]

# Train Model
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1 = f1_score(y_test, pred)

st.subheader("📊 Model Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    f"{accuracy*100:.2f}%"
)

col2.metric(
    "Precision",
    f"{precision*100:.2f}%"
)

col3.metric(
    "Recall",
    f"{recall*100:.2f}%"
)

col4.metric(
    "F1 Score",
    f"{f1*100:.2f}%"
)

st.divider()

# Feature Importance
st.subheader("📌 Feature Importance")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

fig = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    title="Feature Importance Ranking"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Prediction Section
st.subheader("🔍 Predict Transaction")

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=500.0
)

previous_fraud = st.selectbox(
    "Previous Fraud Activity",
    [0, 1]
)

daily_count = st.slider(
    "Daily Transaction Count",
    1,
    20,
    5
)

card_age = st.slider(
    "Card Age",
    1,
    250,
    50
)

if st.button("Predict Fraud"):

    sample = [[
        amount,
        0,
        0,
        0,
        0,
        previous_fraud,
        daily_count,
        card_age
    ]]

    result = model.predict(sample)
    probability = model.predict_proba(sample)[0][1]

    st.write(
        f"Fraud Probability: {probability:.2%}"
    )

    if result[0] == 1:
        st.error("🚨 Potential Fraud Detected")
    else:
        st.success("✅ Legitimate Transaction")

    if probability > 0.70:
        st.error("🔴 Risk Level: High")
    elif probability > 0.40:
        st.warning("🟡 Risk Level: Medium")
    else:
        st.success("🟢 Risk Level: Low")
