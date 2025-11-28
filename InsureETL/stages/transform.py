from pyspark.sql.functions import sum as _sum, avg, count

class TransformStage:
    def __init__(self, logger):

        self.logger = logger

    def enrich(self, claims, customers, policies, payments):
        return (claims.alias("c")
                .join(policies.alias("p"), "policy_id", "left")
                .join(customers.alias("cu"), "customer_id", "left")
                .join(payments.alias("pm"), "policy_id", "left"))

    def generate_metrics(self, df):
        return (df.groupBy("policy_id")
                .agg(
                    _sum("claim_amount").alias("total_claim_amount"),
                    count("claim_id").alias("total_claims"),
                    avg("amount").alias("avg_payment")
                ))
