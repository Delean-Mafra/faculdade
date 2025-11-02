import re
import sys
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PyPDF2 import PdfReader
import re
import statistics
import math
import csv
import os
from textwrap import dedent

# Código exemplo
caminho_arquivo = "familia.csv"
df = pd.read_csv(caminho_arquivo)
print(df.head())
salarios_por_profissao = df.groupby("Profissão")["Salário"].mean()
plt.figure(figsize=(10, 6))
salarios_por_profissao.plot(kind="bar", color="skyblue")
plt.title("Salário médio por profissão")
plt.xlabel("Profissão")
plt.ylabel("Salário")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
media = df["Salário"].mean()
mediana = df["Salário"].median()
desvio = df["Salário"].std()
minimo = df["Salário"].min()
maximo = df["Salário"].max()
print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio)
print("Mínimo:", minimo)
print("Máximo:", maximo)
plt.hist(df["Salário"], bins=10, color="lightgreen", edgecolor="black")
plt.title("Distribuição dos salários")
plt.xlabel("Salário")
plt.ylabel("Frequência")
plt.show()
salario_escolaridade = df.groupby("Escolaridade")["Salário"].mean()
plt.figure(figsize=(10, 6))
salario_escolaridade.plot(kind="bar", color="orange")
plt.title("Salário médio por escolaridade")
plt.xlabel("Escolaridade")
plt.ylabel("Salário médio")
plt.xticks(rotation=45)
plt.show()
correlacao = df["Idade"].corr(df["Salário"])
print("Correlação entre idade e salário:", correlacao)
distribuicao_cidade = df["Local de Nascimento"].value_counts()
plt.pie(distribuicao_cidade, labels=distribuicao_cidade.index, autopct="%1.1f%%")
plt.title("Distribuição por cidade de nascimento")
plt.show()
profissoes = df["Profissão"].value_counts()
plt.pie(profissoes, labels=profissoes.index, autopct="%1.1f%%")
plt.title("Distribuição de profissões na família")
plt.show()
df = pd.read_csv("familia.csv")
sem_segundo_nome = df["Segundo Nome"].isna().sum()
print("Membros sem segundo nome:", sem_segundo_nome)
df.groupby("Profissão")["Salário"].mean().plot(kind="bar", color="cornflowerblue")
plt.title("Salário médio por profissão")
plt.xlabel("Profissão")
plt.ylabel("Salário")
plt.show()
qtd_estudantes = df[df["Profissão"].str.contains("Estudante", case=False)].shape[0]
print("Quantidade de estudantes:", qtd_estudantes)
print(df)
estudantes_medio = df[df["Escolaridade"].str.contains("Médio", case=False)].shape[0]
print("Estudantes do ensino médio:", estudantes_medio)
nao_sp = df[df["Local de Nascimento"] != "São Paulo"].shape[0]
print("Membros que não são de São Paulo:", nao_sp)
df = pd.read_csv("familia.csv") 
def parse_salary(x):
    if pd.isna(x): 
        return np.nan
    s = str(x).replace("R$", "").replace("$", "").replace(" ", "")
    s = s.replace(".", "").replace(",", ".") 
    try:
        return float(s)
    except:
        return np.nan
df["Salário_num"] = df["Salário"].apply(parse_salary)
media = df["Salário_num"].mean()
print(f"Média dos salários: {media:.2f}")
media_salarios = df['Salário'].mean()
print(f"Média dos salários da família: R$ {media_salarios:.2f}")

# FIM DO CÓDIGO EXEMPLO


# ALTERNATIVA 4 DA AULA 9
correlacao_idade_salario = df['Idade'].corr(df['Salário'])
print(f"Correlação entre a idade e o salário: {correlacao_idade_salario:.2f}")
# Selecionando as variáveis
X = df[["Idade"]]   # variável independente (idade)
y = df["Salário"]   # variável dependente (salário)
# Criando e treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)
# Fazendo previsões
y_pred = modelo.predict(X)
# Calculando o coeficiente de correlação de Pearson
correlacao = df["Idade"].corr(df["Salário"])
print(f"Coeficiente de correlação (Pearson): {correlacao:.4f}")
# Exibindo a equação da reta
print(f"Equação da regressão: Salário = {modelo.coef_[0]:.2f} * Idade + {modelo.intercept_:.2f}")
# Criando o gráfico de dispersão com linha de regressão
plt.figure(figsize=(8,6))
plt.scatter(X, y, color="teal", edgecolors="black", s=100, alpha=0.7, label="Dados reais")
plt.plot(X, y_pred, color="red", linewidth=2, label="Linha de regressão")
plt.title(f"Idade vs Salário\nCorrelação: {correlacao:.2f}", fontsize=14, fontweight="bold")
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
# Retorno:
# Correlação entre a idade e o salário: 0.99
# Coeficiente de correlação (Pearson): 0.9898
# Equação da regressão: Salário = 80.77 * Idade + -224.17




