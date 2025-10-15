# Guia Completo: Implementação de Projeto ETL com Airflow e Spark

## 1. PRÉ-REQUISITOS E CONFIGURAÇÃO INICIAL

### 1.1 Instalação de Dependências

```bash
# Criar ambiente virtual Python
python3 -m venv etl_env
source etl_env/bin/activate  # Linux/Mac
# ou
etl_env\Scripts\activate  # Windows

# Instalar Apache Airflow
pip install apache-airflow==2.7.0
pip install apache-airflow-providers-spark==3.1.0
pip install apache-airflow-providers-postgres==5.6.0
pip install apache-airflow-providers-email==0.4.0

# Instalar PySpark
pip install pyspark==3.4.0

# Instalar cliente PostgreSQL
pip install psycopg2-binary

# Instalar driver JDBC para Spark
# Será necessário durante a execução do Spark
```

### 1.2 Estrutura de Diretórios

```
projeto-etl/
├── dags/
│   └── etl_vendas_pipeline.py          # DAG principal do Airflow
├── scripts/
│   ├── spark_full_load.py              # Script carga full
│   ├── spark_incremental_load.py       # Script carga incremental
│   ├── spark_silver_transform.py       # Script transformação silver
│   └── spark_gold_load.py              # Script carregamento gold
├── sql/
│   ├── create_tables.sql               # Criar tabelas PostgreSQL
│   ├── insert_sample_data.sql          # Dados de exemplo
│   └── validation_queries.sql          # Queries de validação
├── config/
│   └── airflow_connections.yaml        # Configurações Airflow
└── docker-compose.yml                  # Stack completo (opcional)
```

## 2. CONFIGURAÇÃO DO POSTGRESQL

### 2.1 Criar Banco de Dados e Tabelas

```sql
-- Criar banco de dados
CREATE DATABASE vendas_db;

-- Conectar ao banco
\c vendas_db;

-- Tabela de Clientes
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(20),
    city VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Produtos
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Pedidos
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    order_date TIMESTAMP NOT NULL,
    total_amount DECIMAL(10, 2),
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Itens do Pedido
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(order_id),
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar índices para performance
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);
```

### 2.2 Inserir Dados de Exemplo

```sql
-- Inserir clientes
INSERT INTO customers (customer_name, email, phone, city) VALUES
('João Silva', 'joao@email.com', '11999999999', 'São Paulo'),
('Maria Santos', 'maria@email.com', '11988888888', 'Rio de Janeiro'),
('Carlos Oliveira', 'carlos@email.com', '21987654321', 'São Paulo');

-- Inserir produtos
INSERT INTO products (product_name, category, price, stock_quantity) VALUES
('Notebook Dell', 'Eletrônicos', 3500.00, 15),
('Mouse Logitech', 'Periféricos', 150.00, 50),
('Teclado Mecânico', 'Periféricos', 450.00, 8),
('Monitor LG 27"', 'Monitores', 1200.00, 5),
('Webcam HD', 'Acessórios', 250.00, 2);

-- Inserir pedidos
INSERT INTO orders (customer_id, order_date, total_amount, status) VALUES
(1, CURRENT_TIMESTAMP - INTERVAL '2 days', 3650.00, 'completed'),
(2, CURRENT_TIMESTAMP - INTERVAL '1 day', 1350.00, 'completed'),
(3, CURRENT_TIMESTAMP, 5100.00, 'pending');

-- Inserir itens dos pedidos
INSERT INTO order_items (order_id, product_id, quantity, unit_price, total_price) VALUES
(1, 1, 1, 3500.00, 3500.00),
(1, 2, 1, 150.00, 150.00),
(2, 3, 1, 450.00, 450.00),
(2, 4, 1, 1200.00, 1200.00),
(3, 1, 1, 3500.00, 3500.00),
(3, 5, 2, 250.00, 500.00);
```

## 3. CONFIGURAÇÃO DO AIRFLOW

### 3.1 Inicializar Airflow

```bash
# Definir diretório do Airflow
export AIRFLOW_HOME=~/airflow

# Inicializar banco de dados
airflow db init

# Criar usuário admin
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# Iniciar servidor web (em um terminal)
airflow webserver --port 8080

# Em outro terminal, iniciar scheduler
airflow scheduler
```

### 3.2 Configurar Conexões no Airflow

```bash
# Adicionar conexão PostgreSQL
airflow connections add 'postgres_vendas' \
    --conn-type 'postgres' \
    --conn-host 'localhost' \
    --conn-port '5432' \
    --conn-login 'postgres' \
    --conn-password 'password' \
    --conn-schema 'vendas_db'

# Adicionar conexão SMTP para envio de emails
airflow connections add 'email_gmail' \
    --conn-type 'smtp' \
    --conn-host 'smtp.gmail.com' \
    --conn-port '587' \
    --conn-login 'seu_email@gmail.com' \
    --conn-password 'sua_senha_app'
```

### 3.3 Configurar Variáveis do Airflow

```bash
airflow variables set postgres_user 'postgres'
airflow variables set postgres_password 'password'
airflow variables set hdfs_host 'localhost'
airflow variables set hdfs_port '9000'
```

## 4. CONFIGURAÇÃO DO HADOOP HDFS

### 4.1 Estrutura do Data Lake

