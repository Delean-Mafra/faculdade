def fix_model_file():
    """Corrige o arquivo models.py manualmente"""
    model_path = 'bookapp/models.py'
    
    try:
        # Ler o conteúdo atual do arquivo
        with open(model_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
        
        # Procurar a linha com o erro e corrigi-la
        for i, line in enumerate(content):
            if 'if self.publication_year >' in line:
                content[i] = '        if self.publication_year is not None and self.publication_year > current_year:\n'
                print(f"Linha {i+1} corrigida no arquivo models.py")
                break
        else:
            print("Não foi possível encontrar a linha para correção no arquivo models.py")
            print("Substituindo o arquivo models.py completamente...")
            
            # Se não encontrar a linha específica, substitui todo o arquivo
            content = """from django.db import models
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
"""
            with open(model_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
            
        # Escrever o conteúdo corrigido de volta para o arquivo
        with open(model_path, 'w', encoding='utf-8') as file:
            file.writelines(content)
            
        print(f"✓ Arquivo {model_path} corrigido com sucesso.")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao corrigir o arquivo {model_path}: {str(e)}")
        return False

if __name__ == "__main__":
    success = fix_model_file()
    if success:
        print("\nAgora execute os testes novamente com:")
        print("& c:/ProgramData/Delean/Python/.venv/Scripts/python.exe manage.py test bookapp.tests")
    else:
        print("\nOcorreu um erro ao corrigir o arquivo models.py.")
        print("Por favor, edite o arquivo manualmente para adicionar a verificação:")
        print("if self.publication_year is not None and self.publication_year > current_year:")