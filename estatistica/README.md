# 📊 Estatística - Trabalhos e Projetos

Esta pasta contém todos os trabalhos desenvolvidos na disciplina de **Estatística** da pós-graduação em Ciência de Dados.

**Linguagem:** R  
**Ambiente:** RStudio  
**Formato:** Scripts R (.R) e R Markdown (.Rmd)

---

## 🎯 Sobre a Disciplina

A disciplina de Estatística aborda análise exploratória de dados, testes estatísticos e criação de relatórios reprodutíveis usando R. Os alunos aprendem desde conceitos básicos de estatística descritiva até aplicação de testes estatísticos em problemas reais.

---

## 📚 Estrutura das Aulas

### 📖 [Aula 01 - Análise Exploratória de Dados (Uma Variável)](./Aula01/)
**Conceitos:** Estatística descritiva, variáveis qualitativas e quantitativas, gráficos descritivos

**Conteúdo:**
- Análise de variáveis qualitativas (frequências, gráficos de barras, pizza)
- Análise de variáveis quantitativas (medidas de tendência central, dispersão, histogramas, boxplots)
- Dataset: `diamonds` (pacote ggplot2)

[📖 Ver Aula](./Aula01/)

---

### 📖 [Aula 03 - Análise Exploratória de Dados (Duas Variáveis)](./Aula03/)
**Conceitos:** Análise bivariada, tabelas de contingência, correlação, comparação de grupos

**Conteúdo:**
- Análise qualitativa × qualitativa (tabelas de contingência)
- Análise quantitativa × quantitativa (correlação, gráficos de dispersão)
- Análise qualitativa × quantitativa (boxplots por grupo)
- Análise de múltiplas variáveis (gráficos de pares, matriz de correlação)
- Dataset: `diamonds` e `veiculos.xls`

[📖 Ver Aula](./Aula03/)

---

### 📖 [Aula 04 - Análise Exploratória com R Markdown](./Aula04/)
**Conceitos:** R Markdown, relatórios reprodutíveis, análise completa de dataset real

**Conteúdo:**
- Criação de documentos R Markdown
- Análise exploratória completa de dataset de colaboradores
- Visualizações profissionais
- Interpretação de resultados
- Dataset: `dados_exercio.csv` (374 colaboradores)

[📖 Ver Aula](./Aula04/)

---

### 📖 [Aula 05 - Transformações de Variáveis e Tamanho de Amostra](./Aula05/)
**Conceitos:** Normalidade, Q-Q plots, transformações, padronização, normalização, cálculo de tamanho de amostra

**Conteúdo:**
- Q-Q plots para verificar normalidade
- Transformações matemáticas (log, raiz, inversa)
- Padronização (Z-score)
- Normalização (Min-Max)
- Cálculo de tamanho de amostra para média e proporção
- Dataset: `birthwt` (pacote MASS)

[📖 Ver Aula](./Aula05/)

---

### 📖 [Aula 07 - Análise de Dados de Bike Sharing](./Aula07/)
**Conceitos:** Análise temporal, testes estatísticos, comparação de grupos, testes não-paramétricos

**Conteúdo:**
- Análise exploratória de dados temporais
- Testes de normalidade (Shapiro-Wilk, Anderson-Darling)
- Testes de comparação (Wilcoxon, Kruskal-Wallis, Dunn)
- Testes de correlação (Spearman)
- Dataset: `yulu_bike_sharing_dataset.csv`

[📖 Ver Aula](./Aula07/)

---

### 📖 [Aula 08 - Avaliação e Trabalhos em Grupo](./Aula08_avaliacao/)
**Conceitos:** Aplicação completa de análise exploratória, trabalho em equipe, apresentação de resultados

**Conteúdo:**
- Trabalho em grupo de análise exploratória completa
- Criação de relatório profissional com R Markdown
- Análise do dataset diamonds
- Dataset: `diamonds` (pacote ggplot2)

[📖 Ver Aula](./Aula08_avaliacao/)

---

### 📖 [Aula 10 - Apresentação Final](./Aula10_apresentacao/)
**Conceitos:** Apresentação final, análise completa de dataset escolhido, comunicação de resultados

**Conteúdo:**
- Análise exploratória completa de dataset de vinhos
- Relação entre preço e qualidade
- Testes de correlação
- Visualizações profissionais
- Dataset: `winemag-data-130k-v2.csv` (130.000+ avaliações de vinhos)

[📖 Ver Aula](./Aula10_apresentacao/)

---

### 📖 [Recuperação](./recuperacao/)
Trabalho de recuperação da disciplina.

[📖 Ver Recuperação](./recuperacao/)

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

### Principais
- **R** - Linguagem de programação estatística
- **RStudio** - Ambiente de desenvolvimento
- **R Markdown** - Documentos reprodutíveis

### Bibliotecas R Principais
- **dplyr** - Manipulação de dados
- **ggplot2** - Visualização de dados
- **tidyr** - Organização de dados
- **lubridate** - Manipulação de datas
- **skimr** - Resumo estatístico moderno
- **knitr** - Renderização de R Markdown
- **kableExtra** - Tabelas formatadas

### Bibliotecas para Testes Estatísticos
- **car** - Testes estatísticos e Q-Q plots melhorados
- **nortest** - Testes de normalidade (Anderson-Darling)
- **dunn.test** - Teste de Dunn (post-hoc)
- **samplingbook** - Cálculo de tamanho de amostra

