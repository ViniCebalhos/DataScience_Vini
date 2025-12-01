###
# Definição caminho, definições e pacotes
###

# Diretório do projeto, de onde serão salvos e lidos os arquivos
project_root_path <- paste0(getwd())

###
# Variáveis e definições
###
source(paste0(project_root_path, "/definitions.R"))

###
# Instalando e carregando pacotes 
###
source(paste0(project_root_path, "/install_load_packages.R"), encoding = encoding)

##############
#   AULA 7 
##############

### 1. Leitura dos dados
yulu <- read.csv(paste0(project_root_path, "/yulu_bike_sharing_dataset.csv"))
head(yulu)
str(yulu)
### Unidade observacional é dia/hora.

### 2. Declarar como fator as variáveis que são qualitativas e criar algumas variáveis úteis
yulu <- yulu %>% 
  dplyr::mutate(season_factor = factor(season,
                                       levels = c(2, 3, 4, 1),
                                       labels = c("Primavera", "Verão", "Outono", "Inverno")),
                holiday_factor = factor(holiday,
                                        levels = c(0, 1),
                                        labels = c('Não', 'Sim')),
                workingday_factor = factor(workingday,
                                           levels = c(0, 1),
                                           labels = c('Não', 'Sim')),
                weather_factor = factor(weather,
                                        levels = c(1, 2, 3, 4),
                                        labels = c("Céu limpo/parcialmente nublado",
                                                   "Névoa + Nuvens",
                                                   "Chuva/Neve leve + trovoada",
                                                   "Chuva forte + granizo + trovoada + névoa")),
                dia = lubridate::as_date(datetime),
                hora = lubridate::hour(datetime),
                ano_mes = lubridate::floor_date(dia, 'month'),
                hora_cat = factor(case_when(
                  between(hora, 6, 9)  ~ "Manhã ini",
                  between(hora, 10, 11) ~ "Manhã",
                  between(hora, 12, 13) ~ "Tarde ini",
                  between(hora, 14, 16) ~ "Tarde",
                  between(hora, 17, 20) ~ "Fim do dia",
                  TRUE ~ "Noite/Madrugada"),
                  levels = c("Manhã ini", "Manhã", "Tarde ini", "Tarde", "Fim do dia", "Noite/Madrugada"))
  )
head(yulu)
str(yulu)

#### "prova real"
table(yulu$season, yulu$season_factor)
table(yulu$holiday, yulu$holiday_factor)
table(yulu$workingday, yulu$workingday_factor)
table(yulu$weather, yulu$weather_factor)

### 3. AED! 
yulu %>% 
  dplyr::select(-c(datetime, season, holiday, workingday, weather)) %>% 
  skimr::skim()

## Há tendência de queda de aluguéis?
uso_dia <- yulu %>% 
  dplyr::select(dia, count) %>% 
  dplyr::group_by(dia) %>% 
  dplyr::summarise(total_alugueis = sum(count)) %>% 
  dplyr::ungroup()

plot(uso_dia$dia, uso_dia$total_alugueis, type = "l",
     main = "Total de aluguéis por dia ao longo do tempo",
     xlab = "Dia",
     ylab = "Total de aluguéis",
     col = "blue",
     lwd = 2
)

### Vamos explorar um pouco os dados pensando sempre na pergunta principal: o que impacta no n. de aluguéis (count)?

boxplot(yulu$count ~ yulu$season_factor) # unidade observacional: alugueis/dia/hora
boxplot(yulu$count ~ yulu$holiday_factor) # unidade observacional: alugueis/dia/hora
boxplot(yulu$count ~ yulu$holiday_factor)$stats
boxplot(yulu$count ~ yulu$workingday_factor) # unidade observacional: alugueis/dia/hora
boxplot(yulu$count ~ yulu$weather_factor)
plot(yulu$humidity, yulu$count)
plot(yulu$windspeed, yulu$count)

viagens_hora <- yulu %>% 
  dplyr::group_by(workingday_factor, hora) %>% 
  dplyr::summarise(media_alugueis = mean(count)) %>% 
  dplyr::ungroup()

