#!/usr/bin/env python
"""
Este script corrige o problema do filtro 'add_class' que está faltando no template.
O problema ocorre porque o filtro personalizado foi criado, mas não está registrado em INSTALLED_APPS.
"""
import os

def update_settings_file():
    """Atualiza o arquivo settings.py para incluir bookapp em INSTALLED_APPS corretamente"""
    settings_path = os.path.join('descomplica', 'settings.py')
    
    with open(settings_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Verifica se 'bookapp' já está nas INSTALLED_APPS
    if "'bookapp'" in content and not "'bookapp.apps.BookappConfig'" in content:
        # Substitui 'bookapp' por 'bookapp.apps.BookappConfig'
        content = content.replace("'bookapp'", "'bookapp.apps.BookappConfig'")
        
        with open(settings_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print("✅ INSTALLED_APPS atualizado para usar BookappConfig")
        return True
    elif "'bookapp.apps.BookappConfig'" in content:
        print("✓ BookappConfig já está configurado corretamente.")
        return True
    else:
        print("❌ Não foi possível encontrar a entrada 'bookapp' em INSTALLED_APPS")
        return False

def update_book_form_template():
    """Atualiza o template do formulário para não usar o filtro personalizado add_class"""
    form_path = os.path.join('templates', 'bookapp', 'book_form.html')
    
    with open(form_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Substitui a linha problemática que usa o filtro add_class
    if '{{ field|add_class:"form-control" }}' in content:
        content = content.replace(
            '{{ field|add_class:"form-control" }}', 
            '{{ field }}'
        )
        
        with open(form_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print("✅ Template do formulário atualizado para não usar filtro add_class")
        return True
    else:
        print("❌ Não foi possível encontrar o uso do filtro add_class no template")
        return False

def main():
    print("\n=== Corrigindo problemas de template e filtros ===\n")
    
    settings_updated = update_settings_file()
    form_updated = update_book_form_template()
    
    if settings_updated and form_updated:
        print("\n✅ Correções aplicadas com sucesso!")
        print("\nAgora você pode reiniciar o servidor e o formulário deve funcionar corretamente.")
    else:
        print("\n❌ Algumas correções não puderam ser aplicadas. Verifique os erros acima.")

if __name__ == "__main__":
    main()