# ALTERNATIVA 5 DA AULA 9
df = pd.read_csv(caminho_arquivo)
# Contando a frequência de cada nível de escolaridade
escolaridade_counts = df['Escolaridade'].value_counts()
# Exibindo os valores no console
print("Distribuição dos níveis de escolaridade:")
print(escolaridade_counts)
# Criando o gráfico de barras
plt.figure(figsize=(8, 6))
escolaridade_counts.plot(kind='bar', color='mediumseagreen')
plt.title('Distribuição dos Níveis de Escolaridade na Família', fontsize=14, fontweight='bold')
plt.xlabel('Escolaridade', fontsize=12)
plt.ylabel('Número de Membros', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()
# Exemplo do professor(Não disponibilizado no codigo exemplo)
nivel_escolaridade_predominante = df['Escolaridade'].mode().values[0]
print(f"Nível de escolaridade predominante: {nivel_escolaridade_predominante}")





# ALTERNATIVA 6 DA AULA 9

# Codigo do professor

Q1 = df['Salário'].quantile(0.25)


Q3 = df['Salário'].quantile(0.75)


IQR = Q3 - Q1


outliers = df[(df['Salário'] < Q1 - 1.5 * IQR) | (df['Salário'] > Q3 + 1.5 * IQR)]


if not outliers.empty:


    print("Sim, há outliers nos salários da família.")


else:


    print("Não, não há outliers nos salários da família.")

# Não, não há outliers nos salários da família.



# Meu propio codigo

# Cálculo dos quartis e do IQR
q1 = df['Salário'].quantile(0.25)
q3 = df['Salário'].quantile(0.75)
iqr = q3 - q1


# Definindo limites para outliers
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr


print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Limite inferior: {limite_inferior}")
print(f"Limite superior: {limite_superior}")


# Verificando se há outliers
outliers = df[(df['Salário'] < limite_inferior) | (df['Salário'] > limite_superior)]
if outliers.empty:
    print("Não há outliers nos salários da família.")
else:
    print("Há outliers nos salários da família:")
    print(outliers)


# Criando o boxplot
plt.figure(figsize=(6, 8))
plt.boxplot(df['Salário'], vert=True, patch_artist=True, boxprops=dict(facecolor="skyblue"))
plt.title("Boxplot dos Salários da Família")
plt.ylabel("Salário")
plt.grid(axis='y', alpha=0.3)
plt.show()

# Q1: 1875.0
# Q3: 3275.0
# IQR: 1400.0
# Limite inferior: -225.0
# Limite superior: 5375.0
# Não há outliers nos salários da família.



# Praticas durante a aula - arquivos CSV e gráficos

df = pd.read_csv('resultados_processados.csv')

print(df.head())
plt.bar(df['NivelPagamento'], df['ID_Amostra'])

plt.xlabel('AnoEntrada')
plt.ylabel('AnoEntrada')
plt.xticks(rotation=45, ha='right')

plt.show()

#import plotly.express as px

dados = pd.read_csv('resultados_processados.csv')

#fig = px.bar(dados, x='NivelPagamento', y='ID_Amostra', title='Gráfico de Barras')

#fig.show()

dados = pd.read_csv('resultados_processados.csv')

plt.scatter(dados['NivelPagamento'], dados['ID_Amostra'])
plt.ylabel('ID_Amostra', color = 'red')
plt.xlabel('NivelPagamento', color = 'blue')
plt.title('Gráfico de Dispersão', color = 'green')
modelo = LinearRegression()
x = dados['NivelPagamento'].values.reshape(-1, 1)
y = dados['ID_Amostra'].values
modelo.fit(x, y)
plt.plot(x, modelo.predict(x), color = 'yellow', linewidth=2)

plt.show()








# Outros codigos testados

def parse_salary(x):
    # recebe valores como 'R$ 1.234,56', '1234,56', '$1234.56', '1.234' etc.
    if pd.isna(x):
        return np.nan
    s = str(x).strip()
    s = re.sub(r'[Rr]\$\s*', '', s)   # remove R$
    s = s.replace('$', '')
    s = s.replace(' ', '')
    # se houver padrão de milhar com ponto e decimal com vírgula: 1.234,56 -> 1234.56
    if re.search(r'^\d{1,3}(?:\.\d{3})+,\d{1,}$', s):
        s = s.replace('.', '').replace(',', '.')
    # se houver vírgula decimal (sem pontos de milhar): 1234,56 -> 1234.56
    elif re.search(r'^\d+,\d+$', s):
        s = s.replace(',', '.')
    # remover quaisquer caracteres não-numéricos exceto ponto e sinal
    s = re.sub(r'[^0-9\.-]', '', s)
    try:
        return float(s) if s not in ("", ".", "-") else np.nan
    except:
        return np.nan

# ler CSV
try:
    df = pd.read_csv(caminho_arquivo)
except Exception as e:
    print("Erro ao ler arquivo:", e)
    sys.exit(1)

# garantir coluna 'Salário' (aceita variantes)
col_sal = None
for candidate in ["Salário", "Salario", "salario", "salário", "SALÁRIO"]:
    if candidate in df.columns:
        col_sal = candidate
        break

if col_sal is None:
    # tentar inferir última coluna como salário (fallback)
    col_sal = df.columns[-1]
    print(f"A coluna de salário não foi encontrada explicitamente. Usando '{col_sal}' como candidata.")

# criar coluna numérica
df["Salario_num"] = df[col_sal].apply(parse_salary)

# remover NaNs para análise
salarios = df["Salario_num"].dropna().astype(float)

if salarios.empty:
    print("Nenhum salário numérico encontrado para análise.")
    sys.exit(0)

# estatísticas básicas
media = salarios.mean()
mediana = salarios.median()
std = salarios.std(ddof=0)   # desvio populacional
minimo = salarios.min()
maximo = salarios.max()
q1 = salarios.quantile(0.25)
q3 = salarios.quantile(0.75)
iqr = q3 - q1

print(f"Count: {len(salarios)}")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio padrão (pop): {std:.2f}")
print(f"Min: {minimo:.2f}  Max: {maximo:.2f}")
print(f"Q1: {q1:.2f}  Q3: {q3:.2f}  IQR: {iqr:.2f}")

# método z-score (thresholds comuns: 2 e 3)
z_scores = (salarios - media) / std
outliers_z2 = salarios[ z_scores.abs() > 2 ]
outliers_z3 = salarios[ z_scores.abs() > 3 ]

print(f"\nOutliers por z-score (|z|>2): {len(outliers_z2)} -> {list(outliers_z2.values)}")
print(f"Outliers por z-score (|z|>3): {len(outliers_z3)} -> {list(outliers_z3.values)}")

# método IQR
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers_iqr = salarios[(salarios < lower) | (salarios > upper)]
print(f"\nIQR lower bound: {lower:.2f}, upper bound: {upper:.2f}")
print(f"Outliers por IQR: {len(outliers_iqr)} -> {list(outliers_iqr.values)}")

# marcar no DataFrame para fácil inspeção
df["is_outlier_z2"] = df["Salario_num"].apply(lambda v: False if pd.isna(v) else abs((v - media) / std) > 2)
df["is_outlier_iqr"] = df["Salario_num"].apply(lambda v: False if pd.isna(v) else (v < lower or v > upper))

# mostrar linhas marcadas como outlier (se houver)
if df["is_outlier_z2"].any() or df["is_outlier_iqr"].any():
    print("\nLinhas marcadas como outlier (exibindo colunas principais):")
    cols_to_show = [c for c in ["Nome","Segundo Nome","Idade","Profissão","Escolaridade","Local de Nascimento", col_sal, "Salario_num","is_outlier_z2","is_outlier_iqr"] if c in df.columns or c in ["Salario_num","is_outlier_z2","is_outlier_iqr"]]
    print(df.loc[df["is_outlier_z2"] | df["is_outlier_iqr"], cols_to_show].to_string(index=False))
else:
    print("\nNenhum outlier detectado pelos métodos (z-score |z|>2 nem IQR).")

# gerar gráficos (histograma e boxplot) para inspeção visual
plt.figure(figsize=(8,4))
plt.hist(salarios, bins=10)
plt.title("Histograma dos salários")
plt.xlabel("Salário")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
plt.boxplot(salarios, vert=False)
plt.title("Boxplot dos salários")
plt.tight_layout()
plt.show()












# Substitua o caminho pelo local do seu arquivo CSV
caminho_arquivo = "familia.csv"
df = pd.read_csv(caminho_arquivo)

# Exibindo as 5 primeiras linhas
print(df.head())

salarios_por_profissao = df.groupby("Profissão")["Salário"].mean()

plt.figure(figsize=(10, 6))
salarios_por_profissao.plot(kind="bar", color="skyblue")
plt.title("Salário médio por profissão")
plt.xlabel("Profissão")
plt.ylabel("Salário")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

media = df["Salário"].mean()
mediana = df["Salário"].median()
desvio = df["Salário"].std()
minimo = df["Salário"].min()
maximo = df["Salário"].max()

print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio)
print("Mínimo:", minimo)
print("Máximo:", maximo)

