from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd


def generate_csv():
    data={
        'nomes': ['mario','erika','eric','nina']
    }
    df = pd.DataFrame(data)
    df.to_csv('teste_dag.csv')


default_args = {
    'owner':'Mário Kojima',
    'start_date': datetime(2025,4,12)
}

dag =  DAG(
    'dag_gera_csv',
    default_args = default_args,
    description = 'Teste Airflow',
    schedule = None,
    catchup=False,
    tags=['teste']
)

tsk_gera_csv = PythonOperator(
    task_id = 'gera_csv',
    python_callable = generate_csv,
    dag=dag,
)

tsk_gera_csv