# Gráficos 3D em R - Guia Completo

## Introdução

Os gráficos 3D em R são ferramentas poderosas para visualização de dados tridimensionais, permitindo a análise de relações entre três variáveis simultaneamente. A principal diferença entre gráficos 2D e 3D é a adição de uma terceira dimensão (profundidade), que possibilita comparar três valores ao mesmo tempo.

### Quando Usar Gráficos 3D?

**Use gráficos 3D quando:**
- Precisar visualizar a relação entre três variáveis numéricas
- Criar gráficos de dispersão com três dimensões
- Plotar superfícies matemáticas ou de resposta
- Visualizar dados espaciais ou volumétricos

**Evite gráficos 3D quando:**
- A informação pode ser representada em 2D (gráficos de barras, pizza, linhas)
- A terceira dimensão não adiciona informação relevante
- A interpretação dos dados seria mais clara em 2D

---

## 1. Pacote `scatterplot3d` - Gráficos Estáticos Simples

### Instalação e Carregamento

```r
# Instalar o pacote
install.packages("scatterplot3d")

# Carregar a biblioteca
library(scatterplot3d)
```

### Exemplo Básico - Gráfico de Dispersão 3D

```r
# Carregar dados
data(iris)

# Criar gráfico de dispersão 3D básico
scatterplot3d(
  x = iris$Sepal.Length,
  y = iris$Sepal.Width,
  z = iris$Petal.Length,
  main = "Gráfico 3D - Iris Dataset",
  xlab = "Comprimento da Sépala (cm)",
  ylab = "Largura da Sépala (cm)",
  zlab = "Comprimento da Pétala (cm)"
)
```

### Exemplo com Cores por Categoria

```r
# Definir cores para cada espécie
colors <- c("#004B95", "#38812F", "#A30000")
shapes <- c(15, 16, 17)

# Criar gráfico com cores diferentes por espécie
scatterplot3d(
  x = iris$Sepal.Length,
  y = iris$Sepal.Width,
  z = iris$Petal.Length,
  angle = 30,
  pch = shapes[as.numeric(iris$Species)],
  color = colors[as.numeric(iris$Species)],
  main = "Iris 3D Scatter Plot",
  xlab = "Sepal Length (cm)",
  ylab = "Sepal Width (cm)",
  zlab = "Petal Length (cm)"
)

# Adicionar legenda
legend(
  "bottom",
  legend = levels(iris$Species),
  col = colors,
  pch = shapes,
  xpd = TRUE,
  horiz = TRUE,
  inset = c(0, -0.18)
)
```

### Características do scatterplot3d:
- ✅ **Simples de usar**
- ✅ **Gráficos de alta qualidade**
- ✅ **Exportação fácil**
- ❌ **Não é interativo** (precisa ajustar o ângulo manualmente)

---

## 2. Pacote `rgl` - Gráficos 3D Interativos

### Instalação e Carregamento

```r
# Instalar o pacote
install.packages("rgl")

# Carregar a biblioteca
library(rgl)
```

### Exemplo Básico - Scatter Plot 3D Interativo

```r
# Carregar dados
data(iris)

# Criar gráfico 3D interativo básico
plot3d(
  x = iris$Sepal.Length,
  y = iris$Sepal.Width,
  z = iris$Petal.Length,
  type = "s",  # "s" para esferas, "p" para pontos
  col = "red",
  size = 1
)
```

### Exemplo com Cores por Categoria

```r
# Definir cores
colors <- c("#004B95", "#38812F", "#A30000")

# Criar gráfico com cores e tamanho ajustado
plot3d(
  x = iris$Sepal.Length,
  y = iris$Sepal.Width,
  z = iris$Petal.Length,
  type = "s",
  col = colors[as.numeric(iris$Species)],
  radius = 0.1,
  main = "Iris 3D Scatter Plot",
  xlab = "Sepal Length (cm)",
  ylab = "Sepal Width (cm)",
  zlab = "Petal Length (cm)"
)
```

### Adicionando Elementos Visuais

