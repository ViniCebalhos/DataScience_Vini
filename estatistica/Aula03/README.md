# Aula 03 - Análise Exploratória de Dados (Duas Variáveis)

**Disciplina:** Estatística  
**Linguagem:** R  
**Objetivo:** Análise exploratória de dados envolvendo duas variáveis (qualitativa × qualitativa, quantitativa × quantitativa, qualitativa × quantitativa)

---

## 🎯 Objetivo da Aula

Esta aula expande a análise exploratória para **duas variáveis simultaneamente**, permitindo identificar relações, associações e padrões entre variáveis. Os alunos aprendem a:

- Analisar relações entre duas variáveis qualitativas (tabelas de contingência)
- Analisar relações entre duas variáveis quantitativas (correlação, gráficos de dispersão)
- Analisar relações entre variáveis qualitativas e quantitativas (comparação de grupos)
- Visualizar relações multivariadas

---

## 📚 Conceitos Estatísticos Envolvidos

### 1. Qualitativa × Qualitativa
- **Tabela de Contingência:** Tabela cruzada mostrando frequências conjuntas
- **Frequência Relativa por Linha:** Percentual dentro de cada categoria da linha
- **Frequência Relativa por Coluna:** Percentual dentro de cada categoria da coluna
- **Gráficos:** Gráficos de barras agrupadas ou empilhadas

### 2. Quantitativa × Quantitativa
- **Correlação de Pearson:** Mede relação linear entre duas variáveis contínuas
- **Correlação de Spearman:** Mede relação monotônica (não necessariamente linear)
- **Gráfico de Dispersão:** Mostra relação visual entre duas variáveis numéricas
- **Matriz de Correlação:** Mostra correlações entre múltiplas variáveis

### 3. Qualitativa × Quantitativa
- **Comparação de Grupos:** Estatísticas descritivas por grupo
- **Boxplot por Grupo:** Comparação visual de distribuições
- **Testes de Comparação:** (não abordados nesta aula, mas preparação para aulas futuras)

### 4. Múltiplas Variáveis
- **Gráfico de Pares (Pairs Plot):** Visualização de relações entre múltiplas variáveis
- **Gráficos de Dispersão Símbolicos:** Diferentes símbolos/cores para diferentes grupos
- **Gráficos de Partição (Facet):** Gráficos separados por categoria

---

## 📁 Arquivos da Aula

### Scripts Principais
- **`aula_03.R`** - Script principal com todas as análises
- **`definitions.R`** - Definições e configurações
- **`install_load_packages.R`** - Instalação e carregamento de pacotes
- **`template_aula.R`** - Template para estrutura

### Datasets Utilizados
- **`diamonds`** - Dataset do pacote `ggplot2` (~54.000 diamantes)
- **`veiculos.xls`** - Dataset de veículos (preço, motor, comprimento, procedência)

---

## 🔍 Análise do Código

### Estrutura do Script `aula_03.R`

#### 1. **Configuração Inicial (linhas 1-16)**
Similar à Aula 01, com configuração de caminhos e carregamento de pacotes.

---

#### 2. **Análise Qualitativa × Qualitativa (linhas 19-64)**

##### 2.1 Tabela de Contingência
```r
tab_n <- table(diamonds$cut, diamonds$clarity)  # Frequências absolutas
round(prop.table(tab_n)*100, 2)  # Frequências relativas totais
tab_freq_linha <- round(prop.table(tab_n, margin=1)*100, 2)  # Por linha
tab_freq_col <- round(prop.table(tab_n, margin=2)*100, 2)  # Por coluna
```

**O que faz:**
- `table()`: Cria tabela cruzada (contingência)
- `prop.table(..., margin=1)`: Calcula percentuais por linha (soma de cada linha = 100%)
- `prop.table(..., margin=2)`: Calcula percentuais por coluna (soma de cada coluna = 100%)

**Conceitos:**
- **Tabela de Contingência:** Mostra distribuição conjunta de duas variáveis categóricas
- **Margin 1:** Percentuais condicionais dado o valor da linha
- **Margin 2:** Percentuais condicionais dado o valor da coluna

##### 2.2 Criação de Variáveis Agregadas
```r
diamonds <- diamonds %>%
  dplyr::mutate(clareza_adj = dplyr::case_when(
    clarity %in% c('I1', 'SI2') ~ 'Baixa pureza',
    clarity %in% c('SI1', 'VS2', 'VS1') ~ 'Média pureza',
    TRUE ~ 'Alta pureza'))
```

**O que faz:**
- Agrupa categorias de clareza em 3 grupos mais simples
- Facilita análise e visualização

**Conceitos:**
- **Recodificação:** Agrupar categorias para simplificar análise
- **Fator Ordenado:** Cria ordem lógica nas categorias

