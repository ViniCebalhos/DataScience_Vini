# Aula 08 - Avaliação e Trabalhos em Grupo

**Disciplina:** Estatística  
**Linguagem:** R (R Markdown)  
**Objetivo:** Trabalho em grupo de análise exploratória de dados completo

---

## 🎯 Objetivo da Aula

Esta aula consiste em uma **avaliação prática** onde os alunos trabalham em grupo para realizar uma análise exploratória completa de dados. O objetivo é:

- Aplicar todos os conceitos aprendidos nas aulas anteriores
- Criar relatório profissional usando R Markdown
- Trabalhar em equipe
- Apresentar resultados de forma clara e interpretável

---

## 📚 Conceitos Estatísticos Envolvidos

### Análise Exploratória de Dados Completa
- **Análise Univariada:** Uma variável por vez
- **Análise Bivariada:** Relações entre duas variáveis
- **Análise Multivariada:** Múltiplas variáveis simultaneamente

### Técnicas Utilizadas
- Tabelas de frequência
- Estatísticas descritivas
- Gráficos diversos (barras, histogramas, boxplots, dispersão)
- Tabelas de contingência
- Correlações
- Comparações entre grupos

---

## 📁 Arquivos da Aula

### Trabalhos em Grupo
- **`Grupo_05.Rmd`** - Trabalho do grupo 5 (análise do dataset diamonds)
- **`Grupo_05_explicado.Rmd`** - Versão explicada do trabalho
- **`Final_Grupo_05.Rmd`** - Versão final do trabalho
- **`Grupo_Revisao.Rmd`** - Trabalho de revisão

### Scripts Auxiliares
- **`Aula_passada.R`** - Script da aula anterior (bike sharing)

### Dataset Utilizado
- **`diamonds`** - Dataset do pacote ggplot2 (~54.000 diamantes)
- **`yulu_bike_sharing_dataset.csv`** - Dataset de bike sharing (para aula passada)

---

## 🔍 Análise do Trabalho `Grupo_05.Rmd`

### Estrutura do Documento

#### 1. **Cabeçalho YAML (linhas 1-11)**
```yaml
---
title: "Análise Exploratória de Dados - Dataset Diamonds"
author: "Seu Nome"
date: "`r Sys.Date()`"
output: 
  html_document:
    toc: true
    toc_float: true
    theme: flatly
    highlight: tango
---
```

**Pontos Fortes:**
- ✅ TOC (índice) ativado
- ✅ Tema profissional
- ✅ Data automática

**Sugestões:**
- Adicionar subtítulo
- Adicionar `code_folding: hide` para ocultar código

---

#### 2. **Configuração Inicial (linhas 13-37)**
```r
knitr::opts_chunk$set(echo = TRUE, warning = FALSE, message = FALSE, 
                      fig.width = 10, fig.height = 6)
```

**O que faz:**
- Configura opções globais do R Markdown
- `echo = TRUE`: Mostra código no documento
- `warning = FALSE`: Oculta avisos
- `message = FALSE`: Oculta mensagens
- `fig.width/height`: Define tamanho das figuras

**Conceitos:**
- **Chunk Options:** Controlam comportamento de cada bloco de código
- **Figuras:** Tamanho padrão para todos os gráficos

---

#### 3. **Análise Exploratória Completa**

##### 3.1 Visão Geral (linhas 39-81)
```r
# Carregamento dos dados
data(diamonds)

# Criação de variável ajustada
diamonds <- diamonds %>% 
  dplyr::mutate(clarity_adj = dplyr::case_when(...))

# Resumo com skimr
skim(diamonds)

# Verificação de valores ausentes
valores_ausentes <- colSums(is.na(diamonds))
```

**O que faz:**
- Carrega e prepara dados
- Cria variáveis auxiliares
- Gera resumo estatístico completo
- Verifica qualidade dos dados

**Pontos Fortes:**
- ✅ Uso de `skimr` para resumo moderno
- ✅ Verificação de valores ausentes
- ✅ Tabelas formatadas com `kableExtra`

---

##### 3.2 Análise Univariada - Variáveis Categóricas (linhas 83-136)
```r
# Tabelas de frequência
freq_cut <- table(diamonds$cut)
prop_cut <- prop.table(freq_cut) * 100

# Tabelas formatadas
tabela_cut <- data.frame(
  Cut = names(freq_cut),
  Frequencia = as.numeric(freq_cut),
  Percentual = round(as.numeric(prop_cut), 2)
)

kable(tabela_cut, caption = "Tabela 2: Distribuição da Variável Cut") %>%
  kable_styling(bootstrap_options = c("striped", "hover"))
```

