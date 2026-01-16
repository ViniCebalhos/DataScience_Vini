# Análise Exploratória Univariada em R

**Linguagem:** R  
**Técnicas:** Estatística descritiva, visualização de dados, análise de distribuições

---

## 📊 Sobre o Projeto

Este projeto demonstra competências em análise exploratória de dados univariada, focando na descrição e visualização de variáveis individuais. A análise cobre tanto variáveis qualitativas (categóricas) quanto quantitativas (numéricas), utilizando técnicas estatísticas descritivas e visualizações profissionais.

---

## 🎯 Competências Demonstradas

### Estatística Descritiva
- **Medidas de Tendência Central:** Média, mediana, moda, quartis
- **Medidas de Dispersão:** Variância, desvio padrão, amplitude interquartil
- **Análise de Frequências:** Frequências absolutas e relativas para variáveis categóricas

### Visualização de Dados
- Gráficos de barras e pizza para variáveis qualitativas
- Histogramas e boxplots para variáveis quantitativas
- Análise de distribuições e identificação de outliers

### Programação em R
- Manipulação de dados com dplyr
- Visualização com ggplot2
- Cálculo de estatísticas descritivas

---

## 📁 Estrutura do Projeto

### Scripts Principais
- **`aed_1var.R`** - Script principal com todas as análises
- **`definitions.R`** - Definições e configurações
- **`install_load_packages.R`** - Instalação e carregamento de pacotes

### Dataset Utilizado
- **`diamonds`** - Dataset do pacote `ggplot2` com informações de ~54.000 diamantes

---

## 🔍 Análise Implementada

### 1. Análise de Variáveis Qualitativas

**Frequências:**
```r
table(diamonds$cut)  # Frequências absolutas
prop.table(table(diamonds$cut)) * 100  # Frequências relativas (%)
```

**Visualizações:**
- Gráficos de barras
- Gráficos de pizza (setores)
- Análise de distribuição de categorias

### 2. Análise de Variáveis Quantitativas

**Estatísticas Descritivas:**
```r
summary(diamonds$price)  # Resumo estatístico completo
mean(diamonds$price)     # Média
median(diamonds$price)   # Mediana
sd(diamonds$price)       # Desvio padrão
quantile(diamonds$price, probs = c(0.25, 0.5, 0.75))  # Quartis
```

**Visualizações:**
- Histogramas para análise de distribuição
- Boxplots para identificação de outliers
- Análise de assimetria e curtose

### 3. Análise Exploratória Completa

**Técnicas Aplicadas:**
- Resumo estatístico completo de todas as variáveis
- Identificação de valores ausentes
- Análise de outliers
- Verificação de distribuições

---

## 🛠️ Tecnologias Utilizadas

### Bibliotecas R
- **dplyr** - Manipulação de dados
- **ggplot2** - Visualização de dados
- **base R** - Funções estatísticas básicas

---

## 📈 Resultados Principais

### Insights Identificados
- Distribuição de características de diamantes (cut, color, clarity)
- Análise de preços e variáveis numéricas (carat, depth, table)
- Identificação de padrões e outliers
- Estatísticas descritivas completas

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
source("aed_1var.R")
```

---

## 📊 Métricas e Visualizações

- Tabelas de frequência para variáveis categóricas
- Estatísticas descritivas completas (média, mediana, desvio padrão, quartis)
- Histogramas de distribuição
- Boxplots para análise de outliers
- Gráficos de barras e pizza

---

**Autor:** Vinícius de Souza Cebalhos
