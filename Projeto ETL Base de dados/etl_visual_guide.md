# 🗺️ Guia Visual - Mapa de Navegação Projeto ETL

## 🎯 Você Está Aqui? Escolha Seu Caminho

```
┌─────────────────────────────────────────────────────────────┐
│              QUAL É SEU OBJETIVO?                          │
└─────────────────────────────────────────────────────────────┘
         │                    │                    │
         │                    │                    │
    ┌────▼─────┐        ┌────▼─────┐        ┌────▼─────┐
    │ APRENDER  │        │ EXECUTAR  │        │ PRODUÇÃO │
    │ NA PRÁTICA│        │ RÁPIDO    │        │ READY    │
    └────┬─────┘        └────┬─────┘        └────┬─────┘
         │                    │                    │
         ▼                    ▼                    ▼
   Leia:                Leia:                Leia:
   1. README.md         1. QUICK_START.md   1. IMPL_GUIDE.md
   2. SUMMARY.md        2. README.md        2. SUMMARY.md
   3. IMP_GUIDE.md      3. Execute Docker   3. Configure Email
```

---

## 📖 Documentação - Qual Ler Primeiro?

### 🚀 Iniciantes (Comece aqui!)
```
┌──────────────────────────────────────┐
│ 1. Quick Start (5 min)               │
│    → Entender o que é ETL            │
│    → Objetivo do projeto             │
│    → Executar com Docker             │
└──────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ 2. README (15 min)                   │
│    → Opções de instalação            │
│    → Estrutura de pastas             │
│    → Verificar dados                 │
└──────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ 3. Resumo Executivo (10 min)         │
│    → Arquitetura completa            │
│    → Fluxo de dados                  │
│    → Próximos passos                 │
└──────────────────────────────────────┘
```

### 💼 Profissionais Experientes
```
┌──────────────────────────────────────┐
│ 1. Resumo Executivo (5 min)          │
│    → Visão geral arquitetura         │
│    → Componentes envolvidos          │
└──────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ 2. Guia de Implementação (20 min)    │
│    → Setup completo                  │
│    → Configurações avançadas         │
│    → Troubleshooting detalhado       │
└──────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│ 3. Analisar Código (variável)        │
│    → Scripts Spark                   │
│    → DAG Airflow                     │
│    → Queries SQL                     │
└──────────────────────────────────────┘
```

---

## 🛠️ Execução - Qual Escolher?

```
        ┌─────────────────────────────┐
        │   COMO EXECUTAR?            │
        └──────────────┬──────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
   ┌────▼────┐                  ┌────▼────┐
   │  DOCKER  │                  │  LOCAL  │
   │ (Fácil)  │                  │ (Manual)│
   └────┬────┘                  └────┬────┘
        │                            │
        ▼                            ▼
   Requisitos:                   Requisitos:
   • Docker                      • Python 3.8+
   • Docker Compose              • Java 8+
   • 8GB RAM                     • PostgreSQL
                                 • Hadoop 3.2+
        │                        • Spark 3.0+
        ▼                            │
   1. Clone projeto             1. Instale deps
   2. docker-compose up -d      2. Setup PG
   3. Aguarde 2-3 min           3. Start Hadoop
   4. Acesse localhost:8080     4. Init Airflow
   5. Dispare DAG               5. Copie scripts
                                6. Start scheduler
        │                            │
        ▼                            ▼
   ✅ Pronto em 5min            ✅ Pronto em 20min
```

---

## 📂 Estrutura de Arquivos - Onde Está O Quê?

