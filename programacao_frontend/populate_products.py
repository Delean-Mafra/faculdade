import os
import django
import random
import sys

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto_django.settings')
django.setup()

try:
    from faker import Faker
    from produtos.models import Produto
    
    fake = Faker('pt_BR')
    
    def criar_produtos(quantidade=50):
        print(f"Tentando criar {quantidade} produtos...")
        sucessos = 0
        
        for _ in range(quantidade):
            try:
                nome = fake.word().capitalize() + ' ' + fake.word().capitalize()
                descricao = fake.paragraph(nb_sentences=3)
                preco = round(random.uniform(10, 5000), 2)
                estoque = random.randint(0, 100)
                
                Produto.objects.create(
                    nome=nome,
                    descricao=descricao,
                    preco=preco,
                    estoque=estoque
                )
                sucessos += 1
            except Exception as e:
                print(f"Erro ao criar produto: {e}")
        
        print(f'{sucessos} produtos criados com sucesso!')
    
    if __name__ == '__main__':
        print('Iniciando criação de produtos...')
        print('Verificando se a tabela produtos_produto existe...')
        
        # Verifica se a tabela existe executando uma consulta
        try:
            count = Produto.objects.count()
            print(f"Tabela encontrada! Já existem {count} produtos.")
        except django.db.utils.OperationalError:
            print("Tabela não encontrada! Execute 'python manage.py makemigrations produtos' seguido de 'python manage.py migrate'")
            sys.exit(1)
        
        criar_produtos(50)  # Criar 50 produtos
        print('Processo finalizado!')
except Exception as e:
    print(f"Erro: {e}")
    print("Verifique se as migrações foram aplicadas corretamente.")
