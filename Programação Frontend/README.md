# Programação Frontend — Paginação Web com Django

Este repositório contém materiais e códigos desenvolvidos para a disciplina de Programação Frontend, com foco em **paginação web** utilizando o framework **Django**. O conteúdo foi elaborado com base em materiais didáticos sobre técnicas de paginação, gerenciamento e exibição eficiente de grandes conjuntos de dados em aplicações web, além da aplicação prática de estilização de páginas com CSS.

## Objetivo

Demonstrar como implementar a paginação de dados em projetos Django, melhorando a experiência do usuário ao navegar por listas extensas, e aplicar técnicas de CSS para tornar a página visualmente mais agradável.

## Conteúdo

- Uso do Django ORM para consultas eficientes em grandes volumes de dados.
- Implementação da paginação utilizando a classe `Paginator` do Django.
- Exemplos de views baseadas em função e em classe para paginação.
- Renderização de páginas com navegação entre resultados.
- Template Tags para controle da navegação e exibição de informações de paginação.
- Estilização de páginas com CSS, utilizando seletores e boas práticas.

## Estrutura do Projeto

```
Programação Frontend/
│
├── db.sqlite3
├── frontend_notes.py
├── manage.py
├── populate_products.py
├── recriar_produtos.py
├── meu_projeto_django/           # Projeto Django
├── produtos/                     # Aplicação Django (exemplo: lista de produtos)
├── static/                       # Arquivos estáticos (CSS, imagens, etc.)
└── templates/                    # Templates HTML
```

## Sobre a Paginação Web

A paginação é fundamental para dividir grandes conjuntos de dados em partes menores, facilitando a navegação, reduzindo a sobrecarga cognitiva do usuário e melhorando o desempenho da aplicação. O Django oferece a classe `Paginator` para dividir e gerenciar a exibição de dados em páginas, com fácil controle sobre navegação, número de itens por página e exibição de informações adicionais.

### Exemplo de uso da classe `Paginator`:

```python
from django.core.paginator import Paginator

produtos = Produto.objects.all()
paginator = Paginator(produtos, 10)  # 10 itens por página
page_number = request.GET.get('page')
page_obj = paginator.get_page(page_number)
return render(request, 'lista_produtos.html', {'page_obj': page_obj})
```

### Renderização no template:

```django
{% for produto in page_obj %}
    <h3>{{ produto.nome }}</h3>
    <p>{{ produto.descricao }}</p>
{% endfor %}

<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; Primeira</a>
            <a href="?page={{ page_obj.previous_page_number }}">anterior</a>
        {% endif %}

        <span class="current-page">{{ page_obj.number }}</span>

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">próxima</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">Última &raquo;</a>
        {% endif %}
    </span>
</div>
```

## Sobre a Atividade Prática

A atividade prática consiste em **estilizar a página de listagem paginada**, utilizando CSS para:

- Definir fontes e cores agradáveis.
- Ajustar margens, preenchimentos e bordas dos elementos.
- Adicionar interatividade com seletores como `:hover`.
- Destacar elementos importantes com bordas arredondadas.

**Exemplo de seletores CSS utilizados:**
```css
.pagination a:hover {
  background-color: #3498db;
  color: #fff;
  border-radius: 5px;
}

.current-page {
  font-weight: bold;
  color: #2c3e50;
}
```
- O seletor `.pagination a:hover` aplica um destaque visual quando o mouse passa sobre os links da paginação.
- O seletor `.current-page` estiliza o número da página atual, tornando-o mais visível.

## Como executar

1. Instale as dependências do Django.
2. Execute as migrações e popule o banco de dados conforme scripts fornecidos.
3. Inicie o servidor de desenvolvimento:
    ```
    python manage.py runserver
    ```
4. Acesse a aplicação no navegador e navegue pelas páginas de produtos.

## Referências

O conteúdo deste repositório foi baseado nos seguintes materiais didáticos:

- [Paginação Web: Técnicas e Boas Práticas](#)
- [Documentação Django — Paginator](https://docs.djangoproject.com/pt-br/4.0/topics/pagination/)
- [Material de aula: Estilização com CSS](#)

---
