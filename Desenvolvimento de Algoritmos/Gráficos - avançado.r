############################################################
# GRÁFICOS AVANÇADOS E 3D EM R - VERSÃO NÃO INTERATIVA
############################################################

# 1. Instalação e Carregamento de Pacotes (silencioso, seguro)
pacotes <- c("ggplot2", "plyr", "scatterplot3d", "rgl", "plotly", "plot3D")
for (p in pacotes) {
  if (!requireNamespace(p, quietly = TRUE)) {
    install.packages(p, dependencies = TRUE)
  }
  # carregue apenas os que existem
  suppressPackageStartupMessages(library(p, character.only = TRUE, quietly = TRUE, warn.conflicts = FALSE))
}

# 2. Dados
data("iris")
# mpg vem do ggplot2; carregue se disponível
if (!exists("mpg")) {
  if ("ggplot2" %in% rownames(installed.packages())) data("mpg", package = "ggplot2")
}

# 3. Função auxiliar para executar blocos sem interromper tudo
safe_eval <- function(expr) {
  tryCatch({
    eval(expr, envir = .GlobalEnv)
  }, error = function(e) {
    message("Erro no bloco: ", conditionMessage(e))
    invisible(NULL)
  })
}

# --- SEÇÃO 1: DENSIDADE ---
safe_eval(quote({
  g_dens1 <- ggplot(iris, aes(x = Sepal.Length)) + geom_density()
  print(g_dens1)
}))

safe_eval(quote({
  g_dens2 <- ggplot(iris, aes(x = Sepal.Length)) +
    geom_density(fill = "lightblue", alpha = .5, color = "red")
  print(g_dens2)
}))

safe_eval(quote({
  g_dens3 <- ggplot(iris, aes(x = Sepal.Length, fill = Species)) +
    geom_density(alpha = .5) +
    theme_classic(base_size = 15) +
    xlab("Comprimento da sépala (mm)") + ylab("Densidade")
  print(g_dens3)
}))

# --- SEÇÃO 2: BOXPLOT ---
safe_eval(quote({
  g_box1 <- ggplot(iris, aes(y = Sepal.Length, x = Species)) +
    geom_boxplot(outlier.color = "red")
  print(g_box1)
}))

safe_eval(quote({
  g_box2 <- ggplot(iris, aes(y = Sepal.Length, x = Species, fill = Species)) +
    geom_boxplot(show.legend = FALSE, alpha = .5) +
    theme_classic(base_size = 15) +
    xlab("Espécie") + ylab("Sépala (mm)")
  print(g_box2)
}))

# --- SEÇÃO 3: PAIRS ---
safe_eval(quote({
  pairs(iris[1:4], main = "Iris Data", pch = 21,
        bg = c("red", "green3", "blue")[unclass(iris$Species)])
}))

# --- SEÇÃO 4: GGPLOT2 AVANÇADO (MPG) ---
safe_eval(quote({
  if (exists("mpg")) {
    carros <- plyr::rename(mpg, c("displ" = "Cilindradas",
                                  "cty" = "Consumo",
                                  "drv" = "Tração",
                                  "class" = "Tipo"))
    g_mpg <- ggplot(carros, aes(Cilindradas, Consumo, size = Tração, color = Tipo)) +
      geom_point() +
      geom_smooth(method = "lm")
    print(g_mpg)
  } else {
    message("Dataset 'mpg' não disponível; pulando seção MPG.")
  }
}))

# --- SEÇÃO 5: GRÁFICOS 3D ---
safe_eval(quote({
  x <- seq(-10, 10, length = 30)
  y <- x
  z <- outer(x, y, function(a, b) sin(sqrt(a^2 + b^2)))
  persp(x, y, z, col = "lightblue", theta = 30, phi = 20)
}))

safe_eval(quote({
  scatterplot3d(iris$Sepal.Length, iris$Sepal.Width, iris$Petal.Length,
                color = as.numeric(iris$Species), pch = 16)
}))

safe_eval(quote({
  if ("plotly" %in% rownames(installed.packages())) {
    p_3d <- plot_ly(iris,
                    x = ~Sepal.Length,
                    y = ~Sepal.Width,
                    z = ~Petal.Length,
                    color = ~Species,
                    type = "scatter3d",
                    mode = "markers")
    print(p_3d)
  }
}))

cat("\n--- SCRIPT EXECUTADO ---\n")
