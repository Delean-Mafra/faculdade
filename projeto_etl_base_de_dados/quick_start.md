# ⚡ Quick Start - Projeto ETL em 5 Minutos

## 🚀 Caminho Mais Rápido: Docker Compose

### Pré-requisito Único
- Docker + Docker Compose instalado

### Passos (Copie e Cole)

#### 1️⃣ Clone o Projeto
```bash
git clone <seu-repo>
cd projeto-etl
```

#### 2️⃣ Inicie Tudo
```bash
docker-compose up -d
```

#### 3️⃣ Aguarde (2-3 minutos)
```bash
# Ver status
docker-compose ps

# Ver logs
docker-compose logs -f airflow_webserver
```

#### 4️⃣ Acesse Airflow
```
http://localhost:8080
Usuário: admin
Senha: admin
```

#### 5️⃣ Dispare a DAG
```
1. Clique na DAG: etl_vendas_pipeline
2. Clique no toggle (ON)
3. Clique em "Trigger DAG"
4. Acompanhe a execução
```

---

## 📊 O que Acontece Automaticamente

```
├─ PostgreSQL inicia com dados de exemplo
├─ Hadoop HDFS cria estrutura /data_lake
├─ Airflow orquestra 9 tasks em sequência
│  ├─ Extrai 4 tabelas (customers, products, orders, order_items)
│  ├─ Valida dados (contagem, integridade)
│  ├─ Transforma e enriquece (joins, limpeza)
│  ├─ Gera 4 relatórios (vendas, produtos, estoque, análises)
│  └─ Envia por email (opcional)
└─ Dados prontos em /data_lake/gold/
```

---

## 🔍 Verificar Dados

### PostgreSQL (Dados de Origem)
```bash
docker-compose exec postgres psql -U postgres -d vendas_db
```

```sql
-- No prompt do psql:
SELECT COUNT(*) as total_clientes FROM customers;
SELECT COUNT(*) as total_pedidos FROM orders;
SELECT SUM(total_amount) as receita FROM orders;
\q
```

### Hadoop HDFS (Data Lake)
```bash
docker-compose exec namenode hdfs dfs -ls /data_lake/bronze/
docker-compose exec namenode hdfs dfs -ls /data_lake/gold/
```

### Airflow Web UI
```
http://localhost:8080/home

Abas úteis:
- DAGs: Ver todas as pipelines
- Grid: Ver timeline de execução
- Task Logs: Ver detalhes de cada task
```

---

## 📈 Exemplo de Resultado Esperado

Após execução bem-sucedida, você terá:

### 1. Bronze Layer (Raw Data)
```
/data_lake/bronze/
├── customers/2025-01-15/  → 3 registros
├── products/2025-01-15/   → 5 registros
├── orders/2025-01-15/     → 3 registros
└── order_items/2025-01-15/ → 6 registros
```

### 2. Silver Layer (Clean Data)
```
/data_lake/silver/
└── orders_enriched/2025-01-15/
    └── dados com clientes e produtos unidos
```

### 3. Gold Layer (Business Reports)
```
/data_lake/gold/
├── vendas_por_dia/2025-01-15/
│   → Total vendas: R$ 5.100,00
│   → Número de pedidos: 3
│
├── maiores_vendas/2025-01-15/
│   → Top 1: João Silva - R$ 3.650,00
│   → Top 2: Maria Santos - R$ 1.350,00
│
├── produtos_vendidos/2025-01-15/
│   → Notebook Dell: 1 unidade (R$ 3.500,00)
│   → Webcam HD: 2 unidades (R$ 500,00)
│
└── estoque_baixo/2025-01-15/
    → Teclado Mecânico: 8 unidades (⚠️ crítico)
    → Monitor LG: 5 unidades (⚠️ crítico)
```

---

## 🎯 Casos de Uso Práticos

### Usar Case 1: Visualizar Vendas do Dia
```bash
# 1. Acesse http://localhost:8080
# 2. Vá para DAG → etl_vendas_pipeline
# 3. Veja task "load_gold_layer" 
# 4. Dados em /data_lake/gold/vendas_por_dia/
```

### Use Case 2: Checar Estoque Baixo
```bash
# Verifique automaticamente via task "load_gold_layer"
# Dados em /data_lake/gold/estoque_baixo/
# Alerta: Produtos com < 10 unidades
```

### Use Case 3: Análise de Clientes
```bash
# Jupyter Notebook (ver etl_jupyter_notebook.py)
# Segmentação RFM (Recência, Frequência, Monetário)
# Identificar clientes-chave e em risco
```

### Use Case 4: Auditar Qualidade
```bash
# Via SQL: 
docker-compose exec postgres psql -U postgres -d vendas_db -f sql/validation_queries.sql

# Via Spark:
python3 etl_test_validation.py
```

---

## 🔧 Comandos Úteis

### Gerenciar Containers
```bash
# Ver status
docker-compose ps

# Ver logs em tempo real
docker-compose logs -f airflow_scheduler

# Parar
docker-compose stop

# Reiniciar
docker-compose restart

# Parar e remover
docker-compose down

# Remover volumes (limpar tudo)
docker-compose down -v
```

### Executar Comandos Dentro dos Containers
```bash
# PostgreSQL
docker-compose exec postgres psql -U postgres -d vendas_db -c "SELECT COUNT(*) FROM orders;"

# HDFS
docker-compose exec namenode hdfs dfs -cat /data_lake/gold/vendas_por_dia/*

# Spark
docker-compose exec namenode spark-shell -c "spark.read.parquet('/data_lake/gold/vendas_por_dia').show()"
```

