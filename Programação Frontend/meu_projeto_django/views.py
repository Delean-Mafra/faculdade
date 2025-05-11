from django.shortcuts import render

def contato(request):
    # Se houver um form, corrigindo o problema dos colchetes duplos
    form = {}  # Substitua isso pelo seu formulário real
    return render(request, 'contato.html', {'form': form})  # Corrigido: usamos apenas um conjunto de chaves
