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

# 2. Read Sales Data using Auto Loader
sales_stream = (
    spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .schema(sales_schema)
        .load("/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/live_sales")
)

# 3. Enriching the data by adding a processing timestamp or cleaning data
enriched_sales = sales_stream.withColumn("processed_at", current_timestamp()) \
                             .withColumn("is_high_value", col("amount") > 400)

# 4. Write to Table in Append Mode. Incremental data processing
query = (
    enriched_sales
        .writeStream
        .format("delta")
        .outputMode("append") 
        .option("checkpointLocation", "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/chkpoint_raw_append")
        .toTable("inceptez_streaming.inputdb.tbl_sales_raw_records")
)
print("Process is running...")
