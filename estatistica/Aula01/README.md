# Aula 01 - Análise Exploratória de Dados (Uma Variável)

**Disciplina:** Estatística  
**Linguagem:** R  
**Objetivo:** Introdução à Análise Exploratória de Dados (AED) para uma única variável

---

## 🎯 Objetivo da Aula

Esta aula introduz os conceitos fundamentais de **Análise Exploratória de Dados (AED)** focando na análise de **uma única variável**. Os alunos aprendem a:

- Descrever e resumir dados de forma estatística
- Visualizar distribuições de variáveis qualitativas e quantitativas
- Calcular medidas de tendência central e dispersão
- Interpretar gráficos descritivos

---

## 📚 Conceitos Estatísticos Envolvidos

### Variáveis Qualitativas (Categóricas)
- **Frequência Absoluta:** Número de ocorrências de cada categoria
- **Frequência Relativa:** Proporção ou percentual de cada categoria
- **Gráficos:** Gráficos de barras e gráficos de pizza (setores)

### Variáveis Quantitativas (Numéricas)
- **Medidas de Tendência Central:**
  - Média aritmética
  - Mediana
  - Quantis (quartis, percentis)
- **Medidas de Dispersão:**
  - Variância
  - Desvio padrão
- **Gráficos:**
  - Histograma
  - Boxplot (diagrama de caixa)

---

## 📁 Arquivos da Aula

### Scripts Principais
- **`aed_1var.R`** - Script principal com toda a análise
- **`definitions.R`** - Definições e configurações (encoding)
- **`install_load_packages.R`** - Instalação e carregamento de pacotes
- **`template_aula.R`** - Template para estrutura de scripts

### Dataset Utilizado
- **`diamonds`** - Dataset do pacote `ggplot2` com informações de ~54.000 diamantes

---

## 🔍 Análise do Código

### Estrutura do Script `aed_1var.R`

#### 1. **Configuração Inicial (linhas 1-16)**
```r
# Define o diretório do projeto
project_root_path <- paste0(getwd(), "/.")

# Carrega definições (encoding)
source(paste0(project_root_path, "/definitions.R"))

# Instala e carrega pacotes necessários
source(paste0(project_root_path, "/install_load_packages.R"), encoding = encoding)
```

**O que faz:**
- Define o caminho do projeto (diretório atual)
- Carrega configurações (encoding UTF-8)
- Instala e carrega todos os pacotes necessários automaticamente

**Problemas identificados:**
- ⚠️ Uso de `paste0(getwd(), "/.")` é redundante (equivalente a `getwd()`)
- ⚠️ Caminho relativo pode quebrar se executado de outro diretório

**Sugestão de melhoria:**
```r
# Usar here::here() ou definir explicitamente
project_root_path <- here::here()
# ou
project_root_path <- getwd()
```

---

#### 2. **Carregamento dos Dados (linhas 22-35)**
```r
dados <- diamonds  # Dataset do pacote ggplot2
View(dados)
?diamonds
dim(dados)
```

**O que faz:**
- Carrega o dataset `diamonds` do pacote `ggplot2`
- Visualiza os dados no RStudio
- Mostra informações sobre o dataset
- Exibe dimensões (número de linhas e colunas)

**Conceitos:**
- **Tibble:** Tipo especial de data frame do tidyverse, mais eficiente e informativo
- **Dimensões:** `dim()` retorna (n_linhas, n_colunas)

---

#### 3. **Análise de Variável Qualitativa - Cut (linhas 42-70)**

##### 3.1 Tabelas de Frequência
```r
freq_abs <- table(dados$cut)
freq_rel <- round(prop.table(freq_abs)*100, 1)
```

**O que faz:**
- `table()`: Cria tabela de frequência absoluta
- `prop.table()`: Calcula proporções (frequência relativa)
- `round(..., 1)`: Arredonda para 1 casa decimal

