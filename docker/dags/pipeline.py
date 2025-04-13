from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


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
    'pipeline_garrafa_stanley',
    default_args = default_args,
    description = 'Pipeline Mackenzie',
    schedule = None,
    catchup=False,
    tags=['pipeline']
)

tsk_gera_csv = BashOperator(
    task_id = 'scrap_magalu',
    bash_command='scrapy runspider /opt/airflow/dags/scrap_magalu.py -O /opt/airflow/dags/sscrap_result.csv',
    dag=dag,
)

tsk_gera_csv