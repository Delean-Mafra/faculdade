############################################################
# COMPILADO COMPLETO: GRÁFICOS AVANÇADOS E 3D EM R
############################################################

# 1. Instalação e Carregamento de Pacotes Necessários
pacotes <- c("ggplot2", "plyr", "scatterplot3d", "rgl", "plotly", "plot3D")

for (p in pacotes) {
  if (!require(p, character.only = TRUE)) {
    install.packages(p)
    library(p, character.only = TRUE)
  }
}

# Função auxiliar para pausar entre os gráficos
pausa <- function(texto) {
  cat("\n---", texto, "---\n")
  readline(prompt = "Pressione [Enter] para ver o próximo gráfico...")
}

# Carregar banco de dados padrão
data("iris")

# ==========================================================
# SEÇÃO 1: GRÁFICOS DE DENSIDADE (Baseado na Figura 01)
# ==========================================================

pausa("GRÁFICO DE DENSIDADE: Simples")
print(ggplot(iris, aes(x = Sepal.Length)) + geom_density())

pausa("GRÁFICO DE DENSIDADE: Com preenchimento 'tomato'")
print(ggplot(iris, aes(x = Sepal.Length)) + geom_density(fill = "tomato"))

pausa("GRÁFICO DE DENSIDADE: Customizado (Azul claro, borda vermelha)")
print(ggplot(iris, aes(x = Sepal.Length)) + 
        geom_density(fill = "lightblue", alpha = .5, color = "red"))

pausa("GRÁFICO DE DENSIDADE: Por Espécie (Sem sobreposição)")
print(ggplot(iris, aes(x = Sepal.Length, fill = Species)) + 
        geom_density() + ggtitle("Sem sobreposição"))

pausa("GRÁFICO DE DENSIDADE: Por Espécie (Com sobreposição/alpha)")
print(ggplot(iris, aes(x = Sepal.Length, fill = Species)) + 
        geom_density(alpha = .5) + ggtitle("Com sobreposição"))

pausa("GRÁFICO DE DENSIDADE: Completo (Gráfico 01 do material)")
g1 <- ggplot(iris, aes(x = Sepal.Length, fill = Species)) +
  geom_density(alpha = .5) +
  theme_classic(base_size = 18) +
  scale_x_continuous(breaks = seq(4, 8, by = 1), limits = c(4, 8)) +
  scale_y_continuous(breaks = seq(0, 1.4, by = .2)) +
  xlab("Comprimento da sépala (mm)") + ylab("Density")
print(g1)


# ==========================================================
# SEÇÃO 2: GRÁFICOS BOXPLOT (Baseado na Figura 02)
# ==========================================================

pausa("BOXPLOT: Básico por Espécie")
print(ggplot(iris, aes(y = Sepal.Length, x = Species)) + geom_boxplot())

pausa("BOXPLOT: Destacando Outliers em Vermelho")
print(ggplot(iris, aes(y = Sepal.Length, x = Species)) + 
        geom_boxplot(outlier.color = "red"))

pausa("BOXPLOT: Com Entalhe (Notch)")
print(ggplot(iris, aes(y = Sepal.Length, x = Species)) + 
        geom_boxplot(notch = TRUE))

pausa("BOXPLOT: Completo (Gráfico 02 do material)")
g2 <- ggplot(iris, aes(y = Sepal.Length, x = Species, fill = Species)) +
  geom_boxplot(show.legend = FALSE, alpha = .5) +
  scale_y_continuous(limits = c(4, 8), breaks = seq(4, 8, 1)) +
  theme_classic(base_size = 18) +
  xlab("Espécie") + ylab("Comprimento da sépala (mm)")
print(g2)


# ==========================================================
# SEÇÃO 3: FUNÇÃO PAIRS (Baseado na Figura 03)
# ==========================================================

pausa("PAIRS: Matriz de Dispersão Colorida (Gráfico 03)")
pairs(iris[1:4], main = "Anderson's Iris Data -- 3 species",
      pch = 21, bg = c("red", "green3", "blue")[unclass(iris$Species)])


# ==========================================================
# SEÇÃO 4: GGPLOT2 AVANÇADO - MPG (Baseado na Figura 04)
# ==========================================================

pausa("GGPLOT2: Pontos e Regressão (Dataset MPG)")
# Preparação dos dados como no código enviado
carros <- plyr::rename(mpg, c("displ" = "Cilindradas", 
                             "cty" = "Consumo", 
                             "drv" = "Tração", 
                             "class" = "Tipo"))

g4 <- ggplot(carros, aes(Cilindradas, Consumo, size = Tração, color = Tipo)) +
  geom_point() +
  geom_smooth(method = "lm")
print(g4)


# ==========================================================
# SEÇÃO 5: GRÁFICOS 3D (Pesquisa Adicional)
# ==========================================================

pausa("3D: Superfície Matemática (Função persp)")
x <- seq(-10, 10, length = 30); y <- x
z <- outer(x, y, function(a, b) sin(sqrt(a^2 + b^2)))
persp(x, y, z, col = "lightblue", theta = 30, phi = 20, main = "persp 3D")

pausa("3D: Dispersão Estática (scatterplot3d)")
scatterplot3d(iris$Sepal.Length, iris$Sepal.Width, iris$Petal.Length,
              color = as.numeric(iris$Species), pch = 16, main = "scatterplot3d")

pausa("3D INTERATIVO: Pacote rgl (Abre nova janela)")
# Nota: Pode não aparecer no painel de plots fixo do RStudio
plot3d(iris$Sepal.Length, iris$Sepal.Width, iris$Petal.Length,
       col = as.numeric(iris$Species), size = 5, type = "s")

pausa("3D INTERATIVO: Pacote Plotly (Abre no navegador/Viewer)")
fig_plotly <- plot_ly(iris, x = ~Sepal.Length, y = ~Sepal.Width, z = ~Petal.Length,
                      color = ~Species, type = "scatter3d", mode = "markers")
print(fig_plotly)

cat("\n--- FIM DO COMPILADO ---\n")
