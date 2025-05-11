from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('class/', views.ProdutoListView.as_view(), name='listar_produtos_class'),
]
