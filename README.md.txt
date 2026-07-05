# 📦 Smart Retail Operations Intelligence

An end-to-end Retail Analytics project that combines *SQL, Python, Machine Learning, and Power BI* to help businesses monitor inventory performance, identify stock risks, and make data-driven inventory decisions.

The project transforms raw retail transaction data into interactive dashboards and predictive insights that support smarter inventory planning and operational efficiency.

---

## 🚀 Project Overview

Retail businesses often struggle with inventory-related challenges such as:

- Overstocking
- Stock shortages
- Inefficient inventory allocation
- Uncertain product demand

This project analyzes historical inventory data, builds a machine learning model to predict inventory risk, and visualizes key business insights using Power BI.

---

## 🛠️ Tech Stack

- *SQL (PostgreSQL)* – Data storage, cleaning and feature engineering
- *Python*
  - Pandas
  - NumPy
  - Scikit-learn
  - SQLAlchemy
  - Joblib
- *Machine Learning*
  - Random Forest Classifier
- *Power BI*
  - Interactive dashboards
  - DAX Measures
  - KPI Cards
  - Slicers
  - Drill-down analysis

---

## 📂 Project Workflow

Raw Retail Dataset

↓

PostgreSQL Data Cleaning

↓

Feature Engineering

↓

Python Data Processing

↓

Machine Learning Model

↓

Inventory Risk Prediction

↓

Power BI Dashboard

---

## 🗄️ SQL Tasks Performed

- Imported raw retail dataset
- Created cleaned inventory table
- Data type conversion
- Revenue calculation
- Inventory Status generation
- Demand Level creation
- Discount Category creation
- Price Band segmentation
- Business analysis queries

---

## 🤖 Machine Learning

A Random Forest Classification model was built to classify inventory into:

- 🟢 Low Risk
- 🟠 Medium Risk
- 🔴 High Risk

Model Output:

- Inventory Risk Prediction
- Risk Probability
- Inventory Risk Model (.pkl)
- Prediction CSV

---

## 📊 Dashboard Pages

### 📄 Page 1 — Retail Inventory Operations Dashboard

Provides a complete operational overview including:

- Total Revenue
- Total Units Sold
- Inventory Turnover
- Revenue Trend
- Revenue by Category
- Revenue by Region
- Revenue by Weather
- Inventory vs Units Sold
- Top Performing Stores

---

### 📄 Page 2 — Inventory Risk Prediction Dashboard

Machine Learning dashboard including:

- High Risk Products
- Medium Risk Products
- Low Risk Products
- Average Risk Probability
- Inventory Risk Distribution
- Risk by Category
- Risk by Region
- Top High Risk Products
- Demand Forecast vs Inventory Level

---

## 📈 Business Insights

The dashboard helps businesses:

- Detect products with high inventory risk
- Identify categories requiring immediate attention
- Compare inventory performance across regions
- Improve inventory planning
- Reduce stock-out situations
- Support data-driven inventory decisions

---

## 📁 Project Structure


Smart-Retail-Operations-Intelligence/

│

├── Dataset/

├── SQL/

│   ├── schema.sql

│   ├── cleaning.sql

│   └── analysis.sql

│

├── Python/

│   ├── demand_forecasting.py

│   ├── inventory_forecasting.py

│   └── inventory_risk_model.pkl

│

├── Dashboard Images/

├── Retail_Inventory_Dashboard.pbix

├── README.md

├── LICENSE

└── requirements.txt


---

## 📷 Dashboard Preview

### Retail Inventory Operations Dashboard

![Operations Dashboard](Dashboard%20Images/operations_dashboard.png)

---

### Inventory Risk Prediction Dashboard

![Inventory Prediction Dashboard](Dashboard%20Images/Inventory_prediction_dashboard.png)
---

## 🎯 Key Features

✔️ SQL Data Cleaning

✔️ Feature Engineering

✔️ Inventory Risk Prediction

✔️ Machine Learning Integration

✔️ Power BI Interactive Dashboard

✔️ Business KPI Monitoring

✔️ Inventory Optimization Insights

---

## 📌 Future Improvements

- Real-time inventory monitoring
- Automated inventory alerts
- Demand forecasting using time-series models
- Supplier performance analysis
- Inventory recommendation engine

---

## Saziya

Developed as an end-to-end Data Analytics & Machine Learning portfolio project using SQL, Python, PostgreSQL and Power BI.