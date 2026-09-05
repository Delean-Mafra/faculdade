# -*- coding: utf-8 -*-
"""
Atividade Prática 14 – Distribuída e Bancos de Dados em Big Data

Arquivo principal de execução do projeto.
Os componentes detalhados ficam nos módulos do projeto:
1_setup_elasticsearch.py
2_gerador_eventos_kafka.py
3_spark_streaming.py
4_busca_recomendacao.py
"""

import os
import sys
import time
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")


def executar(script: str) -> None:
    """Executa um módulo Python do projeto e valida seu resultado inicial."""
    caminho = os.path.join(SRC_DIR, script)
    if not os.path.isfile(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    print(f"\n[PIPELINE] Executando: {script}")
    subprocess.run([sys.executable, caminho], check=True)


def main() -> None:
    print("=" * 65)
    print("ATIVIDADE PRÁTICA 14 - BIG DATA E BUSCA DISTRIBUÍDA")
    print("=" * 65)
    print("Arquitetura: Elasticsearch + Kafka + Spark Streaming + Prometheus + Grafana")

    # Etapa 1 e 2: preparar o catálogo e o mecanismo de busca.
    executar("1_setup_elasticsearch.py")

    print("\n[PIPELINE] Infraestrutura e catálogo preparados.")
    print("[PIPELINE] O streaming e o gerador de eventos devem permanecer em execução em terminais separados.")
    print("[PIPELINE] Consulte o README para a ordem completa de inicialização.")

    # As etapas de streaming são processos contínuos. Por isso, não são iniciadas
    # automaticamente neste arquivo, evitando bloquear a execução do restante do projeto.
    print("\n[PIPELINE] Próximas etapas:")
    print("  1. Inicie 3_spark_streaming.py")
    print("  2. Inicie 2_gerador_eventos_kafka.py")
    print("  3. Inicie 4_busca_recomendacao.py")
    print("  4. Acompanhe as métricas no Prometheus e no Grafana")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[PIPELINE] Execução interrompida pelo usuário.")
    except subprocess.CalledProcessError as exc:
        print(f"\n[PIPELINE] Um componente foi encerrado com código {exc.returncode}.")
        sys.exit(exc.returncode)
    except Exception as exc:
        print(f"\n[PIPELINE] Erro: {exc}")
        sys.exit(1)
