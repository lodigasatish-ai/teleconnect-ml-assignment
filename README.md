#  Telco Customer Churn Prediction & Revenue Forecasting

##  Project Title & Description
Telco Customer Churn Prediction & Revenue Forecasting

This project uses machine learning to predict customer churn and estimate revenue. It analyzes customer behavior data to identify customers likely to leave the service and helps improve retention strategies using data-driven insights.

##  Dataset
- Source: https://www.kaggle.com/blastchar/telco-customer-churn  

### Description:
This dataset contains telecom customer information such as tenure, contract type, monthly charges, and services used. It is used to predict customer churn (whether a customer will leave the service or not).

##  Project Overview
This project focuses on understanding customer behavior using machine learning. The main goal is to predict whether a customer will leave the service (churn) and to estimate monthly revenue based on customer data.

The project covers the complete machine learning workflow including data analysis, preprocessing, model building, evaluation, and business interpretation.

##  Project Structure

- **data/**
  - raw/ → original dataset
  - processed/ → cleaned dataset

- **notebooks/**
  - 01_EDA.ipynb (Exploratory Data Analysis)
  - 02_preprocessing.ipynb (Data cleaning & feature engineering)
  - 03_classification.ipynb (Churn prediction models)
  - 04_regression.ipynb (Revenue prediction models)
  - 05_interpretation.ipynb (SHAP & business insights)

- **src/**
  - data_loader.py
  - preprocessing.py
  - classifiers.py
  - regressors.py
  - evaluation.py
  - utils.py
  - __init__.py

- **models/**
  - best_classifier.pkl
  - best_regressor.pkl
  - scaler.pkl
  - encoder.pkl

- **reports/**
  - classification_report.md
  - regression_report.md
  - figures/ (plots and charts)

- **tests/**
  - test_preprocessing.py
  - test_evaluation.py

## Machine Learning Models Used

### Classification (Churn Prediction)
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  

### Regression (Revenue Prediction)
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Random Forest Regressor  
- Support Vector Regressor (SVR)  

##  Best Performing Models
- **Classification Model:** Logistic Regression  
- **Regression Model:** Linear Regression  

## Model Performance Summary
- Accuracy: ~86%  
- F1 Score: ~0.86  
- ROC-AUC Score: ~0.93  
- R² Score: ~0.99  

These results show strong performance in both classification and regression tasks.

##  Key Business Insights
- Customers with month-to-month contracts are more likely to churn  
- Higher monthly charges increase churn risk  
- New customers (low tenure) are more likely to leave  
- Long-term contracts improve customer retention  
- Targeting high-risk customers improves business profit
  
## Conclusion
This project demonstrates a complete end-to-end machine learning pipeline, starting from raw data and ending with actionable business insights. It helps understand customer churn behavior and supports better decision-making for customer retention strategies.
