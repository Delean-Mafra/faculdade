# Sistema de Gerenciamento de Livros - Projeto Descomplica

Este projeto é um sistema de gerenciamento de livros desenvolvido com Django como demonstração para a "Atividade Prática 1 – Teste de Software" da disciplina "Prática Integradora para Dados Inteligentes".

## Visão Geral

O sistema permite gerenciar um catálogo de livros e autores com as seguintes funcionalidades:
- Visualização da lista de livros cadastrados
- Adição de novos livros
- Edição de livros existentes
- Detalhes de cada livro
- Sistema de autenticação para proteger operações

## Tecnologias Utilizadas

- **Backend**: Django 5.2
- **Banco de Dados**: SQLite
- **Frontend**: HTML, CSS (Bootstrap)
- **Autenticação**: Django Authentication System

## Estrutura do Projeto

O projeto segue a estrutura padrão do Django com os seguintes componentes principais:
- **bookapp**: Aplicação principal contendo os modelos, views e templates
- **templates**: Arquivos HTML para a interface de usuário
- **static**: Arquivos estáticos (CSS, JS, imagens)

## Modelos de Dados

O sistema possui dois modelos principais:
1. **Author**: Armazena informações sobre os autores (nome, data de nascimento)
2. **Book**: Armazena informações sobre os livros (título, ISBN, autor, editora, ano de publicação, páginas, gênero)

## Instruções de Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Delean-Mafra/faculdade.git
cd faculdade/Python/descomplica
```

2. Configure o ambiente virtual e instale as dependências:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install django faker pymysql
```

3. Configure o banco de dados e execute as migrações:
```bash
python manage.py migrate
```

4. Execute o script para popular o banco de dados:
```bash
python fix_project.py
```

5. Inicie o servidor:
```bash
python manage.py runserver
```

6. Acesse a aplicação em seu navegador:
```
http://127.0.0.1:8000/
```

## Cenários de Teste

Este projeto foi desenvolvido para demonstrar a implementação de testes de software. Os principais cenários de teste incluem:

1. **Cadastro de um Novo Livro**
   - Verificação da adição de livros com dados válidos
   - Validação de campos obrigatórios
   - Redirecionamento e mensagens de sucesso

2. **Validação de ISBN Duplicado**
   - Verificação da restrição de duplicidade de ISBN
   - Tratamento de erros de validação
   - Manutenção dos dados do formulário após erro

3. **Edição de Livros Existentes**
   - Verificação da atualização correta de dados
   - Manutenção da integridade dos campos não editados
   - Confirmação de alterações bem-sucedidas

## Observações Importantes

- **Dados Fictícios**: Todos os dados presentes neste sistema são fictícios e foram criados apenas para fins de demonstração.
- **Propósito Educacional**: Este projeto foi desenvolvido exclusivamente para fins educacionais como parte da disciplina mencionada.
- **Não para Produção**: Este sistema não está otimizado para uso em ambiente de produção e pode conter simplificações para facilitar a compreensão didática.

## Direitos Autorais

© 2025 Delean Mafra. Todos os direitos reservados.

Este projeto e todo seu código-fonte, documentação, design e conceitos associados constituem propriedade intelectual de Delean Mafra. O conteúdo deste repositório é disponibilizado exclusivamente para fins educacionais e de avaliação acadêmica no contexto da disciplina "Prática Integradora para Dados Inteligentes".

A redistribuição, reprodução, modificação ou utilização não autorizada deste material para fins comerciais ou não educacionais é expressamente proibida sem permissão prévia por escrito do autor. O uso deste código como referência deve incluir atribuição apropriada ao autor original.

---

Desenvolvido por: Delean Mafra  
Data: Abril de 2025  
Curso: Ciência de Dados
Instituição: Faculdade Descomplica
