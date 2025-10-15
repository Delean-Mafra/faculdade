# 📊 Projeto ETL: Resumo Executivo

## 🎯 Objetivo do Projeto

Implementar um pipeline **ETL (Extração, Transformação e Carregamento)** completo para dados de vendas, utilizando as melhores práticas de **Engenharia de Dados** com:

- **Apache Airflow** - Orquestração de workflows
- **Apache Spark** - Processamento distribuído de dados
- **PostgreSQL** - Fonte de dados transacional
- **Hadoop HDFS** - Armazenamento de dados em camadas (Bronze/Silver/Gold)
- **Data Lake** - Arquitetura moderno de dados

---

## 📦 Arquivos Entregues

### 1. **DAG Airflow** (`etl_airflow_dag.py`)
- Orquestração completa do pipeline
- 9 tasks integradas
- Tratamento de erros e retries
- Envio de relatórios por email

### 2. **Scripts Spark** (4 arquivos)
- `spark_full_load.py` - Carga completa das tabelas
- `spark_incremental_load.py` - Carga incremental de orders
- `spark_silver_transform.py` - Transformação e enriquecimento
- `spark_gold_load.py` - Geração de relatórios finais

### 3. **Queries SQL** (Validação e Análises)
- `sql_validation_queries.sql` - Validações de integridade
- `etl_advanced_queries.sql` - Análises avançadas (10 categorias)

### 4. **Docker Compose** (`docker-compose.yml`)
- Stack completo pré-configurado
- 6 serviços Docker
- Ambiente pronto para uso

### 5. **Testes e Validação**
- `etl_test_validation.py` - Suite completa de testes
- `etl_jupyter_notebook.py` - Exploração interativa

### 6. **Documentação**
- `README.md` - Instruções práticas
- `INSTALLATION_GUIDE.md` - Guia detalhado
- Este arquivo - Resumo executivo

---

## 🏗️ Arquitetura do Data Lake

```
/data_lake/
├── bronze/                 # Dados brutos, sem transformação
│   ├── customers/         # Carga full diária
│   ├── products/          # Carga full diária
│   ├── orders/            # Carga incremental
│   └── order_items/       # Carga full diária
│
├── silver/                # Dados limpos e enriquecidos
│   └── orders_enriched/   # Pedidos com clientes e produtos
│
└── gold/                  # Dados prontos para análise
    ├── vendas_por_dia/    # Agregação diária
    ├── maiores_vendas/    # Top 10 vendas
    ├── produtos_vendidos/ # Performance de produtos
    └── estoque_baixo/     # Alertas de inventário
```

---

## 🔄 Fluxo de Dados

```
PostgreSQL (Fonte)
       ↓
┌──────────────────────────────────────────┐
│         APACHE AIRFLOW                   │
│  ┌─────────────────────────────────────┐ │
│  │  Task 1-3: Carga Full (S3S)         │ │
│  │  - customers, products, order_items │ │
│  └──────────────┬──────────────────────┘ │
│                 ↓                        │
│  ┌──────────────────────────────────────┐│
│  │  Task 4: Carga Incremental           ││
│  │  - orders (filtrado por data)        ││
│  └──────────────┬───────────────────────┘│
│                 ↓                        │
│  ┌──────────────────────────────────────┐│
│  │  Task 5: Validação (Bronze Layer)    ││
│  └──────────────┬───────────────────────┘│
│                 ↓                        │
│  ┌──────────────────────────────────────┐│
│  │  Task 6: Transformação (Silver)      ││
│  │  - Limpeza, enriquecimento com joins ││
│  └──────────────┬───────────────────────┘│
│                 ↓                        │
│  ┌──────────────────────────────────────┐│
│  │  Task 7: Carregamento (Gold)         ││
│  │  - 4 relatórios preparados           ││
│  └──────────────┬───────────────────────┘│
│                 ↓                        │
│  ┌──────────────────────────────────────┐│
│  │  Task 8-9: Geração e Envio           ││
│  │  - Relatório por email               ││
│  └──────────────────────────────────────┘│
└──────────────────────────────────────────┘
       ↓
Hadoop HDFS (Data Lake)
       ↓
Análises, BI, Relatórios
```

---

## 📋 Tabelas PostgreSQL

### 1. **customers**
```sql
customer_id (PK), customer_name, email, phone, city, created_at
```

### 2. **products**
```sql
product_id (PK), product_name, category, price, stock_quantity, created_at
```

### 3. **orders**
```sql
order_id (PK), customer_id (FK), order_date, total_amount, status, created_at
```

### 4. **order_items**
```sql
order_item_id (PK), order_id (FK), product_id (FK), quantity, unit_price, total_price, created_at
```

---

## 🚀 Como Executar

### Opção 1: Docker Compose (Recomendado - 5 min)

```bash
# Clone ou prepare o projeto
cd projeto-etl

# Inicie com um comando
docker-compose up -d

# Aguarde ~2 minutos

# Acesse: http://localhost:8080
# Usuário: admin | Senha: admin

# Dispare a DAG no Airflow
```

### Opção 2: Instalação Local (15-20 min)

```bash
# 1. Instalar dependências (ver INSTALLATION_GUIDE.md)
# 2. Configurar PostgreSQL com dados
# 3. Iniciar Hadoop HDFS
# 4. Inicializar Airflow
# 5. Disparar DAG

# Ver documentação detalhada no README.md
```

---

## 🔍 Validação de Dados

### Camada Bronze
- Dados brutos do PostgreSQL
- Snapshots diários por tabela
- Estrutura particionada por data