### Bibliotecas para Visualização
- **corrplot** - Matriz de correlação
- **graphics** - Gráficos base do R
- **scales** - Formatação de eixos

---

## 📊 Competências Demonstradas

### Técnicas Estatísticas
- ✅ Estatística Descritiva (média, mediana, desvio padrão, quartis)
- ✅ Análise Exploratória de Dados (AED)
- ✅ Análise Univariada (uma variável)
- ✅ Análise Bivariada (duas variáveis)
- ✅ Análise Multivariada (múltiplas variáveis)
- ✅ Verificação de Normalidade (Q-Q plots, testes)
- ✅ Transformações de Variáveis (log, raiz, padronização, normalização)
- ✅ Cálculo de Tamanho de Amostra

### Testes Estatísticos
- ✅ Testes de Normalidade (Shapiro-Wilk, Anderson-Darling)
- ✅ Testes de Homogeneidade de Variâncias (Levene)
- ✅ Testes de Comparação de Médias/Medianas:
  - Teste t de Student (2 grupos, paramétrico)
  - Teste de Wilcoxon (2 grupos, não-paramétrico)
  - ANOVA (3+ grupos, paramétrico)
  - Kruskal-Wallis (3+ grupos, não-paramétrico)
  - Teste de Dunn (post-hoc)
- ✅ Testes de Correlação (Pearson, Spearman)

### Programação e Documentação
- ✅ Programação em R
- ✅ Uso de tidyverse (dplyr, ggplot2, tidyr)
- ✅ Criação de documentos R Markdown
- ✅ Visualização profissional de dados
- ✅ Relatórios reprodutíveis

---

## 📁 Estrutura de Pastas

```
estatistica/
├── README.md                    # Este arquivo
├── Aula01/                      # AED - Uma Variável
│   ├── README.md
│   ├── aed_1var.R
│   └── ...
├── Aula03/                      # AED - Duas Variáveis
│   ├── README.md
│   ├── aula_03.R
│   └── ...
├── Aula04/                      # R Markdown
│   ├── README.md
│   ├── Aula04_AED.Rmd
│   └── ...
├── Aula05/                      # Transformações e Tamanho de Amostra
│   ├── README.md
│   ├── aula_05.R
│   └── ...
├── Aula07/                      # Bike Sharing
│   ├── README.md
│   └── ...
├── Aula08_avaliacao/            # Trabalhos em Grupo
│   ├── README.md
│   ├── Grupo_05.Rmd
│   └── ...
├── Aula10_apresentacao/         # Apresentação Final
│   ├── README.md
│   ├── Vinicius_Cebalhos.Rmd
│   └── ...
├── recuperacao/                 # Trabalho de Recuperação
│   └── README.md
└── template/                    # Template de aula
```

---

## 🚀 Como Executar

### Pré-requisitos

1. **Instale o R:**
```bash
sudo apt-get install r-base
```

2. **Instale o RStudio (opcional, mas recomendado):**
```bash
# Baixe do site oficial: https://www.rstudio.com/products/rstudio/download/
```

3. **Abra o projeto RStudio:**
```bash
# Cada pasta contém um arquivo .Rproj
# Abra no RStudio: File > Open Project
```

### Executar Scripts R

```r
# No RStudio ou R console
source("aula_03.R")
```

### Compilar R Markdown

```r
# No RStudio
rmarkdown::render("arquivo.Rmd")

# Ou use o botão "Knit" no RStudio
```

---

## 📝 Notas Importantes

- Os projetos estão organizados por aula
- Cada pasta contém um arquivo `.Rproj` para abrir no RStudio
- Alguns datasets podem precisar ser baixados separadamente
- Os arquivos `.Rproj.user/` são configurações locais do RStudio e não devem ser versionados
- Arquivos grandes (CSV >10MB) não estão versionados (verificar `.gitignore`)

---

## 📚 Recursos para Aprender R

- **R para Data Science:** https://r4ds.had.co.nz/
- **Curso-R:** https://livro.curso-r.com/
- **Estatística Básica:** https://rpubs.com/EstatBasica
- **R Markdown:** https://bookdown.org/yihui/rmarkdown/

---

## 🎓 Progressão do Curso

1. **Aula 01:** Introdução à AED (uma variável)
2. **Aula 03:** AED avançada (duas variáveis)
3. **Aula 04:** R Markdown e relatórios
4. **Aula 05:** Transformações e tamanho de amostra
5. **Aula 07:** Testes estatísticos aplicados
6. **Aula 08:** Trabalho em grupo
7. **Aula 10:** Apresentação final

---

## 📊 Datasets Utilizados

- **diamonds** - Pacote ggplot2 (~54.000 diamantes)
- **birthwt** - Pacote MASS (peso ao nascer)
- **veiculos.xls** - Dataset de veículos
- **dados_exercio.csv** - Dataset de colaboradores (374 observações)
- **yulu_bike_sharing_dataset.csv** - Dataset de bike sharing
- **winemag-data-130k-v2.csv** - Dataset de vinhos (130.000+ observações)

---

**Disciplina:** Estatística  
**Autor:** Vinícius de Souza Cebalhos  
**Instituição:** UTFPR