plt.hist(df["Salário"], bins=10, color="lightgreen", edgecolor="black")
plt.title("Distribuição dos salários")
plt.xlabel("Salário")
plt.ylabel("Frequência")
plt.show()


salario_escolaridade = df.groupby("Escolaridade")["Salário"].mean()

plt.figure(figsize=(10, 6))
salario_escolaridade.plot(kind="bar", color="orange")
plt.title("Salário médio por escolaridade")
plt.xlabel("Escolaridade")
plt.ylabel("Salário médio")
plt.xticks(rotation=45)
plt.show()

correlacao = df["Idade"].corr(df["Salário"])
print("Correlação entre idade e salário:", correlacao)


distribuicao_cidade = df["Local de Nascimento"].value_counts()

plt.pie(distribuicao_cidade, labels=distribuicao_cidade.index, autopct="%1.1f%%")
plt.title("Distribuição por cidade de nascimento")
plt.show()


profissoes = df["Profissão"].value_counts()

plt.pie(profissoes, labels=profissoes.index, autopct="%1.1f%%")
plt.title("Distribuição de profissões na família")
plt.show()


















pdf_path = "Descomplica.pdf"
script_path = "extract_salarios.py"
csv_out_path = "familia_extracted.csv"

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    texts = []
    for page in reader.pages:
        texts.append(page.extract_text() or "")
    return "\n".join(texts)

