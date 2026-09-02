import streamlit as st
import pandas as pd
import numpy as np

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# PAGE SETTINGS


st.set_page_config(
    page_title="AI Revenue Recovery",
    page_icon="💰",
    layout="wide"
)


# FIND DATASET


current_folder = Path(__file__).resolve().parent

file1 = current_folder / "payments.csv"
file2 = current_folder / "data" / "payments.csv"

if file1.exists():
    data_file = file1
elif file2.exists():
    data_file = file2
else:
    st.error("payments.csv file not found.")
    st.stop()



# LOAD DATA


data = pd.read_csv(data_file)



# CREATE DEMO RECOVERY OUTCOME


np.random.seed(42)

score = (
    0.85
    - 0.035 * data["days_overdue"]
    - 0.18 * data["previous_failures"]
    - 0.000005 * data["amount"]
)

recovery_chance = 1 / (1 + np.exp(-score))

random_values = np.random.rand(len(data))

data["recovery_status"] = np.where(
    random_values < recovery_chance,
    "Recovered",
    "Not Recovered"
)



# MACHINE LEARNING


features = [
    "amount",
    "days_overdue",
    "previous_failures",
    "customer_age"
]

X = data[features]
y = data["recovery_status"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


model = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]
)

model.fit(X_train, y_train)


# MODEL EVALUATION

prediction = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    prediction
)

# RECOVERY PROBABILITY


probability = model.predict_proba(X)

recovered_index = list(
    model.classes_
).index("Recovered")

data["recovery_probability"] = (
    probability[:, recovered_index] * 100
)

data["recovery_probability"] = (
    data["recovery_probability"].round(2)
)



# RISK LEVEL


data["risk_level"] = "Low"

data.loc[
    data["recovery_probability"] < 40,
    "risk_level"
] = "High"

data.loc[
    (data["recovery_probability"] >= 40) &
    (data["recovery_probability"] < 70),
    "risk_level"
] = "Medium"



# PRIORITY


data["priority"] = "Routine"

data.loc[
    data["risk_level"] == "Medium",
    "priority"
] = "Follow-up"

data.loc[
    data["risk_level"] == "High",
    "priority"
] = "Urgent"


# BUSINESS SUMMARY


total_customers = len(data)

paid_count = len(
    data[data["payment_status"] == "Paid"]
)

failed_count = len(
    data[data["payment_status"] == "Failed"]
)

failed_amount = data.loc[
    data["payment_status"] == "Failed",
    "amount"
].sum()



# RISK SUMMARY


high_risk = len(
    data[data["risk_level"] == "High"]
)

medium_risk = len(
    data[data["risk_level"] == "Medium"]
)

low_risk = len(
    data[data["risk_level"] == "Low"]
)


# URGENT SUMMARY


urgent_customers = data[
    data["priority"] == "Urgent"
].copy()

urgent_amount = urgent_customers[
    "amount"
].sum()


# TITLE


st.title("💰 AI Revenue Recovery System")

st.caption(
    "Machine Learning based payment risk analysis "
    "and recovery prioritization"
)

st.markdown("---")


# BUSINESS OVERVIEW


st.header("📊 Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    total_customers
)

col2.metric(
    "Paid Payments",
    paid_count
)

col3.metric(
    "Failed Payments",
    failed_count
)

col4.metric(
    "Failed Amount",
    f"₹{failed_amount:,.0f}"
)

# MACHINE LEARNING SUMMARY

st.header("🤖 Machine Learning Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Model",
    "Logistic Regression"
)

col2.metric(
    "Validation Accuracy",
    f"{accuracy * 100:.1f}%"
)

col3.metric(
    "Predicted Recoveries",
    len(
        data[
            data["recovery_probability"] >= 50
        ]
    )
)



# RISK SUMMARY

st.header("⚠️ Customer Risk Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🔴 High Risk",
    high_risk
)

col2.metric(
    "🟡 Medium Risk",
    medium_risk
)

col3.metric(
    "🟢 Low Risk",
    low_risk
)


# CHARTS

st.header("📈 Payment & Risk Analysis")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:

    st.subheader("Payment Status")

    payment_chart = data[
        "payment_status"
    ].value_counts()

    st.bar_chart(payment_chart)


with chart_col2:

    st.subheader("Customer Risk Level")

    risk_chart = data[
        "risk_level"
    ].value_counts()

    st.bar_chart(risk_chart)


