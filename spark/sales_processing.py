from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Retail Sales Processing") \
    .getOrCreate()

print("Spark Started Successfully")

data = [
    (1, "Laptop", 50000),
    (2, "Mobile", 25000),
    (3, "Mouse", 500),
    (4, "Keyboard", 1500)
]

df = spark.createDataFrame(
    data,
    ["order_id", "product", "amount"]
)

print("\nData:")
df.show()

print("\nTotal Sales:")
df.groupBy().sum("amount").show()

spark.stop()