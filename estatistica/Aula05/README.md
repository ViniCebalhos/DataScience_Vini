# Aula 05 - Transformações de Variáveis e Tamanho de Amostra

**Disciplina:** Estatística  
**Linguagem:** R  
**Objetivo:** Aprender transformações de variáveis e cálculo de tamanho de amostra

---

## 🎯 Objetivo da Aula

Esta aula aborda dois tópicos importantes:

1. **Transformações de Variáveis:** Técnicas para normalizar, padronizar e transformar variáveis
2. **Cálculo de Tamanho de Amostra:** Determinar quantas observações são necessárias para um estudo

---

## 📚 Conceitos Estatísticos Envolvidos

### 1. Normalidade e Q-Q Plots
- **Q-Q Plot (Quantil-Quantil):** Gráfico para verificar se dados seguem distribuição normal
- **Teste de Normalidade:** Verificar se dados são normalmente distribuídos
- **Transformações:** Técnicas para aproximar dados de uma distribuição normal

### 2. Transformações de Variáveis

#### Padronização (Z-score)
- **Fórmula:** $z = \frac{x - \mu}{\sigma}$
- **Resultado:** Média = 0, Desvio padrão = 1
- **Uso:** Comparar variáveis com escalas diferentes

#### Normalização (Min-Max)
- **Fórmula:** $x_{norm} = \frac{x - min(x)}{max(x) - min(x)}$
- **Resultado:** Valores entre 0 e 1
- **Uso:** Reduzir escala para algoritmos de machine learning

#### Transformações Matemáticas
- **Logarítmica:** $log(x)$ - Reduz assimetria positiva
- **Raiz Quadrada:** $\sqrt{x}$ - Reduz assimetria moderada
- **Raiz Cúbica:** $\sqrt[3]{x}$ - Reduz assimetria leve
- **Inversa Negativa:** $-\frac{1}{x}$ - Para assimetria extrema

### 3. Cálculo de Tamanho de Amostra

#### Para Estimar Média
- **Fórmula:** $n = \frac{Z^2 \times S^2}{e^2}$
- **Onde:**
  - $Z$ = valor crítico (1.96 para 95% de confiança)
  - $S$ = desvio padrão populacional (ou estimativa)
  - $e$ = margem de erro desejada

#### Para Estimar Proporção
- **Fórmula:** $n = \frac{Z^2 \times p \times (1-p)}{e^2}$
- **Onde:**
  - $p$ = proporção esperada (ou 0.5 se desconhecida)
  - $e$ = margem de erro desejada

#### Correção para População Finita
- Quando população é conhecida e pequena
- Reduz tamanho de amostra necessário

---

## 📁 Arquivos da Aula

### Scripts Principais
- **`aula_05.R`** - Script principal com todas as análises
- **`definitions.R`** - Definições e configurações
- **`install_load_packages.R`** - Instalação e carregamento de pacotes
- **`template_aula.R`** - Template para estrutura

### Dataset Utilizado
- **`birthwt`** - Dataset do pacote `MASS` com dados de peso ao nascer

---

## 🔍 Análise do Código

### Estrutura do Script `aula_05.R`

#### 1. **Q-Q Plots para Verificar Normalidade (linhas 22-43)**

##### 1.1 Histograma Inicial
```r
dados <- MASS::birthwt
hist(dados$bwt, xlab = "Peso ao nascimento (gramas)", 
     ylab = "Frequência", main = "")
```

**O que faz:**
- Carrega dataset de peso ao nascer
- Cria histograma para visualizar distribuição

**Conceitos:**
- **Histograma:** Mostra forma da distribuição
- Permite identificar assimetria

##### 1.2 Q-Q Plot com stats
```r
stats::qqnorm(dados$bwt, 
              ylab = "Peso no nascimento (gramas)",
              xlab = "Quantis normais",
              col = "dark green")
stats::qqline(dados$bwt, col = "red")
```

**O que faz:**
- Cria Q-Q plot comparando dados com distribuição normal
- Linha vermelha mostra distribuição normal teórica
- Se pontos seguem a linha, dados são aproximadamente normais

**Conceitos:**
- **Q-Q Plot:** Compara quantis dos dados com quantis teóricos
- **Interpretação:**
  - Pontos na linha = normal
  - Pontos curvados = não normal
  - Outliers = pontos distantes da linha

##### 1.3 Q-Q Plot com car
```r
car::qqPlot(dados$bwt, 
            col.lines = "red",
            col = "dark green",
            ylab = "Peso no nascimento (gramas)",
            xlab = "Quantis normais",
            main = "Normal Q-Q Plot")
```

**O que faz:**
- Versão melhorada do Q-Q plot
- Inclui intervalo de confiança
- Identifica outliers automaticamente

**Vantagens:**
- Mais informativo que `qqnorm()`
- Mostra intervalo de confiança
- Identifica outliers

---

#### 2. **Transformações de Variáveis (linhas 46-64)**

##### 2.1 Transformação de Unidades
```r
dados_adj <- dados %>% 
  dplyr::mutate(
    peso_mae = lwt*.453592,  # Libras para kg
    ...
  )
```

