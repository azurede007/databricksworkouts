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

# 3. Aggregation Logic
# We group by 'city' to get a cumulative running total.
sales_agg = (
    sales_stream
        .groupBy(col("city")) 
        .agg(
            sum("amount").alias("total_revenue"), 
            count("transaction_id").alias("transaction_count"),
            max("timestamp").alias("last_transaction_at")
        )
)

# 4. Write to Table in UPDATE Mode
def upsert_to_delta(microBatchDF, batchId):
    # Standard way to access spark session in Spark Connect
    spark = microBatchDF.sparkSession
    
    # Register the micro-batch as a temporary view
    microBatchDF.createOrReplaceTempView("updates")
    
    # Use standard SQL for the Merge
    spark.sql("""
        MERGE INTO inceptez_streaming.inputdb.tbl_city_sales_summary AS target
        USING updates AS source
        ON target.city = source.city
        WHEN MATCHED THEN 
          UPDATE SET 
            target.total_revenue = source.total_revenue,
            target.transaction_count = source.transaction_count,
            target.last_transaction_at = source.last_transaction_at
        WHEN NOT MATCHED THEN 
          INSERT (city, total_revenue, transaction_count, last_transaction_at)
          VALUES (source.city, source.total_revenue, source.transaction_count, source.last_transaction_at)
    """)

sales_agg.writeStream \
    .foreachBatch(upsert_to_delta) \
    .outputMode("update") \
    .option("checkpointLocation", "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/chkpoint_update_sales1") \
    .start()

print("Running processing...")