```
projeto-etl/
│
├─ 📖 DOCUMENTAÇÃO
│  ├─ README.md ............................ Instruções práticas
│  ├─ QUICK_START.md ....................... Iniciar em 5 min
│  ├─ IMPLEMENTATION_GUIDE.md .............. Guia completo
│  ├─ SUMMARY.md ........................... Resumo executivo
│  └─ RESOURCES_INVENTORY.md ............... Este arquivo
│
├─ 🐳 INFRAESTRUTURA
│  └─ docker-compose.yml ................... Stack completo
│
├─ 🔄 AIRFLOW (Orquestração)
│  └─ dags/
│     └─ etl_vendas_pipeline.py ............ DAG principal
│
├─ ⚡ SPARK (Processamento)
│  └─ scripts/
│     ├─ spark_full_load.py ................ Carga full
│     ├─ spark_incremental_load.py ......... Carga incremental
│     ├─ spark_silver_transform.py ......... Transformação
│     └─ spark_gold_load.py ................ Relatórios
│
├─ 🗄️ SQL (Queries)
│  └─ sql/
│     ├─ create_tables.sql ................. Schema BD
│     ├─ insert_sample_data.sql ............ Dados iniciais
│     ├─ validation_queries.sql ............ Validações
│     └─ advanced_queries.sql .............. Análises
│
├─ 🧪 TESTES
│  ├─ etl_test_validation.py ............... Suite completa
│  └─ etl_jupyter_notebook.py .............. Exploração
│
└─ ⚙️ CONFIG
   └─ airflow_connections.yaml ............. Configurações

Qual arquivo você precisa?
↓
```

---

## 🎓 Aprender - Fluxo de Dados Visual

```
┌───────────────────┐
│   PostgreSQL      │
│  (Fonte de Dados) │
│                   │
│ ┌─────────────┐   │
│ │ customers   │   │
│ │ products    │   │
│ │ orders      │   │
│ │ order_items │   │
│ └─────────────┘   │
└─────────┬─────────┘
          │
          │ EXTRAÇÃO
          │ (spark_full_load.py)
          │ (spark_incremental_load.py)
          ▼
┌───────────────────────────────────┐
│      HADOOP HDFS (Data Lake)      │
│                                   │
│  📦 CAMADA BRONZE (Raw)           │
│  ├─ customers/2025-01-15/         │
│  ├─ products/2025-01-15/          │
│  ├─ orders/2025-01-15/            │
│  └─ order_items/2025-01-15/       │
│                                   │
│  SNAPSHOT completo por dia        │
│  (sem transformações)             │
└─────────────┬─────────────────────┘
              │
              │ TRANSFORMAÇÃO
              │ (spark_silver_transform.py)
              │
              ▼
┌───────────────────────────────────┐
│  🧹 CAMADA SILVER (Clean)         │
│                                   │
│  ├─ orders_enriched/2025-01-15/   │
│  │  └─ Com joins:                 │
│  │     • Clientes                 │
│  │     • Produtos                 │
│  │     • Categorias               │
│                                   │
│  Dados limpos, validados,         │
│  deduplícados e enriquecidos      │
└─────────────┬─────────────────────┘
              │
              │ AGREGAÇÃO
              │ (spark_gold_load.py)
              │
              ▼
┌───────────────────────────────────┐
│  🏆 CAMADA GOLD (Business-Ready)  │
│                                   │
│  ├─ vendas_por_dia/               │
│  │  └─ Total vendas por dia       │
│  │                                │
│  ├─ maiores_vendas/               │
│  │  └─ Top 10 transações          │
│  │                                │
│  ├─ produtos_vendidos/            │
│  │  └─ Performance produtos       │
│  │                                │
│  └─ estoque_baixo/                │
│     └─ Alertas inventário         │
│                                   │
│  Pronto para BI, dashboards,      │
│  relatórios e análises            │
└─────────────┬─────────────────────┘
              │
              │ DISTRIBUIÇÃO
              │
              ▼
┌───────────────────────────────────┐
│    RELATÓRIOS & DASHBOARDS        │
│    EMAIL & ALERTAS                │
│    BI TOOLS (Tableau, Power BI)   │
│    ANÁLISES AVANÇADAS             │
└───────────────────────────────────┘
```

---

## 🎯 Relatórios Gerados - Qual Usar Quando?

