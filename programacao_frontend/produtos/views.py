from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Produto

# View baseada em função
def listar_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    paginator = Paginator(produtos, 10)  # 10 produtos por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'produtos/lista_produtos.html', {'page_obj': page_obj})

# View baseada em classe
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/lista_produtos_class.html'
    context_object_name = 'produtos'
    paginate_by = 10
    ordering = ['nome']
