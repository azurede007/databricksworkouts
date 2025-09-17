# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: center; padding-top: 10px;">
# MAGIC   <img src="https://fplogoimages.withfloats.com/actual/68009c3a43430aff8a30419d.png" 
# MAGIC        alt="Inceptez Technology" 
# MAGIC        width="300">
# MAGIC   <h2 style="margin-top: 15px; color: #1f77b4;">Welcome to Learning Databricks</h2>
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #####1. Create a Python Notebook

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 2. Execute the following SQL statement from the notebook
# MAGIC ```
# MAGIC SELECT "Hello Inceptez!"
# MAGIC ```

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World!"

# COMMAND ----------

# MAGIC %md
# MAGIC #####3. Execute the following Scala code from the notebook
# MAGIC ```scala
# MAGIC     var msg = "Hello World!"
# MAGIC     println(msg)
# MAGIC ```

# COMMAND ----------

# MAGIC %scala
# MAGIC var msg = "Hello World!"
# MAGIC println(msg)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 4. Create following markdown at the last cell of your notebook
# MAGIC
# MAGIC @ 2021-2023 ScholarNest Technologies Pvt. Ltd. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC Databricks, Databricks Cloud and the Databricks logo are trademarks of the <a href="https://www.databricks.com/">Databricks Inc</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://www.scholarnest.com/privacy/">Privacy Policy</a> | 
# MAGIC <a href="https://www.scholarnest.com/terms/">Terms of Use</a> | <a href="https://www.scholarnest.com/contact/">Contact Us</a>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #####5. Use the file system command to list the content of the following directory
# MAGIC ```
# MAGIC /databricks-datasets
# MAGIC ```

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets

# COMMAND ----------

# MAGIC %md
# MAGIC #####6.Use the file system command to explore airlines dataset in the databricks example data sets.

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls /databricks-datasets/airlines

# COMMAND ----------

# MAGIC %md
# MAGIC #####7. Use the tail shell command to show few lines of a airlines data file

# COMMAND ----------

# MAGIC %sh
# MAGIC tail /databricks-datasets/airlines/part-00000

# COMMAND ----------

# MAGIC %md
# MAGIC #####8. Show the list of all magic commands in a Databricks Notebook

# COMMAND ----------

# MAGIC %lsmagic

# COMMAND ----------

# MAGIC %md
# MAGIC #####9. Show the list all the environment variables using env magic command

# COMMAND ----------

# MAGIC %env

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Set Environment variable

# COMMAND ----------

# MAGIC %md
# MAGIC #####10. Install python library using pip magic command

# COMMAND ----------

# MAGIC %env MY_ENV='Hello'

# COMMAND ----------

# MAGIC %pip faker

# COMMAND ----------

# MAGIC %%writefile /tmp/test.py
# MAGIC print("Hello World")
# MAGIC
# MAGIC
