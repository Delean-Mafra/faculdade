import os

def create_directory(directory_path):
    """Cria um diretório se ele não existir"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"✓ Diretório criado: {directory_path}")
    else:
        print(f"O diretório já existe: {directory_path}")

def create_file(file_path, content):
    """Cria um arquivo com o conteúdo especificado"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Arquivo criado: {file_path}")

def main():
    # Criar estrutura de diretórios
    create_directory('templates')
    create_directory('templates/bookapp')
    create_directory('static/css')
    
    # Criar arquivo base.html com Bootstrap
    base_html = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Sistema de Cadastro de Livros{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="{% url 'book-list' %}">Biblioteca Virtual</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'book-list' %}">Livros</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'author-list' %}">Autores</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'book-create' %}">Novo Livro</a>
                    </li>
                </ul>
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/admin/">Admin</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}
        {% endblock %}
    </div>

    <footer class="bg-light text-center text-muted py-4 mt-5">
        <div class="container">
            <p>Sistema de Cadastro de Livros &copy; 2025</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''
    
    # Criar template para listar livros
    book_list_html = '''{% extends 'base.html' %}

{% block title %}Lista de Livros{% endblock %}

{% block content %}
    <div class="row mb-4">
        <div class="col">
            <h1>Livros Cadastrados</h1>
        </div>
        <div class="col-auto">
            <a href="{% url 'book-create' %}" class="btn btn-primary">
                <i class="bi bi-plus-circle"></i> Novo Livro
            </a>
        </div>
    </div>

    {% if books %}
        <div class="row row-cols-1 row-cols-md-3 g-4">
            {% for book in books %}
                <div class="col">
                    <div class="card h-100 shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">{{ book.title }}</h5>
                            <p class="card-text">
                                <strong>Autor:</strong> {{ book.author.name }}<br>
                                <strong>ISBN:</strong> {{ book.isbn }}<br>
                                <strong>Editora:</strong> {{ book.publisher }}<br>
                                <strong>Ano:</strong> {{ book.publication_year }}
                            </p>
                        </div>
                        <div class="card-footer bg-transparent">
                            <div class="d-flex justify-content-between">
                                <a href="{% url 'book-detail' book.pk %}" class="btn btn-sm btn-outline-primary">
                                    <i class="bi bi-eye"></i> Detalhes
                                </a>
                                <a href="{% url 'book-update' book.pk %}" class="btn btn-sm btn-outline-secondary">
                                    <i class="bi bi-pencil"></i> Editar
                                </a>
                                <a href="{% url 'book-delete' book.pk %}" class="btn btn-sm btn-outline-danger">
                                    <i class="bi bi-trash"></i> Excluir
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
        
        {% if is_paginated %}
        <nav class="mt-4">
            <ul class="pagination justify-content-center">
                {% if page_obj.has_previous %}
                    <li class="page-item">
                        <a class="page-link" href="?page=1">&laquo; Primeira</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="?page={{ page_obj.previous_page_number }}">Anterior</a>
                    </li>
                {% endif %}
                
                {% for num in page_obj.paginator.page_range %}
                    {% if page_obj.number == num %}
                        <li class="page-item active">
                            <span class="page-link">{{ num }}</span>
                        </li>
                    {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
                        <li class="page-item">
                            <a class="page-link" href="?page={{ num }}">{{ num }}</a>
                        </li>
                    {% endif %}
                {% endfor %}
                
                {% if page_obj.has_next %}
                    <li class="page-item">
                        <a class="page-link" href="?page={{ page_obj.next_page_number }}">Próxima</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="?page={{ page_obj.paginator.num_pages }}">Última &raquo;</a>
                    </li>
                {% endif %}
            </ul>
        </nav>
        {% endif %}
    {% else %}
        <div class="alert alert-info">
            <p>Nenhum livro cadastrado. <a href="{% url 'book-create' %}">Cadastre um novo livro</a>.</p>
        </div>
    {% endif %}
{% endblock %}'''

    # Criar template para detalhes do livro
    book_detail_html = '''{% extends 'base.html' %}

{% block title %}{{ book.title }}{% endblock %}

{% block content %}
    <div class="card shadow">
        <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center">
            <h2 class="mb-0">{{ book.title }}</h2>
            <div>
                <a href="{% url 'book-update' book.pk %}" class="btn btn-light">
                    <i class="bi bi-pencil"></i> Editar
                </a>
                <a href="{% url 'book-delete' book.pk %}" class="btn btn-danger">
                    <i class="bi bi-trash"></i> Excluir
                </a>
            </div>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-8">
                    <table class="table">
                        <tr>
                            <th style="width: 150px;">Autor</th>
                            <td>{{ book.author.name }}</td>
                        </tr>
                        <tr>
                            <th>ISBN</th>
                            <td>{{ book.isbn }}</td>
                        </tr>
                        <tr>
                            <th>Editora</th>
                            <td>{{ book.publisher }}</td>
                        </tr>
                        <tr>
                            <th>Ano de Publicação</th>
                            <td>{{ book.publication_year }}</td>
                        </tr>
                        <tr>
                            <th>Número de Páginas</th>
                            <td>{{ book.page_count }}</td>
                        </tr>
                        {% if book.genre %}
                        <tr>
                            <th>Gênero</th>
                            <td>{{ book.genre }}</td>
                        </tr>
                        {% endif %}
                    </table>
                </div>
            </div>
        </div>
        <div class="card-footer">
            <a href="{% url 'book-list' %}" class="btn btn-secondary">
                <i class="bi bi-arrow-left"></i> Voltar para Lista
            </a>
        </div>
    </div>
{% endblock %}'''

    # Criar template para formulário de livro
    book_form_html = '''{% extends 'base.html' %}

{% block title %}
    {% if form.instance.pk %}
        Editar {{ form.instance.title }}
    {% else %}
        Cadastrar Novo Livro
    {% endif %}
{% endblock %}

{% block content %}
    <div class="card shadow">
        <div class="card-header bg-primary text-white">
            <h2 class="mb-0">
                {% if form.instance.pk %}
                    Editar Livro
                {% else %}
                    Cadastrar Novo Livro
                {% endif %}
            </h2>
        </div>
        <div class="card-body">
            <form method="post">
                {% csrf_token %}
                
                {% for field in form %}
                    <div class="mb-3">
                        <label for="{{ field.id_for_label }}" class="form-label">
                            {{ field.label }}{% if field.field.required %} *{% endif %}
                        </label>
                        {{ field.errors }}
                        {{ field|add_class:"form-control" }}
                        {% if field.help_text %}
                            <div class="form-text">{{ field.help_text }}</div>
                        {% endif %}
                    </div>
                {% endfor %}
                
                <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
                    <a href="{% url 'book-list' %}" class="btn btn-secondary">
                        <i class="bi bi-x-circle"></i> Cancelar
                    </a>
                    <button type="submit" class="btn btn-primary">
                        <i class="bi bi-check-circle"></i> 
                        {% if form.instance.pk %}
                            Atualizar
                        {% else %}
                            Cadastrar
                        {% endif %}
                    </button>
                </div>
            </form>
        </div>
    </div>
{% endblock %}'''

    # Criar template para confirmar exclusão
    book_confirm_delete_html = '''{% extends 'base.html' %}

{% block title %}Excluir {{ object.title }}{% endblock %}

{% block content %}
    <div class="card shadow border-danger">
        <div class="card-header bg-danger text-white">
            <h2 class="mb-0">Confirmar Exclusão</h2>
        </div>
        <div class="card-body">
            <p class="fs-5">Tem certeza que deseja excluir o livro "<strong>{{ object.title }}</strong>"?</p>
            <p class="text-muted">Esta ação não pode ser desfeita.</p>
            
            <form method="post">
                {% csrf_token %}
                <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
                    <a href="{% url 'book-detail' object.pk %}" class="btn btn-secondary">
                        <i class="bi bi-arrow-left"></i> Cancelar
                    </a>
                    <button type="submit" class="btn btn-danger">
                        <i class="bi bi-trash"></i> Confirmar Exclusão
                    </button>
                </div>
            </form>
        </div>
    </div>
{% endblock %}'''

    # Criar template para listar autores
    author_list_html = '''{% extends 'base.html' %}

{% block title %}Lista de Autores{% endblock %}

{% block content %}
    <h1 class="mb-4">Autores Cadastrados</h1>
    
    {% if authors %}
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-primary">
                    <tr>
                        <th>Nome</th>
                        <th>Data de Nascimento</th>
                        <th>Livros</th>
                    </tr>
                </thead>
                <tbody>
                    {% for author in authors %}
                        <tr>
                            <td>{{ author.name }}</td>
                            <td>{{ author.birth_date|date:"d/m/Y" }}</td>
                            <td>
                                {% with book_count=author.book_set.count %}
                                    {{ book_count }} livro{{ book_count|pluralize }}
                                {% endwith %}
                            </td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    {% else %}
        <div class="alert alert-info">
            <p>Nenhum autor cadastrado.</p>
        </div>
    {% endif %}
{% endblock %}'''

    # Criar arquivo CSS
    css_content = '''/* Estilos personalizados para o projeto */
body {
    padding-bottom: 20px;
    background-color: #f8f9fa;
}

.card {
    transition: transform 0.2s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
}

/* Cores de alerta personalizadas */
.alert-success {
    background-color: #d1e7dd;
    border-color: #badbcc;
    color: #0f5132;
}

.alert-danger {
    background-color: #f8d7da;
    border-color: #f5c2c7;
    color: #842029;
}

/* Estilo para validação de formulários */
.invalid-feedback {
    display: block;
    color: #dc3545;
}

/* Estilo para o rodapé */
footer {
    margin-top: 3rem;
    padding: 1rem 0;
    border-top: 1px solid #e9ecef;
}
'''

    # Criar o arquivo de tempate_tags para adicionar classes aos campos do formulário
    create_directory('bookapp/templatetags')
    create_file('bookapp/templatetags/__init__.py', '')
    create_file('bookapp/templatetags/form_tags.py', '''from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Adiciona uma classe CSS a um campo de formulário"""
    return field.as_widget(attrs={'class': css_class})
''')

    # Criar todos os arquivos
    create_file('templates/base.html', base_html)
    create_file('templates/bookapp/book_list.html', book_list_html)
    create_file('templates/bookapp/book_detail.html', book_detail_html)
    create_file('templates/bookapp/book_form.html', book_form_html)
    create_file('templates/bookapp/book_confirm_delete.html', book_confirm_delete_html)
    create_file('templates/bookapp/author_list.html', author_list_html)
    create_file('static/css/style.css', css_content)
    
    print("\n✅ Todos os templates foram criados com sucesso!")
    print("\nAgora reinicie o servidor e acesse http://127.0.0.1:8000/")
    print("Utilize os seguintes comandos:")
    print("\n1. Parar o servidor atual (Ctrl+C)")
    print("2. Reiniciar o servidor:")
    print("   & c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py runserver")
    print("\nDepois de reiniciar, você precisará adicionar alguns dados iniciais para visualizar corretamente:")
    print("1. Acesse http://127.0.0.1:8000/admin/")
    print("2. Faça login com usuário 'admin' e senha '123456Ab'")
    print("3. Adicione alguns autores e livros pelo painel administrativo")
    
if __name__ == "__main__":
    main()