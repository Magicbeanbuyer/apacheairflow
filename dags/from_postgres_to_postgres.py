from airflow import DAG
from datetime import datetime, timedelta

from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from psycopg2.extras import execute_values

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 5, 11),
    "depends_on_past": False,  # dag will run even if the last run failed
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "email@mail.com",
    "retires": 1,
    "retry_delay": timedelta(minutes=3)
}


def etl(ds, **kwargs):
    query = "select * from customers"

    src_conn = PostgresHook(postgres_conn_id='postgres_customer_service').get_conn()
    dest_conn = PostgresHook(postgres_conn_id='postgres_data_service').get_conn()

    src_cursor = src_conn.cursor("serverCursor")
    src_cursor.execute(query)
    dest_cursor = dest_conn.cursor()

    while True:
        records = src_cursor.fetchmany(size=2000)
        if not records:
            break
        dest_cursor.execute("DELETE FROM customers.customers")
        execute_values(dest_cursor, "INSERT INTO customers.customers VALUES %s", records)
        dest_conn.commit()

    src_cursor.close()
    dest_cursor.close()
    src_conn.close()
    dest_conn.close()


with DAG(dag_id="postgres_to_postgres", default_args=default_args, catchup=False) as dag:
    postgres_to_postgres = PythonOperator(
        task_id='postgres_to_postgres',
        provide_context=True,
        python_callable=etl,
        dag=dag
    )