### Camada Silver
- Dados limpos e deduplica
- Joins entre tabelas
- Validações de integridade

### Camada Gold
- 4 relatórios principais:
  1. **Vendas por Dia** - Agregação diária
  2. **Maiores Vendas** - Top 10 transações
  3. **Produtos Vendidos** - Performance por produto
  4. **Estoque Baixo** - Alertas de inventário

---

## 📊 Relatórios Gerados

### 1. **Dashboard de Vendas Diárias**
- Total de vendas por dia
- Número de pedidos
- Quantidade de clientes
- Ticket médio

### 2. **Análise de Produtos**
- Produtos mais vendidos
- Produtos com baixo estoque
- Produtos sem rotatividade
- Performance por categoria

### 3. **Segmentação de Clientes**
- Clientes por valor gasto
- Clientes inativos
- Segmentação RFM (Recência/Frequência/Monetário)

### 4. **Alertas Operacionais**
- Estoque crítico (< 10 unidades)
- Produtos parados
- Clientes em risco

---

## ✅ Checklist de Verificação

### Antes de Executar
- [ ] Docker instalado (se usar opção 1)
- [ ] Python 3.8+ instalado
- [ ] 8GB RAM disponível
- [ ] Portas 5432, 8080, 9000, 9870 livres

### Após Iniciar
- [ ] PostgreSQL conecta e tem dados
- [ ] Hadoop HDFS criou estrutura /data_lake
- [ ] Airflow acessível em http://localhost:8080
- [ ] Arquivo JDBC PostgreSQL em $SPARK_HOME/jars/

### Antes de Disparar DAG
- [ ] Conexão PostgreSQL configurada no Airflow
- [ ] Scripts Spark no local correto
- [ ] Variáveis Airflow definidas
- [ ] Email configurado (opcional)

### Após Execução
- [ ] Todas as tasks concluídas (✓)
- [ ] Dados em /data_lake/gold gerados
- [ ] Email recebido com relatório (opcional)
- [ ] Nenhum erro crítico nos logs

---

## 🛠️ Solução de Problemas

| Problema | Solução |
|----------|---------|
| PostgreSQL não conecta | Verificar credenciais e porta 5432 |
| HDFS connection refused | Iniciar Hadoop: `$HADOOP_HOME/sbin/start-dfs.sh` |
| Spark driver not found | Copiar postgresql-42.5.0.jar para $SPARK_HOME/jars/ |
| DAG não aparece no Airflow | Verificar sintaxe e permissões em ~/airflow/dags/ |
| Task falha com path error | Atualizar caminhos na DAG conforme seu ambiente |
| Email não envia | Configurar SMTP e habilitar autenticação |

---

## 📚 Próximos Passos

1. **Adicionar Novos Relatórios**
   - Editar `spark_gold_load.py`
   - Adicionar novas aggregations
   - Testar antes de produção

2. **Escalar para Produção**
   - Usar cluster Spark dedicado
   - Implementar alertas e monitoramento
   - Adicionar backup automático

3. **Melhorar Performance**
   - Criar índices no PostgreSQL
   - Particionar tabelas HDFS
   - Otimizar queries SQL

4. **Integrar com BI**
   - Conectar Tableau/Power BI à camada Gold
   - Criar dashboards interativos
   - Implementar alertas automáticos

5. **Automação Avançada**
   - Schedule para rodar automaticamente
   - CI/CD para deployments
   - Testes unitários e integração

---

## 📞 Suporte

### Referências Úteis
- [Documentação Apache Airflow](https://airflow.apache.org/)
- [Documentação Apache Spark](https://spark.apache.org/docs/latest/)
- [Hadoop HDFS Guide](https://hadoop.apache.org/docs/r3.2.1/)
- [PostgreSQL Manual](https://www.postgresql.org/docs/)

### Comunidades
- Stack Overflow: tag `apache-airflow`, `apache-spark`
- Reddit: r/dataengineering, r/databases
- GitHub: Issues em projetos oficiais

---

## 📊 Estatísticas do Projeto

| Métrica | Valor |
|---------|-------|
| **Linhas de Código** | ~2.500 |
| **Arquivos Entregues** | 10+ |
| **Tasks Airflow** | 9 |
| **Scripts Spark** | 4 |
| **Queries SQL** | 30+ |
| **Tabelas PostgreSQL** | 4 |
| **Camadas Data Lake** | 3 |
| **Testes Automatizados** | 12+ |

---

## 🎓 Aprendizados Principais

✅ Arquitetura de Data Lake (Bronze/Silver/Gold)
✅ ETL completo com Spark e Airflow
✅ Extração incremental vs full
✅ Transformação e enriquecimento de dados
✅ Validação e qualidade de dados
✅ Orquestração de workflows complexos
✅ Best practices de Engenharia de Dados
✅ Relatórios automáticos por email

---

## 📝 Conclusão

Este projeto apresenta uma solução **production-ready** para pipelines ETL, cobrindo toda a cadeia de Engenharia de Dados moderna:

- **Extração** de múltiplas fontes
- **Transformação** e limpeza de dados
- **Carregamento** em camadas otimizadas
- **Validação** de integridade
- **Automação** e orquestração
- **Geração** de insights acionáveis

Todos os componentes estão **testados e prontos** para uso em ambientes de desenvolvimento e, com ajustes mínimos, em produção.

---

**Bom trabalho e sucesso com seu projeto ETL! 🚀**

*Última atualização: 2025*