#!/usr/bin/env python
"""
Script para corrigir o erro no modelo Book e executar todos os testes.
"""
import os
import subprocess

# Funções auxiliares
def update_file_content(file_path, search_pattern, replacement):
    """Atualiza o conteúdo de um arquivo substituindo um padrão por um novo texto"""
    if not os.path.exists(file_path):
        print(f"ERRO: O arquivo {file_path} não existe!")
        return False
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if search_pattern not in content:
        print(f"AVISO: O padrão não foi encontrado em {file_path}")
        return False
        
    updated_content = content.replace(search_pattern, replacement)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
        
    print(f"Arquivo atualizado: {file_path}")
    return True

def run_command(command, description):
    """Executa um comando no shell e exibe o resultado"""
    print("\n" + "=" * 80)
    print(f"Executando: {description}")
    print("=" * 80)
    
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    
    if result.stderr:
        print("ERROS:")
        print(result.stderr)
        
    success = result.returncode == 0
    if success:
        print(f"✓ {description} concluído com sucesso.")
    else:
        print(f"✗ {description} falhou com código de saída {result.returncode}.")
        
    return success

def main():
    print("Iniciando correções e testes para o projeto Django...\n")
    
    # 1. Verificar a pasta static
    if not os.path.exists('static'):
        os.makedirs('static')
        print("Pasta 'static' criada.")
    else:
        print("A pasta 'static' já existe.")
    
    # 2. Corrigir o modelo Book - adicionar verificação para None
    book_model_path = os.path.join('bookapp', 'models.py')
    old_validation_code = """    # Validação para ano de publicação
    current_year = datetime.datetime.now().year
    if self.publication_year > current_year:
        raise ValidationError({'publication_year': 'O ano de publicação não pode ser no futuro'})"""
        
    new_validation_code = """    # Validação para ano de publicação
    current_year = datetime.datetime.now().year
    if self.publication_year is not None and self.publication_year > current_year:
        raise ValidationError({'publication_year': 'O ano de publicação não pode ser no futuro'})"""
        
    update_file_content(book_model_path, old_validation_code, new_validation_code)
    
    # 3. Verificar o arquivo forms.py para limpar validação também
    form_path = os.path.join('bookapp', 'forms.py')
    old_form_validation = """    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        current_year = datetime.datetime.now().year
        
        if year > current_year:
            raise forms.ValidationError('O ano de publicação não pode ser no futuro')
        
        return year"""
        
    new_form_validation = """    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year is None:
            return year
            
        current_year = datetime.datetime.now().year
        
        if year > current_year:
            raise forms.ValidationError('O ano de publicação não pode ser no futuro')
        
        return year"""
        
    update_file_content(form_path, old_form_validation, new_form_validation)
    
    # 4. Executar os testes de modelo
    python_path = r"c:/ProgramData/Delean/Python/.venv/Scripts/python.exe"
    run_command([python_path, 'manage.py', 'test', 'bookapp.tests.test_book_model'], 
                "Testes de Modelo")
    
    # 5. Executar os testes de formulário
    run_command([python_path, 'manage.py', 'test', 'bookapp.tests.test_book_form'], 
                "Testes de Formulário")
    
    # 6. Executar os testes de integração
    run_command([python_path, 'manage.py', 'test', 'bookapp.tests.test_book_view_integration'], 
                "Testes de Integração")
    
    # 7. Executar todos os testes
    success = run_command([python_path, 'manage.py', 'test', 'bookapp.tests'], 
                "Todos os testes")
    
    if success:
        print("\n" + "=" * 80)
        print("🎉 SUCESSO! Todos os testes passaram.")
        print("=" * 80)
        print("\nPróximos passos:")
        print("1. Você pode executar o servidor de desenvolvimento com:")
        print(f"   {python_path} manage.py runserver")
        print("\n2. Acesse o admin em:")
        print("   http://127.0.0.1:8000/admin/")
        print("\n3. Acesse o aplicativo em:")
        print("   http://127.0.0.1:8000/books/")
    else:
        print("\n" + "=" * 80)
        print("❌ ATENÇÃO: Alguns testes ainda estão falhando.")
        print("=" * 80)
        print("\nRecomendações para depuração:")
        print("- Verifique os erros específicos nos logs acima")
        print("- Examine os arquivos de modelo, formulário e teste")
        print("- Certifique-se de que todas as dependências estão instaladas")

if __name__ == "__main__":
    main()