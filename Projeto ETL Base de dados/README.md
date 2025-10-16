# Projeto ETL Base de dados

## Opção 1: Execução com Docker Compose (Recomendado)

A forma mais rápida de ter tudo funcionando é usar Docker Compose.

### Pré-requisitos
- Docker instalado
- Docker Compose instalado
- 8GB de RAM disponível

### Passos

#### 1. Clonar/Preparar Projeto
```bash
mkdir projeto-etl
cd projeto-etl

# Criar estrutura de diretórios
mkdir -p dags scripts sql config
```

#### 2. Copiar Arquivos
```bash
# Copiar arquivos fornecidos para seus respectivos diretórios
# - DAG airflow para: dags/
# - Scripts spark para: scripts/
# - Queries SQL para: sql/
# - docker-compose.yml para: raiz do projeto
```

#### 3. Iniciar Serviços
```bash
# Iniciar todos os containers
docker-compose up -d

# Verificar status
docker-compose ps

# Ver logs em tempo real
docker-compose logs -f
```

#### 4. Aguardar Inicialização
```bash
# Verificar quando os serviços estão prontos (aguarde ~2-3 minutos)
docker-compose logs airflow_webserver | grep "running on"
docker-compose logs namenode | grep "initialized"
```

#### 5. Acessar Interfaces Web

| Serviço | URL | Credenciais |
|---------|-----|-------------|
| **Airflow Web UI** | http://localhost:8080 | admin/admin |
| **Hadoop NameNode** | http://localhost:9870 | - |
| **PostgreSQL** | localhost:5432 | postgres/password |

### Verificar Dados Carregados

```bash
# Acessar container PostgreSQL
docker-compose exec postgres psql -U postgres -d vendas_db

# No prompt do psql
SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM order_items;

# Sair
\q
```

### Criar Estrutura HDFS

```bash
# Executar em container NameNode
docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/bronze/customers
docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/bronze/products
docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/bronze/orders
docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/bronze/order_items

docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/silver/orders_enriched
docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/gold/vendas_por_dia
docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/gold/maiores_vendas
docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/gold/produtos_vendidos
docker-compose exec namenode hdfs dfs -mkdir -p /data_lake/gold/estoque_baixo

# Definir permissões
docker-compose exec namenode hdfs dfs -chmod -R 777 /data_lake/
```

### Executar DAG no Airflow

1. **Acessar Airflow**: http://localhost:8080
2. **Login**: admin/admin
3. **Procurar DAG**: `etl_vendas_pipeline`
4. **Ativar**: Clique no toggle para ON
5. **Disparar**: Clique em "Trigger DAG"
6. **Monitorar**: Veja execução em tempo real

---

## Opção 2: Execução Local (Sem Docker)

Se preferir instalar manualmente, siga os passos abaixo.

### Pré-requisitos Instalados
- Python 3.8+
- Java 8+
- PostgreSQL 12+
- Hadoop 3.2+
- Apache Spark 3.0+

### 1. Instalar Dependências Python

```bash
# Criar ambiente virtual
python3 -m venv etl_env
source etl_env/bin/activate

# Instalar pacotes
pip install apache-airflow==2.7.0
pip install apache-airflow-providers-spark==3.1.0
pip install apache-airflow-providers-postgres==5.6.0
pip install apache-airflow-providers-email==0.4.0
pip install pyspark==3.4.0
pip install psycopg2-binary
```

### 2. Configurar PostgreSQL

```bash
# Criar banco de dados
createdb vendas_db

# Importar dados iniciais (execute arquivo create_tables.sql + insert_sample_data.sql)
psql -U postgres -d vendas_db < sql/create_tables.sql
psql -U postgres -d vendas_db < sql/insert_sample_data.sql

# Verificar
psql -U postgres -d vendas_db -c "SELECT COUNT(*) FROM customers;"
```

### 3. Iniciar Hadoop HDFS

```bash
# Formatar namenode (primeira vez apenas)
$HADOOP_HOME/bin/hdfs namenode -format

# Iniciar HDFS
$HADOOP_HOME/sbin/start-dfs.sh

# Criar estrutura data lake (veja passo anterior)
hdfs dfs -mkdir -p /data_lake/bronze/{customers,products,orders,order_items}
hdfs dfs -mkdir -p /data_lake/silver/orders_enriched
hdfs dfs -mkdir -p /data_lake/gold/{vendas_por_dia,maiores_vendas,produtos_vendidos,estoque_baixo}
```

### 4. Inicializar Airflow

```bash
# Definir home
export AIRFLOW_HOME=~/airflow

# Inicializar BD
airflow db init

# Criar usuário
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# Adicionar conexão PostgreSQL
airflow connections add 'postgres_vendas' \
    --conn-type 'postgres' \
    --conn-host 'localhost' \
    --conn-port '5432' \
    --conn-login 'postgres' \
    --conn-password 'password' \
    --conn-schema 'vendas_db'

# Adicionar variáveis
airflow variables set postgres_user 'postgres'
airflow variables set postgres_password 'password'
```

### 5. Copiar Arquivos Airflow

```bash
# Copiar DAG
cp dags/etl_vendas_pipeline.py ~/airflow/dags/

# Copiar scripts Spark
mkdir -p ~/spark_jobs
cp scripts/*.py ~/spark_jobs/

# Ajustar paths na DAG conforme necessário
```

