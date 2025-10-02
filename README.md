# dbt + BigQuery Data Warehouse

## 📌 Overview
This project demonstrates how to use **dbt (Data Build Tool)** with **Google BigQuery** to build a scalable and maintainable data warehouse.  

## 🗂 Features
- Configured dbt models for staging and analytics
- Source freshness checks to ensure data reliability
- Data quality tests
- Auto-generated dbt documentation site

## ⚙️ Tech Stack
- dbt
- BigQuery
- SQL
- Airflow (optional)

## 🚀 How to Run
1. Install dbt-bigquery:
   ```bash
   pip install dbt-bigquery
   ```
2. Configure your BigQuery credentials.
3. Run dbt commands:
   ```bash
   dbt run
   dbt test
   dbt docs generate
   dbt docs serve
   ```

## 📊 Example Model
See `models/stg_airbnb_listings.sql` for a transformation example.

---
✨ Author: [Antile-Chenai](https://github.com/Antile-Chenai)