par(mfrow = c(1, 2))  
barplot(height = viagens_hora %>% 
          dplyr::filter(workingday_factor == 'Não') %>% 
          dplyr::select(media_alugueis) %>%
          dplyr::pull(),
        names.arg = viagens_hora %>% 
          dplyr::filter(workingday_factor == 'Não') %>% 
          dplyr::select(hora) %>%
          dplyr::pull(),
        xlab = "Hora",
        ylab = "N. médio de alugúeis",
        col = "skyblue",
        border = "white",
        main = "Aluguéis em finais de semana ou feriados")

barplot(height = viagens_hora %>% 
          dplyr::filter(workingday_factor == 'Sim') %>% 
          dplyr::select(media_alugueis) %>%
          dplyr::pull(),
        names.arg = viagens_hora %>% 
          dplyr::filter(workingday_factor == 'Sim') %>% 
          dplyr::select(hora) %>%
          dplyr::pull(),
        xlab = "Hora",
        ylab = "N. médio de alugúeis",
        col = "skyblue",
        border = "white",
        main = "Aluguéis em dias de semana")
par(mfrow = c(1, 1))  

boxplot(yulu$count ~ yulu$hora_cat)

### O que entendi dessa parte? Quais variáveis parecem impactar no n. de aluguéis? 
#### Lembrando que: aqui na AED minha unidade observacional é alugueis/dia/hora

### 4. Utilizando testes para verificar algumas das minhas hipóteses...

################
### Existe diferença no n. de aluguéis por dia em feriados?
################
## H0: n. médio de aluguéis por dia em feriados = n. médio de aluguéis por dia em dias normais 
## H1: n. médio de aluguéis por dia em feriados # n. médio de aluguéis por dia em dias normais
### Que teste utilizar?

#### Primeiro passo, sempre: AED!
q1 <- yulu %>% 
  dplyr::group_by(dia, holiday_factor) %>% 
  dplyr::summarise(n_alugueis = sum(count)) %>% 
  dplyr::ungroup()

q1 %>% 
  dplyr::group_by(holiday_factor) %>% 
  dplyr::summarise(
    q1 = quantile(n_alugueis, probs = 0.25),
    mediana_alugueis = median(n_alugueis),
    q3 = quantile(n_alugueis, probs = 0.75),
    n = n())


boxplot(q1$n_alugueis ~ q1$holiday_factor)

# Configurar layout com 1 linha e 2 colunas para os gráficos
par(mfrow = c(1, 2))  

# Histograma para feriados (categoria Sim)
hist(q1 %>% 
       dplyr::filter(holiday_factor == "Sim") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Feriado: Sim",
     xlab = "Nº de Aluguéis",
     col = "tomato",
     border = "white")

# Histograma para dias normais (categoria Não)
hist(q1 %>% 
       dplyr::filter(holiday_factor == "Não") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Feriado: Não",
     xlab = "Nº de Aluguéis",
     col = "steelblue",
     border = "white")

#### Comparação de médias: quais as possibilidades?

#### Para teste t: distribuição normal e variâncias homocedasticas
car::qqPlot(q1$n_alugueis[q1$holiday_factor == "Sim"],
            main = "Feriado: Sim")
car::qqPlot(q1$n_alugueis[q1$holiday_factor == "Não"],
            main = "Feriado: Não")
# Resetar layout
par(mfrow = c(1, 1))

shapiro.test(q1$n_alugueis[q1$holiday_factor == "Sim"]) # H0: dados são normais
### Obs.: shapiro.test() é limitado a 5.000 observações. 
### Se sua amostra for maior que isso, nortest::ad.test() é o teste alternativo!
ad.test(q1$n_alugueis[q1$holiday_factor == "Sim"]) # H0: dados são normais

shapiro.test(q1$n_alugueis[q1$holiday_factor == "Não"]) # H0: dados são normais
car::leveneTest(n_alugueis ~ holiday_factor , data = q1) # H0: variâncias são iguais

wilcox.test(n_alugueis ~ holiday_factor , data = q1, alternative = "two.sided")
## Conclusão?


################
### Existe diferença no n. de aluguéis por dia em dias úteis e finais de semana?
################
## H0: n. médio de aluguéis por dia em dias úteis = n. médio de aluguéis por dia em fins de semana 
## H1: n. médio de aluguéis por dia em dias úteis # n. médio de aluguéis por dia em fins de semana
### Que teste utilizar?

