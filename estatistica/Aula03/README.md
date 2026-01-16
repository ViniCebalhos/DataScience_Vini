# Análise Exploratória Bivariada em R

**Linguagem:** R  
**Técnicas:** Análise exploratória de dados, correlação, visualização estatística

---

## 📊 Sobre o Projeto

Este projeto demonstra competências em análise exploratória de dados bivariada, identificando relações, associações e padrões entre variáveis. A análise cobre diferentes tipos de relações: qualitativa × qualitativa, quantitativa × quantitativa, e qualitativa × quantitativa.

---

## 🎯 Competências Demonstradas

### Análise Bivariada
- **Tabelas de Contingência:** Análise de frequências conjuntas entre variáveis categóricas
- **Correlação:** Cálculo de correlação de Pearson e Spearman
- **Visualização:** Gráficos de dispersão, matriz de correlação, boxplots comparativos
- **Análise Multivariada:** Gráficos de pares e visualizações facetadas

### Técnicas Estatísticas
- Tabelas de contingência com frequências absolutas e relativas
- Cálculo de correlações lineares e não-lineares
- Comparação de distribuições entre grupos
- Visualização de relações multivariadas

---

## 📁 Estrutura do Projeto

### Scripts Principais
- **`aula_03.R`** - Script principal com todas as análises
- **`definitions.R`** - Definições e configurações
- **`install_load_packages.R`** - Instalação e carregamento de pacotes

### Datasets Utilizados
- **`diamonds`** - Dataset do pacote `ggplot2` (~54.000 diamantes)
- **`veiculos.xls`** - Dataset de veículos (preço, motor, comprimento, procedência)

---

## 🔍 Análise Implementada

### 1. Análise Qualitativa × Qualitativa

**Tabelas de Contingência:**
```r
tab_n <- table(diamonds$cut, diamonds$clarity)  # Frequências absolutas
round(prop.table(tab_n)*100, 2)  # Frequências relativas totais
tab_freq_linha <- round(prop.table(tab_n, margin=1)*100, 2)  # Por linha
tab_freq_col <- round(prop.table(tab_n, margin=2)*100, 2)  # Por coluna
```

**Técnicas:**
- Criação de tabelas cruzadas
- Cálculo de frequências relativas por linha e coluna
- Agregação de categorias para simplificação
- Visualização com gráficos de barras agrupadas

### 2. Análise Quantitativa × Quantitativa

**Correlação:**
```r
cor(diamonds$carat, diamonds$price, method = "pearson")
cor(diamonds$carat, diamonds$price, method = "spearman")
```

**Técnicas:**
- Cálculo de correlação de Pearson (linear)
- Cálculo de correlação de Spearman (monotônica)
- Matriz de correlação para múltiplas variáveis
- Gráficos de dispersão com linha de tendência

### 3. Análise Qualitativa × Quantitativa

**Comparação de Grupos:**
```r
diamonds %>%
  group_by(cut) %>%
  summarise(
    media = mean(price),
    mediana = median(price),
    desvio = sd(price)
  )
```

**Técnicas:**
- Estatísticas descritivas por grupo
- Boxplots comparativos
- Análise de distribuições condicionais

### 4. Análise Multivariada

**Visualizações:**
- Gráficos de pares (pairs plot)
- Matriz de correlação visual
- Gráficos de dispersão com símbolos diferenciados
- Visualizações facetadas por categoria

---

## 🛠️ Tecnologias Utilizadas

### Bibliotecas R
- **dplyr** - Manipulação de dados
- **ggplot2** - Visualização de dados
- **corrplot** - Matriz de correlação visual
- **tidyr** - Organização de dados
- **readxl** - Leitura de arquivos Excel

---

## 📈 Resultados Principais

### Insights Identificados
- Relações entre características de diamantes (cut, clarity, carat, price)
- Padrões de correlação entre variáveis numéricas
- Diferenças de distribuição entre grupos categóricos
- Visualizações profissionais de relações multivariadas

---

## 🚀 Como Executar

### Pré-requisitos
```r
# Instalar pacotes necessários
source("install_load_packages.R")
```

### Executar Análise
```r
# Executar script principal
source("aula_03.R")
```

---

## 📊 Métricas e Visualizações

- Tabelas de contingência para variáveis categóricas
- Matriz de correlação para variáveis numéricas
- Gráficos de dispersão com análise de tendência
- Boxplots comparativos por grupo
- Gráficos de pares para análise multivariada

---

**Autor:** Vinícius de Souza Cebalhos