### 6. Iniciar Airflow

```bash
# Terminal 1: Webserver
airflow webserver --port 8080

# Terminal 2: Scheduler
airflow scheduler

# Terminal 3: Acessar http://localhost:8080
```

---

## 📋 Checklist de Execução

### Antes de Disparar a DAG

- [ ] PostgreSQL está rodando e com dados carregados
- [ ] Hadoop HDFS está rodando
- [ ] Pasta /data_lake criada no HDFS
- [ ] Airflow Webserver e Scheduler estão rodando
- [ ] Conexão PostgreSQL configurada no Airflow
- [ ] Scripts Spark copiados para local correto
- [ ] Arquivo JAR do PostgreSQL em $SPARK_HOME/jars/

### Primeiro Teste - Carga Full

```bash
# Testar script de carga full manualmente
spark-submit \
    --master local[*] \
    --driver-class-path postgresql-42.5.0.jar \
    ~/spark_jobs/spark_full_load.py \
    --table_name customers \
    --hdfs_path hdfs://localhost:9000/data_lake/bronze/customers \
    --postgres_host localhost \
    --postgres_port 5432 \
    --postgres_db vendas_db \
    --postgres_user postgres \
    --postgres_password password

# Verificar resultado
hdfs dfs -ls /data_lake/bronze/customers/
```

### Segundo Teste - Validação

```bash
# Executar script de validação
python3 etl_test_validation.py

# Verificar resultado
cat etl_validation_report_*.json
```

---

## 🔧 Solução de Problemas Comuns

### Erro: "Connection refused" - PostgreSQL
```bash
# Verificar se PostgreSQL está rodando
sudo systemctl status postgresql
# ou
docker-compose logs postgres
```

### Erro: "HDFS connection refused"
```bash
# Verificar namenode
jps
# Deve listar: NameNode, DataNode

# Se não aparecer, iniciar:
$HADOOP_HOME/sbin/start-dfs.sh
```

### Erro: "Spark driver not found"
```bash
# Verificar JDBC jar
ls $SPARK_HOME/jars/ | grep postgresql

# Se não encontrar, baixar e copiar:
cd $SPARK_HOME/jars/
wget https://jdbc.postgresql.org/download/postgresql-42.5.0.jar
```

### Erro: "No such file or directory" em scripts Spark
```bash
# Atualizar paths nos argumentos conforme seu ambiente
# Verificar:
echo $SPARK_HOME
echo $HADOOP_HOME
echo $AIRFLOW_HOME
```

### DAG não aparece no Airflow
```bash
# Verificar arquivo está em: ~/airflow/dags/
ls -la ~/airflow/dags/

# Verificar sintaxe Python
python3 -m py_compile ~/airflow/dags/etl_vendas_pipeline.py

# Ver logs
tail -f ~/airflow/logs/dagbag_import_errors.log
```

---

## 📊 Validação de Dados

### Verificar Dados no PostgreSQL

```sql
-- Total de registros
SELECT 'customers' as table_name, COUNT(*) FROM customers
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items;

-- Vendas de hoje
SELECT DATE(order_date), SUM(total_amount) 
FROM orders 
GROUP BY DATE(order_date)
ORDER BY DATE(order_date) DESC;
```

### Verificar Dados no HDFS

```bash
# Listar camadas
hdfs dfs -ls /data_lake/

# Listar bronze
hdfs dfs -ls /data_lake/bronze/customers/

# Ver arquivo Parquet (usando Spark)
spark-shell << 'EOF'
val df = spark.read.parquet("hdfs://localhost:9000/data_lake/bronze/customers")
df.show(5)
df.count()
EOF
```

---

## 📧 Configuração de Email (Opcional)

Para enviar relatórios por email:

### Gmail

```bash
# 1. Habilitar 2FA na conta Google
# 2. Gerar senha de app
# 3. Adicionar conexão no Airflow

airflow connections add 'email_gmail' \
    --conn-type 'smtp' \
    --conn-host 'smtp.gmail.com' \
    --conn-port '587' \
    --conn-login 'seu_email@gmail.com' \
    --conn-password 'sua_senha_app'

# 4. Atualizar DAG com seu email
# 5. Testar envio
```

---

## 🎓 Próximos Passos

1. **Explorar DAG**: Entender fluxo de cada task
2. **Analisar Logs**: Ver detalhes de execução
3. **Modificar Queries**: Adicionar novos relatórios
4. **Escalar**: Usar cluster Spark real
5. **Automatizar**: Schedule para rodar diariamente

---

## 📚 Referências Úteis

- [Documentação Apache Airflow](https://airflow.apache.org/)
- [Documentação Apache Spark](https://spark.apache.org/docs/latest/)
- [Documentação Hadoop HDFS](https://hadoop.apache.org/docs/r3.2.1/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## ❓ Dúvidas Frequentes

**P: Posso usar MySQL em vez de PostgreSQL?**
R: Sim, ajuste a string JDBC e use driver MySQL.

**P: Quanto tempo leva para executar?**
R: Com dados de exemplo: 2-5 minutos. Varia com volume de dados.

**P: Posso schedule para rodar automaticamente?**
R: Sim! A DAG já tem `schedule_interval='@daily'`.

**P: Onde ficam os logs?**
R: No Airflow: UI → Task → View Logs. Local: ~/airflow/logs/

---

Bom trabalho! 🎉