```r
# Adicionar cor de fundo
bg3d(color = "lightblue")

# Adicionar caixa delimitadora
bbox3d(col = "blue")

# Adicionar eixos
axes3d()

# Adicionar texto 3D
text3d(iris$Sepal.Length, iris$Sepal.Width, iris$Petal.Length, 
       texts = as.character(iris$Species))
```

### Animações com rgl

```r
# Criar animação de rotação
play3d(spin3d(axis = c(0, 0, 1)), duration = 10)

# Rotação no eixo Y
play3d(spin3d(axis = c(0, 1, 0)), duration = 10)

# Rotação no eixo X
play3d(spin3d(axis = c(1, 0, 0)), duration = 10)
```

### Salvar Gráfico Interativo

```r
# Salvar como HTML interativo
library(htmlwidgets)
htmlwidgets::saveWidget(
  rglwidget(width = 520, height = 520),
  file = "grafico_3d_interativo.html",
  selfcontained = TRUE
)
```

### Características do rgl:
- ✅ **Totalmente interativo** (rotação, zoom)
- ✅ **Animações**
- ✅ **Renderização em tempo real (OpenGL)**
- ✅ **Exportação para HTML**
- ⚠️ **Curva de aprendizado maior**

---

## 3. Pacote `plotly` - Gráficos 3D Interativos Modernos

### Instalação e Carregamento

```r
# Instalar o pacote
install.packages("plotly")

# Carregar a biblioteca
library(plotly)
```

### Exemplo Básico - Scatter 3D

```r
# Criar dados de exemplo
data <- data.frame(
  x = rnorm(100),
  y = rnorm(100),
  z = rnorm(100)
)

# Criar gráfico 3D com plotly
plot_ly(
  data = data,
  x = ~x,
  y = ~y,
  z = ~z,
  type = "scatter3d",
  mode = "markers",
  marker = list(size = 3, color = "blue")
) %>%
  layout(
    title = "Gráfico 3D Scatter com Plotly",
    scene = list(
      xaxis = list(title = "Eixo X"),
      yaxis = list(title = "Eixo Y"),
      zaxis = list(title = "Eixo Z")
    )
  )
```

### Exemplo com Dataset Iris

```r
# Criar gráfico 3D com cores por espécie
plot_ly(
  data = iris,
  x = ~Sepal.Length,
  y = ~Sepal.Width,
  z = ~Petal.Length,
  color = ~Species,
  colors = c("#004B95", "#38812F", "#A30000"),
  type = "scatter3d",
  mode = "markers",
  marker = list(size = 5)
) %>%
  layout(
    title = "Iris Dataset - Visualização 3D",
    scene = list(
      xaxis = list(title = "Comprimento da Sépala"),
      yaxis = list(title = "Largura da Sépala"),
      zaxis = list(title = "Comprimento da Pétala")
    )
  )
```

### Gráfico de Superfície 3D

```r
# Criar dados de superfície
x <- seq(-5, 5, length.out = 50)
y <- seq(-5, 5, length.out = 50)
z <- outer(x, y, function(x, y) sin(sqrt(x^2 + y^2)))

# Plotar superfície
plot_ly(z = ~z, type = "surface") %>%
  layout(
    title = "Superfície 3D",
    scene = list(
      xaxis = list(title = "X"),
      yaxis = list(title = "Y"),
      zaxis = list(title = "Z")
    )
  )
```

### Características do plotly:
- ✅ **Interativo e moderno**
- ✅ **Integração com ggplot2**
- ✅ **Fácil personalização**
- ✅ **Tooltips automáticos**
- ✅ **Exportação para HTML**
- ✅ **Compartilhamento online fácil**

---

## 4. Pacote `plot3D` - Gráficos 3D Avançados

### Instalação e Carregamento

```r
# Instalar o pacote
install.packages("plot3D")

# Carregar a biblioteca
library(plot3D)
```

### Scatter Plot 3D com plot3D

