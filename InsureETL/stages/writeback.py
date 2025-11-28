class WriteBackStage:
    def __init__(self, delta_db, logger):
        """
        delta_db: The database where the metrics Delta table lives
        """
        self.delta_db = delta_db
        self.logger = logger

    def write_metrics(self, df):
        """
        Writes aggregated metrics into Delta table: <delta_db>.insurance_metrics
        """
        try:
            full_table = f"{self.delta_db}.insurance_metrics"

            (
                df.write
                .format("delta")
                .option("mergeSchema", "true")
                .mode("append")
                .saveAsTable(full_table)
            )

            self.logger.info("Metrics written to Delta table")

        except Exception as e:
            self.logger.error(f"Error writing metrics: {str(e)}")
            raise