```bash
# Criar estrutura de pastas no HDFS
hdfs dfs -mkdir -p /data_lake/bronze/customers
hdfs dfs -mkdir -p /data_lake/bronze/products
hdfs dfs -mkdir -p /data_lake/bronze/orders
hdfs dfs -mkdir -p /data_lake/bronze/order_items

hdfs dfs -mkdir -p /data_lake/silver/orders_enriched
hdfs dfs -mkdir -p /data_lake/gold/vendas_por_dia
hdfs dfs -mkdir -p /data_lake/gold/maiores_vendas
hdfs dfs -mkdir -p /data_lake/gold/produtos_vendidos
hdfs dfs -mkdir -p /data_lake/gold/estoque_baixo
hdfs dfs -mkdir -p /data_lake/gold/relatorio_consolidado

# Definir permissões
hdfs dfs -chmod -R 777 /data_lake/
```

## 5. CONFIGURAÇÃO DO SPARK

### 5.1 Variáveis de Ambiente

```bash
# Adicionar ao ~/.bashrc ou ~/.bash_profile
export SPARK_HOME=/path/to/spark
export HADOOP_HOME=/path/to/hadoop
export PATH=$PATH:$SPARK_HOME/bin:$HADOOP_HOME/bin

# Configuração do HDFS para Spark
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
```

### 5.2 Driver JDBC para PostgreSQL

```bash
# Baixar driver PostgreSQL JDBC
wget https://jdbc.postgresql.org/download/postgresql-42.5.0.jar

# Copiar para diretório do Spark
cp postgresql-42.5.0.jar $SPARK_HOME/jars/
```

## 6. POSICIONAMENTO DOS ARQUIVOS

### 6.1 Colocar Scripts no Local Correto

```bash
# Copiar scripts Spark para diretório acessível
cp scripts/spark_full_load.py /opt/spark_jobs/
cp scripts/spark_incremental_load.py /opt/spark_jobs/
cp scripts/spark_silver_transform.py /opt/spark_jobs/
cp scripts/spark_gold_load.py /opt/spark_jobs/

# Copiar DAG para diretório do Airflow
cp dags/etl_vendas_pipeline.py ~/airflow/dags/
```

### 6.2 Ajustar Paths na DAG

Editar `etl_vendas_pipeline.py` e atualizar:

```python
SPARK_MASTER = 'spark://seu_host:7077'  # ou 'local[*]' para teste local
HDFS_HOST = 'hdfs://seu_hdfs_host:9000'
POSTGRES_HOST = 'seu_postgres_host'
# ... outros paths
```

## 7. TESTES E VALIDAÇÃO

### 7.1 Testar Conexão com PostgreSQL

```bash
# Do seu ambiente Python
python3 << EOF
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="vendas_db",
    user="postgres",
    password="password"
)
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM orders;")
print(cursor.fetchone())
conn.close()
print("Conexão PostgreSQL OK!")
EOF
```

### 7.2 Testar Script Spark Full Load

```bash
spark-submit \
    --master local[*] \
    --driver-class-path /opt/spark_jobs/postgresql-42.5.0.jar \
    /opt/spark_jobs/spark_full_load.py \
    --table_name customers \
    --hdfs_path hdfs://localhost:9000/data_lake/bronze/customers \
    --postgres_host localhost \
    --postgres_port 5432 \
    --postgres_db vendas_db \
    --postgres_user postgres \
    --postgres_password password
```

### 7.3 Validar Dados no HDFS

```bash
# Verificar se arquivos foram criados
hdfs dfs -ls /data_lake/bronze/customers/

# Ler arquivo Parquet (usando Spark)
spark-shell << EOF
val df = spark.read.parquet("hdfs://localhost:9000/data_lake/bronze/customers")
df.show()
EOF
```

## 8. EXECUTAR A PIPELINE

### 8.1 Acessar Airflow UI

1. Abrir navegador: `http://localhost:8080`
2. Fazer login (admin/admin)
3. Procurar por `etl_vendas_pipeline`
4. Ativar a DAG (toggle ON)
5. Manualmente disparar: clique em "Trigger DAG"

### 8.2 Monitorar Execução

- Verificar logs em tempo real
- Clicar em cada task para ver detalhes
- Verificar XCom entre tasks (se houver)

## 9. SOLUÇÃO DE PROBLEMAS COMUNS

### Erro: "Spark driver not found"
- Verificar se PostgreSQL JDBC driver está em `$SPARK_HOME/jars/`
- Passar via `--driver-class-path` no spark-submit

### Erro: "HDFS connection refused"
- Verificar se Namenode está rodando: `jps`
- Verificar arquivo `core-site.xml` do Hadoop

### Erro: "Email not sent"
- Habilitar "Aplicativos menos seguros" no Gmail
- Usar senha de aplicativo em vez de senha normal
- Testar SMTP manualmente

### Erro: "No matching records found"
- Verificar data do `processing_date` na DAG
- Confirmar que existem dados no PostgreSQL para a data

## 10. PRÓXIMOS PASSOS

1. **Escalar para produção**: Usar cluster Spark dedicado
2. **Monitoramento**: Integrar com Datadog, Grafana ou similar
3. **Backup**: Implementar política de retenção de dados
4. **CI/CD**: Usar GitLab CI ou GitHub Actions
5. **Testes**: Adicionar testes unitários para scripts Spark
6. **Documentação**: Manter dados lineage atualizado
