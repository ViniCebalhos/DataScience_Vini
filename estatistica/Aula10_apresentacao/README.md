# Aula 10 - Apresentação Final

**Disciplina:** Estatística  
**Linguagem:** R (R Markdown)  
**Objetivo:** Apresentação final de análise exploratória de dados

---

## 🎯 Objetivo da Aula

Esta aula consiste na **apresentação final** do curso, onde os alunos apresentam uma análise completa de um dataset de sua escolha. O objetivo é:

- Demonstrar domínio completo de análise exploratória de dados
- Criar apresentação profissional usando R Markdown
- Comunicar resultados de forma clara e impactante
- Aplicar todos os conceitos aprendidos no curso

---

## 📚 Conceitos Estatísticos Envolvidos

### Análise Exploratória de Dados Completa
- **Análise Univariada:** Uma variável por vez
- **Análise Bivariada:** Relações entre duas variáveis
- **Análise Multivariada:** Múltiplas variáveis simultaneamente
- **Visualização:** Gráficos profissionais e informativos
- **Interpretação:** Conclusões baseadas em dados

---

## 📁 Arquivos da Aula

### Trabalhos do Aluno
- **`Vinicius_Cebalhos.Rmd`** - Apresentação principal (análise de vinhos)
- **`ViniciusCebalhos_Atividade3.Rmd`** - Atividade 3
- **`2.Rmd`** - Outro trabalho

### Dataset Utilizado
- **`winemag-data-130k-v2.csv`** - Dataset com mais de 130.000 avaliações de vinhos:
  - Variáveis: título, país, variedade, pontuação, preço, descrição
  - Fonte: Wine Enthusiast

---

## 🔍 Análise do Trabalho `Vinicius_Cebalhos.Rmd`

### Estrutura do Documento

#### 1. **Cabeçalho YAML**
```yaml
---
title: "Análise de Vinhos: A Relação Entre Preço e Qualidade"
author: "Vinícius Cebalhos"
date: "`r Sys.Date()`"
output: 
  html_document:
    toc: true
    toc_float: true
    theme: united
    code_folding: hide
---
```

**Pontos Fortes:**
- ✅ Título descritivo e objetivo
- ✅ Autor identificado
- ✅ TOC ativado
- ✅ `code_folding: hide` oculta código por padrão

---

#### 2. **Introdução (linhas 24-27)**
```r
## Introdução

Este relatório apresenta uma análise exploratória da relação entre preço e qualidade de vinhos, utilizando um conjunto de dados com mais de 130.000 avaliações de vinhos.
```

**O que faz:**
- Contextualiza o problema
- Define o objetivo da análise
- Informa sobre o dataset

**Pontos Fortes:**
- ✅ Contextualização clara
- ✅ Objetivo bem definido

---

#### 3. **Carregamento e Limpeza (linhas 29-42)**
```r
wine_data <- read_csv("winemag-data-130k-v2.csv")

wine_data_clean <- wine_data %>%
  filter(!is.na(price), !is.na(points))

cat("Dados originais:", nrow(wine_data), "observações\n")
cat("Dados após limpeza:", nrow(wine_data_clean), "observações\n")
cat("Observações removidas:", nrow(wine_data) - nrow(wine_data_clean), "\n")
```

**O que faz:**
- Carrega dados do CSV
- Remove observações com valores ausentes em variáveis críticas
- Reporta perda de dados

**Conceitos:**
- **Limpeza de Dados:** Remoção de valores ausentes
- **Transparência:** Reportar perda de dados

**Pontos Fortes:**
- ✅ Limpeza adequada
- ✅ Transparência sobre perda de dados

---

#### 4. **Análise da Relação Preço vs Qualidade (linhas 50-67)**

##### 4.1 Gráfico de Dispersão
```r
ggplot(wine_data_clean, aes(x = price, y = points)) +
  geom_point(alpha = 0.2, color = "darkblue") +
  geom_smooth(method = "lm", color = "red", se = TRUE) +
  scale_x_log10(labels = dollar_format()) +
  labs(title = "Relação entre Preço e Pontuação do Vinho",
       subtitle = "Escala logarítmica do preço para melhor visualização",
       x = "Preço (USD, escala log)",
       y = "Pontuação (1-100)") +
  theme_minimal()
```

**O que faz:**
- Cria gráfico de dispersão
- Usa escala logarítmica no eixo X (preço)
- Adiciona linha de tendência (regressão linear)
- Formata eixos profissionalmente

**Conceitos:**
- **Escala Logarítmica:** Necessária quando dados têm grande variação
- **Linha de Tendência:** Mostra relação geral entre variáveis
- **Alpha:** Transparência para lidar com sobreposição de pontos

