# Exemplos da aula 2

from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd
import time

# Video 1 - Operadores

def task2():
    print('Ola mundo')


with DAG(
    dag_id="operator_dag",
    schedule=None,
    start_date=datetime(year=2020, month=1, day=1)
) as dag:

    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'Ola Mundo'"
    )

    task2 = PythonOperator(
        task_id="task2",
        python_callable=task2
    )

    task1 >> task2


# Video 2 - Hooks


AIRFLOW_HOME = '/Volumes/GeekFoxLab/Projetos/Descomplica/Aulas/'

def read_data():
    pg_hook = PostgresHook(postgres_conn_id='PG_SWORDBLAST')
    pg_hook.copy_expert(
        sql="COPY (SELECT * FROM characters) TO stdout WITH CSV HEADER",
        filename=AIRFLOW_HOME + 'data/characters.csv'
    )

def copy_data():
    lines = []
    with open(AIRFLOW_HOME + 'data/characters.csv', 'r') as f:
        for line in f:
            lines.append(line)

    with open(AIRFLOW_HOME + 'data/characters_new.csv', 'w') as f:
        f.writelines(lines)

with DAG(
    dag_id="hook_dag",
    schedule=None,
    start_date=datetime(year=2020, month=1, day=1),
) as dag:

    task1 = PythonOperator(
        task_id="task1",
        python_callable=read_data
    )

    task2 = PythonOperator(
        task_id="task2",
        python_callable=copy_data
    )

    task1 >> task2



# Video 3 - XCom



AIRFLOW_HOME = '/Volumes/GeekFoxLab/Projetos/Descomplica/Aulas/'

def read_players():
    pghook = PostgresHook(postgres_conn_id="PG_SWORDBLAST")
    pghook.copy_expert(
        sql="COPY (SELECT * FROM players) TO stdout WITH CSV HEADER",
        filename=AIRFLOW_HOME + "/data/players.csv"
    )

def read_currency():
    pghook = PostgresHook(postgres_conn_id="PG_SWORDBLAST")
    pghook.copy_expert(
        sql="COPY (SELECT * FROM currency) TO stdout WITH CSV HEADER",
        filename=AIRFLOW_HOME + "/data/currency.csv"
    )

def read_currency_modified():
    pghook = PostgresHook(postgres_conn_id="PG_SWORDBLAST")
    pghook.copy_expert(
        sql="COPY (SELECT * FROM currency) TO stdout WITH CSV HEADER",
        filename=AIRFLOW_HOME + "/data/currency_modified.csv"
    )

def read_player_ids(ti):
    df = pd.read_csv(AIRFLOW_HOME + "/data/players.csv")
    player_ids = df['player_id'].tolist()
    ti.xcom_push(key='player_ids', value=player_ids)

with DAG(
    dag_id='xcom_dag',
    schedule=None,
    start_date=datetime(year=2020, month=1, day=1)
) as dag:

    task1 = PythonOperator(
        task_id='read_players',
        python_callable=read_players
    )

    task2 = PythonOperator(
        task_id='read_currency',
        python_callable=read_currency
    )

    task3 = PythonOperator(
        task_id='read_playerid',
        python_callable=read_player_ids
    )

    task4 = PythonOperator(
        task_id='read_currency_modified',
        python_callable=read_currency_modified
    )

    task5 = SQLExecuteQueryOperator(
        task_id='update_currency',
        conn_id='PG_SWORDBLAST',
        sql="""
        UPDATE currency 
        SET currency_amount = currency_amount + 500 
        WHERE player_id IN (
            '{{ task_instance.xcom_pull(task_ids="read_playerid", key="player_ids") }}'
        )
        """
    )

    task1 >> task2 >> task3 >> task4 >> task5



# Fluxo de execução



AIRFLOW_HOME = '/Volumes/GeekFoxLab/Projetos/Descomplica/Aulas/'

# Funções de tarefas
def read_players():
    pghook = PostgresHook(postgres_conn_id="PG_SWORDBLAST")
    pghook.copy_expert(
        sql="COPY (SELECT * FROM players) TO stdout WITH CSV HEADER",
        filename=AIRFLOW_HOME + "/data/players.csv"
    )

def read_currency():
    pghook = PostgresHook(postgres_conn_id="PG_SWORDBLAST")
    pghook.copy_expert(
        sql="COPY (SELECT * FROM currency) TO stdout WITH CSV HEADER",
        filename=AIRFLOW_HOME + "/data/currency.csv"
    )

def read_currency_modified():
    pghook = PostgresHook(postgres_conn_id="PG_SWORDBLAST")
    pghook.copy_expert(
        sql="COPY (SELECT * FROM currency) TO stdout WITH CSV HEADER",
        filename=AIRFLOW_HOME + "/data/currency_modified.csv"
    )

def read_player_ids(ti):
    df = pd.read_csv(AIRFLOW_HOME + "/data/players.csv")
    player_ids = df['player_id'].tolist()
    ti.xcom_push(key='player_ids', value=player_ids)

# Funções de exemplo com delay
def task0():
    print('task0')
    time.sleep(6)

def task1():
    print('task1')
    time.sleep(6)

def task2():
    print('task2')
    time.sleep(6)

def task3():
    print('task3')
    time.sleep(6)

def task4():
    print('task4')
    time.sleep(6)

def task5():
    print('task5')

# Definição da DAG
with DAG(
    dag_id='execution_dag',
    schedule=None,
    start_date=datetime(year=2020, month=1, day=1)
) as dag:

    t0 = PythonOperator(task_id='task0', python_callable=task0)
    t1 = PythonOperator(task_id='task1', python_callable=task1)
    t2 = PythonOperator(task_id='task2', python_callable=task2)
    t3 = PythonOperator(task_id='task3', python_callable=task3)
    t4 = PythonOperator(task_id='task4', python_callable=task4)
    t5 = PythonOperator(task_id='task5', python_callable=task5)

    read_players_task = PythonOperator(task_id='read_players', python_callable=read_players)
    read_currency_task = PythonOperator(task_id='read_currency', python_callable=read_currency)
    read_playerid_task = PythonOperator(task_id='read_playerid', python_callable=read_player_ids)
    read_currency_mod_task = PythonOperator(task_id='read_currency_modified', python_callable=read_currency_modified)

    update_currency_task = SQLExecuteQueryOperator(
        task_id='update_currency',
        conn_id='PG_SWORDBLAST',
        sql="""
        UPDATE currency 
        SET currency_amount = currency_amount + 500 
        WHERE player_id IN (
            '{{ task_instance.xcom_pull(task_ids="read_playerid", key="player_ids") }}'
        )
        """
    )

    # Dependências
    t0 >> t1 >> t2
    [t2, t3, t4] >> t5

    read_players_task >> read_currency_task >> read_playerid_task >> read_currency_mod_task >> update_currency_task
