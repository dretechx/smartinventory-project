import streamlit as st
import pandas as pd

from database import Session
from models import Sale, Product

# ---------------------------
# SESSION + DATA LOAD
# ---------------------------

session = Session()

sales = session.query(Sale).all()
products = session.query(Product).all()

# Convert products to dict
product_map = {
    p.id: {
        "name": p.product_name,
        "category": p.category
    }
    for p in products
}

# Build sales dataframe
data = []

for s in sales:
    data.append({
        "date": s.sales_date,
        "day": s.day_of_week,
        "product_id": s.product_id,
        "product_name": product_map[s.product_id]["name"],
        "category": product_map[s.product_id]["category"],
        "units_sold": s.units_sold,
        "weekend": s.weekend_tracker
    })

df = pd.DataFrame(data)

# ---------------------------
# UI SETUP
# ---------------------------

st.set_page_config(page_title="SmartInventory Dashboard", layout="wide")

st.title("🛒 SmartInventory Sales Dashboard")

st.markdown("Analyze 90-day grocery sales patterns for inventory optimization.")

# ---------------------------
# SIDEBAR FILTERS
# ---------------------------

st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Select Category",
    df["category"].unique(),
    default=df["category"].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product",
    df["product_name"].unique(),
    default=df["product_name"].unique()
)

df = df[
    (df["category"].isin(category_filter)) &
    (df["product_name"].isin(product_filter))
]

# ---------------------------
# KPI METRICS
# ---------------------------

total_sales = df["units_sold"].sum()
avg_sales = df["units_sold"].mean()

weekend_sales = df[df["weekend"] == True]["units_sold"].mean()
weekday_sales = df[df["weekend"] == False]["units_sold"].mean()

top_product = (
    df.groupby("product_name")["units_sold"]
    .sum()
    .sort_values(ascending=False)
    .idxmax()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Units Sold", f"{total_sales:,}")
col2.metric("Avg Daily Sales", f"{avg_sales:.2f}")
col3.metric("Weekend Avg Sales", f"{weekend_sales:.2f}")
col4.metric("Top Product", top_product)

st.divider()

# ---------------------------
# CHART 1: WEEKDAY VS WEEKEND
# ---------------------------

st.subheader("📊 Weekend vs Weekday Sales")

weekend_comparison = df.groupby("weekend")["units_sold"].mean()

st.bar_chart(weekend_comparison)

# ---------------------------
# CHART 2: CATEGORY PERFORMANCE
# ---------------------------

st.subheader("📦 Category Performance")

category_chart = df.groupby("category")["units_sold"].sum()

st.bar_chart(category_chart)

# ---------------------------
# CHART 3: TOP PRODUCTS
# ---------------------------

st.subheader("🔥 Top Selling Products")

top_products = (
    df.groupby("product_name")["units_sold"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)

# ---------------------------
# RAW DATA VIEW
# ---------------------------

st.subheader("📋 Raw Data")

st.dataframe(df)