**O que faz:**
- Converte peso da mãe de libras para quilogramas
- Facilita interpretação

##### 2.2 Transformações Matemáticas
```r
peso_mae_log = log(peso_mae),           # Logarítmica
peso_mae_invneg = -1/(peso_mae),       # Inversa negativa
peso_mae_raiz2 = sqrt(peso_mae),        # Raiz quadrada
peso_mae_raiz3 = (peso_mae)^(1/3),      # Raiz cúbica
```

**O que faz:**
- Aplica diferentes transformações
- Cada uma reduz assimetria de forma diferente

**Conceitos:**
- **Log:** Reduz assimetria positiva forte
- **Raiz:** Reduz assimetria moderada
- **Inversa:** Para assimetria extrema

##### 2.3 Padronização (Z-score)
```r
peso_pad = scale(peso_mae),  # Usando função scale()
peso_pad_calc = (peso_mae - mean(peso_mae))/sd(peso_mae)  # Manual
```

**O que faz:**
- Padroniza variável (média = 0, desvio = 1)
- Duas formas: usando `scale()` ou cálculo manual

**Conceitos:**
- **Z-score:** Quantos desvios padrão acima/abaixo da média
- **Uso:** Comparar variáveis com escalas diferentes

##### 2.4 Normalização (Min-Max)
```r
peso_nor = scales::rescale(peso_mae),  # Usando função
peso_nor_calc = (peso_mae - min(peso_mae))/(max(peso_mae) - min(peso_mae))  # Manual
```

**O que faz:**
- Normaliza variável para escala 0-1
- Duas formas: usando `scales::rescale()` ou cálculo manual

**Conceitos:**
- **Min-Max:** Reduz valores para intervalo [0, 1]
- **Uso:** Preparação para machine learning

##### 2.5 Categorização
```r
peso_mae_cat = dplyr::case_when(
  peso_mae <= 49 ~ "<= 49kg",
  peso_mae > 49 & peso_mae <= 60 ~ ">49 e <= 60kg",
  peso_mae > 60 ~ "> 60kg")
```

**O que faz:**
- Converte variável quantitativa em categórica
- Cria grupos para análise

**Conceitos:**
- **Categorização:** Discretização de variável contínua
- **Uso:** Simplificar análise ou criar grupos

---

#### 3. **Visualização das Transformações (linhas 68-75)**

##### 3.1 Histogramas Comparativos
```r
par(mfrow=c(2,3))
hist(dados_adj$peso_mae, ...)
hist(dados_adj$peso_mae_log, ...)
hist(dados_adj$peso_mae_invneg, ...)
hist(dados_adj$peso_mae_raiz2, ...)
hist(dados_adj$peso_mae_raiz3, ...)
hist(dados_adj$peso_pad, ...)
```

**O que faz:**
- Cria grid de 2×3 com histogramas
- Compara distribuições antes e depois das transformações

**Conceitos:**
- **par(mfrow):** Define layout de gráficos
- Permite comparar visualmente as transformações

##### 3.2 Q-Q Plots Comparativos (linhas 78-121)
```r
par(mfrow=c(2,3))
car::qqPlot(dados_adj$peso_mae, ...)
car::qqPlot(dados_adj$peso_mae_log, ...)
# ... outras transformações
```

**O que faz:**
- Compara normalidade antes e depois das transformações
- Identifica qual transformação melhor aproxima normalidade

**Interpretação:**
- Transformação que deixa pontos mais próximos da linha = melhor para normalidade

---

#### 4. **Cálculo de Tamanho de Amostra (linhas 123-139)**

##### 4.1 Para Estimar Média
```r
samplingbook::sample.size.mean(e = 10, S = 50, level = 0.95)
```

**Parâmetros:**
- `e = 10`: Margem de erro (R$ 10,00)
- `S = 50`: Desvio padrão (R$ 50,00)
- `level = 0.95`: Nível de confiança (95%)

**Exemplo do contexto:**
- Estimar ticket médio de clientes
- Média conhecida: R$ 200,00
- Desvio padrão: R$ 50,00
- Erro desejado: R$ 10,00
- Confiança: 95%

**Resultado:** Número de clientes necessários para a amostra

##### 4.2 Correção para População Finita
```r
samplingbook::sample.size.mean(e = 10, S = 50, level = 0.95, N = 530)
```

**O que faz:**
- Ajusta cálculo quando população total é conhecida
- Reduz tamanho de amostra necessário

**Conceitos:**
- **População Finita:** Quando conhecemos o total (N)
- **Correção:** Reduz amostra necessária
- **Fórmula:** $n_{ajustado} = \frac{n}{1 + \frac{n-1}{N}}$

##### 4.3 Para Estimar Proporção
```r
samplingbook::sample.size.prop(e = 0.05, P = 0.1, level = 0.95)
```

**Parâmetros:**
- `e = 0.05`: Margem de erro (5%)
- `P = 0.1`: Proporção esperada (10% de peças defeituosas)
- `level = 0.95`: Nível de confiança (95%)

**Exemplo do contexto:**
- Estimar proporção de peças defeituosas
- Proporção esperada: 10%
- Erro desejado: 5%
- Confiança: 95%