```
┌─────────────────────────────────────────┐
│    4 RELATÓRIOS AUTOMÁTICOS             │
└─────────────────────────────────────────┘
         │        │         │        │
         │        │         │        │
    ┌────▼─┐ ┌───▼──┐ ┌───▼──┐ ┌──▼───┐
    │  Rel │ │ Rel  │ │ Rel  │ │ Rel  │
    │  1   │ │  2   │ │  3   │ │  4   │
    └────┬─┘ └───┬──┘ └───┬──┘ └──┬───┘
         │       │        │       │
         ▼       ▼        ▼       ▼
     VENDAS   MAIORES  PRODUTOS  ESTOQUE
      DIÁRIAS VENDAS   VENDIDOS   BAIXO

Quem usa?           Quando?             Para quê?
├─ CEO/CFO      Daily 8:00 AM       Decisões estratégicas
├─ Sales        Real-time           Rastreamento vendas
├─ Product Mgr  Weekly              Análise performance
└─ Ops Manager  Always              Alertas inventário
```

---

## 🔍 Validação - Como Verificar Tudo?

```
┌──────────────────────────────────────────┐
│   APÓS EXECUTAR - CHECKLIST              │
└──────────────────────────────────────────┘

┌─ PostgreSQL (Dados Origem)
│  ├─ psql -U postgres -d vendas_db
│  ├─ SELECT COUNT(*) FROM customers;
│  ├─ SELECT COUNT(*) FROM orders;
│  └─ [Resultado esperado: dados carregados]
│
├─ Airflow Web UI
│  ├─ URL: http://localhost:8080
│  ├─ Login: admin / admin
│  ├─ Procura: etl_vendas_pipeline
│  ├─ Grid view: Todas tasks com ✓
│  └─ [Resultado esperado: success em todas]
│
├─ HDFS (Data Lake)
│  ├─ hdfs dfs -ls /data_lake/bronze/
│  ├─ hdfs dfs -ls /data_lake/silver/
│  ├─ hdfs dfs -ls /data_lake/gold/
│  └─ [Resultado esperado: arquivos Parquet]
│
├─ Validação SQL
│  ├─ Queries de integridade
│  ├─ Verificar órfãos
│  ├─ Checar valores negativos
│  └─ [Resultado esperado: sem erros]
│
└─ Testes Automáticos
   ├─ python3 etl_test_validation.py
   ├─ Relatório JSON gerado
   └─ [Resultado esperado: 100% success]
```

---

## 📊 Performance e Monitoramento

```
        DURANTE EXECUÇÃO                    PÓS-EXECUÇÃO
        ─────────────────                   ────────────

1. Airflow Logs             →  Task Details    →  Otimizações
   - Errors               →  Duração         →  Índices PG
   - Warnings             →  Recursos        →  Partições HDFS
   - Status               →  Bottlenecks     →  Spark tuning

2. Docker Stats            →  Consumo         →  Escalabilidade
   - CPU                  →  Memória         →  Cluster Spark
   - Memory               →  Disk I/O        →  Replicação HDFS
   - Network              →  Bandwidth       →  Cache strategies

3. HDFS Logs              →  Tamanho         →  Compressão
   - Storage              →  Replicação      →  Formato Parquet
   - Health               →  Balance         →  Particionamento
```

---

## 🚀 Roadmap - Evolução do Projeto

```
HOJE (Setup Básico)
│
├─ ✅ ETL completo
├─ ✅ 4 relatórios
├─ ✅ Validações básicas
└─ ✅ Docker pronto

        │
        ▼ (Semana 1-2)

CURTÍSSIMO PRAZO
│
├─ 📧 Email real configurado
├─ 📊 Jupyter exploração
├─ 🧪 Testes expandidos
└─ 📈 Novos KPIs

        │
        ▼ (Semana 2-4)

CURTO PRAZO
│
├─ 🎨 Dashboard BI
├─ 🔔 Alertas automáticos
├─ 📝 Documentação API
└─ 🔐 Autenticação Airflow

        │
        ▼ (Mês 2)

MÉDIO PRAZO
│
├─ 🏗️ Cluster Spark prod
├─ 📦 CI/CD pipeline
├─ 🔍 Data quality checks
└─ 🌐 Multi-region setup

        │
        ▼ (Mês 3+)

LONGO PRAZO
│
├─ 🤖 ML predictions
├─ 🔄 Real-time processing
├─ 🌊 Streaming data
└─ 🏆 Production-grade SLA
```

---

## 💻 Ambiente - Requisitos por Opção

