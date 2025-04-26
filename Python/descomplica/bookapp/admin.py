from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_year', 'isbn')
    search_fields = ('title', 'isbn')
    list_filter = ('publication_year', 'publisher')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
