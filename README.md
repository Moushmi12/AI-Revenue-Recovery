# AI Revenue Recovery System

## AI-Based Revenue Recovery and Customer Risk Prediction System

The AI Revenue Recovery System is a machine learning based application developed to analyze customer payment data, estimate payment recovery probability, classify customer risk levels and prioritize recovery actions.

The project combines data analysis, machine learning and an interactive Streamlit dashboard to support payment recovery decision-making.

---

## 1. Project Overview

Businesses may face delayed or failed customer payments, which can affect cash flow and revenue.

When there are many customer payment records, manually identifying which customers require immediate attention can be difficult.

This project provides a data-driven solution to analyze payment behavior, estimate recovery probability and prioritize customers for recovery actions.

The system provides:

- Payment status analysis
- Recovery probability
- Customer risk classification
- Recovery priority
- Recovery recommendations
- Personalized recovery messages
- Downloadable recovery reports

---

## 2. Problem Statement

Businesses may lose revenue because of delayed or failed customer payments.

The main problems addressed by this project are:

- Difficulty in identifying high-risk payment cases
- Large number of payment records
- Delayed payment follow-up
- Manual payment risk analysis
- Lack of customer-level recovery prioritization

The system aims to help identify customers who require urgent recovery attention.

---

## 3. Objectives

The main objectives are:

1. Analyze customer payment data.
2. Identify successful and failed payments.
3. Study overdue payment patterns.
4. Estimate payment recovery probability using machine learning.
5. Classify customers based on recovery risk.
6. Prioritize recovery activities.
7. Provide recovery recommendations.
8. Generate personalized recovery messages.
9. Provide an interactive dashboard.
10. Generate a downloadable recovery report.

---

## 4. Proposed Solution

The system first loads and analyzes customer payment data using Python and Pandas.

The selected payment features are given to a Logistic Regression model to estimate recovery probability.

Based on the predicted probability, customers are classified into:

- High Risk
- Medium Risk
- Low Risk

A recovery priority is then assigned:

- Urgent
- Follow-up
- Routine

The results are presented through an interactive Streamlit dashboard.

---

## 5. System Workflow

```text
Customer Payment Dataset
          ↓
Data Loading
          ↓
Data Analysis
          ↓
Data Preparation
          ↓
Feature Selection
          ↓
Train/Test Split
          ↓
Machine Learning Model
          ↓
Recovery Probability
          ↓
Risk Classification
          ↓
Recovery Priority
          ↓
Recovery Recommendation
          ↓
Personalized Message

6. Technologies Used
Python
Pandas
NumPy
Scikit-learn
Logistic Regression
Matplotlib
Streamlit
GitHub
7. Dataset

The project uses a synthetic payment dataset created for internship and demonstration purposes.

The dataset includes:

Customer ID
Payment Amount
Days Overdue
Previous Payment Failures
Payment Method
Customer Age
Payment Status

No real customer financial information is used.

8. Machine Learning Approach

A Logistic Regression model is used to estimate payment recovery probability.

Input Features
Amount
Days Overdue
Previous Failures
Customer Age
Output
Recovery Probability
Recovery Status

The data is divided into:

80% Training Data
20% Testing Data

The model is evaluated using:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix
9. Risk Classification

Customers are classified based on predicted recovery probability.

Recovery Probability	Risk Level	Priority
Below 40%	High Risk	Urgent
40% to below 70%	Medium Risk	Follow-up
70% and above	Low Risk	Routine
10. Dashboard Features

The Streamlit dashboard provides:

Business summary
Payment status analysis
Customer risk analysis
Recovery probability
Recovery priority
Customer search
Recovery recommendation
Personalized recovery message
Recovery report download
11. How to Run
Step 1: Install Required Libraries
pip install -r requirements.txt
Step 2: Run the Application
streamlit run app.py
Step 3: Open the Dashboard

After running the application, open the URL shown in the terminal.

Usually:

http://localhost:8501
12. Future Enhancements
Real-time payment monitoring
Automated email and SMS reminders
Larger real-world datasets
Advanced machine learning models
Payment gateway integration
Cloud deployment
Note

This project is a prototype developed for internship and educational purposes.

The dataset and recovery outcomes are synthetic and are used only for demonstration.

Author

Moushmi12
          ↓
Streamlit Dashboard
          ↓
Recovery Report
