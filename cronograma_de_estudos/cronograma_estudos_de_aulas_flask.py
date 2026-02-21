#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cronograma de Estudos - Sistema de Acompanhamento de Atividades Acadêmicas

© 2026 Delean Mafra - Todos os direitos reservados

Licença: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
https://creativecommons.org/licenses/by-nc/4.0/

Você tem o direito de:
  - Compartilhar: copiar e redistribuir o material em qualquer meio ou formato
  - Adaptar: remixar, transformar e construir sobre o material

Sob os seguintes termos:
  - Atribuição: Você deve dar o crédito apropriado
  - NãoComercial: Você não pode usar o material para fins comerciais
"""

from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime, timedelta
import os
import webbrowser

app = Flask(__name__)

# Caminho para o arquivo JSON
JSON_FILE = 'cronograma_estudos.json'

def carregar_dados():
    # Carrega os dados do arquivo JSON
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"cronograma": []}

def salvar_dados(dados):
    # Salva os dados no arquivo JSON
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def calcular_progresso():
    # Calcula o progresso geral e por matéria
    dados = carregar_dados()
    cronograma = dados['cronograma']
    notas = dados.get('notas_materias', {})
    
    # Progresso geral
    total_atividades = len(cronograma)
    atividades_concluidas = sum(1 for item in cronograma if item['concluido'])
    progresso_geral = (atividades_concluidas / total_atividades) * 100 if total_atividades > 0 else 0
    
    # Progresso por matéria
    materias = {}
    for item in cronograma:
        materia = item['materia']
        if materia not in materias:
            materias[materia] = {'total': 0, 'concluidas': 0, 'nota': notas.get(materia), 'status_aprovacao': None}
        materias[materia]['total'] += 1
        if item['concluido']:
            materias[materia]['concluidas'] += 1
    
    for materia in materias:
        total = materias[materia]['total']
        concluidas = materias[materia]['concluidas']
        materias[materia]['progresso'] = (concluidas / total) * 100 if total > 0 else 0
        
        # Calcular status de aprovação
        nota = materias[materia]['nota']
        if materias[materia]['progresso'] == 100:
            if nota is not None:
                if nota >= 6:
                    materias[materia]['status_aprovacao'] = 'aprovado'
                else:
                    materias[materia]['status_aprovacao'] = 'reprovado'
            else:
                materias[materia]['status_aprovacao'] = 'sem_nota'
        else:
            materias[materia]['status_aprovacao'] = 'em_andamento'
    
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
    # Calcula a previsão de conclusão baseada na data atual
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
    # Retorna o próximo dia útil (segunda a sábado)
    proxima_data = data_atual + timedelta(days=1)
    while proxima_data.weekday() == 6:  # Domingo
        proxima_data += timedelta(days=1)
    return proxima_data

def calcular_previsao_individual(atividade_id):
    # Calcula a data de previsão de conclusão para uma atividade específica
    # Ordem: Atividades 1-8 de todas as matérias, depois 9-16 de todas as matérias
    # Primeira atividade em 06/01/2026, um dia útil por atividade
    
    data_inicio = datetime.strptime("06/01/2026", "%d/%m/%Y")
    
    dados = carregar_dados()
    cronograma = dados['cronograma']
    
    # Encontrar a atividade atual
    atividade_atual = None
    for item in cronograma:
        if item['id'] == atividade_id:
            atividade_atual = item
            break
    
    if not atividade_atual:
        return "N/A"
    
    # Extrair número da atividade (1-8 ou 9-16)
    numero_atividade = int(atividade_atual['atividade'].split()[-1])
    materia_atual = atividade_atual['materia']
    
    # Contar todas as matérias únicas
    materias_unicas = []
    for item in cronograma:
        if item['materia'] not in materias_unicas:
            materias_unicas.append(item['materia'])
    
    # Encontrar índice da matéria atual
    indice_materia = materias_unicas.index(materia_atual)
    
    # Calcular posição na sequência
    if numero_atividade <= 8:
        # Atividades 1-8: vêm primeiro
        # Posição = (número da atividade - 1) + (índice da matéria * 8)
        posicao = (numero_atividade - 1) + (indice_materia * 8)
    else:
        # Atividades 9-16: vêm depois de todas as 1-8
        # Total de matérias = len(materias_unicas)
        # Posição = (total de atividades 1-8) + (número da atividade - 9) + (índice da matéria * 8)
        posicao = (len(materias_unicas) * 8) + (numero_atividade - 9) + (indice_materia * 8)
    
    # Calcular a data adicionando dias úteis
    data_previsao = data_inicio
    for _ in range(posicao):
        data_previsao += timedelta(days=1)
        while data_previsao.weekday() == 6:  # Domingo
            data_previsao += timedelta(days=1)
    
    return data_previsao.strftime("%d/%m/%Y")

def calcular_progresso_por_data_limite(data_limite_str):
    # Calcula o progresso das atividades com uma data limite específica
    dados = carregar_dados()
    cronograma = dados['cronograma']
    
    # Filtrar atividades com a data limite especificada
    atividades_com_data = [item for item in cronograma if item.get('data_limite_entrega', '19/02/2026') == data_limite_str]
    
    if not atividades_com_data:
        return {
            'total': 0,
            'concluidas': 0,
            'pendentes': 0,
            'progresso': 0,
            'status': 'vazio'
        }
    
    total = len(atividades_com_data)
    concluidas = sum(1 for item in atividades_com_data if item['concluido'])
    pendentes = total - concluidas
    progresso = (concluidas / total) * 100 if total > 0 else 0
    
    return {
        'total': total,
        'concluidas': concluidas,
        'pendentes': pendentes,
        'progresso': progresso,
        'status': 'concluido' if concluidas == total else 'pendente'
    }

def calcular_cor_prazo(data_limite_str, concluido):
    # Calcula a cor do badge baseado na urgência do prazo
    if concluido:
        return "bg-secondary"
    
    hoje = datetime.now()
    limite = datetime.strptime(data_limite_str, "%d/%m/%Y")
    dias_restantes = (limite - hoje).days
    
    if dias_restantes < 0:
        return "bg-danger"  # Atrasado
    elif dias_restantes <= 7:
        return "bg-warning text-dark"  # Urgente (7 dias ou menos)
    else:
        return "bg-info"  # Normal

@app.route('/')
def index():
    dados = carregar_dados()
    progresso = calcular_progresso()
    previsao = calcular_previsao_conclusao()
    
    # Calcular datas limite
    hoje = datetime.now()
    limite_1 = datetime.strptime("19/02/2026", "%d/%m/%Y")
    limite_2 = datetime.strptime("16/03/2026", "%d/%m/%Y")
    
    # Calcular dias restantes para cada limite
    # Se todas as atividades foram entregues, mostrar 0 em vez de negativo
    dias_calc_1 = (limite_1 - hoje).days
    dias_calc_2 = (limite_2 - hoje).days
    
    # Calcular progresso por data limite
    progresso_limite_1 = calcular_progresso_por_data_limite("19/02/2026")
    progresso_limite_2 = calcular_progresso_por_data_limite("16/03/2026")
    
    # Ajustar dias restantes: se concluído e data passou, mostrar 0
    if progresso_limite_1['status'] == 'concluido' and dias_calc_1 < 0:
        dias_restantes_1 = 0
    else:
        dias_restantes_1 = max(0, dias_calc_1)
    
    if progresso_limite_2['status'] == 'concluido' and dias_calc_2 < 0:
        dias_restantes_2 = 0
    else:
        dias_restantes_2 = max(0, dias_calc_2)
    
    # Determinar qual limite está ativo baseado no status das atividades
    # Se limite 1 ainda tem pendentes, mostrar limite 1
    # Se limite 1 está concluído, mostrar limite 2
    if progresso_limite_1['status'] != 'concluido':
        proxima_data_limite = "19/02/2026"
        dias_restantes = dias_restantes_1
        progresso_atual = progresso_limite_1
    elif progresso_limite_2['status'] != 'concluido':
        proxima_data_limite = "16/03/2026"
        dias_restantes = dias_restantes_2
        progresso_atual = progresso_limite_2
    else:
        # Ambos concluídos
        proxima_data_limite = "16/03/2026"
        dias_restantes = dias_restantes_2
        progresso_atual = progresso_limite_2
    
    # Adicionar cor do badge e previsão de conclusão para cada atividade
    for atividade in dados['cronograma']:
        atividade['cor_prazo'] = calcular_cor_prazo(
            atividade.get('data_limite_entrega', '19/02/2026'),
            atividade['concluido']
        )
        atividade['previsao_conclusao'] = calcular_previsao_individual(atividade['id'])
    
    return render_template('index.html',
                         cronograma=dados['cronograma'], 
                         progresso=progresso,
                         previsao=previsao,
                         data_limite=proxima_data_limite,
                         dias_restantes=dias_restantes,
                         dias_restantes_1=dias_restantes_1,
                         dias_restantes_2=dias_restantes_2,
                         limite_1="19/02/2026",
                         limite_2="16/03/2026",
                         progresso_limite_1=progresso_limite_1,
                         progresso_limite_2=progresso_limite_2,
                         progresso_atual=progresso_atual)

@app.route('/api/marcar_atividade', methods=['POST'])
def marcar_atividade():
    # API para marcar/desmarcar uma atividade como concluída
    data = request.get_json()
    atividade_id = data.get('id')
    concluido = data.get('concluido')
    
    dados = carregar_dados()
    
    # Encontrar e atualizar a atividade
    for item in dados['cronograma']:
        if item['id'] == atividade_id:
            item['concluido'] = concluido
            if concluido:
                # Se for marcar como concluída, usar data atual
                item['data_conclusao'] = datetime.now().strftime("%d/%m/%Y")
            else:
                # Se desmarcar, limpar a data
                item['data_conclusao'] = None
            break
    
    salvar_dados(dados)
    
    # Recalcular progresso e previsão
    progresso = calcular_progresso()
    previsao = calcular_previsao_conclusao()
    progresso_limite_1 = calcular_progresso_por_data_limite("19/02/2026")
    progresso_limite_2 = calcular_progresso_por_data_limite("16/03/2026")
    
    # Determinar qual limite está ativo
    hoje = datetime.now()
    limite_1 = datetime.strptime("19/02/2026", "%d/%m/%Y")
    limite_2 = datetime.strptime("16/03/2026", "%d/%m/%Y")
    dias_restantes_1 = (limite_1 - hoje).days
    dias_restantes_2 = (limite_2 - hoje).days
    
    if progresso_limite_1['status'] != 'concluido':
        data_limite = "19/02/2026"
        dias_restantes = dias_restantes_1
        progresso_atual = progresso_limite_1
    elif progresso_limite_2['status'] != 'concluido':
        data_limite = "16/03/2026"
        dias_restantes = dias_restantes_2
        progresso_atual = progresso_limite_2
    else:
        data_limite = "16/03/2026"
        dias_restantes = dias_restantes_2
        progresso_atual = progresso_limite_2
    
    return jsonify({
        'success': True,
        'progresso': progresso,
        'previsao': previsao,
        'progresso_limite_1': progresso_limite_1,
        'progresso_limite_2': progresso_limite_2,
        'progresso_atual': progresso_atual,
        'data_limite': data_limite,
        'dias_restantes': dias_restantes
    })

@app.route('/api/atualizar_data_conclusao', methods=['POST'])
def atualizar_data_conclusao():
    # API para atualizar manualmente a data de conclusão
    data = request.get_json()
    atividade_id = data.get('id')
    data_conclusao = data.get('data_conclusao')
    
    # Validar formato da data
    try:
        datetime.strptime(data_conclusao, "%d/%m/%Y")
    except ValueError:
        return jsonify({
            'success': False,
            'message': 'Formato de data inválido. Use DD/MM/YYYY'
        }), 400
    
    # Validar que a data não está no futuro
    hoje = datetime.now()
    data_informada = datetime.strptime(data_conclusao, "%d/%m/%Y")
    if data_informada > hoje:
        return jsonify({
            'success': False,
            'message': 'A data de conclusão não pode ser no futuro'
        }), 400
    
    dados = carregar_dados()
    
    # Encontrar e atualizar a atividade
    for item in dados['cronograma']:
        if item['id'] == atividade_id:
            item['data_conclusao'] = data_conclusao
            # Se houver data de conclusão, marcar como concluída
            if data_conclusao:
                item['concluido'] = True
            break
    
    salvar_dados(dados) 
    
    # Recalcular progresso e previsão
    progresso = calcular_progresso()
    previsao = calcular_previsao_conclusao()
    progresso_limite_1 = calcular_progresso_por_data_limite("19/02/2026")
    progresso_limite_2 = calcular_progresso_por_data_limite("16/03/2026")
    
    # Determinar qual limite está ativo
    hoje = datetime.now()
    limite_1 = datetime.strptime("19/02/2026", "%d/%m/%Y")
    limite_2 = datetime.strptime("16/03/2026", "%d/%m/%Y")
    dias_restantes_1 = (limite_1 - hoje).days
    dias_restantes_2 = (limite_2 - hoje).days
    
    if progresso_limite_1['status'] != 'concluido':
        data_limite = "19/02/2026"
        dias_restantes = dias_restantes_1
        progresso_atual = progresso_limite_1
    elif progresso_limite_2['status'] != 'concluido':
        data_limite = "16/03/2026"
        dias_restantes = dias_restantes_2
        progresso_atual = progresso_limite_2
    else:
        data_limite = "16/03/2026"
        dias_restantes = dias_restantes_2
        progresso_atual = progresso_limite_2
    
    return jsonify({
        'success': True,
        'progresso': progresso,
        'previsao': previsao,
        'progresso_limite_1': progresso_limite_1,
        'progresso_limite_2': progresso_limite_2,
        'progresso_atual': progresso_atual,
        'data_limite': data_limite,
        'dias_restantes': dias_restantes
    })

@app.route('/api/progresso')
def api_progresso():
    # API para obter dados de progresso
    progresso = calcular_progresso()
    previsao = calcular_previsao_conclusao()
    progresso_limite_1 = calcular_progresso_por_data_limite("19/02/2026")
    progresso_limite_2 = calcular_progresso_por_data_limite("16/03/2026")
    
    # Determinar qual limite está ativo
    hoje = datetime.now()
    limite_1 = datetime.strptime("19/02/2026", "%d/%m/%Y")
    limite_2 = datetime.strptime("16/03/2026", "%d/%m/%Y")
    dias_calc_1 = (limite_1 - hoje).days
    dias_calc_2 = (limite_2 - hoje).days
    
    # Ajustar dias restantes: se concluído e data passou, mostrar 0
    if progresso_limite_1['status'] == 'concluido' and dias_calc_1 < 0:
        dias_restantes_1 = 0
    else:
        dias_restantes_1 = max(0, dias_calc_1)
    
    if progresso_limite_2['status'] == 'concluido' and dias_calc_2 < 0:
        dias_restantes_2 = 0
    else:
        dias_restantes_2 = max(0, dias_calc_2)
    
    if progresso_limite_1['status'] != 'concluido':
        data_limite = "19/02/2026"
        dias_restantes = dias_restantes_1
        progresso_atual = progresso_limite_1
    elif progresso_limite_2['status'] != 'concluido':
        data_limite = "16/03/2026"
        dias_restantes = dias_restantes_2
        progresso_atual = progresso_limite_2
    else:
        data_limite = "16/03/2026"
        dias_restantes = dias_restantes_2
        progresso_atual = progresso_limite_2
    
    return jsonify({
        'progresso': progresso,
        'previsao': previsao,
        'progresso_limite_1': progresso_limite_1,
        'progresso_limite_2': progresso_limite_2,
        'progresso_atual': progresso_atual,
        'data_limite': data_limite,
        'dias_restantes': dias_restantes,
        'dias_restantes_1': dias_restantes_1,
        'dias_restantes_2': dias_restantes_2
    })

@app.route('/api/atualizar_nota', methods=['POST'])
def atualizar_nota():
    # API para atualizar a nota de uma matéria
    data = request.get_json()
    materia = data.get('materia')
    nota = data.get('nota')
    
    # Validar nota (pode ser None para limpar ou número entre 0 e 10)
    if nota is not None:
        try:
            nota = float(nota)
            if nota < 0 or nota > 10:
                return jsonify({
                    'success': False,
                    'message': 'A nota deve estar entre 0 e 10'
                }), 400
        except ValueError:
            return jsonify({
                'success': False,
                'message': 'Nota inválida'
            }), 400
    
    dados = carregar_dados()
    
    # Inicializar notas_materias se não existir
    if 'notas_materias' not in dados:
        dados['notas_materias'] = {}
    
    # Atualizar nota
    dados['notas_materias'][materia] = nota
    
    salvar_dados(dados)
    
    # Recalcular progresso
    progresso = calcular_progresso()
    
    return jsonify({
        'success': True,
        'progresso': progresso,
        'materia': materia,
        'nota': nota
    })

if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        webbrowser.open('http://127.0.0.1:5000')
    app.run(debug=True, host='0.0.0.0', port=5000)
