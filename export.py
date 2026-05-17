import pandas as pd

from database import Session
from models import Sale

session = Session()

# Query all sales
sales = session.query(Sale).all()

# Convert to list of dictionaries
data = []

for sale in sales:
    data.append({
        "sales_date": sale.sales_date,
        "day_of_week": sale.day_of_week,
        "product_id": sale.product_id,
        "units_sold": sale.units_sold,
        "weekend_tracker": sale.weekend_tracker
    })

# Create DataFrame
df = pd.DataFrame(data)

# Export CSV
df.to_csv("sales_data.csv", index=False)

print("CSV exported successfully!")