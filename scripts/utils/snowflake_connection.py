import snowflake.connector

conn = snowflake.connector.connect(
    user="VIVEK001",
    password="VivekPandey1234",
    account="ks57107.ap-southeast-7.aws",
    warehouse="RETAIL_WH",
    database="RETAIL_DB",
    schema="RAW"
)

print("Connected to Snowflake Successfully")

cursor = conn.cursor()

cursor.execute("SHOW TABLES")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()