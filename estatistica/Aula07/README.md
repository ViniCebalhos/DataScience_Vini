# Aula 07 - Análise de Dados de Bike Sharing

**Disciplina:** Estatística  
**Linguagem:** R  
**Objetivo:** Análise exploratória completa de dados de bike sharing com aplicação de testes estatísticos

---

## 🎯 Objetivo da Aula

Esta aula aplica todos os conceitos aprendidos anteriormente em um **dataset real e complexo** de bike sharing. Os alunos aprendem a:

- Realizar análise exploratória completa de dados temporais
- Aplicar testes estatísticos para comparar grupos
- Formular e testar hipóteses estatísticas
- Interpretar resultados de testes não-paramétricos

---

## 📚 Conceitos Estatísticos Envolvidos

### 1. Análise Exploratória de Dados (AED)
- **Análise Temporal:** Padrões ao longo do tempo
- **Análise por Grupos:** Comparação entre categorias
- **Análise Multivariada:** Múltiplas variáveis simultaneamente

### 2. Testes Estatísticos

#### Testes de Normalidade
- **Shapiro-Wilk:** Testa se dados seguem distribuição normal (limite: 5000 obs)
- **Anderson-Darling:** Alternativa para amostras grandes (>5000 obs)

#### Testes de Homogeneidade de Variâncias
- **Levene:** Testa se variâncias são iguais entre grupos

#### Testes de Comparação de Médias/Medianas

**Para 2 grupos:**
- **Teste t de Student:** Compara médias (requer normalidade e variâncias iguais)
- **Teste de Wilcoxon (Mann-Whitney):** Compara medianas (não requer normalidade)

**Para 3+ grupos:**
- **ANOVA:** Compara médias (requer normalidade)
- **Kruskal-Wallis:** Compara medianas (não requer normalidade)
- **Dunn:** Teste post-hoc para identificar quais grupos diferem

#### Testes de Correlação
- **Correlação de Spearman:** Testa correlação monotônica (não requer normalidade)

---

## 📁 Arquivos da Aula

### Scripts Principais
- **`Aula_passada.R`** (em Aula08) - Script principal com todas as análises
- **`definitions.R`** - Definições e configurações
- **`install_load_packages.R`** - Instalação e carregamento de pacotes
- **`template_aula.R`** - Template para estrutura

### Dataset Utilizado
- **`yulu_bike_sharing_dataset.csv`** - Dataset de bike sharing com:
  - Dados temporais (data, hora)
  - Variáveis climáticas (temperatura, umidade, vento)
  - Variáveis categóricas (estação, feriado, dia útil, clima)
  - Variável resposta: número de aluguéis (count)

---

## 🔍 Análise do Código

### Estrutura do Script `Aula_passada.R`

#### 1. **Carregamento e Preparação dos Dados (linhas 1-65)**

##### 1.1 Leitura dos Dados
```r
yulu <- read.csv(paste0(project_root_path, "/yulu_bike_sharing_dataset.csv"))
```

**⚠️ Problema:** Caminho relativo pode quebrar

##### 1.2 Criação de Variáveis Temporais
```r
yulu <- yulu %>% 
  dplyr::mutate(
    dia = lubridate::as_date(datetime),
    hora = lubridate::hour(datetime),
    ano_mes = lubridate::floor_date(dia, 'month'),
    hora_cat = factor(case_when(
      between(hora, 6, 9)  ~ "Manhã ini",
      between(hora, 10, 11) ~ "Manhã",
      # ... outras categorias
    ))
  )
```

**O que faz:**
- Extrai componentes temporais (dia, hora, mês)
- Cria categorias de horário para análise

**Conceitos:**
- **Análise Temporal:** Identificar padrões ao longo do tempo
- **Categorização:** Agrupar horas em períodos do dia

##### 1.3 Criação de Fatores
```r
season_factor = factor(season,
                       levels = c(2, 3, 4, 1),
                       labels = c("Primavera", "Verão", "Outono", "Inverno"))
```

**O que faz:**
- Converte códigos numéricos em labels descritivos
- Define ordem lógica (estações do ano)

---

#### 2. **Análise Exploratória (linhas 67-131)**

##### 2.1 Resumo com skimr
```r
yulu %>% 
  dplyr::select(-c(datetime, season, holiday, workingday, weather)) %>% 
  skimr::skim()
```

**O que faz:**
- Remove variáveis originais (mantém apenas fatores)
- Gera resumo estatístico completo

**Conceitos:**
- **skimr::skim():** Resumo estatístico moderno e informativo
- Mostra: n, média, mediana, quartis, histograma, valores ausentes

