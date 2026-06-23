from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = [
    "Laptop",
    "Mobile",
    "Keyboard",
    "Mouse",
    "Monitor"
]

while True:

    order = {
        "order_id": random.randint(1000, 9999),
        "product": random.choice(products),
        "amount": random.randint(500, 5000)
    }

    producer.send(
        "retail_orders",
        value=order
    )

    print("Sent:", order)

    time.sleep(2)