def parse_currency(value_str):
    if value_str is None:
        return None
    s = str(value_str).strip()
    s = re.sub(r'[Rr]\$\s*', '', s)
    s = s.replace(" ", "")
    # transformar 1.234,56 -> 1234.56
    if re.search(r'\d+\.\d{3}(?:,\d+)?', s):
        s = s.replace('.', '').replace(',', '.')
    elif re.search(r'\d+,\d{1,2}$', s):
        s = s.replace(',', '.')
    s = re.sub(r'[^0-9\.-]', '', s)
    try:
        return float(s)
    except:
        return None

# Extrair texto e tentar localizar bloco CSV com cabeçalho
text = extract_text_from_pdf(pdf_path)
lines = text.splitlines()

header_idx = None
for i, line in enumerate(lines):
    if re.search(r'\bNome\b', line, re.IGNORECASE) and re.search(r'\bSal', line, re.IGNORECASE):
        header_idx = i
        break

rows = []
if header_idx is not None:
    # assumir que as próximas linhas contêm os dados (até 200 linhas)
    header_line = lines[header_idx].strip()
    # tentar normalizar separadores: vírgula ou múltiplos espaços
    for line in lines[header_idx+1: header_idx+200]:
        if not line.strip():
            continue
        # split by comma first
        if ',' in line:
            parts = [p.strip() for p in line.split(',')]
        else:
            # fallback: split by 2+ espaços
            parts = [p.strip() for p in re.split(r'\s{2,}', line) if p.strip()]
        if len(parts) >= 2:
            rows.append(parts)
# Se não encontrou por cabeçalho, tentar extrair linhas que contenham padrões de salário na página inteira
if not rows:
    potential_lines = []
    for line in lines:
        if re.search(r'(R\$|\d{1,3}(?:[\.\d]{0,})?,\d{2})', line):
            potential_lines.append(line)
    for line in potential_lines:
        # tentar separar por vírgula ou ponto e vírgula
        if ',' in line:
            parts = [p.strip() for p in line.split(',')]
        else:
            parts = [p.strip() for p in re.split(r'\s{2,}', line) if p.strip()]
        if len(parts) >= 2:
            rows.append(parts)