# URGENT RECOVERY SUMMARY


st.header("🚨 Urgent Recovery Summary")

col1, col2 = st.columns(2)

col1.metric(
    "Urgent Customers",
    len(urgent_customers)
)

col2.metric(
    "Urgent Payment Amount",
    f"₹{urgent_amount:,.0f}"
)


# TOP URGENT CUSTOMERS


st.subheader("Top Urgent Recovery Customers")

urgent_table = urgent_customers.sort_values(
    by=[
        "days_overdue",
        "amount"
    ],
    ascending=[
        False,
        False
    ]
)

st.dataframe(
    urgent_table[
        [
            "customer_id",
            "amount",
            "days_overdue",
            "previous_failures",
            "recovery_probability",
            "risk_level",
            "priority"
        ]
    ].head(10),
    width="stretch"
)



# RECOVERY ACTION CENTER


st.header("🎯 Recovery Action Center")

risk_choice = st.selectbox(
    "Select Risk Level",
    [
        "All",
        "High",
        "Medium",
        "Low"
    ]
)

if risk_choice == "All":

    filtered_data = data.copy()

else:

    filtered_data = data[
        data["risk_level"] == risk_choice
    ].copy()


st.write(
    "Customers found:",
    len(filtered_data)
)

st.dataframe(
    filtered_data[
        [
            "customer_id",
            "amount",
            "days_overdue",
            "previous_failures",
            "recovery_probability",
            "risk_level",
            "priority"
        ]
    ].sort_values(
        by="days_overdue",
        ascending=False
    ),
    width="stretch"
)

# CUSTOMER SEARCH


st.header("🔎 Customer Search")

customer_id = st.text_input(
    "Enter Customer ID",
    placeholder="Example: C034"
)


if customer_id:

    customer = data[
        data["customer_id"].str.upper()
        == customer_id.upper()
    ]

    if len(customer) > 0:

        selected_customer = customer.iloc[0]

        st.subheader("Customer Details")

        st.dataframe(
            customer[
                [
                    "customer_id",
                    "amount",
                    "days_overdue",
                    "previous_failures",
                    "recovery_probability",
                    "risk_level",
                    "priority"
                ]
            ],
            width="stretch"
        )

        # RECOVERY RECOMMENDATION
      

        st.subheader("💡 Recovery Recommendation")

        if selected_customer["risk_level"] == "High":

            st.error(
                "Recommended Action: Contact the customer "
                "immediately and send a payment reminder."
            )

        elif selected_customer["risk_level"] == "Medium":

            st.warning(
                "Recommended Action: Send a follow-up "
                "reminder and monitor the payment."
            )

        else:

            st.success(
                "Recommended Action: Routine monitoring "
                "is sufficient."
            )

        # PERSONALIZED MESSAGE
      

        st.subheader("✉️ Personalized Recovery Message")

        if selected_customer["days_overdue"] == 0:

            message = (
                f"Hello {selected_customer['customer_id']}, "
                f"your payment of ₹{selected_customer['amount']:,.0f} "
                f"is currently on time. Thank you for your timely payment."
            )

        else:

            message = (
                f"Hello {selected_customer['customer_id']}, "
                f"your payment of ₹{selected_customer['amount']:,.0f} "
                f"is overdue by "
                f"{selected_customer['days_overdue']} days. "
                f"Please complete the payment at the earliest."
            )

            if selected_customer["risk_level"] == "High":

                message += (
                    " Please contact the payment support team "
                    "if you are facing any difficulty."
                )

            elif selected_customer["risk_level"] == "Medium":

                message += (
                    " We kindly request you to complete "
                    "the payment soon."
                )

        st.info(message)

    else:

        st.warning("Customer ID not found.")



# DOWNLOAD REPORT

st.header("📥 Download Recovery Report")

report = data[
    [
        "customer_id",
        "amount",
        "days_overdue",
        "previous_failures",
        "recovery_probability",
        "risk_level",
        "priority"
    ]
].copy()

report_csv = report.to_csv(
    index=False
)

st.download_button(
    label="Download Recovery Report",
    data=report_csv,
    file_name="recovery_priority_report.csv",
    mime="text/csv",
    width="stretch"
)

# FOOTER


st.markdown("---")

st.caption(
    "AI Revenue Recovery System | Internship Project | "
    "Synthetic data used for demonstration"
)
