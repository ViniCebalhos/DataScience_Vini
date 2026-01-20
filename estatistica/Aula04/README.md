# Relatórios Reprodutíveis com R Markdown

**Linguagem:** R (R Markdown)
**Técnicas:** Relatórios reprodutíveis, análise exploratória, documentação técnica

---

## Sobre o Projeto

Este projeto demonstra competências em criação de relatórios reprodutíveis e profissionais usando R Markdown. Combina análise exploratória de dados, visualizações e documentação técnica em um único documento HTML gerado automaticamente.

---

## Competências Demonstradas

### R Markdown
- Criação de documentos reprodutíveis (.Rmd)
- Integração de código R, texto e resultados
- Geração de relatórios HTML profissionais
- Documentação técnica completa

### Análise Exploratória
- Análise univariada e bivariada
- Visualizações profissionais
- Estatísticas descritivas
- Comparação de grupos

### Documentação
- Estruturação de relatórios técnicos
- Interpretação de resultados
- Visualizações com legendas e títulos descritivos

---

## Estrutura do Projeto

### Scripts Principais
- **`Aula04_AED.Rmd`** - R Markdown principal (análise de qualidade de sono e estresse)
- **`ViniciusCebalhos_atividade1.Rmd`** - Análise de qualidade de vida

### Dataset Utilizado
- **`dados_exercio.csv`** - Dataset com informações de 374 colaboradores:
 - Variáveis demográficas (sexo, profissão)
 - Variáveis de saúde (IMC, frequência cardíaca, passos diários)
 - Variáveis de qualidade de vida (qualidade do sono, nível de estresse)

---

## Análise Implementada

### 1. Estrutura do R Markdown

**Cabeçalho YAML:**
```yaml
---
title: "AED - Qualidade de Sono e Nível de Estresse"
output: html_document
---
```

**Chunks de Código:**
```r
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE, warning = FALSE)
```

### 2. Análise Exploratória

**Técnicas Aplicadas:**
- Tabelas de frequência
- Gráficos de barras
- Histogramas
- Boxplots
- Comparação de grupos
- Análise de relações entre variáveis

### 3. Visualizações Profissionais

**Gráficos Gerados:**
- Distribuições de variáveis categóricas
- Distribuições de variáveis numéricas
- Comparações entre grupos
- Análise de relações bivariadas

---

## Tecnologias Utilizadas

### Bibliotecas R
- **rmarkdown** - Criação de documentos
- **knitr** - Renderização de código
- **dplyr** - Manipulação de dados
- **ggplot2** - Visualização
- **kableExtra** - Tabelas formatadas

---

## Resultados Principais

### Relatórios Gerados
- Documentos HTML profissionais
- Análise completa de qualidade de vida
- Visualizações integradas
- Interpretações e conclusões

---

## Como Executar

### Pré-requisitos
```r
# Instalar pacotes necessários
install.packages(c("rmarkdown", "knitr", "dplyr", "ggplot2", "kableExtra"))
```

### Compilar Relatório
```r
# No RStudio: Knit > Knit to HTML
# Ou via console:
rmarkdown::render("Aula04_AED.Rmd")
```

---

## Métricas e Visualizações

- Relatórios HTML completos
- Tabelas de frequência formatadas
- Gráficos profissionais integrados
- Estatísticas descritivas documentadas
- Análise de relações entre variáveis

---

**Autor:** Vinícius de Souza Cebalhos