#### Primeiro passo, sempre: AED!
q2 <- yulu %>% 
  dplyr::group_by(dia, workingday_factor) %>% 
  dplyr::summarise(n_alugueis = sum(count)) %>% 
  dplyr::ungroup()

q2 %>% 
  dplyr::group_by(workingday_factor) %>% 
  dplyr::summarise(
    q1 = quantile(n_alugueis, probs = 0.25),
    mediana_alugueis = median(n_alugueis),
    q3 = quantile(n_alugueis, probs = 0.75),
    n = n())


boxplot(q2$n_alugueis ~ q2$workingday_factor)

# Configurar layout com 1 linha e 2 colunas para os gráficos
par(mfrow = c(1, 2))  
hist(q2 %>% 
       dplyr::filter(workingday_factor == "Sim") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Dia de semana: Sim",
     xlab = "Nº de Aluguéis",
     col = "tomato",
     border = "white")
hist(q2 %>% 
       dplyr::filter(workingday_factor == "Não") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Dia de semana: Não",
     xlab = "Nº de Aluguéis",
     col = "steelblue",
     border = "white")

#### Comparação de médias: que testes posso utilizar?
#### Para teste t: distribuição normal e variâncias homocedasticas
car::qqPlot(q1$n_alugueis[q2$workingday_factor == "Sim"],
            main = "Feriado: Sim")
car::qqPlot(q1$n_alugueis[q2$workingday_factor == "Não"],
            main = "Feriado: Não")
# Resetar layout
par(mfrow = c(1, 1))

shapiro.test(q2$n_alugueis[q2$workingday_factor == "Sim"]) # H0: dados são normais
shapiro.test(q2$n_alugueis[q2$workingday_factor == "Não"]) # H0: dados são normais
car::leveneTest(n_alugueis ~ workingday_factor , data = q2) # H0: variâncias são iguais

wilcox.test(n_alugueis ~ workingday_factor , data = q2, alternative = "two.sided")
## Conclusão?


################
### Existe diferença no n. de aluguéis por dia, considerando as diferentes estações do ano?
################
## H0: n. médio de aluguéis primavera = n. médio de aluguéis verão =  n. médio de aluguéis outono = n. médio de aluguéis inverno
## H1: médias são diferentes para algum par de comparação
### Que teste utilizar?

#### Primeiro passo, sempre: AED!
q3 <- yulu %>% 
  dplyr::group_by(dia, season_factor) %>% 
  dplyr::summarise(n_alugueis = sum(count)) %>% 
  dplyr::ungroup()

q3 %>% 
  dplyr::group_by(season_factor) %>% 
  dplyr::summarise(
    q1 = quantile(n_alugueis, probs = 0.25),
    mediana_alugueis = median(n_alugueis),
    q3 = quantile(n_alugueis, probs = 0.75),
    n = n())


boxplot(q3$n_alugueis ~ q3$season_factor)

# Configurar layout com 2 linhas e 2 colunas para os gráficos
par(mfrow = c(2, 2))  

# Histograma por estação
hist(q3 %>% 
       dplyr::filter(season_factor == "Primavera") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Estação: Primavera",
     xlab = "Nº de Aluguéis",
     col = "#66C2A5",
     border = "white")

hist(q3 %>% 
       dplyr::filter(season_factor == "Verão") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Estação: Verão",
     xlab = "Nº de Aluguéis",
     col = "#FC8D62",
     border = "white")

hist(q3 %>% 
       dplyr::filter(season_factor == "Outono") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Estação: Outono",
     xlab = "Nº de Aluguéis",
     col = "#8DA0CB",
     border = "white")

hist(q3 %>% 
       dplyr::filter(season_factor == "Inverno") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Estação: Inverno",
     xlab = "Nº de Aluguéis",
     col = "#E78AC3",
     border = "white")

#### Comparação de mais do que duas médias: que testes posso utilizar?
#### Para anova: distribuição normal
car::qqPlot(q3$n_alugueis[q3$season_factor == "Primavera"],
            main = "Estação: Primavera")
