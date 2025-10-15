import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date, col
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Carga Full no Data Lake')
    parser.add_argument('--table_name', required=True, help='Nome da tabela no PostgreSQL')
    parser.add_argument('--hdfs_path', required=True, help='Caminho no HDFS')
    parser.add_argument('--postgres_host', required=True)
    parser.add_argument('--postgres_port', required=True, type=int)
    parser.add_argument('--postgres_db', required=True)
    parser.add_argument('--postgres_user', required=True)
    parser.add_argument('--postgres_password', required=True)
    
    args = parser.parse_args()
    
    # Inicializar SparkSession
    spark = SparkSession.builder \
        .appName(f'CargaFull_{args.table_name}') \
        .config('spark.jars.packages', 'org.postgresql:postgresql:42.5.0') \
        .getOrCreate()
    
    try:
        # Configuração de conexão PostgreSQL
        jdbc_url = f'jdbc:postgresql://{args.postgres_host}:{args.postgres_port}/{args.postgres_db}'
        connection_properties = {
            'user': args.postgres_user,
            'password': args.postgres_password,
            'driver': 'org.postgresql.Driver'
        }
        
        # Ler dados do PostgreSQL
        print(f'Lendo tabela {args.table_name} do PostgreSQL...')
        df = spark.read.jdbc(
            url=jdbc_url,
            table=args.table_name,
            properties=connection_properties
        )
        
        print(f'Total de registros lidos: {df.count()}')
        
        # Adicionar coluna de data de partição
        today = datetime.now().strftime('%Y-%m-%d')
        df_partitioned = df.withColumn('data_carga', col(f"to_date('{today}')"))
        
        # Salvar no HDFS em formato Parquet com partição
        output_path = f"{args.hdfs_path}/{today}"
        print(f'Salvando dados em {output_path}...')
        
        df_partitioned.write \
            .mode('overwrite') \
            .format('parquet') \
            .save(output_path)
        
        print(f'Carga full de {args.table_name} concluída com sucesso!')
        
    except Exception as e:
        print(f'Erro durante carga full: {str(e)}')
        raise
    finally:
        spark.stop()

if __name__ == '__main__':
    main()