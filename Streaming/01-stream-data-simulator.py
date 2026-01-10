# Databricks notebook source
import os, time, uuid, random, csv
from datetime import datetime

# Target directory for your streaming source
target_dir = "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/live_weather"
os.makedirs(target_dir, exist_ok=True)

cities = ["New Delhi", "Mumbai", "Kolkatta", "Hyderabad", "Chennai", "Bangalore"]

#cities = ["Mumbai"]

# Define the column order
headers = ["event_id", "timestamp", "city", "temperature_c2", "humidity_percent", "wind_speed_kmh2"]

while True:
    event = [
        str(uuid.uuid4()),                # event_id
        datetime.now().isoformat(),       # timestamp
        random.choice(cities),            # city
        round(random.uniform(-5, 35), 1), # temperature_c
        random.randint(30, 90),           # humidity_percent
        round(random.uniform(0, 40), 1)   # wind_speed_kmh
    ]

    # Use timestamp for filename (safe format for files)
    ts_filename = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{target_dir}/weather_{ts_filename}.csv"

    # Write single-row CSV
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerow(event)

    print(f"Wrote {file_path}: {event}")
    time.sleep(10)   # wait 10 seconds before writing next weather reading