car::qqPlot(q3$n_alugueis[q3$season_factor == "Verão"],
            main = "Estação: Verão")
car::qqPlot(q3$n_alugueis[q3$season_factor == "Outono"],
            main = "Estação: Outono")
car::qqPlot(q3$n_alugueis[q3$season_factor == "Inverno"],
            main = "Estação: Inverno")
# Resetar layout
par(mfrow = c(1, 1))

shapiro.test(q3$n_alugueis[q3$season_factor == "Primavera"]) # H0: dados são normais
shapiro.test(q3$n_alugueis[q3$season_factor == "Verão"]) # H0: dados são normais
shapiro.test(q3$n_alugueis[q3$season_factor == "Outono"]) # H0: dados são normais
shapiro.test(q3$n_alugueis[q3$season_factor == "Inverno"]) # H0: dados são normais
car::leveneTest(n_alugueis ~ season_factor , data = q3) # H0: variâncias são iguais

kruskal.test(n_alugueis ~ season_factor, data = q3) # H0: medianas são iguais
dunn.test(q3$n_alugueis, q3$season_factor, method = "bonferroni")
## Conclusão: ?

################
### Existe diferença no n. de aluguéis por dia, considerando as diferentes condições climáticas?
################
## H0: n. médio de aluguéis em dias com céu limpo = n. médio de aluguéis em dias de névoa = n. médio de alugúeis em dias com chuva
### Que teste utilizar?

#### Primeiro passo, sempre: AED!
q4 <- yulu %>% 
  dplyr::group_by(dia, weather_factor) %>% 
  dplyr::summarise(n_alugueis = sum(count)) %>% 
  dplyr::ungroup() %>% 
  dplyr::group_by(dia) %>% 
  dplyr::mutate(maximo = max(n_alugueis)) %>% 
  dplyr::filter(n_alugueis == maximo)

q4 %>% 
  dplyr::group_by(weather_factor) %>% 
  dplyr::summarise(
    q1 = quantile(n_alugueis, probs = 0.25),
    mediana_alugueis = median(n_alugueis),
    q3 = quantile(n_alugueis, probs = 0.75),
    n = n())

q4_adj <- yulu %>% 
  dplyr::mutate(weather_factor_adj = dplyr::case_when(weather_factor %in% c("Chuva/Neve leve + trovoada", "Chuva forte + granizo + trovoada + névoa") ~ 'Chuva',
                                                      TRUE ~ weather_factor)) %>% 
  dplyr::group_by(dia, weather_factor_adj) %>% 
  dplyr::summarise(n_alugueis = sum(count)) %>% 
  dplyr::ungroup()

q4_adj %>% 
  dplyr::group_by(weather_factor_adj) %>% 
  dplyr::summarise(
    q1 = quantile(n_alugueis, probs = 0.25),
    mediana_alugueis = median(n_alugueis),
    q3 = quantile(n_alugueis, probs = 0.75),
    n = n())

boxplot(q4_adj$n_alugueis ~ q4_adj$weather_factor_adj)

# Configurar layout com 2 linhas e 2 colunas para os gráficos
par(mfrow = c(2, 2))  

# Histograma por estação
hist(q4_adj %>% 
       dplyr::filter(weather_factor_adj == "Céu limpo/parcialmente nublado") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Condição tempo: Céu limpo/parcialmente nublado",
     xlab = "Nº de Aluguéis",
     col = "#66C2A5",
     border = "white")

hist(q4_adj %>% 
       dplyr::filter(weather_factor_adj == "Névoa + Nuvens") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Condição tempo: Névoa + Nuvens",
     xlab = "Nº de Aluguéis",
     col = "#FC8D62",
     border = "white")

hist(q4_adj %>% 
       dplyr::filter(weather_factor_adj == "Chuva") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Condição tempo: Chuva",
     xlab = "Nº de Aluguéis",
     col = "#8DA0CB",
     border = "white")

# Resetar layout
par(mfrow = c(1, 1))

