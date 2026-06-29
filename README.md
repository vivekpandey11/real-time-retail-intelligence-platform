# 🚀 Real-Time Retail Intelligence Platform

> End-to-End Data Engineering, Analytics & Machine Learning Solution for Retail Businesses

![Python](https://img.shields.io/badge/Python-3.11-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-blue)
![Snowflake](https://img.shields.io/badge/Snowflake-Cloud%20Analytics-29B5E8)
![dbt](https://img.shields.io/badge/dbt-Transformations-orange)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-red)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Fraud%20Detection-green)

---

## 📌 Project Overview

The Real-Time Retail Intelligence Platform is an end-to-end analytics solution built using modern Data Engineering and Machine Learning technologies.

The platform ingests retail transaction data, performs ETL processing, stores data in PostgreSQL and Snowflake, applies dbt transformations, orchestrates workflows using Apache Airflow, supports streaming pipelines via Kafka, and visualizes business insights through an interactive Power BI dashboard.

Additionally, a Machine Learning fraud detection module identifies potentially suspicious transactions.

---

## 🏗 Architecture


![Architecture](assets/architecture_diagram.png)


```text
Kaggle Retail Dataset
        │
        ▼
 Python ETL Pipelines
        │
        ▼
 PostgreSQL Warehouse
        │
        ▼
    dbt Models
        │
        ▼
 Snowflake Analytics
        │
        ▼
 Power BI Dashboard
        │
        ▼
 Business Insights

 Machine Learning
 Fraud Detection
```

---

## ⚙️ Tech Stack

### Data Engineering

- Python
- PostgreSQL
- Snowflake
- Apache Airflow
- Apache Kafka
- dbt
- SQL

### Analytics

- Power BI
- Star Schema Modeling
- Business Intelligence

### Machine Learning

- Scikit-Learn
- Fraud Detection Model

---

## 📊 Dataset

Source:

**Brazilian E-Commerce Public Dataset by Olist**

Data includes:

- Customers
- Orders
- Products
- Payments
- Reviews
- Sellers
- Geolocation

Processed Records:

| Dataset | Records |
|----------|----------|
| Orders | 99K+ |
| Customers | 99K+ |
| Payments | 103K+ |
| Products | 32K+ |

---

## 📂 Project Structure

```text
Real-Time Retail Intelligence Platform/

├── airflow/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample_data/
│
├── database/
│   ├── postgres/
│   └── snowflake/
│
├── dbt/
├── docker/
├── kafka/
├── logs/
├── ml_model/
├── notebooks/
├── scripts/
├── spark/
├── sql/
└── dashboard/
```

---

## 🔄 Data Pipeline

### Data Ingestion

- Kaggle Dataset
- Excel Files
- JSON Streaming Events

### ETL Processing

- Data Cleaning
- Validation
- Transformation
- Standardization

### Warehouse Layer

- PostgreSQL

### Analytics Layer

- Snowflake

### Transformation Layer

- dbt Staging Models
- dbt Mart Models

### Visualization Layer

- Power BI

---

## ⭐ Star Schema Design

### Fact Table

#### fct_sales

- order_id
- customer_id
- product_id
- price
- payment_value
- order_date

### Dimension Tables
#### dim_customers

- customer_id
- customer_city
- customer_state

#### dim_products

- product_id
- product_category_name

---

# 📈 Power BI Dashboard

## Executive KPIs

- Total Revenue
- Total Orders
- Total Customers
- Total Products
- Revenue Per Customer
- Average Order Value


## Dashboard Preview

![Dashboard](https://github.com/vivekpandey11/real-time-retail-intelligence-platform/blob/main/dashboard.jpeg?raw=true)


## Insights

- Monthly Revenue Trend
- Revenue by State
- Revenue by Product Category
- Revenue Contribution Analysis
- Top Revenue States
- Top Revenue Categories
- Interactive Filtering

---

## 🧠 Machine Learning Fraud Detection

### Features

- Transaction Monitoring
- Fraud Prediction
- Alert Generation

### Sample Output

```python
Prediction Result:
[1]

Fraud Transaction Detected
```

---

## 🎯 Key Achievements

✅ Processed 99K+ Retail Orders

✅ Built End-to-End ETL Pipelines

✅ Implemented PostgreSQL & Snowflake Integration

✅ Designed Star Schema Data Models

✅ Created Interactive Power BI Dashboard

✅ Integrated Airflow & Kafka Components

✅ Developed ML-Based Fraud Detection

---

## 🚀 Future Enhancements

- Real-Time Kafka Analytics
- Automated Scheduling
- Customer Segmentation
- Sales Forecasting
- Cloud Deployment

---

## 👨‍💻 Author

**Vivek Pandey**

B.Tech Electronics & Communication

Data Engineering • Analytics • Machine Learning
