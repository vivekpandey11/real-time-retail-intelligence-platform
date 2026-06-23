import os

folders = [
"data/raw/kaggle",
"data/raw/excel",
"data/raw/streaming",
"data/processed/cleaned",
"data/processed/transformed",
"data/sample_data",

"scripts/data_generation",
"scripts/ingestion",
"scripts/etl",
"scripts/utils",

"notebooks",

"sql/postgres",
"sql/snowflake",
"sql/dbt_queries",

"airflow/dags",
"airflow/plugins",
"airflow/logs",

"dbt/models/staging",
"dbt/models/marts",
"dbt/tests",

"kafka/config",

"docker",

"database/postgres",
"database/snowflake",

"dashboards/powerbi",
"dashboards/tableau",
"dashboards/qlik",

"ml_model",

"logs/airflow_logs",
"logs/kafka_logs",
"logs/pipeline_logs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("✅ Project structure created successfully!")