##### 2.2 Análise Temporal
```r
uso_dia <- yulu %>% 
  dplyr::select(dia, count) %>% 
  dplyr::group_by(dia) %>% 
  dplyr::summarise(total_alugueis = sum(count)) %>% 
  dplyr::ungroup()

plot(uso_dia$dia, uso_dia$total_alugueis, type = "l",
     main = "Total de aluguéis por dia ao longo do tempo",
     xlab = "Dia", ylab = "Total de aluguéis", col = "blue", lwd = 2)
```

**O que faz:**
- Agrega aluguéis por dia
- Cria gráfico de linha temporal

**Conceitos:**
- **Série Temporal:** Dados ordenados no tempo
- **Tendência:** Padrão de longo prazo
- **Sazonalidade:** Padrões que se repetem

##### 2.3 Análise por Grupos
```r
boxplot(yulu$count ~ yulu$season_factor)
boxplot(yulu$count ~ yulu$holiday_factor)
boxplot(yulu$count ~ yulu$workingday_factor)
boxplot(yulu$count ~ yulu$weather_factor)
```

**O que faz:**
- Compara distribuições de aluguéis entre grupos
- Identifica diferenças visuais

---

#### 3. **Testes Estatísticos (linhas 136-551)**

##### 3.1 Teste: Diferença em Feriados (linhas 136-205)

**Hipótese:**
- H₀: Média de aluguéis em feriados = Média em dias normais
- H₁: Médias são diferentes

**Metodologia:**
1. **AED:** Boxplots, histogramas, estatísticas descritivas
2. **Verificação de Pressupostos:**
   - Normalidade: Q-Q plots, Shapiro-Wilk, Anderson-Darling
   - Homogeneidade de variâncias: Levene
3. **Teste:** Wilcoxon (dados não normais)

```r
# Verificação de normalidade
shapiro.test(q1$n_alugueis[q1$holiday_factor == "Sim"])
ad.test(q1$n_alugueis[q1$holiday_factor == "Sim"])

# Teste de homogeneidade
car::leveneTest(n_alugueis ~ holiday_factor, data = q1)

# Teste de comparação
wilcox.test(n_alugueis ~ holiday_factor, data = q1, alternative = "two.sided")
```

**Conceitos:**
- **Teste Não-Paramétrico:** Não requer normalidade
- **Wilcoxon:** Compara medianas (não médias)
- **p-valor < 0.05:** Rejeita H₀ (há diferença significativa)

##### 3.2 Teste: Diferença em Dias Úteis vs Finais de Semana (linhas 207-264)

Similar ao anterior, mas comparando dias úteis vs finais de semana.

##### 3.3 Teste: Diferença entre Estações (linhas 266-352)

**Hipótese:**
- H₀: Medianas são iguais em todas as estações
- H₁: Pelo menos uma mediana é diferente

**Metodologia:**
1. **AED:** Boxplots, histogramas por estação
2. **Verificação de Normalidade:** Q-Q plots, Shapiro-Wilk por grupo
3. **Teste:** Kruskal-Wallis (mais de 2 grupos, não paramétrico)
4. **Post-hoc:** Dunn (identifica quais grupos diferem)

```r
# Teste principal
kruskal.test(n_alugueis ~ season_factor, data = q3)

# Teste post-hoc
dunn.test(q3$n_alugueis, q3$season_factor, method = "bonferroni")
```

**Conceitos:**
- **Kruskal-Wallis:** ANOVA não-paramétrica
- **Dunn:** Teste post-hoc com correção de Bonferroni
- **Correção de Bonferroni:** Ajusta p-valores para múltiplas comparações

##### 3.4 Teste: Diferença entre Condições Climáticas (linhas 354-434)

Similar ao teste de estações, mas para condições climáticas.

##### 3.5 Teste: Correlação com Velocidade do Vento (linhas 436-462)

**Hipótese:**
- H₀: ρ = 0 (sem correlação)
- H₁: ρ ≠ 0 (há correlação)

**Metodologia:**
1. **AED:** Gráfico de dispersão, histogramas
2. **Verificação de Normalidade:** Shapiro-Wilk
3. **Teste:** Correlação de Spearman (dados não normais)

```r
cor.test(y = q5$n_alugueis,
         x = q5$velocidade_vento,
         method = "spearman")
```

**Conceitos:**
- **Correlação de Spearman:** Baseada em postos (ranks)
- **p-valor < 0.05:** Correlação significativa

##### 3.6 Teste: Diferença entre Turnos (linhas 464-551)

Similar ao teste de estações, mas para categorias de horário.

---

## 🚀 Como Executar