**Conceitos:**
- **Frequência Absoluta:** Contagem simples de cada categoria
- **Frequência Relativa:** Proporção de cada categoria (soma = 100%)

##### 3.2 Gráficos de Barras
```r
gbarras2 <- barplot(freq_abs, 
                    xlab = 'Qualidade do corte',
                    ylab = 'Frequência absoluta',
                    main = "Qualidade do corte (n)",
                    col = 'blue',
                    ylim = c(0,23500))
text(x = gbarras2, y = freq_abs+1000, labels = as.character(freq_abs))
```

**O que faz:**
- Cria gráfico de barras com frequências absolutas
- Adiciona rótulos nos eixos e título
- Adiciona valores numéricos no topo de cada barra

**Conceitos:**
- **Gráfico de Barras:** Ideal para variáveis qualitativas
- **Parâmetros importantes:**
  - `xlab`, `ylab`: Rótulos dos eixos
  - `main`: Título do gráfico
  - `col`: Cor das barras
  - `ylim`: Limites do eixo Y

##### 3.3 Gráfico de Pizza
```r
gpizza2 <- pie(freq_abs,
               labels = paste0(freq_rel,"%"),
               border = "white",
               col = rainbow(length(freq_abs)),
               main = 'Qualidade do corte')
legend("bottomright", levels(dados$cut), fill = rainbow(length(freq_abs)), cex = 0.7)
```

**O que faz:**
- Cria gráfico de pizza (setores) com percentuais
- Adiciona legenda com cores correspondentes

**⚠️ Problema:** Gráfico de pizza geralmente não é recomendado para análise estatística (difícil comparar áreas)

**Sugestão:** Preferir gráfico de barras horizontal

---

#### 4. **Análise de Variável Quantitativa - Price (linhas 73-105)**

##### 4.1 Medidas Descritivas
```r
media <- mean(dados$price)
mediana <- median(dados$price)
quantis_default <- quantile(dados$price)
variancia <- var(dados$price)
desvio_padrao <- sd(dados$price)
```

**O que faz:**
- Calcula medidas de tendência central (média, mediana)
- Calcula quartis (Q1, Q2=mediana, Q3)
- Calcula medidas de dispersão (variância, desvio padrão)

**Conceitos:**
- **Média:** Soma dos valores dividida pelo número de observações
- **Mediana:** Valor que divide os dados ao meio (50% acima, 50% abaixo)
- **Quartis:** Dividem os dados em 4 partes iguais
- **Variância:** Medida de dispersão (média dos quadrados dos desvios)
- **Desvio Padrão:** Raiz quadrada da variância (mesma unidade dos dados)

##### 4.2 Histograma
```r
ghist2 <- hist(dados$price,
               main = "Histograma preço",
               ylab = "Frequência",
               xlab = "Preço",
               col = "lightgreen",
               border = "white",
               breaks = seq(0, 19000, by = 500))
```

**O que faz:**
- Cria histograma mostrando distribuição dos preços
- Define intervalos (breaks) de R$ 500 em R$ 500

**Conceitos:**
- **Histograma:** Mostra a forma da distribuição
- **Breaks:** Define os intervalos (bins) do histograma
- Permite identificar:
  - Simetria/assimetria
  - Moda(s)
  - Outliers

##### 4.3 Boxplot
```r
gboxplot2 <- boxplot(dados$price,
                     pch = "*",
                     col = "lightblue",
                     border = "darkgrey",
                     boxwex = 0.3)
```

**O que faz:**
- Cria diagrama de caixa (boxplot)
- Mostra quartis, mediana e outliers

**Conceitos:**
- **Boxplot:** Mostra:
  - Q1, Q2 (mediana), Q3
  - Bigodes (whiskers): 1.5 × IQR
  - Outliers: pontos além dos bigodes
- **IQR:** Intervalo interquartil (Q3 - Q1)

---

## 🚀 Como Executar

### Pré-requisitos
1. R instalado (versão 4.0+)
2. RStudio (recomendado)

### Passo a Passo

