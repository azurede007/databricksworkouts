# Databricks notebook source
# MAGIC %md
# MAGIC ## Checkpoint Directory – Summary
# MAGIC
# MAGIC ### 1. `offsets/`
# MAGIC - Tracks what data has been processed in each micro-batch  
# MAGIC - Stores **file names** (Auto Loader) or **partition offsets** (Kafka)  
# MAGIC - Enables **exactly-once processing** by preventing duplicate reads  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 2. `commits/`
# MAGIC - Confirms a micro-batch was **successfully written to the sink**  
# MAGIC - On restart, Spark reprocesses batches with offsets but **missing commits**  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 3. `state/`
# MAGIC - Present only for **stateful operations** (window, groupBy, deduplication)  
# MAGIC - Stores intermediate aggregation values  
# MAGIC - Uses **RocksDB / StateStore** to survive cluster restarts  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 4. `metadata`
# MAGIC - Contains a **unique Stream ID**  
# MAGIC - Prevents multiple streaming queries from sharing the same checkpoint  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### 5. `sources/` (Auto Loader only)
# MAGIC - Maintains the **file discovery log**  
# MAGIC - Tracks every processed file path  
# MAGIC - Ensures scalable ingestion even with millions of files  
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Summary
# MAGIC > The checkpoint directory ensures **fault tolerance, exactly-once processing, and reliable recovery** for Spark Structured Streaming jobs.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading Streaming from delta table

# COMMAND ----------

df = spark.readStream.\
    format("delta").\
    table("inceptez_streaming.inputdb.tblsales")

df.createOrReplaceTempView("sales")

df1 = spark.sql("select * from sales where salesamt > 5000")

#df1.display()

df1.writeStream \
  .format("delta") \
  .option("checkpointLocation", "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/checkpoint") \
  .table("inceptez_streaming.inputdb.tblsales1")

print("Processing Running...")


# COMMAND ----------

# MAGIC %md 
# MAGIC ### To Generate test data for Demo or Validation

# COMMAND ----------

df = spark.readStream \
  .format("rate") \
  .option("rowsPerSecond", 5) \
  .load()

display(df)
