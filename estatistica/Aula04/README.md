# Aula 04 - Análise Exploratória de Dados com R Markdown

**Disciplina:** Estatística  
**Linguagem:** R (R Markdown)  
**Objetivo:** Criar relatórios reprodutíveis de análise exploratória de dados usando R Markdown

---

## 🎯 Objetivo da Aula

Esta aula introduz **R Markdown** como ferramenta para criar relatórios reprodutíveis e profissionais. Os alunos aprendem a:

- Criar documentos R Markdown (.Rmd)
- Combinar texto, código R e resultados em um único documento
- Gerar relatórios HTML profissionais
- Realizar análise exploratória completa de um dataset real

---

## 📚 Conceitos Estatísticos Envolvidos

### Análise Exploratória de Dados (AED)
- **Análise Univariada:** Uma variável por vez
- **Análise Bivariada:** Relações entre duas variáveis
- **Análise Multivariada:** Múltiplas variáveis simultaneamente

### Tipos de Variáveis
- **Qualitativas (Categóricas):** Sexo, profissão, categoria IMC
- **Quantitativas (Numéricas):** Frequência cardíaca, passos diários, qualidade do sono

### Técnicas Utilizadas
- Tabelas de frequência
- Gráficos de barras
- Histogramas
- Boxplots
- Comparação de grupos

---

## 📁 Arquivos da Aula

### Scripts Principais
- **`Aula04_AED.Rmd`** - R Markdown principal da aula (análise de qualidade de sono e estresse)
- **`ViniciusCebalhos_atividade1.Rmd`** - Trabalho do aluno (análise de qualidade de vida)
- **`SeuNome_atividade1.Rmd`** - Template para atividade
- **`SeuNome_atividade1_Ajustado.Rmd`** - Versão ajustada do template

### Dataset Utilizado
- **`dados_exercio.csv`** - Dataset com informações de 374 colaboradores:
  - Variáveis demográficas (sexo, profissão)
  - Variáveis de saúde (IMC, frequência cardíaca, passos diários)
  - Variáveis de qualidade de vida (qualidade do sono, nível de estresse, distúrbios do sono)

---

## 🔍 Análise do Código

### Estrutura do R Markdown `Aula04_AED.Rmd`

#### 1. **Cabeçalho YAML (linhas 1-4)**
```yaml
---
title: "AED - Qualidade de sono e nível de strees"
output: html_document
---
```

**O que faz:**
- Define metadados do documento
- Especifica formato de saída (HTML)

**⚠️ Problema:** Erro de digitação: "strees" → deveria ser "stress"

**Sugestão:**
```yaml
---
title: "AED - Qualidade de Sono e Nível de Estresse"
author: "Vinícius de Souza Cebalhos"
date: "`r Sys.Date()`"
output: 
  html_document:
    toc: true
    toc_float: true
    theme: flatly
---
```

---

#### 2. **Carregamento de Dados (linhas 6-25)**
```r
project_root_path <- paste0(getwd())
source(paste0(project_root_path, "/definitions.R"))
source(paste0(project_root_path, "/install_load_packages.R"), encoding = encoding)

dados <- read.csv("dados_exercio.csv")
head(dados)
str(dados)
```

**O que faz:**
- Carrega configurações e pacotes
- Lê dataset CSV
- Mostra primeiras linhas e estrutura

**⚠️ Problema:** Caminho relativo pode quebrar

**Sugestão:**
```r
dados <- read.csv(file.path(project_root_path, "dados_exercio.csv"))
```

---

