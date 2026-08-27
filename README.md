# SmartInventory – QuickMart Sales Analysis System

## Overview
SmartInventory is a data analytics project that simulates grocery store sales to help QuickMart improve inventory decisions. It generates fake product and sales data, stores it in a database, and analyzes patterns to reduce stock shortages.

---

## Problem
QuickMart frequently runs out of popular items due to fixed inventory schedules instead of data-driven forecasting. This leads to lost sales and poor customer experience.

---

## Solution
This project builds a full data pipeline:
- Generates realistic product and sales data using Faker
- Stores data in a SQLite database using SQLAlchemy
- Simulates 90 days of sales activity
- Exports data to CSV for visualization
- Builds an interactive dashboard using Streamlit (in this repo), plus a separate
  exploratory dashboard built with Lovable AI (not included in this repository)

---

## Tech Stack
Python, SQLAlchemy, SQLite, Pandas, Faker, Streamlit, Lovable AI

---

## Database Structure

**Products Table**
- id (PK)
- product_name
- category
- base_sale_rate
- weekend_multiplier

**Sales Table**
- id (PK)
- sales_date
- day_of_week
- product_id (FK)
- units_sold
- weekend_tracker

---

## Workflow
1. Generate product data (Faker)
2. Simulate 90 days of sales
3. Store data in SQLite database
4. Export sales data to CSV
5. Visualize insights in Streamlit and Lovable dashboards

---

## Key Insights
- Weekend sales are higher than weekday sales
- Dairy and Meat are top-performing categories
- A small number of products drive most sales
- Demand spikes occur during weekends and holidays

---

## How to Run

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt

python seed.py                 # creates smartinventory.db and generates 90 days of sales data
python export.py               # optional: re-exports sales_data.csv from the database
streamlit run app.py           # launches the dashboard
```