```r
# Carregar dados
data(iris)

# Separar variáveis
x <- iris$Sepal.Length
y <- iris$Petal.Length
z <- iris$Sepal.Width

# Criar gráfico de dispersão 3D
scatter3D(
  x = x,
  y = y,
  z = z,
  colvar = as.numeric(iris$Species),
  col = c("red", "green", "blue"),
  pch = 19,
  cex = 1.5,
  theta = 30,
  phi = 20,
  xlab = "Sepal Length",
  ylab = "Petal Length",
  zlab = "Sepal Width",
  main = "Iris Dataset - 3D Scatter",
  bty = "g",
  ticktype = "detailed"
)
```

### Gráfico de Superfície com persp3D

```r
# Criar superfície
x <- seq(-2, 2, length.out = 50)
y <- seq(-2, 2, length.out = 50)
M <- mesh(x, y)
z <- with(M, x * exp(-x^2 - y^2))

# Plotar superfície
persp3D(
  x = M$x,
  y = M$y,
  z = z,
  theta = 30,
  phi = 20,
  expand = 0.5,
  col = "lightblue",
  shade = 0.5,
  xlab = "X",
  ylab = "Y",
  zlab = "Z",
  main = "Superfície 3D"
)
```

### Histograma 3D

```r
# Criar histograma 3D
x <- rnorm(100)
y <- rnorm(100)

hist3D(
  x = x,
  y = y,
  breaks = 10,
  col = "lightblue",
  border = "black",
  shade = 0.8,
  theta = 30,
  phi = 20,
  xlab = "X",
  ylab = "Y",
  zlab = "Frequência",
  main = "Histograma 3D"
)
```

### Texto 3D com plot3D

```r
# Adicionar texto em 3D
text3D(
  x = iris$Sepal.Length,
  y = iris$Sepal.Width,
  z = iris$Petal.Length,
  labels = rownames(iris),
  col = "blue",
  cex = 0.6,
  theta = 60,
  phi = 20,
  xlab = "Sepal Length",
  ylab = "Sepal Width",
  zlab = "Petal Length"
)
```

### Paletas de Cores no plot3D

```r
# Paletas disponíveis
# jet.col(n) - cores estilo MATLAB (padrão)
# jet2.col(n) - similar ao jet.col mas sem azul profundo
# gg.col(n) e gg2.col(n) - estilo ggplot
# ramp.col(col = c("grey", "black"), n) - interpolação customizada

# Exemplo com paleta customizada
col_palette <- colorRampPalette(c("blue", "cyan", "yellow", "red"))

scatter3D(
  x = iris$Sepal.Length,
  y = iris$Sepal.Width,
  z = iris$Petal.Length,
  colvar = iris$Petal.Width,
  col = col_palette(100),
  pch = 19,
  cex = 1.5,
  theta = 30,
  phi = 20,
  main = "Iris com Paleta Customizada"
)
```

### Características do plot3D:
- ✅ **Muitas funções especializadas**
- ✅ **Excelente para superfícies**
- ✅ **Suporte a 4D (x, y, z, cor)**
- ✅ **Histogramas 3D**
- ✅ **Contornos e projeções**
- ⚠️ **Menos interativo que plotly/rgl**

---

## 5. Função Base `persp()` - Gráficos de Superfície

### Exemplo Básico com persp()

```r
# Criar cone simples
cone <- function(x, y) {
  sqrt(x^2 + y^2)
}

# Preparar variáveis
x <- y <- seq(-1, 1, length = 30)
z <- outer(x, y, cone)

# Plotar superfície 3D
persp(
  x = x,
  y = y,
  z = z,
  theta = 30,
  phi = 30,
  expand = 0.5,
  col = "lightblue",
  xlab = "X",
  ylab = "Y",
  zlab = "Z",
  main = "Cone 3D"
)
```

### Exemplo com Função Matemática

```r
# Criar função matemática
f <- function(x, y) {
  x * y * sin(x^2 + y^2)
}

# Preparar dados
x <- seq(-2, 2, length.out = 50)
y <- seq(-2, 2, length.out = 50)
z <- outer(x, y, f)

# Plotar com cores e sombreamento
persp(
  x = x,
  y = y,
  z = z,
  theta = 45,
  phi = 30,
  expand = 0.7,
  col = "cyan",
  shade = 0.5,
  border = NA,
  xlab = "X",
  ylab = "Y",
  zlab = "f(x,y)",
  main = "Função x*y*sin(x² + y²)"
)
```