# Tentar normalizar e montar CSV com colunas: Nome, Segundo Nome, Idade, Profissão, Escolaridade, Local de Nascimento, Salário
# Se não houver todos os campos, iremos colocar em colunas conforme disponível e garantir que última coluna seja Salário quando possível.
normalized = []
for parts in rows:
    # Garantir ao menos 2 colunas
    if len(parts) < 2:
        continue
    # tentar identificar o campo salário como o último token que contenha número e vírgula/ponto
    salary_val = None
    for i in range(len(parts)-1, -1, -1):
        if re.search(r'(R\$|\d{1,3}(?:[\.\d]{0,})?,\d{2}|\d+\.\d{2})', parts[i]):
            salary_val = parts[i]
            last_idx = i
            break
    if salary_val is not None:
        # tudo antes do last_idx -> outros campos (tentativa)
        others = parts[:last_idx]
        # preenchar para 6 colunas de meta
        while len(others) < 6:
            others.append("")
        row = others[:6] + [salary_val]
        normalized.append(row)
    else:
        # fallback: colocar tudo como campos e última coluna como salário candidata (mesmo que não seja)
        while len(parts) < 7:
            parts.append("")
        normalized.append(parts[:7])

# Se ainda vazio, tentar extrair salários puros para cálculo
salarios = []
for row in normalized:
    sal_raw = row[-1]
    val = parse_currency(sal_raw)
    if val is not None:
        salarios.append(val)

# Se normalized vazio, tentar extrair apenas valores numéricos no texto
if not normalized:
    found = re.findall(r'(R\$[\s]*\d[\d\.\,]*\d|(?<!R\$)\d{1,3}(?:[\.\d]{0,})?,\d{2})', text)
    for f in found:
        v = parse_currency(f)
        if v is not None:
            salarios.append(v)

