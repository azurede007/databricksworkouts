# Databricks notebook source
from pyspark.sql.types import *
from pyspark.sql.functions import *

# 1. Define Sales Schema
sales_schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("city", StringType(), True),
    StructField("category", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("payment_method", StringType(), True)
])

# 2. Read with Auto Loader
sales_stream = (
    spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .schema(sales_schema)
        .load("/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/live_sales")
)

# 3. Simple Aggregation
# In Complete Mode, we often aggregate across the entire history
sales_total = (
    sales_stream
        .groupBy("category")
        .agg(
            sum("amount").alias("grand_total_revenue"),
            count("*").alias("total_transactions")
        )
        .orderBy(col("grand_total_revenue").desc()) # Sorting is allowed in Complete Mode
)

# 4. Write to Table in COMPLETE Mode
query = (
    sales_total
        .writeStream
        .format("delta")
        .outputMode("complete") # Entire table is overwritten each batch
        .option("checkpointLocation", "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/chkpoint_complete_mode")
        .toTable("inceptez_streaming.inputdb.tbl_sales_global_leaderboard")
)
print("process is running..")
