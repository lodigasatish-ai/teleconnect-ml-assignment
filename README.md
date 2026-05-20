# Telco Customer Churn Prediction & Revenue Forecasting

## Project Overview
This project focuses on understanding customer behavior using machine learning. The main goal is to predict whether a customer will leave the service (churn) and to estimate monthly revenue based on customer data.

The project covers the complete machine learning workflow including data analysis, preprocessing, model building, evaluation, and business interpretation.

## Project Structure

The repository is organized as follows:

- **data/** → Raw dataset  
- **notebooks/** → All Jupyter notebooks  
  - 01_EDA.ipynb (Exploratory Data Analysis)  
  - 02_preprocessing.ipynb (Data cleaning & feature engineering)  
  - 03_classification.ipynb (Churn prediction models)  
  - 04_regression.ipynb (Revenue prediction models)  
  - 05_interpretation.ipynb (SHAP & business insights)  

- **src/** → Reusable Python scripts  
- **models/** → Trained ML models  
  - best_classifier.pkl  
  - best_regressor.pkl  
  - scaler.pkl  
  - encoder.pkl  

- **reports/** → Final reports and visual outputs  
  - classification_report.md  
  - regression_report.md  
  - figures/ (plots and charts)

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

## Best Performing Models

- **Classification Model:** Logistic Regression  
- **Regression Model:** Linear Regression  

##  Model Performance Summary

- Accuracy: ~86%  
- F1 Score: ~0.86  
- ROC-AUC Score: ~0.93  
- R² Score: ~0.99  

These results show that the models perform well in both classification and regression tasks.

## Key Business Insights

- Customers with month-to-month contracts are more likely to churn  
- Higher monthly charges increase the chance of churn  
- New customers (low tenure) are at higher risk of leaving  
- Long-term contracts help in improving customer retention  

## Conclusion

This project demonstrates a complete end-to-end machine learning pipeline, starting from raw data and ending with actionable business insights. It helps in understanding customer churn behavior and supports better decision-making for customer retention strategies.
