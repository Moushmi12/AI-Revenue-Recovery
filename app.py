import streamlit as st
import pandas as pd

# page settings
st.set_page_config(
    page_title="AI Revenue Recovery",
    page_icon="💰",
    layout="wide"
)

# load data
data = pd.read_csv("payments.csv")

# title
st.title("💰 AI Revenue Recovery System")
st.write("Payment risk analysis and recovery priority dashboard")

# basic calculations
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

# create risk levels
data["risk_level"] = "Low"

data.loc[
    (data["days_overdue"] > 7) |
    (data["previous_failures"] > 1),
    "risk_level"
] = "High"

data.loc[
    (data["days_overdue"].between(4, 7)) &
    (data["previous_failures"] <= 1),
    "risk_level"
] = "Medium"

# create priority
data["priority"] = "Routine"

data.loc[
    data["risk_level"] == "Medium",
    "priority"
] = "Follow-up"

data.loc[
    data["risk_level"] == "High",
    "priority"
] = "Urgent"

# risk counts
high_risk = len(
    data[data["risk_level"] == "High"]
)

medium_risk = len(
    data[data["risk_level"] == "Medium"]
)

low_risk = len(
    data[data["risk_level"] == "Low"]
)

# summary section
st.subheader("Business Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", total_customers)
col2.metric("Paid Payments", paid_count)
col3.metric("Failed Payments", failed_count)
col4.metric("Failed Amount", f"₹{failed_amount:,.0f}")

# risk section
st.subheader("Customer Risk Summary")

col1, col2, col3 = st.columns(3)

col1.metric("High Risk", high_risk)
col2.metric("Medium Risk", medium_risk)
col3.metric("Low Risk", low_risk)

# charts
st.subheader("Payment Status")

payment_chart = data["payment_status"].value_counts()

st.bar_chart(payment_chart)

st.subheader("Customer Risk Level")

risk_chart = data["risk_level"].value_counts()

st.bar_chart(risk_chart)

# urgent customers
st.subheader("Top Urgent Recovery Customers")

urgent_customers = data[
    data["priority"] == "Urgent"
].sort_values(
    by="days_overdue",
    ascending=False
)

st.dataframe(
    urgent_customers[
        [
            "customer_id",
            "amount",
            "days_overdue",
            "previous_failures",
            "risk_level",
            "priority"
        ]
    ].head(10),
    use_container_width=True
)

st.success("Dashboard loaded successfully!")
# recovery action center

st.subheader("Recovery Action Center")

choice = st.selectbox(
    "Select Risk Level",
    ["All", "High", "Medium", "Low"]
)

if choice == "All":
    filtered_data = data.copy()
else:
    filtered_data = data[
        data["risk_level"] == choice
    ].copy()

st.write("Customers found:", len(filtered_data))

st.dataframe(
    filtered_data[
        [
            "customer_id",
            "amount",
            "days_overdue",
            "previous_failures",
            "risk_level",
            "priority"
        ]
    ].sort_values(
        by="days_overdue",
        ascending=False
    ),
    width="stretch"
)
# urgent recovery summary

urgent_amount = data.loc[
    data["priority"] == "Urgent",
    "amount"
].sum()

st.subheader("Urgent Recovery Summary")

col1, col2 = st.columns(2)

col1.metric(
    "Urgent Customers",
    len(data[data["priority"] == "Urgent"])
)

col2.metric(
    "Urgent Payment Amount",
    f"₹{urgent_amount:,.0f}"
)
# customer search

st.subheader("Customer Search")

customer_id = st.text_input(
    "Enter Customer ID",
    placeholder="Example: C034"
)

if customer_id:
    customer = data[
        data["customer_id"].str.upper() == customer_id.upper()
    ]

    if len(customer) > 0:
        st.write("Customer Details")

        st.dataframe(
            customer[
                [
                    "customer_id",
                    "amount",
                    "days_overdue",
                    "previous_failures",
                    "risk_level",
                    "priority"
                ]
            ],
            width="stretch"
        )
    else:
        st.warning("Customer ID not found.")
        # recovery recommendation

if customer_id:
    customer = data[
        data["customer_id"].str.upper() == customer_id.upper()
    ]

    if len(customer) > 0:
        selected_customer = customer.iloc[0]

        st.subheader("Recovery Recommendation")

        if selected_customer["risk_level"] == "High":
            st.error(
                "Recommended Action: Contact the customer immediately "
                "and send a payment reminder."
            )

        elif selected_customer["risk_level"] == "Medium":
            st.warning(
                "Recommended Action: Send a follow-up reminder "
                "and monitor the payment."
            )

        else:
            st.success(
                "Recommended Action: Routine monitoring is sufficient."
            )            
# personalized recovery message

if customer_id:
    customer = data[
        data["customer_id"].str.upper() == customer_id.upper()
    ]

    if len(customer) > 0:
        selected_customer = customer.iloc[0]

        st.subheader("Personalized Recovery Message")

        message = (
            f"Hello {selected_customer['customer_id']}, "
            f"your payment of ₹{selected_customer['amount']:,.0f} "
            f"is pending for {selected_customer['days_overdue']} days. "
            f"Please complete the payment at the earliest."
        )

        if selected_customer["risk_level"] == "High":
            message += (
                " Please contact the payment support team "
                "if you are facing any difficulty."
            )

        elif selected_customer["risk_level"] == "Medium":
            message += (
                " We kindly request you to complete the payment soon."
            )

        else:
            message += (
                " Thank you for your timely payment."
            )

        st.info(message)