**O que faz:**
- Calcula frequências absolutas e relativas
- Cria tabelas formatadas profissionalmente
- Usa `kableExtra` para formatação HTML

**Pontos Fortes:**
- ✅ Tabelas bem formatadas
- ✅ Legendas descritivas
- ✅ Código organizado

---

##### 3.3 Gráficos com ggplot2 (linhas 140+)
```r
p1 <- ggplot(diamonds, aes(x = cut, fill = cut)) +
  geom_bar() +
  labs(title = "Distribuição de Cut", x = "Cut", y = "Frequência") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
```

**O que faz:**
- Cria gráficos modernos com ggplot2
- Aplica temas profissionais
- Formata eixos e títulos

**Pontos Fortes:**
- ✅ Uso consistente de ggplot2
- ✅ Temas profissionais
- ✅ Gráficos informativos

---

## 🚀 Como Executar

### Pré-requisitos
1. R instalado (versão 4.0+)
2. RStudio (recomendado)
3. Pacote `rmarkdown` instalado

### Passo a Passo

1. **Abra o projeto RStudio:**
```r
# File > Open Project > Aula08_avaliacao.Rproj
```

2. **Abra o arquivo .Rmd:**
```r
# File > Open File > Grupo_05.Rmd
```

3. **Renderize o documento:**
```r
# No RStudio: Knit > Knit to HTML
# Ou no console:
rmarkdown::render("Grupo_05.Rmd")
```

### Dependências

Pacotes necessários:
- `dplyr` - Manipulação de dados
- `ggplot2` - Visualização
- `skimr` - Resumo estatístico
- `knitr` - Renderização
- `kableExtra` - Tabelas formatadas
- `corrplot` - Matriz de correlação

---

## 📊 Resultados Esperados

Ao renderizar o R Markdown, você obterá:

1. **Documento HTML Profissional:**
   - Índice navegável
   - Tabelas formatadas
   - Gráficos de alta qualidade
   - Interpretações dos resultados

2. **Análise Completa:**
   - Visão geral dos dados
   - Análise univariada
   - Análise bivariada
   - Análise multivariada
   - Conclusões

---

## ⚠️ Problemas Identificados

### 1. Autor Genérico
- **Problema:** "Seu Nome" no cabeçalho
- **Solução:** Substituir por nome real do grupo

### 2. Falta de Interpretação
- **Problema:** Alguns gráficos sem interpretação
- **Solução:** Adicionar texto explicativo após cada análise

### 3. Código Não Comentado
- **Problema:** Alguns blocos sem comentários
- **Solução:** Adicionar comentários explicativos

### 4. Falta de Conclusões
- **Problema:** Documento poderia ter seção de conclusões mais robusta
- **Solução:** Expandir seção de conclusões

---

## 💡 Melhorias Sugeridas

### 1. Adicionar Seção de Metodologia
```r
## Metodologia

Este trabalho segue os seguintes passos:
1. Carregamento e limpeza dos dados
2. Análise exploratória univariada
3. Análise exploratória bivariada
4. Análise exploratória multivariada
5. Conclusões e recomendações
```

### 2. Adicionar Interpretação Após Cada Gráfico
```r
# Após cada gráfico:
cat("### Interpretação:\n")
cat("Observa-se que a distribuição de", variavel, "apresenta...\n")
```

### 3. Criar Funções para Análises Repetitivas
```r
analisar_variavel_categorica <- function(dados, variavel) {
  # Código reutilizável
}
```

### 4. Adicionar Tabelas de Resumo
```r
# Tabela resumo de todas as análises
resumo_analises <- criar_tabela_resumo(diamonds)
```

### 5. Adicionar Referências
```r
## Referências

- Dataset diamonds: pacote ggplot2
- Wickham, H. (2016). ggplot2: Elegant Graphics for Data Analysis
```

---

## 📦 Dependências

### Pacotes Necessários
- `dplyr` - Manipulação de dados
- `ggplot2` - Visualização
- `skimr` - Resumo estatístico
- `knitr` - Renderização
- `kableExtra` - Tabelas formatadas
- `corrplot` - Matriz de correlação

---

## ✅ Checklist da Aula

- [x] Trabalho em grupo completo
- [x] R Markdown bem estruturado
- [x] Análise exploratória completa
- [x] Gráficos profissionais
- [ ] Autor atualizado
- [ ] Interpretações adicionadas
- [ ] Conclusões expandidas
- [ ] README.md criado

---

**Autor:** Vinícius de Souza Cebalhos  
**Data:** 2024  
**Disciplina:** Estatística - UTFPR

