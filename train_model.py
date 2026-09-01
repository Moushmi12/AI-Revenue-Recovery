import pandas as pd

# read the payment data
data = pd.read_csv("data/payments.csv")

print("Payment Data")
print(data.head())

# basic information
print("\nTotal customers:", len(data))

print("\nPayment Status:")
print(data["payment_status"].value_counts())

# check missing values
print("\nChecking missing values:")
print(data.isnull().sum())

# payment analysis
print("\nTotal payment amount:")
print(data["amount"].sum())

failed = data[data["payment_status"] == "Failed"]

print("\nFailed payment count:", len(failed))
print("Failed payment amount:", failed["amount"].sum())

print("\nAverage payment amount:", data["amount"].mean())

# create recovery status
data["recovery_status"] = "Not Recovered"

for i in range(len(data)):
    if data.loc[i, "payment_status"] == "Paid":
        data.loc[i, "recovery_status"] = "Recovered"
    elif data.loc[i, "days_overdue"] <= 7 and data.loc[i, "previous_failures"] <= 1:
        data.loc[i, "recovery_status"] = "Recovered"

print("\nRecovery Status:")
print(data["recovery_status"].value_counts())

# prepare data for machine learning
X = data[
    [
        "amount",
        "days_overdue",
        "previous_failures",
        "customer_age"
    ]
]

y = data["recovery_status"]

print("\nInput data:")
print(X.head())

print("\nTarget data:")
print(y.head())

# split the data into training and testing
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:", len(X_train))
print("Testing data:", len(X_test))
# train the machine learning model

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("\nModel training completed!")
# check the model accuracy

from sklearn.metrics import accuracy_score

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\nModel Accuracy:", accuracy)
# predict recovery probability

probability = model.predict_proba(X_test)

print("\nRecovery Probability:")

for i in range(len(X_test)):
    print(
        y_test.iloc[i],
        "->",
        round(max(probability[i]) * 100, 2),
        "%"
    )
    # check model performance

from sklearn.metrics import classification_report, confusion_matrix

print("\nClassification Report:")
print(classification_report(y_test, prediction))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, prediction))
# create risk levels

recovery_probability = probability[:, list(model.classes_).index("Recovered")]

risk_level = []

for p in recovery_probability:
    if p < 0.40:
        risk_level.append("High")
    elif p < 0.70:
        risk_level.append("Medium")
    else:
        risk_level.append("Low")

print("\nRisk Levels:")

for i in range(len(X_test)):
    print(
        "Recovery probability:",
        round(recovery_probability[i] * 100, 2),
        "% -> Risk:",
        risk_level[i]
    )
    # create customer recovery priority

results = data.loc[X_test.index, [
    "customer_id",
    "amount",
    "days_overdue",
    "previous_failures"
]].copy()

results["recovery_probability"] = recovery_probability * 100
results["risk_level"] = risk_level

priority = []

for risk in risk_level:
    if risk == "High":
        priority.append("Urgent")
    elif risk == "Medium":
        priority.append("Follow-up")
    else:
        priority.append("Routine")

results["priority"] = priority

results = results.sort_values(
    by="recovery_probability"
)

print("\nCustomer Recovery Priority:")
print(results.to_string(index=False))