**Resultado:** Número de peças a inspecionar

##### 4.4 Correção para População Finita (Proporção)
```r
samplingbook::sample.size.prop(e = 0.05, P = 0.1, level = 0.95, N = 1500)
```

**O que faz:**
- Ajusta quando população total é conhecida (1500 peças/semana)
- Reduz amostra necessária

---

## 🚀 Como Executar

### Pré-requisitos
1. R instalado (versão 4.0+)
2. RStudio (recomendado)

### Passo a Passo

1. **Abra o projeto RStudio:**
```r
# File > Open Project > Aula5.Rproj
```

2. **Execute o script:**
```r
source("aula_05.R")
```

### Dependências

Pacotes instalados automaticamente:
- `dplyr` - Manipulação de dados
- `MASS` - Dataset birthwt
- `car` - Q-Q plots melhorados
- `samplingbook` - Cálculo de tamanho de amostra
- `scales` - Normalização

---

## 📊 Resultados Esperados

1. **Q-Q Plots:**
   - Visualização da normalidade dos dados
   - Identificação de outliers

2. **Histogramas Comparativos:**
   - Distribuições antes e depois das transformações
   - Identificação da melhor transformação

3. **Q-Q Plots Comparativos:**
   - Verificação de qual transformação melhor aproxima normalidade

4. **Cálculos de Tamanho de Amostra:**
   - Número de observações necessárias para estimar média
   - Número de observações necessárias para estimar proporção
   - Valores com e sem correção para população finita

---

## ⚠️ Problemas Identificados

### 1. Código Windows Específico
```r
windows()  # Linha 68 e 78
```
- **Problema:** Só funciona no Windows
- **Solução:** Usar `dev.new()` ou remover (RStudio abre automaticamente)

### 2. Falta de Limpeza de Dispositivos
```r
dev.off()  # Linha 121
```
- **Problema:** Só fecha no final, pode causar problemas
- **Solução:** Fechar após cada grid de gráficos

### 3. Erro de Expressão
```r
ylab = expression(sqrt('Peso da mãe', 3))  # Linha 116
```
- **Problema:** Sintaxe incorreta para raiz cúbica
- **Solução:** `ylab = expression(sqrt('Peso da mãe', 3))` ou texto simples

### 4. Falta de Validação
- **Problema:** Não verifica se transformações melhoraram normalidade
- **Solução:** Adicionar testes de normalidade (Shapiro-Wilk)

### 5. Comentários Insuficientes
- **Problema:** Algumas seções sem explicação
- **Solução:** Adicionar comentários explicativos

---

## 💡 Melhorias Sugeridas

### 1. Adicionar Testes de Normalidade
```r
# Testar normalidade antes e depois
shapiro_before <- shapiro.test(dados_adj$peso_mae)
shapiro_after <- shapiro.test(dados_adj$peso_mae_log)
cat("p-valor antes:", shapiro_before$p.value, "\n")
cat("p-valor depois:", shapiro_after$p.value, "\n")
```

### 2. Criar Função para Comparar Transformações
```r
comparar_transformacoes <- function(variavel) {
  # Aplica todas as transformações
  # Testa normalidade de cada uma
  # Retorna tabela comparativa
}
```

### 3. Usar ggplot2 para Gráficos
```r
# Grid de histogramas com ggplot2
library(gridExtra)
p1 <- ggplot(...) + geom_histogram()
p2 <- ggplot(...) + geom_histogram()
grid.arrange(p1, p2, p3, p4, p5, p6, ncol = 3)
```

### 4. Salvar Gráficos
```r
png("figures/qqplots_comparativos.png", width = 1200, height = 800)
# ... código dos gráficos
dev.off()
```

### 5. Documentar Resultados
```r
# Criar tabela com resultados
resultados <- data.frame(
  Transformacao = c("Original", "Log", "Raiz2", "Raiz3"),
  Shapiro_p = c(p1, p2, p3, p4),
  Melhor = c(FALSE, TRUE, FALSE, FALSE)
)
```

---

## 📦 Dependências

### Pacotes Necessários
- `dplyr` - Manipulação de dados
- `MASS` - Dataset birthwt
- `car` - Q-Q plots melhorados
- `samplingbook` - Cálculo de tamanho de amostra
- `scales` - Normalização

---

## 📚 Referências

- **Livro de Amostragem:** https://www.lume.ufrgs.br/handle/10183/175312
- **Transformações de Variáveis:** https://www.statisticshowto.com/transformations/
- **Q-Q Plots:** https://data.library.virginia.edu/understanding-q-q-plots/

---

## ✅ Checklist da Aula

- [x] Script principal funcional
- [x] Q-Q plots implementados
- [x] Transformações de variáveis implementadas
- [x] Cálculo de tamanho de amostra implementado
- [ ] Código Windows específico corrigido
- [ ] Testes de normalidade adicionados
- [ ] Gráficos salvos em arquivos
- [ ] README.md criado

---

**Autor:** Vinícius de Souza Cebalhos  
**Data:** 2024  
**Disciplina:** Estatística - UTFPR