**Pontos Fortes:**
- ✅ Escala logarítmica apropriada
- ✅ Visualização clara
- ✅ Formatação profissional

---

##### 4.2 Teste de Correlação (linhas 69-100)
```r
cor_test <- cor.test(wine_data_clean$price, wine_data_clean$points)
cor_coef <- round(cor_test$estimate, 3)
p_value <- round(cor_test$p.value, 10)

# Interpretação didática
interpretacao <- case_when(
  abs(cor_coef) >= 0.7 ~ "forte",
  abs(cor_coef) >= 0.5 ~ "moderada",
  abs(cor_coef) >= 0.3 ~ "fraca",
  TRUE ~ "muito fraca"
)
```

**O que faz:**
- Calcula correlação de Pearson
- Testa significância estatística
- Interpreta força da correlação

**Conceitos:**
- **Correlação de Pearson:** Mede relação linear
- **p-valor:** Probabilidade de obter resultado por acaso
- **Interpretação:** Classifica força da correlação

**Pontos Fortes:**
- ✅ Teste estatístico apropriado
- ✅ Interpretação didática
- ✅ Explicação clara dos conceitos

---

## 🚀 Como Executar

### Pré-requisitos
1. R instalado (versão 4.0+)
2. RStudio (recomendado)
3. Arquivo `winemag-data-130k-v2.csv` na pasta

### Passo a Passo

1. **Abra o projeto RStudio:**
```r
# File > Open Project > Aula10_apresentacao.Rproj
```

2. **Abra o arquivo .Rmd:**
```r
# File > Open File > Vinicius_Cebalhos.Rmd
```

3. **Renderize o documento:**
```r
# No RStudio: Knit > Knit to HTML
# Ou no console:
rmarkdown::render("Vinicius_Cebalhos.Rmd")
```

### Dependências

Pacotes necessários:
- `tidyverse` - Manipulação e visualização
- `knitr` - Renderização
- `scales` - Formatação de eixos
- `gridExtra` - Layout de gráficos

---

## 📊 Resultados Esperados

1. **Documento HTML Profissional:**
   - Apresentação clara e organizada
   - Gráficos de alta qualidade
   - Interpretações dos resultados
   - Conclusões bem fundamentadas

2. **Análise Completa:**
   - Carregamento e limpeza de dados
   - Análise exploratória
   - Testes estatísticos
   - Visualizações profissionais
   - Conclusões e recomendações

---

## ⚠️ Problemas Identificados

### 1. Arquivo CSV Grande
- **Problema:** `winemag-data-130k-v2.csv` é muito grande (>75MB)
- **Solução:** Não versionar, usar `.gitignore` ou Git LFS

### 2. Caminho Relativo
- **Problema:** `read_csv("winemag-data-130k-v2.csv")` pode quebrar
- **Solução:** Usar `file.path()` ou `here::here()`

### 3. Falta de Validação
- **Problema:** Não verifica se arquivo existe
- **Solução:** Adicionar verificação

---

## 💡 Melhorias Sugeridas

### 1. Adicionar Mais Análises
```r
# Análise por país
# Análise por variedade
# Análise temporal (se houver data)
```

### 2. Adicionar Seção de Metodologia
```r
## Metodologia

1. Carregamento e limpeza dos dados
2. Análise exploratória inicial
3. Análise da relação preço-qualidade
4. Testes estatísticos
5. Conclusões
```

### 3. Adicionar Visualizações Adicionais
```r
# Boxplot de preço por país
# Histograma de pontuações
# Gráfico de barras de países mais frequentes
```

### 4. Adicionar Análise de Outliers
```r
# Identificar vinhos muito caros ou muito baratos
# Analisar se são outliers legítimos ou erros
```

### 5. Adicionar Recomendações Práticas
```r
## Recomendações

Baseado na análise:
1. Para consumidores: ...
2. Para produtores: ...
3. Para pesquisadores: ...
```

---

## 📦 Dependências

### Pacotes Necessários
- `tidyverse` - Manipulação e visualização
- `knitr` - Renderização
- `scales` - Formatação
- `gridExtra` - Layout

### Arquivos de Dados
- `winemag-data-130k-v2.csv` - Dataset de vinhos (não versionado - muito grande)

---

## ✅ Checklist da Aula

- [x] Apresentação completa
- [x] R Markdown bem estruturado
- [x] Análise exploratória implementada
- [x] Gráficos profissionais
- [x] Testes estatísticos
- [ ] Arquivo CSV no .gitignore
- [ ] Caminhos corrigidos
- [ ] README.md criado

---

**Autor:** Vinícius de Souza Cebalhos  
**Data:** 2024  
**Disciplina:** Estatística - UTFPR

