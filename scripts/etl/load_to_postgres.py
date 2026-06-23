import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Connection

DATABASE_URL = "postgresql://postgres:VivekA123@localhost:5432/retail_dw"

engine = create_engine(DATABASE_URL)

# File Paths

files = {
    "orders": "data/processed/cleaned/orders_cleaned.csv",
    "customers": "data/processed/cleaned/customers_cleaned.csv",
    "products": "data/processed/cleaned/products_cleaned.csv",
    "order_items": "data/processed/cleaned/order_items_cleaned.csv",
    "payments": "data/processed/cleaned/payments_cleaned.csv"
}

# Load Data

for table_name, file_path in files.items():

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(file_path)

    print(f"Rows Found: {len(df)}")

    df.to_sql(
        name=table_name,
        con=engine,
        schema="raw",
        if_exists="append",
        index=False
    )

    print(f"{table_name} loaded successfully")

print("\nAll Tables Loaded Successfully")

