###
# Declarando caminho, definições e pacotes
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

yulu <- read.csv(paste0(project_root_path, "/yulu_bike_sharing_dataset.csv"))
View(yulu)
str(yulu)

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
                weather_adj = dplyr::case_when(weather == 3 | weather == 4 ~ 3,
                                               TRUE ~ weather),
                weather_factor = factor(weather_adj,
                                        levels = c(1, 2, 3),
                                        labels = c("Céu limpo/parcialmente nublado",
                                                   "Névoa + Nuvens",
                                                   "Chuva")),
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

table(yulu$hora_cat, yulu$hora)
table(yulu$weather, yulu$weather_adj)
table(yulu$weather_factor, yulu$weather_adj)

## 3. AED

yulu %>% 
  dplyr::select(-c(season, holiday, datetime, workingday, weather)) %>% 
  skimr::skim()


### 1. Existe diferença no total de viagens em dias de semana e feriados?

### H0: média de alugueis  por dia em feriados = média de alugueis /demais dias

q1 <- yulu %>% 
  dplyr::group_by(dia, holiday_factor) %>% 
  dplyr::summarise(total = sum(count)) %>% 
  dplyr::ungroup()

boxplot(q1$total ~ q1$holiday_factor)

hist(q1 %>%
       dplyr::filter(holiday_factor == "Não") %>% 
       dplyr::select(total) %>% 
       dplyr::pull()
)

hist(q1 %>%
       dplyr::filter(holiday_factor == "Sim") %>% 
       dplyr::select(total) %>% 
       dplyr::pull()
)

car::qqPlot(q1 %>%
              dplyr::filter(holiday_factor == "Não") %>% 
              dplyr::select(total) %>% 
              dplyr::pull())

shapiro.test(q1 %>%
               dplyr::filter(holiday_factor == "Não") %>% 
               dplyr::select(total) %>% 
               dplyr::pull()) # H0: os dados sao normais 

