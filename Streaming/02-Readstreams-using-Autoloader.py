# Databricks notebook source
# MAGIC %md
# MAGIC ### Links and Resources
# MAGIC
# MAGIC - [Structured Streaming Concepts](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/concepts)
# MAGIC - [Structured Streaming Programming Guide](https://spark.apache.org/docs/3.5.1/structured-streaming-programming-guide.html)
# MAGIC - [What is Auto Loader?](https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/auto-loader/)
# MAGIC - [Schema Inference](https://learn.microsoft.com/en-gb/azure/databricks/ingestion/cloud-object-storage/auto-loader/schema)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading Streaming Data Files with Auto Loader

# COMMAND ----------

source_path = "dbfs:/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    load(source_path)

# COMMAND ----------

df1 = df.select("city","timestamp","temperature_c")

# COMMAND ----------

#df1.display()

df1.writeStream \
  .format("delta") \
  .option("checkpointLocation", "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/checkpointweather") \
  .table("inceptez_streaming.inputdb.tblweather")

print("Stream Started")

# COMMAND ----------

# MAGIC %md 
# MAGIC - Setting Max Bytes per Trigger 10 10GB
# MAGIC - Setting Max Files per Trigger 100

# COMMAND ----------

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    option("cloudFiles.maxFilesPerTrigger", "100").\
    option("cloudFiles.maxBytesPerTrigger", "10g"). \
    load(source_path)