### Ver Logs Detalhados
```bash
# Airflow Webserver
docker-compose logs airflow_webserver | tail -50

# Airflow Scheduler
docker-compose logs airflow_scheduler | tail -50

# PostgreSQL
docker-compose logs postgres | tail -50

# Todos os containers
docker-compose logs --follow
```

---

## 🐛 Troubleshooting Rápido

| Sintoma | Solução |
|---------|---------|
| "Connection refused" | Aguarde 2-3 min, containers iniciando |
| DAG não aparece | `docker-compose restart airflow_scheduler` |
| Task falha | Ver logs: http://localhost:8080 → DAG → Task → Logs |
| PostgreSQL vazio | Dados carregam automático no init |
| HDFS inacessível | `docker-compose logs namenode` |
| Airflow lento | Aumentar memória Docker (Settings) |

---

## 📋 Estrutura de Arquivos Esperada

Após clone, você deve ter:

```
projeto-etl/
├── docker-compose.yml          ✅ Orquestração Docker
├── dags/
│   └── etl_vendas_pipeline.py  ✅ DAG Airflow
├── scripts/
│   ├── spark_full_load.py      ✅ Carga full
│   ├── spark_incremental_load.py ✅ Carga incremental
│   ├── spark_silver_transform.py ✅ Transformação
│   └── spark_gold_load.py      ✅ Relatórios
├── sql/
│   ├── create_tables.sql       ✅ Schema PostgreSQL
│   ├── insert_sample_data.sql  ✅ Dados iniciais
│   └── validation_queries.sql  ✅ Queries de teste
├── config/
│   └── airflow_connections.yaml ✅ Configurações
├── README.md                    ✅ Documentação
└── etl_test_validation.py      ✅ Testes

Todos fornecidos neste projeto!
```

---

## 🎓 Aprendizados em Prática

Ao executar este projeto, você pratica:

✅ **Orquestração** - Airflow orquestração de tasks
✅ **Spark SQL** - PySpark dataframes e queries
✅ **Engenharia de Dados** - ETL completo
✅ **Data Lake** - Bronze/Silver/Gold layers
✅ **Docker** - Containerização e composição
✅ **PostgreSQL** - Banco relacional
✅ **HDFS** - Sistema de arquivos distribuído
✅ **Validação** - Testes de qualidade de dados
✅ **Automation** - Workflows automáticos
✅ **Relatórios** - Geração de insights

---

## 📞 Próximos Passos

### Imediato (Após 1ª Execução)
1. ✅ Executar DAG e ver tudo funcionar
2. ✅ Explorar dados em PostgreSQL
3. ✅ Ver arquivos em HDFS
4. ✅ Verificar logs no Airflow

### Curto Prazo (1-2 horas)
1. 📖 Ler comentários nos scripts
2. 📊 Executar queries SQL para análise
3. 🔍 Explorar com Jupyter Notebook
4. 🧪 Rodar testes de validação

### Médio Prazo (1-2 dias)
1. 🎨 Customizar relatórios
2. 📧 Configurar email real
3. 📈 Adicionar novos KPIs
4. 🚀 Preparar para produção

### Longo Prazo
1. 🏗️ Escalar para dados reais
2. 📊 Integrar com BI (Tableau/Power BI)
3. 🔔 Implementar alertas
4. 🤖 Automação avançada

---

## ⭐ Dicas Profissionais

### 1. Monitoramento
```bash
# Ver execução em tempo real
watch 'docker-compose ps'

# Monitorar recursos
docker stats
```

### 2. Desenvolvimento
```bash
# Testar script Spark localmente
spark-submit scripts/spark_full_load.py --help

# Validar DAG Airflow
python3 -m py_compile dags/etl_vendas_pipeline.py
```

### 3. Debugging
```bash
# Ver variáveis de ambiente
docker-compose exec airflow_webserver printenv

# Acessar bash do container
docker-compose exec postgres bash

# Inspecionar arquivo Parquet
docker-compose exec namenode spark-shell
```

### 4. Performance
```bash
# Aumentar worker threads
# Editar docker-compose.yml:
# AIRFLOW__CORE__PARALLELISM: 32

# Aumentar memória Spark
# Editar DAG: conf={'spark.executor.memory': '4g'}
```

---

## 🎯 Checklist Final

Antes de considerar "pronto":

- [ ] Docker Compose rodando sem erros
- [ ] Airflow acessível em http://localhost:8080
- [ ] DAG `etl_vendas_pipeline` visível
- [ ] Primeira execução concluída (✓ em todas as tasks)
- [ ] Dados em PostgreSQL verificados
- [ ] Dados em HDFS (/data_lake) verificados
- [ ] Relatórios em gold/ gerados
- [ ] Nenhum erro crítico nos logs
- [ ] (Opcional) Email recebido com relatório

---

## 🎉 Parabéns!

Você agora tem um **projeto ETL production-ready** totalmente funcional! 

### O que você conquistou:
✅ Pipeline ETL completo  
✅ Arquitetura moderna de dados  
✅ Automação com Airflow  
✅ Processamento com Spark  
✅ Data Lake em 3 camadas  
✅ Relatórios automáticos  
✅ Testes de qualidade  

### Agora você pode:
- 📊 Adicionar novos relatórios
- 🚀 Escalar para produção
- 🤖 Automatizar decisões
- 📈 Gerar insights em tempo real
- 🎯 Transformar dados em valor

---

**Tempo total esperado: 5-10 minutos ⚡**

**Sucesso! Happy Data Engineering! 🚀**
