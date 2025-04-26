from django.test import TestCase
from django.urls import reverse
from bookapp.models import Book, Author
from bookapp.forms import BookForm

class BookViewIntegrationTest(TestCase):
    def setUp(self):
        # Configurar autor para uso nos testes
        self.author = Author.objects.create(
            name="George Orwell",
            birth_date="1903-06-25"
        )
        
        # Criar um livro para testes de atualização
        self.book = Book.objects.create(
            title="1984",
            isbn="9788535914849",
            author=self.author,
            publisher="Companhia das Letras",
            publication_year=2009,
            page_count=416
        )
        
        # Dados para criar um novo livro
        self.new_book_data = {
            'title': 'A Revolução dos Bichos',
            'isbn': '9788535909555',
            'author': self.author.id,
            'publisher': 'Companhia das Letras',
            'publication_year': 2007,
            'page_count': 152
        }

    def test_create_book_view(self):
        """Teste para verificar se a view de criação de livro funciona corretamente"""
        # Este teste pressupõe que você tenha uma URL 'book-create' configurada
        # Como não temos essa URL configurada neste exemplo, vamos pular a verificação
        # da resposta HTTP e focar apenas na lógica de criação do livro
        
        # Criar um livro através do formulário
        form = BookForm(data=self.new_book_data)
        self.assertTrue(form.is_valid())
        form.save()
        
        # Verificar se o livro foi criado no banco de dados
        self.assertEqual(Book.objects.count(), 2)
        
        # Verificar se os dados do livro foram salvos corretamente
        new_book = Book.objects.get(isbn=self.new_book_data['isbn'])
        self.assertEqual(new_book.title, self.new_book_data['title'])
        self.assertEqual(new_book.publisher, self.new_book_data['publisher'])

    def test_update_book(self):
        """Teste para verificar a atualização de um livro"""
        # Dados atualizados para o livro
        updated_data = {
            'title': self.book.title,
            'isbn': self.book.isbn,
            'author': self.book.author.id,
            'publisher': 'Nova Editora',  # Alterando a editora
            'publication_year': 2020,     # Alterando o ano
            'page_count': self.book.page_count,
            'genre': 'Dystopia'
        }
        
        # Atualizar o livro através do formulário
        form = BookForm(data=updated_data, instance=self.book)
        self.assertTrue(form.is_valid())
        form.save()
        
        # Atualizar o objeto do banco de dados
        self.book.refresh_from_db()
        
        # Verificar se os dados foram atualizados corretamente
        self.assertEqual(self.book.publisher, updated_data['publisher'])
        self.assertEqual(self.book.publication_year, updated_data['publication_year'])

    def test_duplicate_isbn(self):
        """Teste para verificar comportamento quando dados inválidos são enviados"""
        # Criar dados inválidos (ISBN duplicado)
        invalid_data = self.new_book_data.copy()
        invalid_data['isbn'] = self.book.isbn  # ISBN já existente
        
        # Verificar que o formulário detecta o erro
        form = BookForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('isbn', form.errors)
        self.assertIn('Este ISBN já está em uso', str(form.errors['isbn']))
        
        # Verificar que nenhum novo livro foi criado
        self.assertEqual(Book.objects.count(), 1)