##### 2.3 Análise com dplyr e tidyr
```r
ex1 <- diamonds %>% 
  dplyr::group_by(cut, clareza_adj2) %>%
  dplyr::summarise(n = dplyr::n()) %>%
  dplyr::group_by(cut) %>%
  dplyr::mutate(total = sum(n),
                pct = round((n/total)*100,2)) %>%
  dplyr::ungroup()
```

**O que faz:**
- Usa tidyverse para calcular percentuais por grupo
- Mais legível e moderno que `prop.table()`

**Conceitos:**
- **Pipe (`%>%`):** Encadeia operações de forma legível
- **group_by():** Agrupa dados por variável
- **summarise():** Calcula estatísticas por grupo
- **mutate():** Cria novas variáveis

##### 2.4 Gráfico de Barras Agrupadas
```r
barplot(tab_n, 
        beside = FALSE,  # Barras empilhadas
        col = rainbow(nrow(tab_n)), 
        legend.text = rownames(tab_n),
        xlab = "Qualidade do corte", 
        ylab = "n",
        main = "Distribuição de frequência qualidade corte x pureza diamantes")
```

**O que faz:**
- Cria gráfico de barras mostrando distribuição conjunta
- `beside = FALSE`: Barras empilhadas (mostra composição)
- `beside = TRUE`: Barras lado a lado (facilita comparação)

---

#### 3. **Análise Quantitativa × Quantitativa (linhas 82-102)**

##### 3.1 Carregamento de Dados Externos
```r
veiculos <- read_excel("veiculos.xls")
```

**⚠️ Problema:** Caminho relativo pode quebrar se executado de outro diretório

**Sugestão:**
```r
veiculos <- read_excel(file.path(project_root_path, "veiculos.xls"))
```

##### 3.2 Gráfico de Dispersão
```r
plot(x = veiculos$preco,
     y = veiculos$motor, 
     xlab = "Preço", 
     ylab = "Pot. Motor", 
     main = "Gráfico dispersão preço potência")
```

**O que faz:**
- Mostra relação visual entre duas variáveis numéricas
- Permite identificar:
  - Tendência (positiva/negativa)
  - Forma da relação (linear/não-linear)
  - Outliers

##### 3.3 Correlação
```r
cor(veiculos$preco, veiculos$motor, method = "pearson")
cor(veiculos$preco, veiculos$motor, method = "spearman")
```

**O que faz:**
- **Pearson:** Mede correlação linear (requer normalidade)
- **Spearman:** Mede correlação de postos (não requer normalidade)

**Conceitos:**
- **Correlação de Pearson (r):**
  - Varia de -1 a +1
  - r = 1: correlação positiva perfeita
  - r = 0: sem correlação linear
  - r = -1: correlação negativa perfeita
- **Correlação de Spearman (ρ):**
  - Baseada em postos (ranks)
  - Mais robusta a outliers
  - Não assume linearidade

---

#### 4. **Análise Qualitativa × Quantitativa (linhas 105-117)**

##### 4.1 Estatísticas por Grupo
```r
mr1 <- tapply(veiculos$motor, veiculos$proc_adj, summary)
mr2 <- tapply(veiculos$motor, veiculos$proc_adj, sd)
```

**O que faz:**
- Calcula estatísticas descritivas separadamente para cada grupo
- `tapply()`: Aplica função a cada grupo

##### 4.2 Boxplot por Grupo
```r
boxplot(veiculos$motor ~ veiculos$proc_adj, 
        col = "lightblue",
        xlab = "Procedência",
        ylab = "Pot Motor", 
        main = "Boxplot pot X procedência")
```

**O que faz:**
- Compara distribuições de variável quantitativa entre grupos
- Permite identificar diferenças entre grupos

**Conceitos:**
- **Comparação de Grupos:** Avalia se há diferença entre grupos
- **Boxplot:** Mostra mediana, quartis e outliers por grupo

---

#### 5. **Análise de Múltiplas Variáveis (linhas 120-153)**

##### 5.1 Gráfico de Pares
```r
g1 <- graphics::pairs(~preco + comp + motor, data = veiculos)
```

**O que faz:**
- Cria matriz de gráficos de dispersão
- Mostra todas as relações entre múltiplas variáveis

##### 5.2 Gráfico de Dispersão Símbolico
```r
plot(x = veiculos$comp, 
     y = veiculos$preco, 
     pch = as.numeric(veiculos$proc_adj),  # Símbolo diferente por grupo
     col = veiculos$proc_adj,  # Cor diferente por grupo
     ylab = "Preço", 
     xlab = "Comp", 
     main = "Dispersão entre preço e comp por procedência")
```

**O que faz:**
- Mostra relação entre duas variáveis quantitativas
- Diferencia grupos usando símbolos e cores diferentes

##### 5.3 Gráfico de Partição (Facet)
```r
ggplot2::ggplot(data = veiculos,
                aes(x = motor, y = comp)) +
  geom_point() + 
  facet_wrap(~proc)
```

