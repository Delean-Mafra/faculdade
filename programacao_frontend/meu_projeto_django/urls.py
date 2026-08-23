from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    # Redireciona a URL raiz para /produtos/
    path('', RedirectView.as_view(url='/produtos/', permanent=True)),
]
