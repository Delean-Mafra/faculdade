# Definindo os nós (agentes)


# Exemplo 1
from xml.dom.minidom import Node


class DataCollector(Node):
    def run(self, data):
        print("Coletando dados...")
        return {"data": "dados coletados"}

class DataProcessor(Node):
    def run(self, data):
        print("Processando dados...")
        processed_data = data["data"] + " processados"
        return {"processed_data": processed_data}

class DataAnalyzer(Node):
    def run(self, data):
        print("Analisando dados...")
        analysis = data["processed_data"] + " analisados"
        return {"analysis": analysis}

# Exemplo 2
def agente_input():
    """
    Este agente solicita informações ao usuário.
    """
    nome = input("Por favor, digite seu nome: ")
    idade = int(input("Por favor, digite sua idade: "))
    return nome, idade

def agente_processamento(nome, idade):
    """
    Este agente processa as informações recebidas.
    """
    mensagem = f"Olá, {nome}! Você tem {idade} anos."
    return mensagem

# Exemplo de uso
nome_usuario, idade_usuario = agente_input()
mensagem_final = agente_processamento(nome_usuario, idade_usuario)
print(mensagem_final)

# Exemplo 3

from crewai import Task
from crewai import Agent, Crew, Process
from crewai.agents import WebResearcher, ArticleWriter
from crewai.agents import SalesAgent

# Definindo os agentes
pesquisador = WebResearcher()
escritor = ArticleWriter()
agente_vendas = SalesAgent()

# Definindo as tarefas
tarefa_pesquisa = Task(
    description='Pesquisar informações sobre IA',
    agent=pesquisador,
    expected_output='Dados coletados sobre IA'
)

tarefa_escrever_artigo = Task(
    description='Escrever artigo sobre IA',
    agent=escritor,
    expected_output='Artigo completo sobre IA'
)

tarefa = Task(
    description='Encontre e resuma as notícias mais recentes e relevantes sobre IA',
    agent=agente_vendas,
    expected_output='Um resumo em lista dos 5 principais notícias sobre IA',
)

# Montar a equipe com um processo sequencial
minha_equipe = Crew(
    agents=[pesquisador, escritor],
    tasks=[tarefa_pesquisa, tarefa_escrever_artigo],
    process=Process.sequencial,
    full_output=True,
    verbose=True,
)

agent = Agent(
    role='Analista de Dados',
    goal='Extrair insights acionáveis',
    backstory="""Você é um analista de dados em uma grande empresa.
Você é responsável por analisar dados e fornecer insights para o negócio.

Atualmente, você está trabalhando em um projeto para analisar
o desempenho de nossas campanhas de marketing."""
)
agent.add_node(DataCollector())
agent.add_node(DataProcessor())
agent.add_node(DataAnalyzer())



# Exemplo 4

class AgenteControlador:
    def __init__(self):
        self.agente_interacao = AgenteInteracaoComUsuario()
        self.agente_processamento = AgenteProcessamento()

    def iniciar_interacao(self):
        informacao = self.agente_interacao.solicitar_informacao("Digite seu nome: ")
        resultado = self.agente_processamento.processar_informacao(informacao)
        print(resultado)

class AgenteInteracaoComUsuario:
    def solicitar_informacao(self, mensagem):
        return input(mensagem)

class AgenteProcessamento:
    def processar_informacao(self, informacao):
        # Processamento simples: capitalizar o nome
        return informacao.capitalize()

if __name__ == "__main__":
    controlador = AgenteControlador()
    controlador.iniciar_interacao()