**O que faz:**
- Cria gráficos separados para cada categoria
- Facilita comparação entre grupos

**Conceitos:**
- **Facet:** Divide gráfico em painéis por categoria
- **ggplot2:** Sistema de gráficos mais moderno e flexível

##### 5.4 Matriz de Correlação
```r
tab_corr <- round(cor(veiculos[,c("preco", "comp", "motor")]), 1)
corrplot::corrplot(tab_corr)
```

**O que faz:**
- Calcula correlações entre múltiplas variáveis
- Visualiza matriz de correlação com cores

**Conceitos:**
- **Matriz de Correlação:** Mostra todas as correlações entre variáveis
- **Corrplot:** Visualização colorida (vermelho = negativa, azul = positiva)

---

## 🚀 Como Executar

### Pré-requisitos
1. R instalado (versão 4.0+)
2. RStudio (recomendado)
3. Arquivo `veiculos.xls` na pasta da aula

### Passo a Passo

1. **Abra o projeto RStudio:**
```r
# File > Open Project > Aula3.Rproj
```

2. **Execute o script:**
```r
source("aula_03.R")
```

### Dependências

Pacotes instalados automaticamente:
- `dplyr` - Manipulação de dados
- `ggplot2` - Visualização
- `readxl` - Leitura de arquivos Excel
- `corrplot` - Visualização de correlações
- `tidyr` - Organização de dados

---

## 📊 Resultados Esperados

1. **Tabelas de Contingência:**
   - Frequências absolutas e relativas
   - Percentuais por linha e por coluna

2. **Gráficos de Relações:**
   - Gráficos de barras agrupadas/empilhadas
   - Gráficos de dispersão
   - Boxplots por grupo
   - Matriz de correlação

3. **Estatísticas:**
   - Correlações de Pearson e Spearman
   - Estatísticas descritivas por grupo

---

## ⚠️ Problemas Identificados

### 1. Caminho do Arquivo Excel
- **Problema:** `read_excel("veiculos.xls")` usa caminho relativo
- **Solução:** Usar caminho absoluto ou `file.path()`

### 2. Erro no Código (linha 146)
```r
tapply(veiculos$motos, veiculos$proc, summary)
```
- **Problema:** Variável `motos` não existe (deveria ser `motor`)
- **Solução:** Corrigir nome da variável

### 3. Mistura de Estilos
- **Problema:** Mistura gráficos base do R com ggplot2
- **Solução:** Padronizar uso de ggplot2

### 4. Falta de Validação
- **Problema:** Não verifica se arquivo Excel existe
- **Solução:** Adicionar verificação

### 5. Comentários Insuficientes
- **Problema:** Algumas seções sem explicação
- **Solução:** Adicionar comentários explicativos

---

## 💡 Melhorias Sugeridas

### 1. Usar ggplot2 Consistentemente
```r
# Em vez de gráficos base:
ggplot(diamonds, aes(x = cut, fill = clarity_adj)) +
  geom_bar(position = "stack") +
  labs(title = "Distribuição de Corte por Pureza")
```

### 2. Criar Função para Tabelas de Contingência
```r
criar_tabela_contingencia <- function(dados, var1, var2) {
  # Código reutilizável
}
```

### 3. Adicionar Testes de Correlação
```r
# Teste de significância da correlação
cor.test(veiculos$preco, veiculos$motor)
```

### 4. Salvar Gráficos
```r
ggsave("figures/dispersao_preco_motor.png", width = 10, height = 6)
```

### 5. Documentar Resultados
```r
# Adicionar interpretação dos resultados
cat("Correlação entre preço e motor:", cor_preco_motor, "\n")
cat("Interpretação: correlação", ifelse(cor_preco_motor > 0.5, "forte", "fraca"), "\n")
```

---

## 📦 Dependências

### Pacotes Necessários
- `dplyr` - Manipulação de dados
- `ggplot2` - Visualização
- `readxl` - Leitura de Excel
- `corrplot` - Matriz de correlação
- `tidyr` - Organização de dados

### Arquivos de Dados
- `veiculos.xls` - Dataset de veículos (deve estar na pasta da aula)

---

## ✅ Checklist da Aula

- [x] Script principal funcional
- [x] Análise qualitativa × qualitativa implementada
- [x] Análise quantitativa × quantitativa implementada
- [x] Análise qualitativa × quantitativa implementada
- [x] Análise de múltiplas variáveis implementada
- [ ] Erro na linha 146 corrigido (variável `motos`)
- [ ] Caminhos de arquivos corrigidos
- [ ] Gráficos salvos em arquivos
- [ ] README.md criado

---

**Autor:** Vinícius de Souza Cebalhos  
**Data:** 2024  
**Disciplina:** Estatística - UTFPR