```
┌─────────────────────────────────────────┐
│     DOCKER (Recomendado)                │
├─────────────────────────────────────────┤
│ • Docker Desktop                        │
│ • Docker Compose                        │
│ • 8GB RAM                               │
│ • 20GB Disk                             │
│ ⏱️  Setup: 5 minutos                     │
│ 💻 Suportado: Linux, Mac, Windows       │
└─────────────────────────────────────────┘

vs

┌─────────────────────────────────────────┐
│    LOCAL (Avançado)                     │
├─────────────────────────────────────────┤
│ • Python 3.8+                           │
│ • Java 8+                               │
│ • PostgreSQL 12+                        │
│ • Hadoop 3.2+                           │
│ • Spark 3.0+                            │
│ • 16GB RAM                              │
│ • 30GB Disk                             │
│ ⏱️  Setup: 20-30 minutos                 │
│ 💻 Suportado: Linux, Mac (Windows →WSL) │
└─────────────────────────────────────────┘
```

---

## 🎯 Decision Tree - O Que Fazer Agora?

```
                  PROJETO ETL
                      │
        ┌─────────────┴─────────────┐
        │                           │
    "JÁ TENHO                   "QUERO
    DOCKER?"                    SETUP LOCAL?"
        │                           │
       SIM  NÃO                    SIM  NÃO
        │    │                      │    │
        │    ▼                      │    ▼
        │  Instale Docker           │  Instale tudo
        │  (5 min)                  │  (30 min)
        │    │                      │    │
        │    ▼                      │    ▼
        │  docker-compose           │  ./setup.sh
        │  up -d                    │  ou manual
        │    │                      │    │
        └────┴──────────┬───────────┘    │
                        │                │
                        ▼                ▼
                  ESPERE 2-3 MIN
                        │
                  ACESSE LOCALHOST:8080
                        │
                  ┌──────┴──────┐
                  │ LOGIN AIRFLOW│
                  │ admin/admin  │
                  └──────┬──────┘
                        │
                  DISPARE DAG
                        │
                  ACOMPANHE LOGS
                        │
                  ✅ SUCESSO!
```

---

## 📞 Precisa de Ajuda? Qual Documento?

```
PERGUNTA                          RESPOSTA ESTÁ EM
────────────────────────────────────────────────────────
"Como começo?"                    → QUICK_START.md

"Dá erro X, e agora?"             → README.md (Troubleshooting)

"Entendi nada!"                   → SUMMARY.md (Visão geral)

"Preciso mais detalhes"           → IMPLEMENTATION_GUIDE.md

"Qual arquivo é qual?"            → RESOURCES_INVENTORY.md

"Quero entender código"           → Explore scripts Python/SQL

"Quero testar dados"              → etl_jupyter_notebook.py

"Preciso validar tudo"            → etl_test_validation.py

"Quero fazer querys SQL"          → sql/advanced_queries.sql

"Preciso integrar com BI"         → IMPLEMENTATION_GUIDE.md
```

---

## ✨ Próximo Passo Recomendado

```
┌──────────────────────────────────────────┐
│  VOCÊ ESTÁ ONDE? COMECE AQUI!           │
├──────────────────────────────────────────┤
│                                          │
│  1️⃣  Não tem Docker instalado?          │
│      → Instale Docker Desktop           │
│      → docker-compose --version         │
│                                          │
│  2️⃣  Tem Docker pronto?                 │
│      → Leia QUICK_START.md               │
│      → docker-compose up -d              │
│                                          │
│  3️⃣  Containers rodando?                │
│      → http://localhost:8080             │
│      → admin / admin                     │
│                                          │
│  4️⃣  Airflow aberto?                    │
│      → etl_vendas_pipeline               │
│      → Trigger DAG                       │
│                                          │
│  5️⃣  DAG executando?                    │
│      → Acompanhe logs                    │
│      → Veja dados em HDFS                │
│                                          │
│  6️⃣  Tudo funcionando?                  │
│      → Parabéns! 🎉                      │
│      → Próximo passo: Customizar        │
│                                          │
└──────────────────────────────────────────┘
```

---

**🎉 Você tem tudo o que precisa!**

Tempo até "Está funcionando!": **5-10 minutos**

**Comece agora:** `docker-compose up -d` ⚡