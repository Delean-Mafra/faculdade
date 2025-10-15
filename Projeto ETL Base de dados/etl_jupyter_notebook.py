# Projeto ETL - Exploração Interativa com PySpark
# Execute este notebook para explorar os dados em tempo real

# ============================================================
# CÉLULA 1: Imports e Configuração
# ============================================================

import pandas as pd
import psycopg2
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Configurar estilo dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("✓ Imports realizados com sucesso!")

# ============================================================
# CÉLULA 2: Inicializar Spark
# ============================================================

spark = SparkSession.builder \
    .appName("ETL_Explorer") \
    .config("spark.driver.memory", "2g") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")
print("✓ SparkSession criada com sucesso!")

# ============================================================
# CÉLULA 3: Conectar ao PostgreSQL
# ============================================================

# Configuração de conexão
postgres_config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'vendas_db',
    'user': 'postgres',
    'password': 'password'
}

# Criar conexão
try:
    conn = psycopg2.connect(**postgres_config)
    cursor = conn.cursor()
    print("✓ Conexão PostgreSQL estabelecida!")
except Exception as e:
    print(f"✗ Erro na conexão: {e}")

# ============================================================
# CÉLULA 4: Carregar Dados no Spark
# ============================================================

jdbc_url = f"jdbc:postgresql://{postgres_config['host']}:{postgres_config['port']}/{postgres_config['database']}"

connection_properties = {
    'user': postgres_config['user'],
    'password': postgres_config['password'],
    'driver': 'org.postgresql.Driver'
}

# Ler tabelas
orders_df = spark.read.jdbc(jdbc_url, 'orders', properties=connection_properties)
order_items_df = spark.read.jdbc(jdbc_url, 'order_items', properties=connection_properties)
customers_df = spark.read.jdbc(jdbc_url, 'customers', properties=connection_properties)
products_df = spark.read.jdbc(jdbc_url, 'products', properties=connection_properties)

print("✓ Dados carregados no Spark!")
print(f"  - Orders: {orders_df.count()} registros")
print(f"  - Order Items: {order_items_df.count()} registros")
print(f"  - Customers: {customers_df.count()} registros")
print(f"  - Products: {products_df.count()} registros")

# ============================================================
# CÉLULA 5: Exploração Inicial dos Dados
# ============================================================

print("\n=== SCHEMA DAS TABELAS ===\n")

print("📊 ORDERS:")
orders_df.printSchema()

print("\n📦 ORDER_ITEMS:")
order_items_df.printSchema()

print("\n👥 CUSTOMERS:")
customers_df.printSchema()

print("\n🏷️ PRODUCTS:")
products_df.printSchema()

# ============================================================
# CÉLULA 6: Análise Descritiva
# ============================================================

print("\n=== ANÁLISE DESCRITIVA ===\n")

print("📊 ESTATÍSTICAS - ORDERS:")
orders_df.describe('total_amount').show()

print("\n📦 ESTATÍSTICAS - ORDER_ITEMS:")
order_items_df.describe('quantity', 'total_price').show()

print("\n🏷️ ESTATÍSTICAS - PRODUCTS:")
products_df.describe('price', 'stock_quantity').show()

# ============================================================
# CÉLULA 7: KPIs Principais
# ============================================================

print("\n=== KPIs PRINCIPAIS ===\n")

# Receita total
receita_total = orders_df.agg(sum('total_amount')).collect()[0][0]
print(f"💰 Receita Total: R$ {receita_total:,.2f}")

# Número de pedidos
num_pedidos = orders_df.count()
print(f"📋 Número de Pedidos: {num_pedidos}")

# Número de clientes
num_clientes = orders_df.select('customer_id').distinct().count()
print(f"👥 Número de Clientes: {num_clientes}")

# Ticket médio
ticket_medio = orders_df.agg(avg('total_amount')).collect()[0][0]
print(f"🎫 Ticket Médio: R$ {ticket_medio:,.2f}")

# Produtos vendidos
produtos_vendidos = order_items_df.select('product_id').distinct().count()
print(f"📦 Produtos Diferentes Vendidos: {produtos_vendidos}")

# Data última venda
ultima_venda = orders_df.agg(max('order_date')).collect()[0][0]
print(f"📅 Última Venda: {ultima_venda}")

# ============================================================
# CÉLULA 8: Vendas por Cliente (Top 10)
# ============================================================

print("\n=== TOP 10 CLIENTES POR RECEITA ===\n")

top_clientes = orders_df.join(customers_df, 'customer_id') \
    .groupby('customer_name') \
    .agg(
        sum('total_amount').alias('receita_total'),
        count('order_id').alias('numero_pedidos')
    ) \
    .orderBy(desc('receita_total')) \
    .limit(10)

top_clientes.show()

# ============================================================
# CÉLULA 9: Produtos Mais Vendidos (Top 10)
# ============================================================

print("\n=== TOP 10 PRODUTOS MAIS VENDIDOS ===\n")

top_produtos = order_items_df.join(products_df, 'product_id') \
    .groupby('product_name', 'category', 'price') \
    .agg(
        sum('quantity').alias('quantidade_vendida'),
        sum('total_price').alias('receita_produto')
    ) \
    .orderBy(desc('quantidade_vendida')) \
    .limit(10)

top_produtos.show()

# ============================================================
# CÉLULA 10: Vendas por Dia
# ============================================================

print("\n=== VENDAS POR DIA ===\n")

vendas_dia = orders_df \
    .withColumn('data', to_date(col('order_date'))) \
    .groupby('data') \
    .agg(
        count('order_id').alias('numero_pedidos'),
        sum('total_amount').alias('receita_dia')
    ) \
    .orderBy(desc('data'))

