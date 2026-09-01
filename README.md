# AI Revenue Recovery System

## AI-Based Revenue Recovery and Customer Risk Prediction System

The AI Revenue Recovery System is a machine learning based application developed to analyze customer payment data, estimate payment recovery probability, classify customer risk levels and prioritize recovery actions.

The project combines data analysis, machine learning and an interactive Streamlit dashboard to support payment recovery decision-making.

---

## 1. Project Overview

Businesses often receive payments from customers after an invoice or due date. Some payments may be delayed or fail completely. When the number of customers is large, manually identifying which customers need immediate attention can be difficult.

This project provides a simple data-driven solution for analyzing payment behavior and identifying customers who may require different levels of recovery attention.

The system processes payment information and produces:

- Payment status analysis
- Recovery probability
- Customer risk classification
- Recovery priority
- Customer-specific recommendations
- Personalized recovery messages
- Downloadable recovery reports

---

## 2. Problem Statement

Businesses may face revenue loss because of delayed or failed customer payments.

The main problems addressed by this project are:

- Difficulty in identifying high-risk payment cases
- Large number of customer payment records
- Delayed payment follow-up
- Lack of customer-level recovery prioritization
- Manual analysis of payment recovery situations

The system aims to provide a simple and automated approach for identifying customers who require urgent recovery attention.

---

## 3. Objectives

The main objectives of this project are:

1. To analyze customer payment data.
2. To identify successful and failed payments.
3. To study overdue payment patterns.
4. To estimate payment recovery probability using machine learning.
5. To classify customers into different risk levels.
6. To prioritize customers for recovery follow-up.
7. To provide recovery recommendations.
8. To generate personalized recovery messages.
9. To provide an interactive dashboard for analysis.
10. To generate a downloadable recovery report.

---

## 4. Proposed Solution

The proposed system follows a data-driven approach.

Customer payment information is first loaded and analyzed using Python and Pandas.

The relevant features are then provided to a Logistic Regression model to estimate the probability of payment recovery.

Based on the predicted recovery probability, customers are classified into:

- High Risk
- Medium Risk
- Low Risk

A recovery priority is then assigned:

- Urgent
- Follow-up
- Routine

The results are displayed through an interactive Streamlit dashboard.

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
## 6. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- Matplotlib
- Streamlit
- GitHub

---

## 7. Dataset

The project uses a synthetic payment dataset created for internship and demonstration purposes.

The dataset includes:

- Customer ID
- Payment Amount
- Days Overdue
- Previous Payment Failures
- Payment Method
- Customer Age
- Payment Status

No real customer financial information is used.

---

## 8. Machine Learning Approach

A Logistic Regression model is used to estimate payment recovery probability.

### Input Features

- Amount
- Days Overdue
- Previous Failures
- Customer Age

### Output

- Recovery Probability
- Recovery Status

The data is divided into 80% training data and 20% testing data.

The model is evaluated using accuracy, precision, recall, F1-score and confusion matrix.

---

## 9. Risk Classification

Customers are classified based on recovery probability.

| Recovery Probability | Risk Level | Priority |
|---|---|---|
| Below 40% | High Risk | Urgent |
| 40% to below 70% | Medium Risk | Follow-up |
| 70% and above | Low Risk | Routine |

---

## 10. Dashboard Features

The Streamlit dashboard provides:

- Payment status analysis
- Customer risk analysis
- Recovery probability
- Recovery priority
- Customer search
- Recovery recommendation
- Personalized recovery message
- Recovery report download

---

## 11. How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
## 12. Future Enhancements

- Real-time payment monitoring
- Automated email or SMS reminders
- Larger real-world datasets
- Advanced machine learning models
- Payment gateway integration
- Cloud deployment

---

## Note

This project is a prototype developed for internship and educational purposes.

The dataset and recovery outcomes are synthetic and are used only for demonstration.

## Author

**Moushmi12**
