# Programação Frontend — Paginação Web e Estilização com CSS

Este repositório reúne exemplos práticos e material de estudo para a disciplina de Programação Frontend da Faculdade Descomplica, focando na implementação de **paginação web** com Django e na **estilização de páginas HTML com CSS**.

## Sobre a Atividade Prática

> **Título da Prática:** Estilizando uma página com CSS  
> **Objetivo:**  
> - Utilizar conhecimentos de CSS para estilizar uma página HTML existente.
> - Selecionar e utilizar seletores CSS adequados para estilizar elementos específicos.
>
> **Ferramentas utilizadas:**  
> - Framework Django  
> - IDE: VSCode
> - Servidor de desenvolvimento Django  
>
> **Resumo da atividade:**  
> O exercício propõe utilizar a página criada durante a aula de “Paginação Web”, adicione estilos CSS para torná-la mais atraente visualmente e explique dois seletores CSS escolhidos, descrevendo os estilos aplicados.

---

## Estrutura do Projeto

```
Programação Frontend/
├── manage.py
├── db.sqlite3
├── frontend_notes.py
├── populate_products.py
├── recriar_produtos.py
├── meu_projeto_django/           # Projeto Django (configurações)
├── produtos/                     # App Django com views, models, etc.
│   └── templates/
│       └── produtos/
│           └── lista_produtos.html  # Página principal de produtos
├── static/
│   └── css/
│       └── styles.css             # Arquivo principal de estilos CSS
└── templates/
    └── base.html                  # Template base do projeto
```

---

## Paginação Web no Django

Paginação é essencial para a experiência do usuário em páginas com muitos registros (como listas de produtos). O Django facilita isso com a classe `Paginator`.

### Exemplo de view paginada:

```python
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    paginator = Paginator(produtos, 8)  # Exibe 8 produtos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'produtos/lista_produtos.html', {'page_obj': page_obj})
```

### Exemplo de template HTML (`lista_produtos.html`):

```django
<h1>Lista de Produtos</h1>
<div class="produtos-container">
  {% for produto in page_obj %}
    <div class="produto-item">
      <h3>{{ produto.nome }}</h3>
      <p>{{ produto.descricao }}</p>
      <span class="preco">R$ {{ produto.preco }}</span>
      <span class="estoque">Estoque: {{ produto.estoque }}</span>
    </div>
  {% endfor %}
</div>

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

---

## Estilização com CSS — Exemplos Práticos

O arquivo `static/css/styles.css` foi criado para tornar a página mais agradável e moderna, atendendo aos requisitos da atividade prática.

### Trecho do CSS utilizado:

```css
.produto-item {
    background-color: white;
    border-radius: 10px;
    padding: 25px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid rgba(0,0,0,0.05);
}

.produto-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.1);
}

.pagination .step-links {
    background-color: white;
    padding: 10px 15px;
    border-radius: 50px;
    display: inline-block;
    box-shadow: 0 3px 8px rgba(0,0,0,0.1);
}
```

#### Exemplos de seletores CSS escolhidos:

1. **`.produto-item:hover`**  
   - **Descrição:** Aplica estilos quando o mouse passa sobre um produto.
   - **Estilos aplicados:**  
     - `transform: translateY(-5px);` — Eleva o cartão do produto, criando efeito de destaque.
     - `box-shadow: 0 8px 15px rgba(0,0,0,0.1);` — Sombra maior para dar sensação de profundidade.
   - **Impacto:** Melhora a interatividade e o feedback visual para o usuário.

2. **`.pagination .step-links`**  
   - **Descrição:** Seleciona o elemento de links de navegação dentro da área de paginação.
   - **Estilos aplicados:**  
     - `background-color: white;` — Fundo branco para os controles de paginação.
     - `padding: 10px 15px;` — Espaçamento interno confortável.
     - `border-radius: 50px;` — Bordas arredondadas em estilo "pill-shaped".
     - `box-shadow: 0 3px 8px rgba(0,0,0,0.1);` — Sombra sutil para destaque.
   - **Impacto:** Deixa a paginação moderna, acessível e agradável de usar.

---

## Outras melhorias implementadas

- Fonte moderna: `'Nunito', 'Segoe UI', Arial, sans-serif`
- Paleta de cores consistente e agradável
- Transições suaves em botões e cartões
- Layout responsivo com media queries
- Efeito de hover em produtos e botões de navegação
- Paginação destacada e fácil de usar

---

## Como rodar localmente

1. Instale o Django e dependências:
    ```bash
    pip install django
    ```
2. Aplique as migrações e popule o banco de dados:
    ```bash
    python manage.py migrate
    python populate_products.py
    ```
3. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```
4. Acesse `http://localhost:8000/produtos/` no navegador.

---

## Material de Apoio

- [Documentação oficial do Django - Paginação](https://docs.djangoproject.com/pt-br/4.0/topics/pagination/)
- [CSS Tricks: Layouts modernos com Flexbox e Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

---
