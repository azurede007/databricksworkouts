# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; padding-top: 10px;">
# MAGIC   <img src="https://fplogoimages.withfloats.com/actual/68009c3a43430aff8a30419d.png" 
# MAGIC        alt="Inceptez Technologies" 
# MAGIC        width="300">
# MAGIC   <h2 style="margin-top: 15px; color: #1f77b4;">Welcome to Learning Databricks</h2>
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #####1. Show the list of all available databricks utilities

# COMMAND ----------

dbutils.help()

# COMMAND ----------

# MAGIC %md
# MAGIC #####2. Show the documentation for fs utility

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# MAGIC %md
# MAGIC #####3. Show the documentation for the cp command of the fs utiltity

# COMMAND ----------

dbutils.fs.help("cp")

# COMMAND ----------

# MAGIC %md
# MAGIC #####4. Use the file system command to list the content of the following directory
# MAGIC ```
# MAGIC /databricks-datasets
# MAGIC ```  

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets

# COMMAND ----------

# MAGIC %md
# MAGIC #####5. Use the file system utility to list the content of the following directory
# MAGIC ```
# MAGIC 	/databricks-datasets
# MAGIC ```

# COMMAND ----------

dbutils.fs.ls("/databricks-datasets")

# COMMAND ----------

# MAGIC %md
# MAGIC #####6.Loop through the items in the databricks-datasets and print the path of each item

# COMMAND ----------

for items in dbutils.fs.ls("/databricks-datasets"):
    print(items.path)
