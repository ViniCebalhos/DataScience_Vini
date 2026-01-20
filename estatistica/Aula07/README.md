# Análise Estatística com Testes Não-Paramétricos

**Linguagem:** R
**Técnicas:** Testes estatísticos, análise temporal, comparação de grupos, testes não-paramétricos

---

## Sobre o Projeto

Este projeto demonstra competências em análise estatística aplicada a dados reais de bike sharing, utilizando testes estatísticos paramétricos e não-paramétricos para comparar grupos e testar hipóteses. Inclui análise temporal, comparação de grupos e interpretação de resultados estatísticos.

---

## Competências Demonstradas

### Testes Estatísticos
- **Testes de Normalidade:** Shapiro-Wilk, Anderson-Darling
- **Testes de Homogeneidade:** Levene
- **Testes de Comparação:**
 - Teste t de Student (2 grupos, paramétrico)
 - Teste de Wilcoxon (2 grupos, não-paramétrico)
 - ANOVA (3+ grupos, paramétrico)
 - Kruskal-Wallis (3+ grupos, não-paramétrico)
 - Teste de Dunn (post-hoc)
- **Testes de Correlação:** Spearman

### Análise de Dados
- Análise temporal de séries
- Comparação de grupos categóricos
- Análise de relações entre variáveis
- Interpretação de resultados estatísticos

---

## Estrutura do Projeto

### Scripts Principais
- **`definitions.R`** - Definições e configurações
- **`install_load_packages.R`** - Instalação e carregamento de pacotes

### Dataset Utilizado
- **`yulu_bike_sharing_dataset.csv`** - Dataset de bike sharing com:
 - Dados temporais (data, hora)
 - Variáveis climáticas (temperatura, umidade, vento)
 - Variáveis categóricas (estação, feriado, dia útil, clima)
 - Variável resposta: número de aluguéis (count)

---

## Análise Implementada

### 1. Testes de Normalidade

**Shapiro-Wilk (amostras < 5000):**
```r
shapiro.test(dados$variavel)
```

**Anderson-Darling (amostras grandes):**
```r
nortest::ad.test(dados$variavel)
```

### 2. Testes de Comparação

**Teste t de Student (2 grupos):**
```r
t.test(variavel ~ grupo, data = dados)
```

**Teste de Wilcoxon (2 grupos, não-paramétrico):**
```r
wilcox.test(variavel ~ grupo, data = dados)
```

**Kruskal-Wallis (3+ grupos):**
```r
kruskal.test(variavel ~ grupo, data = dados)
```

**Teste de Dunn (post-hoc):**
```r
dunn.test(dados$variavel, dados$grupo)
```

### 3. Análise Temporal

**Padrões Temporais:**
- Análise por estação do ano
- Análise por dia da semana
- Análise por hora do dia
- Identificação de tendências

---

## Tecnologias Utilizadas

### Bibliotecas R
- **dplyr** - Manipulação de dados
- **ggplot2** - Visualização
- **nortest** - Testes de normalidade
- **dunn.test** - Teste de Dunn
- **car** - Teste de Levene

---

## Resultados Principais

### Testes Estatísticos Aplicados
- Verificação de normalidade das distribuições
- Comparação de grupos categóricos
- Identificação de diferenças significativas
- Análise de correlações

### Insights Identificados
- Padrões temporais de aluguel de bikes
- Efeito de variáveis climáticas
- Diferenças entre grupos (estação, dia útil, etc.)
- Relações entre variáveis

---

## Como Executar

### Pré-requisitos
```r
# Instalar pacotes necessários
source("install_load_packages.R")
```

### Executar Análise
```r
# Executar análises específicas conforme necessário
```

---

## Métricas e Visualizações

- Resultados de testes estatísticos (p-valores, estatísticas)
- Gráficos de comparação de grupos (boxplots)
- Análise temporal (séries temporais)
- Tabelas de resultados estatísticos

---

**Autor:** Vinícius de Souza Cebalhos
