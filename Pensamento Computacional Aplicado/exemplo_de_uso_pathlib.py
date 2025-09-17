from pathlib import Path

# 1. Define o caminho base do projeto e cria os diretórios necessários
# O método .home() obtém o diretório home do usuário.
# O operador / permite concatenar caminhos de forma intuitiva e segura.
projeto_root = Path.home() / 'projetos' / 'analise_dados_clientes'
dados_dir = projeto_root / 'dados_brutos'

# O método .mkdir(parents=True, exist_ok=True) cria os diretórios pais se não existirem
# e evita erros se o diretório final já existir.
dados_dir.mkdir(parents=True, exist_ok=True)

# 2. Cria alguns arquivos CSV de exemplo para demonstração
(dados_dir / 'vendas_janeiro.csv').write_text("id_venda,produto,valor\n1,Celular,1500\n2,Tablet,800")
(dados_dir / 'subcategoria' / 'vendas_fevereiro.csv').write_text("id_venda,produto,valor\n3,Fone,200\n4,Smartwatch,300")
(dados_dir / 'relatorios' / 'resumo_anual.txt').write_text("Relatório anual de vendas.") # Um arquivo não CSV

print("--- Análise de Arquivos CSV ---")

# 3. Localiza recursivamente todos os arquivos .csv dentro da estrutura do projeto
# O método .rglob('*.csv') retorna um iterador para todos os arquivos .csv
# em qualquer subdiretório, de forma recursiva.
for csv_file_path in dados_dir.rglob('*.csv'):
    # O método .read_text(encoding='utf-8') lê o conteúdo completo do arquivo
    # de forma segura (abrindo e fechando automaticamente), e .splitlines() divide em linhas.
    conteudo_linhas = csv_file_path.read_text(encoding='utf-8').splitlines()
    print(f"Arquivo: {csv_file_path.name}, Caminho: {csv_file_path}, Linhas: {len(conteudo_linhas)}")

# 4. Grava um arquivo de resumo no diretório raiz do projeto
resumo_path = projeto_root / 'relatorio_final.txt'
resumo_path.write_text("Análise de dados de vendas concluída com sucesso!\nTotal de arquivos CSV processados: (implementar contagem real aqui)")

print(f"\nResumo gravado em: {resumo_path}")
