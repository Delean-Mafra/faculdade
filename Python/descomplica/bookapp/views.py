from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


from .models import Book, Author
from .forms import BookForm

class BookListView(ListView):
    model = Book
    template_name = 'bookapp/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookDetailView(DetailView):
    model = Book
    template_name = 'bookapp/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/book_form.html'
    success_url = reverse_lazy('book-list')
    
    def form_valid(self, form):
        messages.success(self.request, "Livro cadastrado com sucesso!")
        return super().form_valid(form)

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/book_form.html'
    success_url = reverse_lazy('book-list')
    
    def form_valid(self, form):
        messages.success(self.request, "Informações atualizadas com sucesso!")
        return super().form_valid(form)

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'bookapp/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Livro excluído com sucesso!")
        return super().delete(request, *args, **kwargs)

# Buscas simples de autor
class AuthorListView(ListView):
    model = Author
    template_name = 'bookapp/author_list.html'
    context_object_name = 'authors'
