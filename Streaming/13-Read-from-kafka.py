# Databricks notebook source
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Define the schema to match your generator
schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("city", StringType(), True),
    StructField("category", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("payment_method", StringType(), True)
])

# 1. Kafka Configuration
kafka_broker = "34.60.170.86:9092"
topic_name = "test-topic"
checkpoint_location = "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/checkpoints/kafka_to_delta"
target_table_name = "sales_kafka_table"

# 2. Read from Kafka
kafka_stream_df = (spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", kafka_broker)
    .option("subscribe", topic_name)
    .option("startingOffsets", "earliest") # Read from beginning
    .load())

# 3. Transform: Convert binary to string and parse JSON
parsed_df = (kafka_stream_df
    .selectExpr("CAST(value AS STRING) as json_payload")
    .select(from_json(col("json_payload"), schema).alias("data"))
    .select("data.*"))

# 4. Write to Delta Table
query = (parsed_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_location)
    .trigger(availableNow=True).toTable(target_table_name)) # Automatically creates the table if it doesn't exist
print("Started streaming..")
