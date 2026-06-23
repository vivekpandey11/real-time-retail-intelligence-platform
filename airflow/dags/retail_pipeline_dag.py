from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="retail_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    etl_load = BashOperator(
        task_id="etl_load",
        bash_command="""
        cd "/mnt/d/Real-time Retail Intelligence Platform" &&
        python3 scripts/etl/load_to_postgres.py
        """
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="""
        export PATH=$PATH:/home/vivek/.local/bin &&
        cd "/mnt/d/Real-time Retail Intelligence Platform/dbt/retail_dbt" &&
        dbt run
        """
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="""
        export PATH=$PATH:/home/vivek/.local/bin &&
        cd "/mnt/d/Real-time Retail Intelligence Platform/dbt/retail_dbt" &&
        dbt test
        """
    )

    etl_load >> dbt_run >> dbt_test