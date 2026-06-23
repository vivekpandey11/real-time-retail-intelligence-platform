from airflow.models import BaseOperator


class RetailValidationOperator(BaseOperator):

    def execute(self, context):
        self.log.info("Retail ETL Validation Started")
        return True