### Pré-requisitos
1. R instalado (versão 4.0+)
2. RStudio (recomendado)
3. Arquivo `yulu_bike_sharing_dataset.csv` na pasta

### Passo a Passo

1. **Abra o projeto RStudio:**
```r
# File > Open Project > Aula07.Rproj
```

2. **Execute o script:**
```r
source("Aula_passada.R")  # Ou o script da Aula07 se existir
```

### Dependências

Pacotes necessários:
- `dplyr` - Manipulação de dados
- `lubridate` - Manipulação de datas
- `skimr` - Resumo estatístico
- `car` - Testes estatísticos
- `nortest` - Testes de normalidade
- `dunn.test` - Teste de Dunn

---

## 📊 Resultados Esperados

1. **Análise Exploratória:**
   - Resumo estatístico completo
   - Gráficos temporais
   - Comparações visuais entre grupos

2. **Testes Estatísticos:**
   - Resultados de testes de normalidade
   - Resultados de testes de comparação
   - Interpretação dos p-valores

3. **Conclusões:**
   - Identificação de fatores que impactam aluguéis
   - Padrões temporais identificados
   - Recomendações baseadas em dados

---

## ⚠️ Problemas Identificados

### 1. Erro no Código (linha 252)
```r
car::qqPlot(q1$n_alugueis[q2$workingday_factor == "Sim"], ...)
```
- **Problema:** Usa `q1` mas deveria ser `q2`
- **Solução:** Corrigir referência

### 2. Caminhos Relativos
- **Problema:** Caminhos podem quebrar
- **Solução:** Usar `file.path()` ou `here::here()`

### 3. Falta de Interpretação
- **Problema:** Testes são executados mas resultados não são interpretados
- **Solução:** Adicionar interpretação após cada teste

### 4. Falta de Documentação
- **Problema:** Hipóteses não estão claramente documentadas
- **Solução:** Adicionar comentários explicando H₀ e H₁

### 5. Código Repetitivo
- **Problema:** Mesmo padrão de código repetido várias vezes
- **Solução:** Criar funções reutilizáveis

---

## 💡 Melhorias Sugeridas

### 1. Criar Função para Teste Completo
```r
testar_diferenca_grupos <- function(dados, variavel, grupo) {
  # 1. AED
  # 2. Verificação de pressupostos
  # 3. Teste apropriado
  # 4. Interpretação
  # Retorna relatório completo
}
```

### 2. Adicionar Interpretação Automática
```r
interpretar_teste <- function(p_valor, alpha = 0.05) {
  if (p_valor < alpha) {
    cat("Rejeitamos H₀. Há evidência de diferença significativa (p =", p_valor, ")\n")
  } else {
    cat("Não rejeitamos H₀. Não há evidência de diferença (p =", p_valor, ")\n")
  }
}
```

### 3. Usar ggplot2 Consistentemente
```r
# Em vez de gráficos base:
ggplot(q1, aes(x = holiday_factor, y = n_alugueis)) +
  geom_boxplot() +
  labs(title = "Aluguéis por Tipo de Dia")
```

### 4. Criar Relatório Automático
```r
# Gerar relatório com todos os testes
relatorio <- criar_relatorio_testes(yulu)
```

### 5. Adicionar Tamanho de Efeito
```r
# Além de p-valor, calcular tamanho de efeito
library(effsize)
cohen.d(q1$n_alugueis[q1$holiday_factor == "Sim"],
        q1$n_alugueis[q1$holiday_factor == "Não"])
```

---

## 📦 Dependências

### Pacotes Necessários
- `dplyr` - Manipulação de dados
- `lubridate` - Datas
- `skimr` - Resumo estatístico
- `car` - Testes estatísticos
- `nortest` - Testes de normalidade
- `dunn.test` - Teste de Dunn

### Arquivos de Dados
- `yulu_bike_sharing_dataset.csv` - Dataset de bike sharing

---

## 📚 Referências

- **Testes Não-Paramétricos:** https://www.statisticshowto.com/non-parametric/
- **Kruskal-Wallis:** https://www.statisticshowto.com/kruskal-wallis/
- **Teste de Dunn:** https://www.statisticshowto.com/dunns-test/

---

## ✅ Checklist da Aula

- [x] Script principal funcional
- [x] Análise exploratória implementada
- [x] Testes estatísticos implementados
- [ ] Erro na linha 252 corrigido
- [ ] Interpretação dos resultados adicionada
- [ ] Funções reutilizáveis criadas
- [ ] README.md criado

---

**Autor:** Vinícius de Souza Cebalhos  
**Data:** 2024  
**Disciplina:** Estatística - UTFPR

