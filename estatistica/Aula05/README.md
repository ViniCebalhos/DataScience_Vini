# Transformações de Variáveis e Cálculo de Tamanho de Amostra

**Linguagem:** R  
**Técnicas:** Transformações estatísticas, normalização, padronização, cálculo de tamanho de amostra

---

## Sobre o Projeto

Este projeto demonstra competências em transformações de variáveis para normalização de dados e cálculo de tamanho de amostra para estudos estatísticos. Inclui verificação de normalidade, aplicação de transformações matemáticas e determinação de tamanhos amostrais adequados.

---

## Competências Demonstradas

### Transformações de Variáveis
- **Padronização (Z-score):** Normalização para média 0 e desvio padrão 1
- **Normalização (Min-Max):** Escala de 0 a 1
- **Transformações Matemáticas:** Logarítmica, raiz quadrada, raiz cúbica, inversa
- **Verificação de Normalidade:** Q-Q plots e testes estatísticos

### Cálculo de Tamanho de Amostra
- **Para Estimar Média:** Cálculo baseado em nível de confiança e margem de erro
- **Para Estimar Proporção:** Cálculo para variáveis categóricas
- **Correção para População Finita:** Ajuste quando população é conhecida

---

## Estrutura do Projeto

### Scripts Principais
- **`aula_05.R`** - Script principal com todas as análises
- **`definitions.R`** - Definições e configurações
- **`install_load_packages.R`** - Instalação e carregamento de pacotes

### Dataset Utilizado
- **`birthwt`** - Dataset do pacote `MASS` com dados de peso ao nascer

---

## Análise Implementada

### 1. Verificação de Normalidade

**Q-Q Plots:**
```r
qqnorm(dados$variavel)
qqline(dados$variavel)
```

**Testes de Normalidade:**
```r
shapiro.test(dados$variavel)  # Para amostras < 5000
```

### 2. Transformações de Variáveis

**Padronização (Z-score):**
```r
z_score <- (x - mean(x)) / sd(x)
```

**Normalização (Min-Max):**
```r
min_max <- (x - min(x)) / (max(x) - min(x))
```

**Transformação Logarítmica:**
```r
log_transform <- log(x)
```

### 3. Cálculo de Tamanho de Amostra

**Para Estimar Média:**
```r
n <- (Z^2 * S^2) / e^2
```

**Para Estimar Proporção:**
```r
n <- (Z^2 * p * (1-p)) / e^2
```

---

## Tecnologias Utilizadas

### Bibliotecas R
- **MASS** - Dataset birthwt
- **car** - Q-Q plots melhorados
- **nortest** - Testes de normalidade (Anderson-Darling)
- **samplingbook** - Cálculo de tamanho de amostra

---

## Resultados Principais

### Transformações Aplicadas
- Análise de distribuições antes e depois das transformações
- Comparação de normalidade
- Seleção de transformação mais adequada

### Tamanhos de Amostra Calculados
- Para diferentes níveis de confiança
- Para diferentes margens de erro
- Com e sem correção para população finita

---

## Como Executar

### Pré-requisitos
```r
# Instalar pacotes necessários
source("install_load_packages.R")
```

### Executar Análise
```r
# Executar script principal
source("aula_05.R")
```

---

## Métricas e Visualizações

- Q-Q plots para verificação de normalidade
- Histogramas antes e depois das transformações
- Comparação de estatísticas descritivas
- Tabelas de tamanhos de amostra calculados

---

**Autor:** Vinícius de Souza Cebalhos
