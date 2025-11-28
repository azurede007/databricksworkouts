from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from delta.tables import DeltaTable

class OffsetManager:
    def __init__(self, spark: SparkSession, delta_db: str = "default"):
        """
        delta_db: Database where etl_offsets delta table exists
        """
        self.spark = spark
        self.delta_table_path = f"{delta_db}.etl_offsets"

    def get_last_offset(self, table: str) -> int:
        """
        Reads offset from Delta table.
        Equivalent SQL:
        SELECT last_offset
        FROM etl_offsets
        WHERE table_name = '<table>'
        ORDER BY inserted_ts DESC
        LIMIT 1
        """
        try:
            df = (
                self.spark.table(self.delta_table_path)
                .filter(F.col("table_name") == table)
                .orderBy(F.col("inserted_ts").desc())
                .limit(1)
            )

            if df.count() == 0:
                return 0

            return df.first()["last_offset"]

        except Exception as e:
            print(f"Error reading last offset for {table}: {e}")
            return 0

    def update_offset(self, table: str, pk: str, df):
        """
        Writes updated offset into Delta table.
        """
        try:
            if df.count() == 0:
                return

            max_pk = df.agg({pk: "max"}).first()[0]
            print(f"Updating Delta offset → table={table}, last_offset={max_pk}")

            offset_df = self.spark.createDataFrame(
                [(table, max_pk)],
                ["table_name", "last_offset"]
            ).withColumn("inserted_ts", F.current_timestamp())

            offset_df.write.format("delta").mode("append").saveAsTable(self.delta_table_path)

            print("Delta offset updated successfully.")

        except Exception as e:
            print("Failed to update Delta offset:", e)
