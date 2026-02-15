# Exemplo 1

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


# Exemplo 2

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

# Exemplo 3: Visualização de Clusters

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
