from django.test import TestCase
from django.core.exceptions import ValidationError
from bookapp.models import Book, Author

class BookModelTest(TestCase):
    def setUp(self):
        # Configuração inicial para cada teste
        self.author = Author.objects.create(
            name="Douglas Adams",
            birth_date="1952-03-11"
        )
        
        self.book_data = {
            'title': 'O Guia do Mochileiro das Galáxias',
            'isbn': '9788576572145',
            'publisher': 'Arqueiro',
            'publication_year': 2010,
            'page_count': 208
        }

    def test_create_book_with_valid_data(self):
        """Teste para verificar se um livro é criado com dados válidos"""
        # Criar um novo livro
        book = Book.objects.create(author=self.author, **self.book_data)
        
        # Verificar se o livro foi salvo no banco de dados
        self.assertEqual(Book.objects.count(), 1)
        
        # Verificar se os campos foram salvos corretamente
        saved_book = Book.objects.first()
        self.assertEqual(saved_book.title, self.book_data['title'])
        self.assertEqual(saved_book.isbn, self.book_data['isbn'])
        self.assertEqual(saved_book.publisher, self.book_data['publisher'])
        self.assertEqual(saved_book.publication_year, self.book_data['publication_year'])
        self.assertEqual(saved_book.page_count, self.book_data['page_count'])
        
        # Verificar relacionamento com o autor
        self.assertEqual(saved_book.author, self.author)

    def test_book_with_invalid_isbn(self):
        """Teste para verificar se um erro é lançado quando o ISBN é inválido"""
        # Tentar criar um livro com ISBN inválido (muito curto)
        with self.assertRaises(ValidationError):
            book = Book(
                author=self.author,
                title=self.book_data['title'],
                isbn='12345',  # ISBN inválido
                publisher=self.book_data['publisher'],
                publication_year=self.book_data['publication_year'],
                page_count=self.book_data['page_count']
            )
            # Validação explícita para acionar o ValidationError
            book.full_clean()

    def test_unique_isbn_constraint(self):
        """Teste para verificar se não é possível criar dois livros com o mesmo ISBN"""
        # Criar o primeiro livro
        Book.objects.create(author=self.author, **self.book_data)
        
        # Tentar criar um segundo livro com o mesmo ISBN
        duplicate_book = Book(
            author=self.author,
            title="Outro Livro",
            isbn=self.book_data['isbn'],  # mesmo ISBN
            publisher="Outra Editora",
            publication_year=2020,
            page_count=300
        )
        
        # Verificar se um erro é lançado ao tentar salvar
        with self.assertRaises(Exception):  # Poderia ser mais específico com IntegrityError
            duplicate_book.save()
