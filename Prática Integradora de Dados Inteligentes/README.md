---

**Relatório de Planejamento e Execução da Primeira Sprint**

**Projeto:** Sistema de Seguro de Veículos para Aposentados (API Backend com Django/DRF)

**Responsável:** Delean Plince Mafra

**Data:** 21/04/2025

**1. Contexto do Projeto**

Fui contratado como Product Owner (PO) para liderar o desenvolvimento da API RESTful para um novo sistema de seguros de veículos voltado para aposentados. A seguradora precisa de endpoints para simulação, cadastro de clientes e gerenciamento de apólices. O projeto será desenvolvido usando Scrum, com sprints de 2 semanas, utilizando Python com os frameworks Django e Django REST Framework (DRF) para o backend.

**2. Product Backlog (Priorizado)**

Criei o backlog com as principais funcionalidades, classificadas por valor para o negócio e complexidade:

*Em anexo "Product Backlog.xlsx"*

**3. Planejamento da Sprint 1**

*   **Duração:** 2 semanas
*   **Objetivo: Entregar o Simulador de Apólice e o Cadastro Básico de Cliente.


*   *Atividades:** Entregar os endpoints públicos iniciais da API (`POST /v1/simular` e `POST /v1/cadastro`) funcionais, utilizando Django e DRF, conforme especificação da documentação. Estabelecer a estrutura base do projeto, incluindo configuração do DRF e modelos de dados iniciais.
*   **Itens do Product Backlog Selecionados:** Itens correspondentes aos endpoints `POST /v1/simular` e `POST /v1/cadastro`.
*   **Tarefas da Sprint (Sprint Backlog):** As tarefas detalhadas (setup do projeto Django/DRF, definição de modelos, criação de serializers, views baseadas em DRF, configuração de URLs) estão listadas no arquivo anexo.

*Em anexo "tarefa.xlsx"*

**4. Execução da Sprint (Python/Django/DRF API)**

*   **Semana 1: Setup, Estrutura, Modelos, Serializers e Endpoint de Simulação**
    *   **Dia 1-2: Ambiente e Estrutura**
        *   Reunião de alinhamento da equipe sobre padrões Python/Django/DRF.
        *   Setup do ambiente virtual
        *   Instalação das dependências
        *   Criação do projeto Django: `django-admin startproject seguradora_api`.
        *   Criação do app Django para a API: `cd seguradora_api`, `python manage.py startapp api_v1`.
    *   **Dia 3-5: Configuração, Modelos, Serializers e View `/simular`**
        *   Ajuste do `seguradora_api/settings.py`: Adição de `'rest_framework'` e `'api_v1'` a `INSTALLED_APPS`, configuração do `DATABASES`.
        *   Definição dos modelos iniciais em `api_v1/models.py` (ex: `Cliente`, `Veiculo` se necessário para cadastro).
        ```python
        # api_v1/models.py (Exemplo inicial para Cliente)
        from django.db import models
        class Cliente(models.Model):
            nome = models.CharField(max_length=100)
            cpf = models.CharField(max_length=14, unique=True)
            data_nascimento = models.DateField()
            # ... outros campos necessários ...
        ```
        *   Criação de `api_v1/serializers.py`: Definição de serializers para os requests e responses dos endpoints.
        ```python
        # api_v1/serializers.py (Exemplo para Simulação)
        from rest_framework import serializers
        class SimulacaoRequestSerializer(serializers.Serializer):
            idade = serializers.IntegerField(min_value=18)
            valorVeiculo = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0)
            historico = serializers.ChoiceField(choices=['limpo', 'com_sinistros'])
        class SimulacaoResponseSerializer(serializers.Serializer):
            valorSeguro = serializers.DecimalField(max_digits=10, decimal_places=2)
            descontoAposentado = serializers.CharField(max_length=5)
        ```
        *   Implementação da View para `/simular` em `api_v1/views.py` usando DRF (`APIView`).
        ```python
        # api_v1/views.py (Exemplo para Simulação)
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework import status
        from .serializers import SimulacaoRequestSerializer, SimulacaoResponseSerializer
        class SimularApoliceAPIView(APIView):
            def post(self, request, *args, **kwargs):
                serializer = SimulacaoRequestSerializer(data=request.data)
                if serializer.is_valid():
                    idade = serializer.validated_data['idade']
                    valor_veiculo = serializer.validated_data['valorVeiculo']
                    historico = serializer.validated_data['historico']

                    taxa_base = 0.05
                    fator_historico = 1.1 if historico == 'com_sinistros' else 1.0
                    valor_final = float(valor_veiculo) * taxa_base * fator_historico
                    desconto_str = "0%"

                    if idade >= 60:
                        desconto = 0.20
                        valor_final *= (1 - desconto)
                        desconto_str = "20%"

                    response_data = {'valorSeguro': round(valor_final, 2), 'descontoAposentado': desconto_str}
                    response_serializer = SimulacaoResponseSerializer(response_data)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```
        *   Configuração das URLs em `api_v1/urls.py` e `seguradora_api/urls.py`.