1. **Abra o projeto RStudio:**
```r
# No RStudio: File > Open Project > Aula01.Rproj
```

2. **Execute o script principal:**
```r
source("aed_1var.R")
```

Ou execute célula por célula no RStudio.

### Dependências

Os pacotes são instalados automaticamente pelo script `install_load_packages.R`:
- `dplyr` - Manipulação de dados
- `ggplot2` - Visualização (contém dataset diamonds)
- `graphics` - Gráficos base do R

---

## 📊 Resultados Esperados

Ao executar o script, você verá:

1. **Informações do dataset:**
   - Dimensões: 53.940 linhas × 10 colunas
   - Estrutura dos dados

2. **Análise da variável `cut` (qualitativa):**
   - Tabelas de frequência absoluta e relativa
   - Gráfico de barras com frequências
   - Gráfico de pizza com percentuais

3. **Análise da variável `price` (quantitativa):**
   - Estatísticas descritivas (média, mediana, desvio padrão)
   - Histograma da distribuição
   - Boxplot com identificação de outliers

---

## ⚠️ Problemas Identificados

### 1. Caminhos Relativos
- **Problema:** `project_root_path <- paste0(getwd(), "/.")` é redundante
- **Solução:** Usar `getwd()` ou `here::here()`

### 2. Gráfico de Pizza
- **Problema:** Gráfico de pizza não é ideal para análise estatística
- **Solução:** Preferir gráfico de barras horizontal

### 3. Falta de Comentários
- **Problema:** Alguns blocos de código não têm comentários explicativos
- **Solução:** Adicionar comentários explicando o propósito de cada seção

### 4. Código Não Modularizado
- **Problema:** Tudo em um único script
- **Solução:** Separar em funções reutilizáveis

### 5. Falta de Salvamento de Gráficos
- **Problema:** Gráficos são apenas exibidos, não salvos
- **Solução:** Adicionar código para salvar gráficos em `figures/`

---

## 💡 Melhorias Sugeridas

### 1. Usar Tidyverse Consistentemente
```r
# Em vez de:
freq_abs <- table(dados$cut)

# Usar:
freq_abs <- dados %>%
  count(cut) %>%
  pull(n)
```

### 2. Criar Funções para Análises Repetitivas
```r
analisar_variavel_qualitativa <- function(dados, variavel) {
  # Código reutilizável
}
```

### 3. Salvar Gráficos
```r
ggsave("figures/histograma_preco.png", plot = ghist2, width = 10, height = 6)
```

### 4. Usar ggplot2 em vez de gráficos base
```r
# Mais moderno e flexível
ggplot(dados, aes(x = cut)) +
  geom_bar() +
  labs(title = "Distribuição da Qualidade do Corte")
```

### 5. Adicionar Validação de Dados
```r
# Verificar se dados existem
if (!exists("dados")) {
  stop("Dataset não encontrado!")
}
```

---

## 📦 Dependências

### Pacotes Necessários
- `dplyr` - Manipulação de dados
- `ggplot2` - Visualização e dataset diamonds
- `graphics` - Gráficos base do R

### Instalação Automática
O script `install_load_packages.R` instala automaticamente todos os pacotes necessários.

---

## 📚 Referências

- **Livro R para Data Science:** https://r4ds.had.co.nz/
- **Curso-R:** https://livro.curso-r.com/
- **Estatística Básica:** https://rpubs.com/EstatBasica

---

## ✅ Checklist da Aula

- [x] Script principal funcional
- [x] Dataset carregado corretamente
- [x] Análise de variável qualitativa implementada
- [x] Análise de variável quantitativa implementada
- [x] Gráficos gerados
- [ ] Gráficos salvos em arquivos
- [ ] Código comentado adequadamente
- [ ] Funções modularizadas
- [ ] README.md criado

---

**Autor:** Vinícius de Souza Cebalhos  
**Data:** 2024  
**Disciplina:** Estatística - UTFPR

