from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'retail_orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer Started...\n")

for message in consumer:
    print("Received:", message.value)