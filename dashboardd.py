import pandas as pd
import matplotlib.pyplot as plt

# read the payment data
data = pd.read_csv("data/payments.csv")

# calculate basic details
total_customers = len(data)

paid_count = len(data[data["payment_status"] == "Paid"])
failed_count = len(data[data["payment_status"] == "Failed"])

failed_amount = data.loc[
    data["payment_status"] == "Failed",
    "amount"
].sum()

print("===================================")
print("       AI REVENUE RECOVERY")
print("===================================")

print("Total Customers :", total_customers)
print("Paid Payments   :", paid_count)
print("Failed Payments :", failed_count)
print("Failed Amount   : ₹", failed_amount)

print("===================================")

# payment status graph
data["payment_status"].value_counts().plot(kind="bar")

plt.title("Payment Status")
plt.xlabel("Payment Status")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()
# risk level analysis

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

print("\nRisk Level Summary:")
print(data["risk_level"].value_counts())

# risk level graph
plt.figure()

data["risk_level"].value_counts().plot(kind="bar")

plt.title("Customer Risk Level")
plt.xlabel("Risk Level")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()
# create recovery priority

data["priority"] = "Routine"

data.loc[data["risk_level"] == "Medium", "priority"] = "Follow-up"
data.loc[data["risk_level"] == "High", "priority"] = "Urgent"

priority_data = data[
    [
        "customer_id",
        "amount",
        "days_overdue",
        "previous_failures",
        "risk_level",
        "priority"
    ]
].copy()

priority_data = priority_data.sort_values(
    by=["risk_level", "days_overdue"],
    ascending=[True, False]
)

print("\nCustomer Recovery Priority:")
print(priority_data.to_string(index=False))
# save recovery priority report

priority_data.to_csv(
    "recovery_priority_report.csv",
    index=False
)

print("\nRecovery priority report saved successfully!")