vendas_dia.show(10)

# ============================================================
# CÉLULA 11: Análise de Estoque
# ============================================================

print("\n=== PRODUTOS COM ESTOQUE BAIXO (< 10) ===\n")

estoque_baixo = products_df.filter(col('stock_quantity') < 10) \
    .select('product_name', 'category', 'price', 'stock_quantity') \
    .orderBy('stock_quantity')

estoque_baixo.show()

print(f"\n⚠️ Total de produtos com estoque crítico: {estoque_baixo.count()}")

# ============================================================
# CÉLULA 12: Validações e Qualidade de Dados
# ============================================================

print("\n=== VALIDAÇÃO DE QUALIDADE DE DADOS ===\n")

# Verificar nulos
print("🔍 Verificando campos nulos:")

for col_name in ['order_id', 'customer_id', 'order_date', 'total_amount']:
    null_count = orders_df.filter(col(col_name).isNull()).count()
    print(f"  {col_name}: {null_count} nulos")

# Verificar órfãos
orphaned_items = order_items_df.join(
    orders_df.select('order_id'),
    'order_id',
    'left_anti'
).count()
print(f"\n📦 Order items órfãos: {orphaned_items}")

# Verificar valores negativos
negative_prices = order_items_df.filter(col('total_price') < 0).count()
print(f"💰 Preços negativos: {negative_prices}")

negative_quantities = order_items_df.filter(col('quantity') < 0).count()
print(f"📊 Quantidades negativas: {negative_quantities}")

# ============================================================
# CÉLULA 13: Visualizações - Vendas por Dia
# ============================================================

# Converter para Pandas para visualização
vendas_dia_pandas = vendas_dia.toPandas()

plt.figure(figsize=(14, 6))
plt.plot(vendas_dia_pandas['data'], vendas_dia_pandas['receita_dia'], marker='o', linewidth=2)
plt.title('Receita de Vendas por Dia', fontsize=16, fontweight='bold')
plt.xlabel('Data', fontsize=12)
plt.ylabel('Receita (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("✓ Gráfico de vendas por dia exibido!")

# ============================================================
# CÉLULA 14: Visualizações - Top Produtos
# ============================================================

top_produtos_pandas = top_produtos.toPandas()

plt.figure(figsize=(12, 6))
bars = plt.barh(range(len(top_produtos_pandas)), top_produtos_pandas['quantidade_vendida'])
plt.yticks(range(len(top_produtos_pandas)), top_produtos_pandas['product_name'])
plt.title('Top 10 Produtos Mais Vendidos', fontsize=16, fontweight='bold')
plt.xlabel('Quantidade Vendida', fontsize=12)
plt.colorbar(bars, label='Quantidade')
plt.tight_layout()
plt.show()

print("✓ Gráfico de produtos mais vendidos exibido!")

# ============================================================
# CÉLULA 15: Visualizações - Distribuição de Preços
# ============================================================

produtos_pandas = products_df.toPandas()

plt.figure(figsize=(12, 6))
plt.hist(produtos_pandas['price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição de Preços dos Produtos', fontsize=16, fontweight='bold')
plt.xlabel('Preço (R$)', fontsize=12)
plt.ylabel('Número de Produtos', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

print("✓ Gráfico de distribuição de preços exibido!")

# ============================================================
# CÉLULA 16: Segmentação RFM
# ============================================================

print("\n=== SEGMENTAÇÃO RFM (Recência, Frequência, Monetário) ===\n")

rfm_df = orders_df.join(customers_df, 'customer_id') \
    .groupby('customer_id', 'customer_name') \
    .agg(
        max('order_date').alias('ultima_compra'),
        count('order_id').alias('frequencia'),
        sum('total_amount').alias('monetario')
    )

# Calcular recência
data_ref = orders_df.agg(max('order_date')).collect()[0][0]
rfm_df = rfm_df.withColumn(
    'recencia_dias',
    datediff(lit(data_ref), col('ultima_compra'))
)

# Segmentação
rfm_df = rfm_df.withColumn(
    'segmento',
    when((col('recencia_dias') <= 7) & (col('frequencia') >= 3), 'CAMPEÃO')
    .when((col('recencia_dias') <= 30) & (col('frequencia') >= 2), 'LEAL')
    .when((col('recencia_dias') > 90) & (col('frequencia') >= 1), 'EM RISCO')
    .when(col('recencia_dias') > 180, 'DORMINHOCO')
    .otherwise('NOVO')
)

rfm_df.select('customer_name', 'frequencia', 'monetario', 'segmento') \
    .orderBy(desc('monetario')) \
    .show(15)

# ============================================================
# CÉLULA 17: Exportar Relatório
# ============================================================

print("\n=== EXPORTANDO DADOS PROCESSADOS ===\n")

# Exportar dados para Parquet (simulando camada Gold)
try:
    vendas_dia.write.mode('overwrite').parquet('/tmp/etl_vendas_por_dia')
    top_produtos.write.mode('overwrite').parquet('/tmp/etl_top_produtos')
    
    print("✓ Dados exportados com sucesso!")
    print("  - /tmp/etl_vendas_por_dia")
    print("  - /tmp/etl_top_produtos")
except Exception as e:
    print(f"✗ Erro ao exportar: {e}")

# ============================================================
# CÉLULA 18: Limpeza
# ============================================================

# Fechar conexão
conn.close()
print("\n✓ Conexão fechada!")
print("✓ Análise concluída com sucesso!")