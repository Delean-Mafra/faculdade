from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Caminho para o arquivo JSON
JSON_FILE = 'cronograma_estudos.json'

def carregar_dados():
    """Carrega os dados do arquivo JSON"""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"cronograma": []}

def salvar_dados(dados):
    """Salva os dados no arquivo JSON"""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def calcular_progresso():
    """Calcula o progresso geral e por matéria"""
    dados = carregar_dados()
    cronograma = dados['cronograma']
    
    # Progresso geral
    total_atividades = len(cronograma)
    atividades_concluidas = sum(1 for item in cronograma if item['concluido'])
    progresso_geral = (atividades_concluidas / total_atividades) * 100 if total_atividades > 0 else 0
    
    # Progresso por matéria
    materias = {}
    for item in cronograma:
        materia = item['materia']
        if materia not in materias:
            materias[materia] = {'total': 0, 'concluidas': 0}
        materias[materia]['total'] += 1
        if item['concluido']:
            materias[materia]['concluidas'] += 1
    
    for materia in materias:
        total = materias[materia]['total']
        concluidas = materias[materia]['concluidas']
        materias[materia]['progresso'] = (concluidas / total) * 100 if total > 0 else 0
    
    return {
        'geral': {
            'total': total_atividades,
            'concluidas': atividades_concluidas,
            'pendentes': total_atividades - atividades_concluidas,
            'progresso': progresso_geral
        },
        'materias': materias
    }

def calcular_previsao_conclusao():
    """Calcula a previsão de conclusão baseada na data atual"""
    dados = carregar_dados()
    cronograma = dados['cronograma']
    
    # Atividades pendentes
    atividades_pendentes = [item for item in cronograma if not item['concluido']]
    
    if not atividades_pendentes:
        return "Todas as atividades foram concluídas!"
    
    # Data atual
    hoje = datetime.now()
    
    # Calcular próximos dias úteis (segunda a sábado)
    data_previsao = hoje
    atividades_restantes = len(atividades_pendentes)
    
    while atividades_restantes > 0:
        data_previsao += timedelta(days=1)
        # Segunda a sábado (0-5 em weekday())
        if data_previsao.weekday() < 6:  # 0=segunda, 6=domingo
            atividades_restantes -= 1
    
    return data_previsao.strftime("%d/%m/%Y")

def proximo_dia_util(data_atual):
    """Retorna o próximo dia útil (segunda a sábado)"""
    proxima_data = data_atual + timedelta(days=1)
    while proxima_data.weekday() == 6:  # Domingo
        proxima_data += timedelta(days=1)
    return proxima_data

@app.route('/')
def index():
    dados = carregar_dados()
    progresso = calcular_progresso()
    previsao = calcular_previsao_conclusao()
    
    return render_template('index.html', 
                         cronograma=dados['cronograma'], 
                         progresso=progresso,
                         previsao=previsao)

@app.route('/api/marcar_atividade', methods=['POST'])
def marcar_atividade():
    """API para marcar/desmarcar uma atividade como concluída"""
    data = request.get_json()
    atividade_id = data.get('id')
    concluido = data.get('concluido')
    
    dados = carregar_dados()
    
    # Encontrar e atualizar a atividade
    for item in dados['cronograma']:
        if item['id'] == atividade_id:
            item['concluido'] = concluido
            if concluido:
                item['data_conclusao'] = datetime.now().strftime("%d/%m/%Y")
            else:
                item['data_conclusao'] = None
            break
    
    salvar_dados(dados)
    
    # Recalcular progresso e previsão
    progresso = calcular_progresso()
    previsao = calcular_previsao_conclusao()
    
    return jsonify({
        'success': True,
        'progresso': progresso,
        'previsao': previsao
    })

@app.route('/api/progresso')
def api_progresso():
    """API para obter dados de progresso"""
    progresso = calcular_progresso()
    previsao = calcular_previsao_conclusao()
    
    return jsonify({
        'progresso': progresso,
        'previsao': previsao
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
