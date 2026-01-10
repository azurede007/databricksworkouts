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



# COMMAND ----------

# MAGIC %md
# MAGIC ### Default Trigger (Unspecified)
# MAGIC If we don't specify a trigger, Spark will process data as soon as the previous micro-batch finishes.<br>
# MAGIC This is essentially "as fast as possible."

# COMMAND ----------

query = (enriched_sales.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/chkpoint_raw_default")
    .toTable("inceptez_streaming.inputdb.tbl_sales_default_records")
    .start()) # No trigger specified

# COMMAND ----------

# MAGIC %md
# MAGIC ### Processing Time Trigger (Fixed Interval)
# MAGIC This is the most common trigger. It runs micro-batches at a fixed interval (e.g., every 5 minute). If a batch takes longer than the interval, the next batch starts as soon as the current one finishes.
# MAGIC
# MAGIC Best for: Balancing cost and latency.

# COMMAND ----------

query = (enriched_sales.writeStream
    .format("delta")
    .trigger(processingTime='5 minutes') # Checks for data every 5 minutes
    .option("checkpointLocation", "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/chkpoint_raw_fixed_interval")
    .toTable("inceptez_streaming.inputdb.tbl_sales_fixed_records"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### AvailableNow Trigger (Incremental Batch)
# MAGIC This is a "Trigger Once" style. It processes all available data in the source and then stops the stream automatically. It is smarter than the old once=True because it can break large volumes of data into multiple micro-batches to avoid crashing the cluster.
# MAGIC
# MAGIC Best for: Cost-saving. Run this as a scheduled job once an hour or once a day.

# COMMAND ----------

query = (enriched_sales.writeStream
    .format("delta")
    .trigger(availableNow=True) # Process everything currently in the source and stop
    .option("checkpointLocation", "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/chkpoint_raw_available_interval")
    .toTable("inceptez_streaming.inputdb.tbl_sales_available_records"))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Continuous Trigger (Experimental)
# MAGIC This is for ultra-low latency (millisecond range). Instead of micro-batches, Spark processes data record-by-record. Note that it only supports specific operations (stateless) and has limited sink support.
# MAGIC
# MAGIC Best for: High-frequency trading or immediate fraud detection.

# COMMAND ----------

query = (
    enriched_sales.writeStream
    .format("console")
    .trigger(continuous='1 second')
    .option("checkpointLocation", "/Volumes/inceptez_streaming/sales_stream/sales_stream_volume/source/chkpoint_raw_continous_interval")
    .start()
)

# COMMAND ----------