shapiro.test(q4_adj$n_alugueis[q4_adj$weather_factor_adj == "Céu limpo/parcialmente nublado"]) # H0: dados são normais
shapiro.test(q4_adj$n_alugueis[q4_adj$weather_factor_adj == "Névoa + Nuvens"]) # H0: dados são normais
shapiro.test(q4_adj$n_alugueis[q4_adj$weather_factor_adj == "Chuva"]) # H0: dados são normaisshapiro.test(q3$n_alugueis[q3$season_factor == "Inverno"]) # H0: dados são normais

kruskal.test(n_alugueis ~ weather_factor_adj, data = q4_adj) # H0: medianas são iguais
dunn.test(q4_adj$n_alugueis, q4_adj$weather_factor_adj, method = "bonferroni")
## Conclusão: ?


################
### Existe correlação entre velociodade do vento e total de viagens?
################
## H0: rho = 0
### Que teste utilizar?

#### Primeiro passo, sempre: AED!
q5 <- yulu %>% 
  dplyr::group_by(dia) %>% 
  dplyr::summarise(velocidade_vento = median(windspeed),
                   n_alugueis = sum(count)) %>% 
  dplyr::ungroup()

plot(y = q5$n_alugueis,
     x = q5$velocidade_vento )

hist(q5$n_alugueis)
hist(q5$velocidade_vento)

shapiro.test(q5$n_alugueis) # H0: dados são normais
shapiro.test(q5$velocidade_vento) # H0: dados são normais

cor.test(y = q5$n_alugueis,
         x = q5$velocidade_vento,
         method = "spearman")
## Conclusão: ?

################
### Existe diferença no n. de alugueis por dia considerando os turnos?
################
## H0: n. médio de aluguéis por dia do início da manhã = ... = n. médio de aluguéis por dia de madrugada
## H1: médias são diferentes para algum par de comparação
### Que teste utilizar?

#### Primeiro passo, sempre: AED!
q6 <- yulu %>% 
  dplyr::group_by(dia, hora_cat) %>% 
  dplyr::summarise(n_alugueis = sum(count)) %>% 
  dplyr::ungroup()

q6 %>% 
  dplyr::group_by(hora_cat) %>% 
  dplyr::summarise(
    q1 = quantile(n_alugueis, probs = 0.25),
    mediana_alugueis = median(n_alugueis),
    q3 = quantile(n_alugueis, probs = 0.75),
    n = n())

boxplot(q6$n_alugueis ~ q6$hora_cat)

# Configurar layout com 2 linhas e 2 colunas para os gráficos
par(mfrow = c(3, 2))  

# Histograma por hora_cat
hist(q6 %>% 
       dplyr::filter(hora_cat == "Manhã ini") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Turno: Início da manhã",
     xlab = "Nº de Aluguéis",
     col = "#FC8D62",
     border = "white")

hist(q6 %>% 
       dplyr::filter(hora_cat == "Manhã") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Turno: Manhã",
     xlab = "Nº de Aluguéis",
     col = "#FC8D62",
     border = "white")

hist(q6 %>% 
       dplyr::filter(hora_cat == "Tarde ini") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Turno: Início da tarde",
     xlab = "Nº de Aluguéis",
     col = "#FC8D62",
     border = "white")

hist(q6 %>% 
       dplyr::filter(hora_cat == "Tarde") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Turno: Tarde",
     xlab = "Nº de Aluguéis",
     col = "#FC8D62",
     border = "white")
hist(q6 %>% 
       dplyr::filter(hora_cat == "Fim do dia") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Turno: Fim do dia",
     xlab = "Nº de Aluguéis",
     col = "#FC8D62",
     border = "white")

hist(q6 %>% 
       dplyr::filter(hora_cat == "Noite/Madrugada") %>% 
       dplyr::select(n_alugueis) %>% 
       dplyr::pull(),
     main = "Turno: Noite/Madrugada",
     xlab = "Nº de Aluguéis",
     col = "#FC8D62",
     border = "white")

# Resetar layout
par(mfrow = c(1, 1))

shapiro.test(q6$n_alugueis[q6$hora_cat == "Manhã ini"]) # H0: dados são normais

kruskal.test(n_alugueis ~ hora_cat, data = q6) # H0: medianas são iguais
dunn.test(q6$n_alugueis, q6$hora_cat, method = "bonferroni")
## Conclusão: ?
