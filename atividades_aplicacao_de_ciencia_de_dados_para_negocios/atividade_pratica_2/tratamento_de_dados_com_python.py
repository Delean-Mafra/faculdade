import base64
from datetime import datetime
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template_string


ARQUIVO_ENTRADA = "livros_books_toscrape.csv"
ARQUIVO_SAIDA = "livros_books_toscrape_limpos.csv"
SEPARADOR = "|"
PRECO_MINIMO = 30


HTML_TEMPLATE = """
<!doctype html>
<html lang="pt-br">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Analise de Produtos - Books to Scrape</title>
	<style>
		:root {
			--bg: #f4f8ff;
			--card: #ffffff;
			--ink: #102a43;
			--accent: #0b7285;
			--accent-soft: #dff5fa;
			--ok: #2f9e44;
			--line: #d9e2ec;
		}
		* { box-sizing: border-box; }
		body {
			margin: 0;
			font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
			color: var(--ink);
			background:
				radial-gradient(circle at 10% 10%, #cce3ff 0%, transparent 36%),
				radial-gradient(circle at 90% 20%, #b9fbc0 0%, transparent 28%),
				var(--bg);
		}
		.container {
			max-width: 1200px;
			margin: 0 auto;
			padding: 24px;
		}
		h1 {
			margin: 0 0 8px;
			font-size: 2rem;
		}
		.subtitle {
			margin: 0 0 22px;
			opacity: 0.85;
		}
		.grid {
			display: grid;
			gap: 14px;
			grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
			margin-bottom: 18px;
		}
		.card {
			background: var(--card);
			border: 1px solid var(--line);
			border-radius: 14px;
			padding: 14px;
			box-shadow: 0 8px 20px rgba(16, 42, 67, 0.08);
		}
		.label {
			font-size: 0.84rem;
			opacity: 0.78;
			margin-bottom: 6px;
		}
		.value {
			font-size: 1.35rem;
			font-weight: 700;
			color: var(--accent);
		}
		.block-title {
			margin: 20px 0 10px;
			font-size: 1.2rem;
		}
		.big-card {
			background: var(--card);
			border: 1px solid var(--line);
			border-radius: 14px;
			padding: 16px;
			box-shadow: 0 8px 20px rgba(16, 42, 67, 0.08);
			overflow-x: auto;
		}
		img {
			width: 100%;
			height: auto;
			border-radius: 10px;
			border: 1px solid var(--line);
		}
		table {
			border-collapse: collapse;
			width: 100%;
			font-size: 0.9rem;
		}
		th, td {
			border: 1px solid var(--line);
			padding: 8px;
			text-align: left;
		}
		th {
			background: var(--accent-soft);
		}
		.highlight {
			background: #f1f8e9;
			border-left: 4px solid var(--ok);
			padding: 10px;
			border-radius: 8px;
			margin-bottom: 12px;
		}
	</style>
</head>
<body>
	<div class="container">
		<h1>Analise de Tratamento de Dados</h1>
		<p class="subtitle">Resultado gerado com pandas, matplotlib e Flask em um unico arquivo Python.</p>

		<div class="grid">
			<div class="card">
				<div class="label">Total de registros analisados</div>
				<div class="value">{{ total_registros }}</div>
			</div>
			<div class="card">
				<div class="label">Preco medio</div>
				<div class="value">{{ preco_medio }}</div>
			</div>
			<div class="card">
				<div class="label">Preco mediano</div>
				<div class="value">{{ preco_mediano }}</div>
			</div>
			<div class="card">
				<div class="label">Preco que mais se repete (moda)</div>
				<div class="value">{{ preco_moda }}</div>
			</div>
		</div>

		<div class="big-card">
			<div class="highlight"><strong>Produto mais caro:</strong> {{ produto_mais_caro }}</div>
			<div class="highlight"><strong>Produto mais barato:</strong> {{ produto_mais_barato }}</div>
		</div>

		<h2 class="block-title">Distribuicao de Precos</h2>
		<div class="big-card">
			<img src="data:image/png;base64,{{ grafico_base64 }}" alt="Grafico de distribuicao de precos">
		</div>

		<h2 class="block-title">Amostra de Dados Tratados</h2>
		<div class="big-card">{{ tabela_html|safe }}</div>
	</div>
</body>
</html>
"""


