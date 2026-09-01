import pandas as pd
import matplotlib.pyplot as plt

# load the payment data
data = pd.read_csv("data/payments.csv")

# basic calculations
total_customers = len(data)

paid_count = len(data[data["payment_status"] == "Paid"])
failed_count = len(data[data["payment_status"] == "Failed"])

failed_amount = data.loc[
    data["payment_status"] == "Failed",
    "amount"
].sum()

# risk levels
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

# priority
data["priority"] = "Routine"

data.loc[
    data["risk_level"] == "Medium",
    "priority"
] = "Follow-up"

data.loc[
    data["risk_level"] == "High",
    "priority"
] = "Urgent"

# risk summary
high_risk = len(data[data["risk_level"] == "High"])
medium_risk = len(data[data["risk_level"] == "Medium"])
low_risk = len(data[data["risk_level"] == "Low"])

# display dashboard
print("\n==============================================")
print("          AI REVENUE RECOVERY SYSTEM")
print("==============================================")

print("\nBUSINESS SUMMARY")
print("----------------------------------------------")
print("Total Customers       :", total_customers)
print("Paid Payments         :", paid_count)
print("Failed Payments       :", failed_count)
print("Failed Payment Amount : ₹", failed_amount)

print("\nRISK SUMMARY")
print("----------------------------------------------")
print("High Risk             :", high_risk)
print("Medium Risk           :", medium_risk)
print("Low Risk              :", low_risk)

# urgent customers
urgent = data[data["priority"] == "Urgent"].copy()

urgent = urgent.sort_values(
    by="days_overdue",
    ascending=False
)

print("\nTOP URGENT RECOVERY CUSTOMERS")
print("----------------------------------------------")

print(
    urgent[
        [
            "customer_id",
            "amount",
            "days_overdue",
            "previous_failures",
            "risk_level",
            "priority"
        ]
    ].head(10).to_string(index=False)
)

# payment status chart
plt.figure(figsize=(7, 5))

data["payment_status"].value_counts().plot(kind="bar")

plt.title("Payment Status")
plt.xlabel("Payment Status")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# risk level chart
plt.figure(figsize=(7, 5))

data["risk_level"].value_counts().plot(kind="bar")

plt.title("Customer Risk Level")
plt.xlabel("Risk Level")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

print("\n==============================================")
print("Dashboard completed successfully!")
print("==============================================")