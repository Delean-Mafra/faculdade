from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.decorators import apply_defaults
from airflow.models import Variable

# Configurações padrão
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email': ['seu_email@exemplo.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_vendas_pipeline',
    default_args=default_args,
    description='Pipeline ETL para dados de vendas',
    schedule_interval='@daily',
    catchup=False,
    tags=['etl', 'vendas', 'spark']
)

# Variáveis
SPARK_MASTER = 'spark://localhost:7077'
HDFS_HOST = 'hdfs://localhost:9000'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5432
POSTGRES_DB = 'vendas_db'
POSTGRES_USER = Variable.get('postgres_user', 'postgres')
POSTGRES_PASSWORD = Variable.get('postgres_password', 'password')

# ============== CARGAS FULL ==============

task_carga_full_customers = SparkSubmitOperator(
    task_id='carga_full_customers',
    application='/path/to/spark_full_load.py',
    conf={
        'spark.master': SPARK_MASTER,
    },
    application_args=[
        '--table_name', 'customers',
        '--hdfs_path', f'{HDFS_HOST}/data_lake/bronze/customers',
        '--postgres_host', POSTGRES_HOST,
        '--postgres_port', str(POSTGRES_PORT),
        '--postgres_db', POSTGRES_DB,
        '--postgres_user', POSTGRES_USER,
        '--postgres_password', POSTGRES_PASSWORD,
    ],
    dag=dag
)

task_carga_full_products = SparkSubmitOperator(
    task_id='carga_full_products',
    application='/path/to/spark_full_load.py',
    conf={'spark.master': SPARK_MASTER},
    application_args=[
        '--table_name', 'products',
        '--hdfs_path', f'{HDFS_HOST}/data_lake/bronze/products',
        '--postgres_host', POSTGRES_HOST,
        '--postgres_port', str(POSTGRES_PORT),
        '--postgres_db', POSTGRES_DB,
        '--postgres_user', POSTGRES_USER,
        '--postgres_password', POSTGRES_PASSWORD,
    ],
    dag=dag
)

task_carga_full_order_items = SparkSubmitOperator(
    task_id='carga_full_order_items',
    application='/path/to/spark_full_load.py',
    conf={'spark.master': SPARK_MASTER},
    application_args=[
        '--table_name', 'order_items',
        '--hdfs_path', f'{HDFS_HOST}/data_lake/bronze/order_items',
        '--postgres_host', POSTGRES_HOST,
        '--postgres_port', str(POSTGRES_PORT),
        '--postgres_db', POSTGRES_DB,
        '--postgres_user', POSTGRES_USER,
        '--postgres_password', POSTGRES_PASSWORD,
    ],
    dag=dag
)

# ============== CARGAS INCREMENTAIS ==============

task_carga_incremental_orders = SparkSubmitOperator(
    task_id='carga_incremental_orders',
    application='/path/to/spark_incremental_load.py',
    conf={'spark.master': SPARK_MASTER},
    application_args=[
        '--hdfs_path', f'{HDFS_HOST}/data_lake/bronze/orders',
        '--postgres_host', POSTGRES_HOST,
        '--postgres_port', str(POSTGRES_PORT),
        '--postgres_db', POSTGRES_DB,
        '--postgres_user', POSTGRES_USER,
        '--postgres_password', POSTGRES_PASSWORD,
        '--processing_date', '{{ ds }}',
    ],
    dag=dag
)

# ============== TRANSFORMAÇÃO E CARREGAMENTO SILVER ==============

task_transform_silver = SparkSubmitOperator(
    task_id='transform_to_silver',
    application='/path/to/spark_silver_transform.py',
    conf={'spark.master': SPARK_MASTER},
    application_args=[
        '--hdfs_bronze', f'{HDFS_HOST}/data_lake/bronze',
        '--hdfs_silver', f'{HDFS_HOST}/data_lake/silver',
        '--processing_date', '{{ ds }}',
    ],
    dag=dag
)

# ============== VALIDAÇÃO ==============

def validate_data():
    """Valida dados na camada bronze"""
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder \
        .appName('ValidacaoDados') \
        .getOrCreate()
    
    # Validar contagem de registros
    customers_df = spark.read.parquet(f'{HDFS_HOST}/data_lake/bronze/customers')
    orders_df = spark.read.parquet(f'{HDFS_HOST}/data_lake/bronze/orders')
    
    customers_count = customers_df.count()
    orders_count = orders_df.count()
    
    print(f'Clientes: {customers_count}, Pedidos: {orders_count}')
    
    if customers_count == 0 or orders_count == 0:
        raise ValueError('Dados vazios detectados na validação!')
    
    spark.stop()

task_validation = PythonOperator(
    task_id='validate_bronze_layer',
    python_callable=validate_data,
    dag=dag
)

# ============== CARREGAMENTO GOLD E RELATÓRIO ==============

task_load_gold = SparkSubmitOperator(
    task_id='load_gold_layer',
    application='/path/to/spark_gold_load.py',
    conf={'spark.master': SPARK_MASTER},
    application_args=[
        '--hdfs_silver', f'{HDFS_HOST}/data_lake/silver',
        '--hdfs_gold', f'{HDFS_HOST}/data_lake/gold',
        '--processing_date', '{{ ds }}',
    ],
    dag=dag
)

# ============== ENVIO DE RELATÓRIO ==============

def generate_email_report():
    """Gera relatório em formato texto para envio"""
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder \
        .appName('GeracaoRelatorio') \
        .getOrCreate()
    
    # Leitura dos dados da camada gold
    gold_df = spark.read.parquet(f'{HDFS_HOST}/data_lake/gold/vendas')
    
    # Gerar conteúdo do relatório
    report = "RELATÓRIO DE VENDAS DO DIA\n"
    report += "="*50 + "\n\n"
    
    # Vendas por dia
    vendas_dia = gold_df.groupby('data').sum('total_vendas').collect()
    report += "TOTAL DE VENDAS:\n"
    for row in vendas_dia:
        report += f"Data: {row['data']}, Total: R$ {row['sum(total_vendas)']}\n"
    
    report += "\n" + "="*50 + "\n"
    
    spark.stop()
    return report

task_generate_report = PythonOperator(
    task_id='generate_report',
    python_callable=generate_email_report,
    dag=dag
)

task_send_email = EmailOperator(
    task_id='send_report_email',
    to=['seu_email@exemplo.com'],
    subject='Relatório de Vendas - {{ ds }}',
    html_content="""
    <html>
        <body>
            <h2>Relatório de Vendas</h2>
            <p>Data: {{ ds }}</p>
            <p>Verifique os dados em anexo ou acesse o painel de BI.</p>
        </body>
    </html>
    """,
    dag=dag
)

# ============== DEFINIR DEPENDÊNCIAS ==============

[task_carga_full_customers, 
 task_carga_full_products, 
 task_carga_full_order_items] >> task_carga_incremental_orders

task_carga_incremental_orders >> task_validation

task_validation >> task_transform_silver

task_transform_silver >> task_load_gold

task_load_gold >> task_generate_report >> task_send_email