### Parâmetros Importantes do persp():
- `theta` - ângulo azimutal (rotação horizontal)
- `phi` - ângulo colatitude (inclinação vertical)
- `expand` - fator de expansão do eixo Z
- `col` - cor da superfície
- `shade` - sombreamento (0 a 1)
- `border` - cor das bordas (NA para sem bordas)

---

## 6. Integração plot3D com rgl (plot3Drgl)

### Tornando Gráficos plot3D Interativos

```r
# Instalar pacote
install.packages("plot3Drgl")

# Carregar bibliotecas
library(plot3D)
library(plot3Drgl)

# Criar gráfico com plot3D
scatter3D(
  x = iris$Sepal.Length,
  y = iris$Sepal.Width,
  z = iris$Petal.Length,
  colvar = as.numeric(iris$Species),
  col = c("red", "green", "blue"),
  pch = 19
)

# Converter para rgl interativo
plotrgl()

# Agora o gráfico é interativo!
# Funções úteis:
# croprgl(xlim, ylim, zlim) - modificar ranges
# cutrgl() - zoom em região selecionada
# uncutrgl() - restaurar gráfico original
```

---

## 7. Comparação entre os Pacotes

| Pacote | Interativo | Facilidade | Qualidade | Melhor Para |
|--------|-----------|------------|-----------|-------------|
| **scatterplot3d** | ❌ Não | ⭐⭐⭐⭐⭐ Muito Fácil | ⭐⭐⭐⭐ Ótima | Gráficos estáticos simples |
| **rgl** | ✅ Sim | ⭐⭐⭐ Média | ⭐⭐⭐⭐⭐ Excelente | Exploração interativa, animações |
| **plotly** | ✅ Sim | ⭐⭐⭐⭐ Fácil | ⭐⭐⭐⭐⭐ Excelente | Visualizações web, dashboards |
| **plot3D** | ⚠️ Limitado | ⭐⭐⭐ Média | ⭐⭐⭐⭐ Ótima | Superfícies, gráficos científicos |
| **persp()** | ❌ Não | ⭐⭐⭐⭐ Fácil | ⭐⭐⭐ Boa | Superfícies matemáticas básicas |

---

## 8. Exemplos Práticos Completos

### Exemplo 1: Análise de Dados de Vendas

```r
# Criar dados fictícios de vendas
vendas <- data.frame(
  preco = runif(100, 10, 100),
  publicidade = runif(100, 1000, 10000),
  vendas = runif(100, 50, 500)
)

# Visualizar com plotly
library(plotly)

plot_ly(
  data = vendas,
  x = ~preco,
  y = ~publicidade,
  z = ~vendas,
  type = "scatter3d",
  mode = "markers",
  marker = list(
    size = 5,
    color = ~vendas,
    colorscale = "Viridis",
    showscale = TRUE
  )
) %>%
  layout(
    title = "Análise de Vendas 3D",
    scene = list(
      xaxis = list(title = "Preço (R$)"),
      yaxis = list(title = "Investimento em Publicidade (R$)"),
      zaxis = list(title = "Volume de Vendas")
    )
  )
```

### Exemplo 2: Superfície de Resposta

```r
library(plot3D)

# Criar dados de experimento
x <- seq(-3, 3, length.out = 30)
y <- seq(-3, 3, length.out = 30)
M <- mesh(x, y)

# Função de resposta
z <- with(M, 10 + 2*x + 3*y - 0.5*x^2 - 0.3*y^2 + 0.1*x*y)

# Plotar superfície de resposta
persp3D(
  x = M$x,
  y = M$y,
  z = z,
  theta = 40,
  phi = 25,
  col = terrain.colors(100),
  shade = 0.5,
  xlab = "Fator X",
  ylab = "Fator Y",
  zlab = "Resposta",
  main = "Superfície de Resposta Experimental",
  contour = list(
    side = c("zmin", "z"),
    col = "grey"
  )
)
```

### Exemplo 3: Visualização de Clusters