# Salvar CSV normalizado (se houver) e também calcular média
if normalized:
    header = ["Nome","Segundo Nome","Idade","Profissão","Escolaridade","Local de Nascimento","Salário"]
    with open(csv_out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in normalized:
            writer.writerow(row)
elif salarios:
    # escrever um CSV simples contendo apenas um campo Salário
    header = ["Salário"]
    with open(csv_out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for s in salarios:
            writer.writerow([f"{s:.2f}"])
# Calcular média dos salários extraídos
salarios = [s for s in salarios if s is not None and not math.isnan(s) and s >= 0.01]
media = statistics.mean(salarios) if salarios else None

# Criar o script .py que pode ser executado no VS Code
script_content = dedent(f'''
    # Script para extrair salários do PDF e calcular média.
    # Uso: python extract_salarios.py <caminho_para_pdf>
    import sys, re, csv, math, statistics
    from PyPDF2 import PdfReader

    def parse_currency(value_str):
        if value_str is None:
            return None
        s = str(value_str).strip()
        s = re.sub(r'[Rr]\\$\\s*', '', s)
        s = s.replace(" ", "")
        if re.search(r'\\d+\\.\\d{{3}}(?:,\\d+)?', s):
            s = s.replace('.', '').replace(',', '.')
        elif re.search(r'\\d+,\\d{{1,2}}$', s):
            s = s.replace(',', '.')
        s = re.sub(r'[^0-9\\.-]', '', s)
        try:
            return float(s)
        except:
            return None

    pdf_path = sys.argv[1] if len(sys.argv) > 1 else "{pdf_path}"
    reader = PdfReader(pdf_path)
    text = "\\n".join([p.extract_text() or "" for p in reader.pages])

    found = re.findall(r'(R\\$[\\s]*\\d[\\d\\.\\,]*\\d|(?<!R\\$)\\d{{1,3}}(?:[\\.]\\d{{3}})*,\\d{{2}})', text)
    salarios = []
    for f in found:
        v = parse_currency(f)
        if v is not None:
            salarios.append(v)
    salarios = [s for s in salarios if s is not None and not math.isnan(s) and s >= 0.01]
    if salarios:
        print("Quantidade de salários encontrados:", len(salarios))
        print("Salários:", salarios)
        print("Média: R$ {{:.2f}}".format(statistics.mean(salarios)))
    else:
        print("Nenhum salário encontrado.")
''').strip()

with open(script_path, "w", encoding="utf-8") as f:
    f.write(script_content)

# Preparar saída para o usuário: conteúdo do CSV extraído (se existir) e links para downloads
csv_content = ""
if os.path.exists(csv_out_path):
    with open(csv_out_path, "r", encoding="utf-8") as f:
        csv_content = f.read()

output = {
    "script_file": script_path,
    "csv_file": csv_out_path if os.path.exists(csv_out_path) else None,
    "media": media,
    "count_salarios": len(salarios),
    "csv_content": csv_content
}

output

# Usar PyPDF2 (disponível) para extrair texto e então procurar os salários.
from PyPDF2 import PdfReader
import re
import statistics
import math

pdf_path = "Descomplica.pdf"

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    texts = []
    for page in reader.pages:
        try:
            texts.append(page.extract_text() or "")
        except Exception as e:
            texts.append("")
    return "\n".join(texts)

def parse_currency(value_str):
    if value_str is None:
        return None
    s = value_str.strip()
    s = re.sub(r'[Rr]\$\s*', '', s)
    s = s.replace(" ", "")
    if re.search(r'\d+\.\d{3}(?:,\d+)?', s):
        s = s.replace('.', '').replace(',', '.')
    elif re.search(r'\d+,\d{1,2}$', s):
        s = s.replace(',', '.')
    s = re.sub(r'[^0-9\.-]', '', s)
    try:
        return float(s)
    except:
        return None

text = extract_text_from_pdf(pdf_path)

# tentar localizar cabeçalho CSV
salarios = []
lines = text.splitlines()
header_idx = None
for i, line in enumerate(lines):
    if re.search(r'\bNome\b', line, re.IGNORECASE) and re.search(r'\bSal', line, re.IGNORECASE):
        header_idx = i
        break

if header_idx is not None:
    for line in lines[header_idx+1: header_idx+200]:
        if not line.strip() or len(line.strip()) < 5:
            continue
        m = re.search(r'(R\$|\$)\s*\d[\d\.,]*', line)
        if m:
            val = parse_currency(m.group(0))
            if val is not None:
                salarios.append(val)
                continue
        parts = [p.strip() for p in re.split(r'[;,]', line) if p.strip()]
        if len(parts) >= 2:
            candidate = parts[-1]
            val = parse_currency(candidate)
            if val is not None:
                salarios.append(val)
                continue
        m2 = re.findall(r'\d{1,3}(?:[\.\d]{0,})?(?:,\d{2})', line)
        for tok in m2:
            val = parse_currency(tok)
            if val is not None:
                salarios.append(val)

if not salarios:
    pattern = re.compile(r'(R\$[\s]*\d[\d\.\,]*\d|(?<!R\$)[\d]{1,3}(?:[\.\d]{0,})?,\d{2})')
    matches = pattern.findall(text)
    for m in matches:
        val = parse_currency(m)
        if val is not None:
            salarios.append(val)

salarios = [s for s in salarios if s is not None and not math.isnan(s)]
salarios = [s for s in salarios if s >= 0.01]

if salarios:
    media = statistics.mean(salarios)
    resultado = {
        "media": media,
        "count": len(salarios),
        "salarios_extraidos": salarios[:50]
    }
else:
    resultado = {
        "media": None,
        "count": 0,
        "salarios_extraidos": []
    }

resultado

def parse_salary(x):
    if pd.isna(x): 
        return np.nan
    s = str(x).replace("R$", "").replace("$", "").replace(" ", "")
    s = s.replace(".", "").replace(",", ".")  # transforma "1.234,56" -> "1234.56"
    try:
        return float(s)
    except:
        return np.nan

df["Salário_num"] = df["Salário"].apply(parse_salary)
media = df["Salário_num"].mean()
print(f"Média dos salários: {media:.2f}")




sem_segundo_nome = df["Segundo Nome"].isna().sum()
print("Membros sem segundo nome:", sem_segundo_nome)

df.groupby("Profissão")["Salário"].mean().plot(kind="bar", color="cornflowerblue")
plt.title("Salário médio por profissão")
plt.xlabel("Profissão")
plt.ylabel("Salário")
plt.show()


qtd_estudantes = df[df["Profissão"].str.contains("Estudante", case=False)].shape[0]
print("Quantidade de estudantes:", qtd_estudantes)

print(df)

estudantes_medio = df[df["Escolaridade"].str.contains("Médio", case=False)].shape[0]
print("Estudantes do ensino médio:", estudantes_medio)

nao_sp = df[df["Local de Nascimento"] != "São Paulo"].shape[0]
print("Membros que não são de São Paulo:", nao_sp)


