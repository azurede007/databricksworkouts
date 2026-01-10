# Databricks notebook source
import os, time, uuid, random, csv
from datetime import datetime

# 1. Update target directory for sales data
target_dir = "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/live_sales"
os.makedirs(target_dir, exist_ok=True)

# 2. Define Sales Categories and Payment Methods
categories = ["Electronics", "Home & Garden", "Clothing", "Books", "Beauty"]
# cities = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
cities = ["Bangalore", "Pune"]

payment_methods = ["Credit Card", "UPI", "Cash", "Net Banking"]

# 3. Define Sales Headers
headers = ["transaction_id", "timestamp", "city", "category", "amount", "payment_method"]

print(f"Starting Sales Data Generator in {target_dir}...")

while True:
    # 4. Generate Sales Event
    event = [
        str(uuid.uuid4()),                  # transaction_id
        datetime.now().isoformat(),         # timestamp
        random.choice(cities),              # city
        random.choice(categories),          # category
        round(random.uniform(10.0, 500.0), 2), # amount (price)
        random.choice(payment_methods)       # payment_method
    ]

    # 5. Create Filename
    ts_filename = datetime.now().strftime("%Y%m%d_%H%M%S_%f") # Added %f for microsecond uniqueness
    file_path = f"{target_dir}/sales_{ts_filename}.csv"

    # 6. Write to CSV
    try:
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerow(event)
        
        print(f"Recorded Sale: {event[3]} in {event[2]} for ${event[4]}")
    except Exception as e:
        print(f"Error writing file: {e}")

    # 7. Interval
    time.sleep(10) # Faster generation for sales (10 seconds)