def tratar_dados(caminho_entrada: str, caminho_saida: str) -> pd.DataFrame:
	"""Carrega, limpa, transforma e salva os dados tratados."""
	dados = pd.read_csv(caminho_entrada, sep=SEPARADOR)

	if "preco" in dados.columns:
		dados["preco"] = pd.to_numeric(dados["preco"], errors="coerce").fillna(0)

	if "preco_texto" in dados.columns:
		dados["preco_texto"] = dados["preco_texto"].fillna("").astype(str)

	dados = dados.drop_duplicates()

	if "data" in dados.columns:
		dados["data"] = pd.to_datetime(dados["data"], errors="coerce").dt.strftime("%Y-%m-%d")

	if "preco" in dados.columns:
		dados = dados[dados["preco"] > PRECO_MINIMO]

	if "disponibilidade" in dados.columns:
		dados = dados[dados["disponibilidade"].str.contains("In stock", na=False)]

	global ARQUIVO_SAIDA
	try:
		dados.to_csv(caminho_saida, index=False, sep=SEPARADOR)
	except PermissionError:
		sufixo = datetime.now().strftime("%Y%m%d_%H%M%S")
		caminho_alternativo = caminho_saida.replace(".csv", f"_{sufixo}.csv")
		dados.to_csv(caminho_alternativo, index=False, sep=SEPARADOR)
		ARQUIVO_SAIDA = caminho_alternativo

	return dados


def gerar_analise(dados: pd.DataFrame) -> dict:
	"""Calcula metricas principais de analise."""
	if dados.empty:
		return {
			"total_registros": 0,
			"preco_medio": "R$ 0.00",
			"preco_mediano": "R$ 0.00",
			"preco_moda": "Sem dados",
			"produto_mais_caro": "Sem dados",
			"produto_mais_barato": "Sem dados",
		}

	indice_max = dados["preco"].idxmax()
	indice_min = dados["preco"].idxmin()

	produto_mais_caro = f"{dados.loc[indice_max, 'titulo']} (R$ {dados.loc[indice_max, 'preco']:.2f})"
	produto_mais_barato = f"{dados.loc[indice_min, 'titulo']} (R$ {dados.loc[indice_min, 'preco']:.2f})"

	modas = dados["preco"].mode()
	preco_moda = ", ".join([f"R$ {valor:.2f}" for valor in modas.tolist()]) if not modas.empty else "Sem moda"

	return {
		"total_registros": int(len(dados)),
		"preco_medio": f"R$ {dados['preco'].mean():.2f}",
		"preco_mediano": f"R$ {dados['preco'].median():.2f}",
		"preco_moda": preco_moda,
		"produto_mais_caro": produto_mais_caro,
		"produto_mais_barato": produto_mais_barato,
	}


def gerar_grafico_base64(dados: pd.DataFrame) -> str:
	"""Gera grafico de distribuicao de precos e retorna imagem em base64."""
	fig, ax = plt.subplots(figsize=(10, 4.5))
	ax.hist(dados["preco"], bins=18, color="#0b7285", edgecolor="#dff5fa")
	ax.set_title("Distribuicao dos Precos", fontsize=12)
	ax.set_xlabel("Preco")
	ax.set_ylabel("Quantidade")
	ax.grid(axis="y", alpha=0.3)

	buffer = BytesIO()
	fig.tight_layout()
	fig.savefig(buffer, format="png", dpi=120)
	plt.close(fig)
	buffer.seek(0)
	return base64.b64encode(buffer.read()).decode("utf-8")


def mostrar_resultados_terminal(analise: dict) -> None:
	"""Exibe as principais metricas no terminal."""
	print("\n===== RESUMO DA ANALISE =====")
	print(f"Total de registros analisados: {analise['total_registros']}")
	print(f"Preco medio: {analise['preco_medio']}")
	print(f"Preco mediano: {analise['preco_mediano']}")
	print(f"Preco mais frequente (moda): {analise['preco_moda']}")
	print(f"Produto mais caro: {analise['produto_mais_caro']}")
	print(f"Produto mais barato: {analise['produto_mais_barato']}")


if __name__ == "__main__":
	dados_tratados = tratar_dados(ARQUIVO_ENTRADA, ARQUIVO_SAIDA)
	analise = gerar_analise(dados_tratados)
	mostrar_resultados_terminal(analise)

	grafico_base64 = gerar_grafico_base64(dados_tratados) if not dados_tratados.empty else ""
	tabela_html = dados_tratados.head(25).to_html(index=False, classes="tabela") if not dados_tratados.empty else "<p>Sem dados para exibir.</p>"

	app = Flask(__name__)

	@app.route("/")
	def pagina_principal():
		return render_template_string(
			HTML_TEMPLATE,
			total_registros=analise["total_registros"],
			preco_medio=analise["preco_medio"],
			preco_mediano=analise["preco_mediano"],
			preco_moda=analise["preco_moda"],
			produto_mais_caro=analise["produto_mais_caro"],
			produto_mais_barato=analise["produto_mais_barato"],
			grafico_base64=grafico_base64,
			tabela_html=tabela_html,
		)

	print("\nArquivo limpo salvo em:", ARQUIVO_SAIDA)
	print("Abrindo servidor Flask em http://127.0.0.1:5000")
	app.run(debug=False)
