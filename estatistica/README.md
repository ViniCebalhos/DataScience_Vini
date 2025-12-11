# 📊 Estatística - Trabalhos e Projetos

Esta pasta contém todos os trabalhos desenvolvidos na disciplina de **Estatística** da pós-graduação em Ciência de Dados.

**Linguagem:** R  
**Ambiente:** RStudio

---

## 📚 Trabalhos Desenvolvidos

Esta disciplina foi desenvolvida em R, focando em análise estatística e visualização de dados.

### 📋 Estrutura das Aulas

- **Aula 1:** Análise Exploratória de Dados (AED) - Uma Variável
- **Aula 3:** Análise Exploratória de Dados
- **Aula 4:** Análise Exploratória de Dados (AED) - Múltiplas Variáveis
- **Aula 5:** Análise Estatística
- **Aula 7:** Análise de Dados de Bike Sharing
- **Aula 8:** Avaliação e Apresentação de Trabalhos
- **Aula 10:** Apresentação Final

---

## 🛠️ Tecnologias Utilizadas

- **R** (linguagem de programação estatística)
- **RStudio** (ambiente de desenvolvimento)
- **R Markdown** (.Rmd) para relatórios reproduzíveis
- **Bibliotecas R:** dplyr, ggplot2, tidyr, lubridate, entre outras

---

## 📁 Estrutura de Pastas

```
estatistica/
├── README.md                    # Este arquivo
├── Aula01/                      # Análise Exploratória de Dados - 1 variável
├── Aula03/                      # Análise Exploratória de Dados - múltiplas variáveis
├── Aula04/                      # Análise Exploratória de Dados - R Markdown
├── Aula05/                      # Análise Exploratória de Dados avançada
├── Aula07/                      # Análise Estatística
├── Aula08_avaliacao/            # Avaliação - Trabalho em grupo
├── Aula10_apresentacao/         # Apresentação final
└── recuperacao/                 # Trabalho de recuperação
```

---

## 📚 Trabalhos Desenvolvidos

### Aula 01 - Análise Exploratória de Dados (1 variável)
**Objetivo:** Introdução à análise exploratória de dados com foco em uma variável.

**Conteúdo:**
- Estatísticas descritivas
- Visualizações univariadas
- Distribuições de frequência

**Arquivos principais:**
- `aed_1var.R` - Script R principal

---

### Aula 03 - Análise Exploratória de Dados (múltiplas variáveis)
**Objetivo:** Análise exploratória de dados com múltiplas variáveis.

**Conteúdo:**
- Análise bivariada
- Correlações
- Visualizações multivariadas

**Arquivos principais:**
- `aula_03.R` - Script R principal

---

### Aula 04 - R Markdown
**Objetivo:** Criar relatórios reproduzíveis com R Markdown.

**Conteúdo:**
- Estrutura de documentos R Markdown
- Integração de código R e texto
- Geração de relatórios em PDF/HTML

**Arquivos principais:**
- `Aula04_AED.Rmd` - Documento R Markdown
- `ViniciusCebalhos_atividade1.Rmd` - Atividade do aluno

---

### Aula 05 - Análise Exploratória Avançada
**Objetivo:** Técnicas avançadas de análise exploratória de dados.

**Conteúdo:**
- Análise de séries temporais
- Análise de grupos
- Técnicas avançadas de visualização

**Arquivos principais:**
- `aula_05.R` - Script R principal

---

### Aula 07 - Análise Estatística
**Objetivo:** Aplicação de técnicas estatísticas inferenciais.

**Conteúdo:**
- Testes de hipóteses
- Intervalos de confiança
- Análise de variância (ANOVA)

**Arquivos principais:**
- Scripts R da aula

---

### Aula 08 - Avaliação (Trabalho em Grupo)
**Objetivo:** Trabalho em grupo aplicando técnicas de análise estatística.

**Conteúdo:**
- Análise completa de um dataset
- Aplicação de técnicas aprendidas
- Relatório final em R Markdown

**Arquivos principais:**
- `Final_Grupo_05.Rmd` - Relatório final do grupo
- `Grupo_05.Rmd` - Versão do trabalho
- `Grupo_05_explicado.Rmd` - Versão explicada

---

### Aula 10 - Apresentação Final
**Objetivo:** Apresentação de projeto final de análise estatística.

**Conteúdo:**
- Análise completa de dataset escolhido
- Visualizações profissionais
- Relatório final

**Arquivos principais:**
- `Vinicius_Cebalhos.Rmd` - Apresentação do aluno
- `ViniciusCebalhos_Atividade3.Rmd` - Atividade 3

**Dataset utilizado:**
- `winemag-data-130k-v2.json` - Dataset de vinhos (Yelp)

---

### Recuperação
**Objetivo:** Trabalho de recuperação da disciplina.

**Arquivos principais:**
- `ViniciusCebalhos_Recuperacao.Rmd` - Trabalho de recuperação

---

## 🚀 Como Executar

### Pré-requisitos

1. **Instalar R:**
```bash
# Ubuntu/Debian
sudo apt-get install r-base r-base-dev

# Ou baixar de: https://cran.r-project.org/
```

2. **Instalar RStudio (opcional, mas recomendado):**
```bash
# Baixar de: https://www.rstudio.com/products/rstudio/download/
```

3. **Instalar pacotes R necessários:**
```r
# Abrir R ou RStudio e executar:
install.packages(c("dplyr", "ggplot2", "tidyr", "lubridate", "knitr", "rmarkdown"))
```

### Executar um Trabalho

1. **Para scripts .R:**
```bash
Rscript Aula01/aed_1var.R
```

2. **Para documentos R Markdown (.Rmd):**
```r
# No RStudio: Abrir o arquivo .Rmd e clicar em "Knit"
# Ou via linha de comando:
Rscript -e "rmarkdown::render('Aula04/Aula04_AED.Rmd')"
```

---

## 📊 Competências Demonstradas

- ✅ Análise Exploratória de Dados (EDA)
- ✅ Estatísticas descritivas
- ✅ Visualização de dados com ggplot2
- ✅ Manipulação de dados com dplyr
- ✅ Relatórios reproduzíveis com R Markdown
- ✅ Análise estatística inferencial
- ✅ Testes de hipóteses
- ✅ Análise de séries temporais

---

## 📝 Notas

- Os trabalhos foram desenvolvidos em **R**, diferente dos outros projetos do portfólio que usam Python
- Alguns datasets podem precisar ser baixados separadamente
- Os arquivos `.Rproj` são projetos do RStudio e podem ser abertos diretamente no RStudio
- Os templates (`template_aula.R`, `definitions.R`) são arquivos auxiliares fornecidos pelo professor

---

## 🔗 Recursos Adicionais

- [Documentação do R](https://www.r-project.org/)
- [R Markdown Guide](https://rmarkdown.rstudio.com/)
- [ggplot2 Documentation](https://ggplot2.tidyverse.org/)
- [dplyr Documentation](https://dplyr.tidyverse.org/)

---

**Disciplina:** Estatística  
**Autor:** Vinícius de Souza Cebalhos  
**Instituição:** UTFPR
