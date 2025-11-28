import traceback
from pyspark.sql.functions import col

class IngestStage:
    def __init__(self, spark, delta_db, offset_manager, logger):
        """
        delta_db: Database where Delta tables exist (bronze tables)
        """
        self.spark = spark
        self.delta_db = delta_db
        self.offset_manager = offset_manager
        self.logger = logger

    def _read(self, table, where=None):
        """
        Equivalent of reading MySQL, but now reading Delta tables.
        """
        try:
            full_table = f"{self.delta_db}.{table}"

            df = self.spark.table(full_table)

            if where:
                df = df.filter(where)

            return df

        except Exception as e:
            self.logger.error(str(e))
            self.logger.error(traceback.format_exc())
            raise

    def load_incremental(self, table, pk):
        """
        Loads **incremental Delta data** using the offset manager.
        """
        try:
            last = self.offset_manager.get_last_offset(table)
            where = f"{pk} > {last}"

            df = self._read(table, where)

            count = df.count()
            self.logger.info(f"Loaded {count} new rows from Delta table: {table}")

            return df

        except Exception as e:
            self.logger.error("Failed incremental load: " + str(e))
            self.logger.error(traceback.format_exc())
            raise