#### 3. **Transformação de Variáveis (linhas 28-63)**
```r
dados <- dados %>%
  dplyr::mutate(
    sexo = factor(Gender),
    prof = factor(Occupation),
    imc_cat = factor(BMI.Category),
    desordem_sono = factor(Sleep.Disorder),
    imc_cat_adj = factor(dplyr::case_when(
      imc_cat == 'Normal Weight' ~ 'Normal',
      TRUE ~ imc_cat),
      level = c('Normal', 'Overweight', 'Obese'),
      ordered = TRUE),
    qualidade_sono = factor(dplyr::case_when(
      Quality.of.Sleep <= 3 ~ 'Ruim',
      Quality.of.Sleep <= 6 ~ 'Médio',
      Quality.of.Sleep <= 9 ~ 'Bom',
      TRUE ~ 'Excelente'),
      levels = c('Ruim', 'Médio', 'Bom', 'Excelente'),
      ordered = TRUE),
    nivel_estresse = factor(dplyr::case_when(
      Stress.Level < 3 ~ 'Baixo',
      Stress.Level < 6 ~ 'Médio',
      TRUE ~ 'Alto'),
      levels = c('Baixo', 'Médio', 'Alto'),
      ordered = TRUE)
  )
```

**O que faz:**
- Converte variáveis para fatores (categóricas)
- Recodifica categorias de IMC
- Cria categorias ordenadas para qualidade do sono e estresse

**Conceitos:**
- **Fator Ordenado:** Categorias com ordem lógica (Ruim < Médio < Bom < Excelente)
- **Recodificação:** Agrupar ou renomear categorias
- **case_when():** Criação condicional de categorias

---

#### 4. **Análise de Estresse por Profissão (linhas 72-76)**
```r
table(dados$nivel_estresse, dados$prof_adj)
round(prop.table(table(dados$nivel_estresse, dados$prof_adj), margin=1)*100,0)
```

**O que faz:**
- Cria tabela de contingência
- Calcula percentuais por linha (dado o nível de estresse, qual % em cada profissão)

**Interpretação:**
- Permite identificar se certas profissões têm maior proporção de estresse alto

---

### Análise do Trabalho do Aluno `ViniciusCebalhos_atividade1.Rmd`

Este é um exemplo completo de análise exploratória bem estruturada:

#### Estrutura do Documento:
1. **Introdução** - Contextualização do problema
2. **Carregamento e Limpeza** - Preparação dos dados
3. **Análise Univariada** - Uma variável por vez
4. **Análise Bivariada** - Relações entre variáveis
5. **Considerações Finais** - Interpretação e recomendações

#### Destaques do Código:

**Análise de Variável Qualitativa:**
```r
bmi_freq <- table(dados$BMI.Category)
barplot(bmi_freq, main = "Distribuição por Categoria de IMC", 
        col = "lightblue", ylab = "Frequência")
```

**Análise de Variável Quantitativa:**
```r
summary(dados$Heart.Rate)
hist(dados$Heart.Rate, col = "lightgreen", 
     main = "Distribuição da Frequência Cardíaca", xlab = "BPM")
```

**Análise Bivariada:**
```r
boxplot(Heart.Rate ~ BMI.Category, data = dados, 
        main = "Frequência Cardíaca por Categoria de IMC",
        col = c("lightblue", "lightgreen", "pink"), ylab = "BPM")
aggregate(Heart.Rate ~ BMI.Category, data = dados, FUN = mean)
```

**Pontos Fortes:**
- ✅ Estrutura clara e organizada
- ✅ Comentários explicativos
- ✅ Interpretação dos resultados
- ✅ Recomendações práticas

---

## 🚀 Como Executar

### Pré-requisitos
1. R instalado (versão 4.0+)
2. RStudio (recomendado)
3. Pacote `rmarkdown` instalado

### Passo a Passo

1. **Abra o projeto RStudio:**
```r
# File > Open Project > Aula4.Rproj
```

2. **Abra o arquivo .Rmd:**
```r
# File > Open File > Aula04_AED.Rmd
```

3. **Renderize o documento:**
```r
# No RStudio: Knit > Knit to HTML
# Ou no console:
rmarkdown::render("Aula04_AED.Rmd")
```

### Dependências

Pacotes necessários (instalados automaticamente):
- `dplyr` - Manipulação de dados
- `ggplot2` - Visualização
- `knitr` - Renderização de R Markdown
- `rmarkdown` - Criação de documentos

---

## 📊 Resultados Esperados

