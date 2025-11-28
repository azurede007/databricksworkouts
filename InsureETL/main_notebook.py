# Databricks notebook source
# MAGIC %md
# MAGIC # Insurance ETL - Main Notebook
# MAGIC
# MAGIC Orchestration notebook for the Insurance ETL pipeline (Extract -> Transform -> Load).

# COMMAND ----------

# MAGIC %md
# MAGIC ##Import class

# COMMAND ----------

from utils.logger import get_logger
from utils.offsets import OffsetManager
from stages.ingest import IngestStage
from stages.transform import TransformStage
from stages.writeback import WriteBackStage
import yaml, sys, traceback
logger = get_logger('InsuranceETL')

def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Creating Object for the required classes

# COMMAND ----------

config = load_config("conf/config.yml")
offset_table   = config["delta"]["offset_table"]
delta_db       = config["delta"]["database"]
# Offset manager (Delta version)
offset_mgr = OffsetManager(spark=spark, delta_db=delta_db)

# ETL pipeline stages (Delta versions)
ingest = IngestStage(spark=spark, delta_db=delta_db, offset_manager=offset_mgr, logger=logger)
transform = TransformStage(logger=logger)
writeback = WriteBackStage(delta_db=delta_db, logger=logger)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read incremental data

# COMMAND ----------


# Incremental loads from Delta tables
claims    = ingest.load_incremental("claims", "claim_id")
customers = ingest.load_incremental("customers", "customer_id")
policies  = ingest.load_incremental("policies", "policy_id")
payments  = ingest.load_incremental("payments", "payment_id")



# COMMAND ----------

# MAGIC %md
# MAGIC ## Transform

# COMMAND ----------

curated = transform.enrich(claims, customers, policies, payments)
metrics = transform.generate_metrics(curated)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Generate Metrics

# COMMAND ----------

writeback.write_metrics(metrics)

# COMMAND ----------

# Update Delta-based offsets
offset_mgr.update_offset("claims", "claim_id", claims)
offset_mgr.update_offset("customers", "customer_id", customers)
offset_mgr.update_offset("policies", "policy_id", policies)
offset_mgr.update_offset("payments", "payment_id", payments)

logger.info("ETL Completed Successfully")
