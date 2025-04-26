from django import forms
import datetime
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'author', 'publisher', 'publication_year', 'page_count', 'genre']

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year is None:
            return year
            
        current_year = datetime.datetime.now().year
        
        if year > current_year:
            raise forms.ValidationError('O ano de publicação não pode ser no futuro')
        
        return year
        
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        
        # Verifica se o ISBN tem o comprimento adequado
        if len(isbn) != 10 and len(isbn) != 13:
            raise forms.ValidationError('ISBN deve ter 10 ou 13 caracteres')
            
        # Verificar se o ISBN já existe
        if Book.objects.filter(isbn=isbn).exclude(id=self.instance.id if self.instance.pk else None).exists():
            raise forms.ValidationError('Este ISBN já está em uso.')
            
        return isbn
