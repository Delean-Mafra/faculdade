from django.test import TestCase
from bookapp.forms import BookForm
from bookapp.models import Author, Book

class BookFormTest(TestCase):
    def setUp(self):
        # Configurar autor para uso nos testes
        self.author = Author.objects.create(
            name="J.R.R. Tolkien",
            birth_date="1892-01-03"
        )
        
        # Dados válidos para o formulário
        self.valid_form_data = {
            'title': 'O Senhor dos Anéis',
            'isbn': '9788533613379',
            'author': self.author.id,
            'publisher': 'Martins Fontes',
            'publication_year': 2001,
            'page_count': 1200,
            'genre': 'Fantasy'
        }

    def test_valid_form(self):
        """Teste para verificar se o formulário é válido com dados corretos"""
        form = BookForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        
        # Verificar se não há erros nos campos
        self.assertEqual(len(form.errors), 0)

    def test_form_with_missing_required_fields(self):
        """Teste para verificar erros quando campos obrigatórios não são preenchidos"""
        # Remover título e ISBN que são campos obrigatórios
        invalid_data = self.valid_form_data.copy()
        del invalid_data['title']
        del invalid_data['isbn']
        
        form = BookForm(data=invalid_data)
        
        # Verificar que o formulário é inválido
        self.assertFalse(form.is_valid())
        
        # Verificar que temos erros específicos para os campos obrigatórios
        self.assertIn('title', form.errors)
        self.assertIn('isbn', form.errors)
        
        # Verificar as mensagens de erro
        self.assertEqual(form.errors['title'][0], 'Este campo é obrigatório.')
        self.assertEqual(form.errors['isbn'][0], 'Este campo é obrigatório.')

    def test_form_clean_method(self):
        """Teste para verificar validações personalizadas do formulário"""
        # Criar dados com ano de publicação futuro (inválido)
        invalid_year_data = self.valid_form_data.copy()
        invalid_year_data['publication_year'] = 2030  # Ano futuro
        
        form = BookForm(data=invalid_year_data)
        
        # Assumindo que o formulário tem uma validação para rejeitar anos futuros
        self.assertFalse(form.is_valid())
        self.assertIn('publication_year', form.errors)
        
        # Verificar mensagem de erro específica
        self.assertIn('O ano de publicação não pode ser no futuro', form.errors['publication_year'][0])
