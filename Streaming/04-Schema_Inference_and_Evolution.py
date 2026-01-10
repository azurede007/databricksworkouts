# Databricks notebook source
# MAGIC %md
# MAGIC ### Links and Resources
# MAGIC
# MAGIC - [Configure schema inference and evolution in Auto Loader](https://learn.microsoft.com/en-gb/azure/databricks/ingestion/cloud-object-storage/auto-loader/schema)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Setting the Schema Evolution Mode
# MAGIC
# MAGIC | Schema Evolution Mode | Behavior on New Columns | Typical Use Case |
# MAGIC |----------------------|------------------------|------------------|
# MAGIC | none | Ignores new columns. Pipeline keeps running. | Pipeline not to fail on schema change |
# MAGIC | addNewColumns | Automatically adds new columns | Most production pipelines |
# MAGIC | rescue | Stores unexpected columns in `_rescued_data` | Controlled / governed ingestion |
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC `none` Does not evolve the schema, new columns are ignored, and data is not rescued unless the rescuedDataColumn option is set. Stream does not fail due to schema changes.

# COMMAND ----------

source_path = "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    option("cloudFiles.schemaEvolutionMode", "none").\
    load(source_path)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC `addNewColumns` is the default. Stream fails. New columns are added to the schema. Existing columns do not evolve data types.

# COMMAND ----------

source_path = "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    option("cloudFiles.schemaEvolutionMode", "addNewColumns").\
    load(source_path)

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC `rescue` Schema is never evolved and stream does not fail due to schema changes. All new columns are recorded in the rescued data column.

# COMMAND ----------

source_path = "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/inceptez_streaming/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    option("cloudFiles.schemaEvolutionMode", "rescue").\
    load(source_path)

df.display()
