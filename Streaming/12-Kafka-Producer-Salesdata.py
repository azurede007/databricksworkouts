# Databricks notebook source
import time
import uuid
import random
import json
from datetime import datetime
from pyspark.sql import Row

# 1. Kafka Configuration
kafka_broker = "34.60.170.86:9092"
topic_name = "test-topic"

# 2. Define Sales Categories and Payment Methods
categories = ["Electronics", "Home & Garden", "Clothing", "Books", "Beauty"]
cities = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
payment_methods = ["Credit Card", "UPI", "Cash", "Net Banking"]

print(f"Starting Sales Data Stream to Kafka topic: {topic_name}...")

while True:
    try:
        # 3. Create the Sales Event Dictionary
        event_data = {
            "transaction_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "city": random.choice(cities),
            "category": random.choice(categories),
            "amount": round(random.uniform(10.0, 500.0), 2),
            "payment_method": random.choice(payment_methods)
        }

        # 4. Convert dictionary to a JSON string (this will be the Kafka message 'value')
        json_payload = json.dumps(event_data)

        # 5. Create a small Spark DataFrame for the single event
        # Kafka requires a 'value' column (and optionally a 'key' column)
        df = spark.createDataFrame([Row(value=json_payload)])

        # 6. Write to Kafka
        (df.write
            .format("kafka")
            .option("kafka.bootstrap.servers", kafka_broker)
            .option("topic", topic_name)
            .save())

        print(f"Sent to Kafka: {event_data['category']} in {event_data['city']} for ${event_data['amount']}")

    except Exception as e:
        print(f"Error sending to Kafka: {e}")
        # Serverless note: If this fails with a timeout, check your GCP Firewall rules for the Databricks NAT IP.

    # 7. Interval
    time.sleep(10)
