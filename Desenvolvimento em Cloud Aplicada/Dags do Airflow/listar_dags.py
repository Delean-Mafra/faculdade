"""
Script para listar e validar DAGs do Airflow sem precisar do webserver
"""
import sys
import os
from airflow.models import DagBag

# Configurar o caminho dos DAGs
DAGS_FOLDER = r"D:\Python\complementos\faculdade"

def listar_dags():
    """Lista todos os DAGs disponíveis"""
    print("=" * 60)
    print("🔍 LISTANDO DAGs DISPONÍVEIS")
    print("=" * 60)
    
    dagbag = DagBag(dag_folder=DAGS_FOLDER, include_examples=False)
    
    if dagbag.import_errors:
        print("\n❌ ERROS DE IMPORTAÇÃO:")
        for filename, error in dagbag.import_errors.items():
            print(f"\n📄 Arquivo: {filename}")
            print(f"⚠️  Erro: {error}")
    
    if dagbag.dags:
        print(f"\n✅ {len(dagbag.dags)} DAG(s) encontrada(s):\n")
        
        for dag_id, dag in dagbag.dags.items():
            print(f"📊 DAG ID: {dag_id}")
            print(f"   📝 Descrição: {dag.description or 'Sem descrição'}")
            print(f"   📅 Start Date: {dag.start_date}")
            print(f"   ⏰ Schedule: {dag.schedule_interval}")
            print(f"   🔢 Tarefas: {len(dag.tasks)}")
            
            # Listar tarefas
            if dag.tasks:
                print(f"   📋 Lista de Tarefas:")
                for task in dag.tasks:
                    print(f"      - {task.task_id} ({task.task_type})")
            
            print()
    else:
        print("\n⚠️  Nenhum DAG encontrado!")
    
    print("=" * 60)

if __name__ == "__main__":
    try:
        listar_dags()
    except Exception as e:
        print(f"\n❌ Erro ao carregar DAGs: {e}")
        sys.exit(1)
