# requirements.R
# Lista completa de pacotes necessários para a disciplina de Estatística
# Execute este arquivo para instalar todas as dependências

#####################
## PACOTES NECESSÁRIOS
#####################

required_packages <- c(
  # Manipulação de dados
  "dplyr",           # Manipulação de dados (tidyverse)
  "tidyr",           # Organização de dados (tidyverse)
  "readxl",          # Leitura de arquivos Excel
  "lubridate",       # Manipulação de datas
  
  # Visualização
  "ggplot2",         # Visualização de dados (tidyverse)
  "corrplot",        # Matriz de correlação
  "scales",          # Formatação de eixos
  "gridExtra",       # Layout de gráficos
  
  # Estatística
  "stats",           # Funções estatísticas base do R
  "MASS",            # Dataset birthwt e funções estatísticas
  "car",             # Testes estatísticos e Q-Q plots melhorados
  "nortest",         # Testes de normalidade (Anderson-Darling)
  "dunn.test",       # Teste de Dunn (post-hoc)
  "samplingbook",    # Cálculo de tamanho de amostra
  
  # Relatórios
  "knitr",           # Renderização de R Markdown
  "rmarkdown",       # Criação de documentos
  "kableExtra",      # Tabelas formatadas
  
  # Resumo e análise
  "skimr",           # Resumo estatístico moderno
  
  # Utilitários
  "here"             # Gerenciamento de caminhos
)

#####################
## INSTALAR PACOTES
#####################

install_if_missing <- function(packages) {
  new_packages <- packages[!(packages %in% installed.packages()[,"Package"])]
  if(length(new_packages) > 0) {
    message("Instalando pacotes que você ainda não tem no seu ambiente...")
    utils::install.packages(new_packages, dependencies = TRUE)
    message("Pacotes instalados com sucesso!")
  } else {
    message("Seu ambiente já tem todos os pacotes necessários!")
  }
}

# Instalar pacotes faltantes
install_if_missing(required_packages)

#####################
## CARREGAR PACOTES
#####################

# Carregar pacotes no ambiente
for (package in required_packages) {
  suppressWarnings(suppressMessages(
    require(package, character.only = TRUE, quietly = TRUE)
  ))
}

message("Todos os pacotes estão carregados. Bom trabalho!")

#####################
## VERIFICAÇÃO
#####################

# Verificar se todos os pacotes foram carregados
loaded_packages <- sapply(required_packages, function(pkg) {
  requireNamespace(pkg, quietly = TRUE)
})

if (all(loaded_packages)) {
  message("✅ Todos os pacotes foram carregados com sucesso!")
} else {
  missing <- names(loaded_packages)[!loaded_packages]
  warning("⚠️ Os seguintes pacotes não puderam ser carregados: ", 
          paste(missing, collapse = ", "))
}

