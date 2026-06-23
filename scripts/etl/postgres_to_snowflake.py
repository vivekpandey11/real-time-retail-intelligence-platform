import pandas as pd
from sqlalchemy import create_engine
import snowflake.connector

# PostgreSQL

pg_engine = create_engine(
    "postgresql+psycopg2://postgres:postgres123@localhost:5432/retail_dw"
)

# Snowflake

conn = snowflake.connector.connect(
    user="VIVEK001",
    password="VivekPandey1234",
    account="ks57107.ap-southeast-7.aws",
    warehouse="RETAIL_WH",
    database="RETAIL_DB",
    schema="RAW"
)

cursor = conn.cursor()

print("Reading PostgreSQL Orders...")
df = pd.read_sql(
    "SELECT * FROM raw.orders LIMIT 100",
    pg_engine
)

print("Rows Found:", len(df))

for _, row in df.iterrows():

    sql = f"""
    INSERT INTO ORDERS_RAW
    VALUES (
        '{row["order_id"]}',
        '{row["customer_id"]}',
        '{row["order_status"]}',
        '{row["order_purchase_timestamp"]}',
        '{row["order_approved_at"]}',
        '{row["order_delivered_carrier_date"]}',
        '{row["order_delivered_customer_date"]}',
        '{row["order_estimated_delivery_date"]}'
    )
    """

    cursor.execute(sql)

conn.commit()

cursor.execute("SELECT COUNT(*) FROM ORDERS_RAW")

print("Snowflake Row Count:")
print(cursor.fetchone())

cursor.close()
conn.close()