*   **Semana 2: Endpoint de Cadastro, Migrations e Verificação**
    *   **Dia 6-8: Implementação do Endpoint `/cadastro` e Migrations**
        *   Criação de serializers para o cadastro (`CadastroRequestSerializer`, `CadastroResponseSerializer`).
        *   Implementação da View para `/cadastro` em `api_v1/views.py` (`APIView` ou `CreateAPIView`).
        ```python
        # api_v1/views.py (Exemplo conceitual para Cadastro)
        # Assumindo a existência de ClienteSerializer e Veiculo (ou dados no Cliente)
        class CadastroClienteAPIView(APIView): # Ou generics.CreateAPIView
             def post(self, request, *args, **kwargs):
                 serializer = CadastroRequestSerializer(data=request.data)
                 if serializer.is_valid():
                     # Lógica para verificar duplicação de CPF
                     cpf = serializer.validated_data['cpf']
                     if Cliente.objects.filter(cpf=cpf).exists():
                         return Response({"erro": "CPF já cadastrado."}, status=status.HTTP_409_CONFLICT)

                     # Lógica para criar o cliente (e veículo, se aplicável)
                     # cliente = Cliente.objects.create(...) # Usando dados validados
                     # ... salvar veículo se necessário ...
                     cliente_id_gerado = "cliente_fake_123" # Substituir pelo ID real

                     response_data = {"clienteId": cliente_id_gerado, "mensagem": "Cadastro realizado com sucesso."}
                     return Response(response_data, status=status.HTTP_201_CREATED)
                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```
        *   Execução das migrações: `python manage.py makemigrations api_v1`, `python manage.py migrate`.
    *   **Dia 9-10: Testes e Encerramento**
        *   Testes manuais dos endpoints `/v1/simular` e `/v1/cadastro` usando `curl` ou Postman, validando requests e responses JSON conforme documentação da API.
        *   Verificação dos códigos de status (200, 201, 400, 409).
        *   Revisão final do código Python/Django/DRF e preparação para a Sprint Review.

**5. Entrega da Sprint 1 (Demo / Sprint Review)**

*   **Resultados alcançados:**
    *   ✅ Estrutura base do projeto Django/DRF (`seguradora_api`) configurada.
    *   ✅ App `api_v1` criado e integrado, com modelos e serializers iniciais.
    *   ✅ Endpoint `POST /v1/simular` implementado em Django/DRF, funcional e aderente à documentação.
    *   ✅ Endpoint `POST /v1/cadastro` implementado em Django/DRF, funcional (com persistência básica via ORM) e aderente à documentação.
    *   ✅ Validações iniciais usando serializers do DRF implementadas.
*   **Próximos passos (Planejamento para Sprint 2):**
    *   Implementar autenticação JWT para proteger endpoints futuros (ex: `/apolices`).
    *   Desenvolver o endpoint `GET /v1/apolices` usando DRF (ListAPIView/ViewSet).
    *   Refinar a persistência de dados e tratamento de erros.
    *   Implementar testes automatizados (unitários/integração) usando o framework de testes do Django/DRF.

**6. Materiais de Apoio**

*   Repositório no GitHub *(link fictício)*
*   Documentação da API *(Referência à documentação fornecida)*
*   Documentação Django REST Framework: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)

**7. Lições Aprendidas e o que deu certo**

*   A documentação da API serviu como um bom guia para a implementação com DRF.
*   O uso de Serializers do DRF facilitou a validação dos dados de entrada e a formatação das saídas.
*   O escopo da Sprint 1 (dois endpoints públicos) foi adequado para iniciar o projeto com a nova stack.
*   A implementação da autenticação (JWT) é prioritária para a próxima Sprint.
*   A definição de uma estratégia robusta de testes automatizados é crucial para garantir a qualidade da API.
