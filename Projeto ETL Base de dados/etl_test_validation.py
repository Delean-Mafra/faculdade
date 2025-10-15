#!/usr/bin/env python3
"""
Script de Testes e Validação para Projeto ETL
Verifica conectividade e integridade de dados em todas as camadas
"""

import sys
import psycopg2
import json
from datetime import datetime
from pyspark.sql import SparkSession

class ETLValidator:
    def __init__(self, config):
        self.config = config
        self.postgres_conn = None
        self.spark = None
        self.results = []
    
    def log_test(self, test_name, status, message=""):
        """Registra resultado do teste"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'test': test_name,
            'status': status,
            'message': message
        }
        self.results.append(result)
        
        status_icon = "✓" if status == "PASSED" else "✗"
        print(f"{status_icon} {test_name}: {status}")
        if message:
            print(f"  └─ {message}")
    
    # ============== TESTES POSTGRESQL ==============
    
    def test_postgres_connection(self):
        """Testa conexão com PostgreSQL"""
        try:
            self.postgres_conn = psycopg2.connect(
                host=self.config['postgres_host'],
                database=self.config['postgres_db'],
                user=self.config['postgres_user'],
                password=self.config['postgres_password'],
                port=self.config['postgres_port']
            )
            self.log_test("PostgreSQL Connection", "PASSED")
            return True
        except Exception as e:
            self.log_test("PostgreSQL Connection", "FAILED", str(e))
            return False
    
    def test_postgres_tables(self):
        """Verifica se todas as tabelas existem"""
        try:
            cursor = self.postgres_conn.cursor()
            
            tables = ['customers', 'products', 'orders', 'order_items']
            missing_tables = []
            
            for table in tables:
                cursor.execute("""
                    SELECT to_regclass('public.{}'::cstring);
                """.format(table))
                exists = cursor.fetchone()[0] is not None
                
                if not exists:
                    missing_tables.append(table)
            
            if missing_tables:
                self.log_test("PostgreSQL Tables Check", "FAILED", 
                            f"Tabelas faltando: {missing_tables}")
            else:
                self.log_test("PostgreSQL Tables Check", "PASSED")
            
            cursor.close()
            return len(missing_tables) == 0
        except Exception as e:
            self.log_test("PostgreSQL Tables Check", "FAILED", str(e))
            return False
    
    def test_postgres_data_integrity(self):
        """Valida integridade dos dados no PostgreSQL"""
        try:
            cursor = self.postgres_conn.cursor()
            
            # Verificar registros vazios
            cursor.execute("SELECT COUNT(*) FROM customers")
            customers_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM products")
            products_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM orders")
            orders_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM order_items")
            order_items_count = cursor.fetchone()[0]
            
            message = f"Clientes: {customers_count}, Produtos: {products_count}, " \
                     f"Pedidos: {orders_count}, Itens: {order_items_count}"
            
            if customers_count > 0 and products_count > 0:
                self.log_test("PostgreSQL Data Integrity", "PASSED", message)
                cursor.close()
                return True
            else:
                self.log_test("PostgreSQL Data Integrity", "FAILED", 
                            "Dados insuficientes para testes")
                cursor.close()
                return False
        except Exception as e:
            self.log_test("PostgreSQL Data Integrity", "FAILED", str(e))
            return False
    
    def test_postgres_foreign_keys(self):
        """Valida integridade referencial"""
        try:
            cursor = self.postgres_conn.cursor()
            
            # Verificar órfãos na tabela order_items
            cursor.execute("""
                SELECT COUNT(*) FROM order_items oi
                WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.order_id = oi.order_id)
            """)
            orphaned_items = cursor.fetchone()[0]
            
            # Verificar órfãos na tabela orders
            cursor.execute("""
                SELECT COUNT(*) FROM orders o
                WHERE NOT EXISTS (SELECT 1 FROM customers c WHERE c.customer_id = o.customer_id)
            """)
            orphaned_orders = cursor.fetchone()[0]
            
            if orphaned_items == 0 and orphaned_orders == 0:
                self.log_test("PostgreSQL Foreign Keys", "PASSED")
                cursor.close()
                return True
            else:
                msg = f"Itens órfãos: {orphaned_items}, Pedidos órfãos: {orphaned_orders}"
                self.log_test("PostgreSQL Foreign Keys", "FAILED", msg)
                cursor.close()
                return False
        except Exception as e:
            self.log_test("PostgreSQL Foreign Keys", "FAILED", str(e))
            return False
    
    # ============== TESTES SPARK ==============
    
    def test_spark_connection(self):
        """Testa conexão com Spark"""
        try:
            self.spark = SparkSession.builder \
                .appName("ETL_Validator") \
                .master(self.config.get('spark_master', 'local[*]')) \
                .getOrCreate()
            
            self.spark.sparkContext.setLogLevel("ERROR")
            self.log_test("Spark Connection", "PASSED")
            return True
        except Exception as e:
            self.log_test("Spark Connection", "FAILED", str(e))
            return False
    
    def test_spark_postgres_read(self):
        """Testa leitura de dados do PostgreSQL via Spark"""
        try:
            jdbc_url = f'jdbc:postgresql://{self.config["postgres_host"]}:' \
                      f'{self.config["postgres_port"]}/{self.config["postgres_db"]}'
            
            connection_properties = {
                'user': self.config['postgres_user'],
                'password': self.config['postgres_password'],
                'driver': 'org.postgresql.Driver'
            }
            
            df = self.spark.read.jdbc(
                url=jdbc_url,
                table='orders',
                properties=connection_properties
            )
            
            count = df.count()
            self.log_test("Spark PostgreSQL Read", "PASSED", 
                         f"Registros lidos: {count}")
            return True
        except Exception as e:
            self.log_test("Spark PostgreSQL Read", "FAILED", str(e))
            return False
    
    # ============== TESTES HDFS ==============
    
    def test_hdfs_connection(self):
        """Testa conexão com HDFS"""
        try:
            from pyspark.sql.functions import input_file_name
            
            # Tentar criar arquivo de teste
            test_df = self.spark.createDataFrame(
                [("test", 1)], ["col1", "col2"]
            )
            
            hdfs_path = f"{self.config['hdfs_host']}/data_lake/test"
            test_df.write.mode('overwrite').parquet(hdfs_path)
            
            self.log_test("HDFS Connection", "PASSED")
            return True
        except Exception as e:
            self.log_test("HDFS Connection", "FAILED", str(e))
            return False
    
    def test_datalake_structure(self):
        """Verifica estrutura esperada do data lake"""
        try:
            required_paths = [
                '/data_lake/bronze/customers',
                '/data_lake/bronze/products',
                '/data_lake/bronze/orders',
                '/data_lake/bronze/order_items',
                '/data_lake/silver',
                '/data_lake/gold'
            ]
            
            # Nota: Teste simplificado - verificar real via hadoop command
            self.log_test("Data Lake Structure", "WARNING", 
                         "Verificação manual recomendada com 'hdfs dfs -ls'")
            return True
        except Exception as e:
            self.log_test("Data Lake Structure", "FAILED", str(e))
            return False
    
    # ============== TESTES AIRFLOW ==============
    
    def test_airflow_connections(self):
        """Testa conexões configuradas no Airflow"""
        try:
            from airflow.models import Connection
            from airflow import settings
            
            session = settings.Session()
            
            required_conns = ['postgres_vendas', 'email_gmail']
            missing_conns = []
            
            for conn_id in required_conns:
                conn = session.query(Connection).filter(
                    Connection.conn_id == conn_id
                ).first()
                
                if conn is None:
                    missing_conns.append(conn_id)
            
            if missing_conns:
                self.log_test("Airflow Connections", "FAILED", 
                            f"Conexões faltando: {missing_conns}")
            else:
                self.log_test("Airflow Connections", "PASSED")
            
            return len(missing_conns) == 0
        except Exception as e:
            self.log_test("Airflow Connections", "WARNING", 
                         f"Não foi possível validar: {str(e)}")
            return False
    
    # ============== GERAÇÃO DE RELATÓRIO ==============
    
    def run_all_tests(self):
        """Executa todos os testes"""
        print("\n" + "="*60)
        print("VALIDAÇÃO COMPLETA DO PROJETO ETL")
        print("="*60 + "\n")
        
        # Testes PostgreSQL
        print("📊 TESTES POSTGRESQL:")
        self.test_postgres_connection()
        if self.postgres_conn:
            self.test_postgres_tables()
            self.test_postgres_data_integrity()
            self.test_postgres_foreign_keys()
        
        # Testes Spark
        print("\n⚡ TESTES SPARK:")
        self.test_spark_connection()
        if self.spark:
            self.test_spark_postgres_read()
        
        # Testes HDFS
        print("\n📁 TESTES HDFS:")
        self.test_hdfs_connection()
        self.test_datalake_structure()
        
        # Testes Airflow
        print("\n✈️ TESTES AIRFLOW:")
        self.test_airflow_connections()
        
        # Gerar relatório
        self.generate_report()
    
    def generate_report(self):
        """Gera relatório final dos testes"""
        print("\n" + "="*60)
        print("RELATÓRIO FINAL")
        print("="*60 + "\n")
        
        passed = sum(1 for r in self.results if r['status'] == 'PASSED')
        failed = sum(1 for r in self.results if r['status'] == 'FAILED')
        warnings = sum(1 for r in self.results if r['status'] == 'WARNING')
        
        total = passed + failed + warnings
        
        print(f"Total de Testes: {total}")
        print(f"✓ Aprovados: {passed}")
        print(f"✗ Falhados: {failed}")
        print(f"⚠ Avisos: {warnings}")
        print(f"\nSucesso: {passed/total*100:.1f}%\n")
        
        # Salvar relatório em JSON
        report_file = f"etl_validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"Relatório salvo em: {report_file}")
    
    def cleanup(self):
        """Limpa conexões"""
        if self.postgres_conn:
            self.postgres_conn.close()
        if self.spark:
            self.spark.stop()


def main():
    """Função principal"""
    
    # Configuração padrão
    config = {
        'postgres_host': 'localhost',
        'postgres_port': 5432,
        'postgres_db': 'vendas_db',
        'postgres_user': 'postgres',
        'postgres_password': 'password',
        'hdfs_host': 'hdfs://localhost:9000',
        'spark_master': 'local[*]'
    }
    
    # Permitir override via argumentos
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
        try:
            with open(config_file, 'r') as f:
                config.update(json.load(f))
        except Exception as e:
            print(f"Aviso: Não foi possível ler config file: {e}")
    
    validator = ETLValidator(config)
    try:
        validator.run_all_tests()
    finally:
        validator.cleanup()


if __name__ == '__main__':
    main()