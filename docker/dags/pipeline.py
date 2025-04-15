from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import datetime
from process_csv import load_csv_to_postgres, archive_file, remove_file
from send_alert import send_email
from ai_feedback import ai_request

default_args = {
    'owner':'Mário Kojima',
    'start_date': datetime.datetime(2025,4,12)
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
    bash_command='scrapy runspider /opt/airflow/dags/scrap_magalu.py -O /opt/airflow/dags/scrap_result.csv',
    dag=dag,
)

csv_file_path = '/opt/airflow/dags/scrap_result.csv' 
db_params = {
    'host': '172.17.0.1',  
    'database': 'postgres', 
    'user': 'postgres',     
    'password': '1234'  
}
destination_file = f"scrap_result_{str(datetime.datetime.now()).replace(' ','_').split('.')[0]}.csv"

# alerts configuration
ob_alert = {
   "subject" : f"Pipeline Executada com sucesso - {str(datetime.datetime.now()).split('.')[0]}",
    "body" : f"Pipeline Executada com sucesso às {str(datetime.datetime.now()).split('.')[0]}",
    "sender" : "mariokojima@gmail.com",
    "recipients" : ["mariokojima@gmail.com", "mariokojimajunior@gmail.com"] 
}



tsk_etl_scrap = PythonOperator(
    task_id='etl_scrap',
    python_callable=load_csv_to_postgres,
    provide_context=True,
    op_kwargs={"csv_file_path":csv_file_path, "db_params":db_params}
)

tsk_storage_scrap = PythonOperator(
    task_id='storage_scrap',
    python_callable=archive_file,
    provide_context=True,
    op_kwargs={"source_file": csv_file_path, "destination_file": destination_file }
)

tsk_remove_file = PythonOperator(
    task_id='remove_file',
    python_callable=remove_file,
    provide_context=True,
    op_kwargs={"source_file": csv_file_path}
)

tsk_ai_feedback = PythonOperator(
    task_id='ai_feedback',
    python_callable=ai_request,
    provide_context=True,
    op_kwargs={"db_params":db_params}
)


tsk_send_alert = PythonOperator(
    task_id='send_alert',
    python_callable=send_email,
    provide_context=True,
    op_kwargs=ob_alert
)



tsk_gera_csv >> tsk_etl_scrap >> tsk_storage_scrap >> tsk_remove_file  >> tsk_ai_feedback >> tsk_send_alert