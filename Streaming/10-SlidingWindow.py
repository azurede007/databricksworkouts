# Databricks notebook source
from pyspark.sql.types import *
from pyspark.sql.functions import *

# 1. Define Sales Schema
# Matches the generator: transaction_id, timestamp, city, category, amount, payment_method
sales_schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("city", StringType(), True),
    StructField("category", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("payment_method", StringType(), True)
])

# 2. Read Sales Data with Auto Loader
sales_stream = (
    spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .schema(sales_schema)
        # Point to the sales volume path
        .load("/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/live_sales")
)

# 3. Aggregation with Sliding Window
# Calculating revenue every 1 minute for the last 2 minutes
sales_agg = (
    sales_stream
        .withWatermark("timestamp", "1 minute") 
        .groupBy(
            window(col("timestamp"), "2 minutes", "1 minute"), 
            col("city")
        )
        .agg(
            sum("amount").alias("total_revenue"),
            count("transaction_id").alias("transaction_count"),
            avg("amount").alias("avg_transaction_value")
        )
)

# 4. Write to Sales Delta Table
query = (
    sales_agg
        .writeStream
        .format("delta")
        .outputMode("append")
        .option("checkpointLocation", "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/chkpoint_sales_agg")
        .toTable("inceptez_streaming.inputdb.tbl_sales_metrics")
)
