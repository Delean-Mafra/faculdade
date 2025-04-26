from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    page_count = models.IntegerField()
    genre = models.CharField(max_length=50, blank=True, null=True)

    def clean(self):
        # Validação personalizada para ISBN
        if self.isbn and len(self.isbn) != 13 and len(self.isbn) != 10:
            raise ValidationError({'isbn': 'ISBN deve ter 10 ou 13 caracteres'})
            
        # Validação para ano de publicação
        current_year = datetime.datetime.now().year
        if self.publication_year is not None and self.publication_year > current_year:
            raise ValidationError({'publication_year': 'O ano de publicação não pode ser no futuro'})

    def __str__(self):
        return self.title