```r
library(rgl)

# Criar dados com 3 clusters
set.seed(123)
cluster1 <- data.frame(
  x = rnorm(50, 0, 1),
  y = rnorm(50, 0, 1),
  z = rnorm(50, 0, 1)
)

cluster2 <- data.frame(
  x = rnorm(50, 5, 1),
  y = rnorm(50, 5, 1),
  z = rnorm(50, 5, 1)
)

cluster3 <- data.frame(
  x = rnorm(50, 0, 1),
  y = rnorm(50, 5, 1),
  z = rnorm(50, 5, 1)
)

# Plotar com cores diferentes
plot3d(cluster1$x, cluster1$y, cluster1$z, 
       type = "s", col = "red", radius = 0.2)
plot3d(cluster2$x, cluster2$y, cluster2$z, 
       type = "s", col = "blue", radius = 0.2, add = TRUE)
plot3d(cluster3$x, cluster3$y, cluster3$z, 
       type = "s", col = "green", radius = 0.2, add = TRUE)

# Adicionar elementos visuais
axes3d()
title3d(main = "Visualização de 3 Clusters", 
        xlab = "Dimensão 1", 
        ylab = "Dimensão 2", 
        zlab = "Dimensão 3")
```

---

## 9. Dicas e Boas Práticas

### ✅ FAÇA:

1. **Use cores para diferenciar categorias**
   - Facilita a interpretação visual
   - Use paletas de cores contrastantes

2. **Adicione rótulos claros aos eixos**
   - Sempre inclua unidades de medida
   - Use nomes descritivos

3. **Ajuste o ângulo de visualização**
   - Teste diferentes valores de `theta` e `phi`
   - Escolha o ângulo que melhor mostra os dados

4. **Prefira gráficos interativos quando apropriado**
   - plotly e rgl para exploração de dados
   - Permite rotação e zoom

5. **Exporte gráficos em alta resolução**
   - Use PNG ou PDF para publicações
   - HTML para compartilhamento web

### ❌ EVITE:

1. **Gráficos 3D quando 2D é suficiente**
   - Gráficos de barras 3D são confusos
   - Pizza 3D é especialmente problemática

2. **Muitas cores diferentes**
   - Dificulta a interpretação
   - Use no máximo 5-7 cores distintas

3. **Pontos muito grandes ou muito pequenos**
   - Ajuste o tamanho para melhor visualização
   - Considere transparência se houver sobreposição

4. **Ângulos que ocultam dados importantes**
   - Sempre verifique se todos os dados são visíveis
   - Teste múltiplas perspectivas

---

## 10. Recursos Adicionais

### Documentação Oficial:
- **scatterplot3d**: `help(scatterplot3d)`
- **rgl**: `help(plot3d)` ou https://dmurdoch.github.io/rgl/
- **plotly**: https://plotly.com/r/
- **plot3D**: `vignette("plot3D")`

### Tutoriais Online:
- R Graph Gallery: https://r-graph-gallery.com/3d.html
- STHDA: http://www.sthda.com/english/wiki/3d-graphics

### Galerias de Exemplos:
- plot3D Gallery: http://www.rforscience.com/rpackages/visualisation/oceanview/
- plotly R Examples: https://plotly.com/r/3d-charts/

---

## Conclusão

Os gráficos 3D em R oferecem diversas opções para diferentes necessidades:

- **Para iniciantes**: comece com `scatterplot3d` (simples e direto)
- **Para interatividade**: use `plotly` (moderno e fácil) ou `rgl` (mais controle)
- **Para superfícies científicas**: use `plot3D` (muitas opções especializadas)
- **Para superfícies matemáticas básicas**: use `persp()` (função base do R)

A escolha do pacote depende das suas necessidades específicas:
- Precisa de interatividade? → **plotly** ou **rgl**
- Gráfico estático de qualidade? → **scatterplot3d**
- Superfícies complexas? → **plot3D**
- Apenas superfície matemática? → **persp()**

Lembre-se: use gráficos 3D apenas quando a terceira dimensão adicionar valor real à visualização. Em muitos casos, múltiplos gráficos 2D ou outras técnicas de visualização podem ser mais eficazes!