Ao renderizar o R Markdown, você obterá:

1. **Documento HTML Profissional:**
   - Título e estrutura organizada
   - Código e resultados intercalados
   - Gráficos incorporados
   - Tabelas formatadas

2. **Análises Realizadas:**
   - Estatísticas descritivas
   - Tabelas de frequência
   - Gráficos de distribuição
   - Comparações entre grupos

3. **Interpretações:**
   - Conclusões sobre os dados
   - Identificação de padrões
   - Recomendações práticas

---

## ⚠️ Problemas Identificados

### 1. Erro de Digitação no Título
- **Problema:** "strees" → deveria ser "stress"
- **Solução:** Corrigir no cabeçalho YAML

### 2. Caminhos Relativos
- **Problema:** `read.csv("dados_exercio.csv")` pode quebrar
- **Solução:** Usar `file.path()` ou `here::here()`

### 3. Falta de Validação de Dados
- **Problema:** Não verifica se arquivo existe
- **Solução:** Adicionar verificação

### 4. Código Não Reproduzível
- **Problema:** Alguns resultados podem variar
- **Solução:** Adicionar `set.seed()` se houver aleatoriedade

### 5. Falta de Seções no Documento
- **Problema:** Documento poderia ter mais estrutura
- **Solução:** Adicionar mais seções e subseções

---

## 💡 Melhorias Sugeridas

### 1. Melhorar Cabeçalho YAML
```yaml
---
title: "Análise Exploratória: Qualidade de Sono e Estresse"
subtitle: "Análise de Dados de Colaboradores"
author: "Vinícius de Souza Cebalhos"
date: "`r Sys.Date()`"
output: 
  html_document:
    toc: true
    toc_float: true
    theme: flatly
    code_folding: hide
---
```

### 2. Adicionar Chunk de Configuração
```r
```{r setup, include=FALSE}
knitr::opts_chunk$set(
  echo = TRUE,
  warning = FALSE,
  message = FALSE,
  fig.width = 10,
  fig.height = 6
)
```
```

### 3. Usar ggplot2 para Gráficos
```r
# Em vez de gráficos base:
ggplot(dados, aes(x = BMI.Category)) +
  geom_bar(fill = "lightblue") +
  labs(title = "Distribuição por Categoria de IMC",
       x = "Categoria de IMC",
       y = "Frequência") +
  theme_minimal()
```

### 4. Adicionar Tabelas Formatadas
```r
# Usar kableExtra para tabelas bonitas
library(kableExtra)
dados %>%
  count(BMI.Category) %>%
  kable() %>%
  kable_styling()
```

### 5. Adicionar Interpretação dos Resultados
```r
# Após cada análise, adicionar interpretação:
cat("### Interpretação:\n")
cat("Observa-se que", percentual, "% dos colaboradores...\n")
```

---

## 📦 Dependências

### Pacotes Necessários
- `dplyr` - Manipulação de dados
- `ggplot2` - Visualização
- `knitr` - Renderização
- `rmarkdown` - Documentos
- `kableExtra` - Tabelas formatadas (opcional)

### Arquivos de Dados
- `dados_exercio.csv` - Dataset de colaboradores (374 observações)

---

## 📚 Recursos para Aprender R Markdown

- **R Markdown: The Definitive Guide:** https://bookdown.org/yihui/rmarkdown/
- **R Markdown Cheat Sheet:** https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf
- **R Markdown Gallery:** https://rmarkdown.rstudio.com/gallery.html

---

## ✅ Checklist da Aula

- [x] R Markdown principal funcional
- [x] Dataset carregado corretamente
- [x] Análise exploratória implementada
- [x] Gráficos gerados
- [x] Documento HTML renderizado
- [ ] Erro de digitação corrigido ("strees")
- [ ] Caminhos de arquivos corrigidos
- [ ] Tabelas formatadas com kableExtra
- [ ] README.md criado

---

**Autor:** Vinícius de Souza Cebalhos  
**Data:** 2024  
**Disciplina:** Estatística - UTFPR

