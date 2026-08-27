from faker import Faker
from datetime import datetime, timedelta
import random

from database import Session, engine, Base
from models import Product, Sale
from helpers import (
    generate_daily_sales,
    apply_weekend_boost,
    apply_holiday_boost
)

# Initialize
fake = Faker()
session = Session()

# Create tables
Base.metadata.create_all(engine)

# ----------------------------
# CONFIG
# ----------------------------

categories = [
    "Dairy",
    "Meat",
    "Produce",
    "Bakery",
    "Beverages",
    "Frozen"
]

labels = ["Premium", "Organic", "Classic", "Fresh"]

products = []

# ----------------------------
# CREATE PRODUCTS
# ----------------------------

for _ in range(50):

    product = Product(
        product_name=f"{random.choice(labels)} {fake.word().title()}",
        category=random.choice(categories),
        base_sale_rate=random.randint(5, 40),
        weekend_multiplier=round(random.uniform(1.2, 2.5), 2)
    )

    session.add(product)
    products.append(product)

session.commit()

# ----------------------------
# CREATE SALES (90 DAYS)
# ----------------------------

start_date = datetime(2025, 1, 1)

for day_offset in range(90):

    current_date = start_date + timedelta(days=day_offset)

    day_name = current_date.strftime("%A")

    is_weekend = day_name in ["Saturday", "Sunday"]

    for product in products:

        daily_sales = generate_daily_sales(product.base_sale_rate)

        if is_weekend:
            daily_sales = apply_weekend_boost(
                daily_sales,
                product.weekend_multiplier
            )

        if current_date.month in [7, 12]:
            daily_sales = apply_holiday_boost(daily_sales)

        sale = Sale(
            sales_date=current_date.date(),
            day_of_week=day_name,
            product_id=product.id,
            units_sold=daily_sales,
            weekend_tracker=is_weekend
        )

        session.add(sale)

session.commit()

print("Database seeded successfully!")