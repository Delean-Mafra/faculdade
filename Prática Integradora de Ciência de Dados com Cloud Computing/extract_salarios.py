# Script para extrair salários do PDF e calcular média.
# Uso: python extract_salarios.py <caminho_para_pdf>
import sys, re, csv, math, statistics
from PyPDF2 import PdfReader

def parse_currency(value_str):
    if value_str is None:
        return None
    s = str(value_str).strip()
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

pdf_path = sys.argv[1] if len(sys.argv) > 1 else "Descomplica.pdf"
reader = PdfReader(pdf_path)
text = "\n".join([p.extract_text() or "" for p in reader.pages])

found = re.findall(r'(R\$[\s]*\d[\d\.\,]*\d|(?<!R\$)\d{1,3}(?:[\.]\d{3})*,\d{2})', text)
salarios = []
for f in found:
    v = parse_currency(f)
    if v is not None:
        salarios.append(v)
salarios = [s for s in salarios if s is not None and not math.isnan(s) and s >= 0.01]
if salarios:
    print("Quantidade de salários encontrados:", len(salarios))
    print("Salários:", salarios)
    print("Média: R$ {:.2f}".format(statistics.mean(salarios)))
else:
    print("Nenhum salário encontrado.")