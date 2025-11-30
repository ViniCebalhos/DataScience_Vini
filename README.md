# 📊 Portfólio de Ciência de Dados - Pós-Graduação

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Autor:** Vinícius de Souza Cebalhos  
**Instituição:** Universidade Tecnológica Federal do Paraná (UTFPR)  
**Área:** Especialização em Ciência de Dados

---

## 🎯 Sobre o Portfólio

Este repositório contém todos os trabalhos desenvolvidos durante a pós-graduação em Ciência de Dados, demonstrando competências em:

- **Análise Exploratória de Dados (EDA)**
- **Mineração de Dados (Data Mining)**
- **Banco de Dados e SQL**
- **Machine Learning e Modelagem Preditiva**
- **Visualização de Dados**
- **Análise Estatística**
- **Análise Geoespacial**

---

## 📚 Estrutura do Portfólio

### 🗂️ [Data Mining](./data_mining/)
Trabalhos de mineração de dados, incluindo:
- **Work 1:** Web Scraping e Análise de Dados do YouTube
- **Work 2:** Regressão Linear e Análise de Dados
- **Work 3:** Classificação e Agrupamento (Clustering)
- **Work 4:** Regras de Associação e Mineração de Texto
- **Challenge:** Competição Kaggle - Previsão de Locais Altamente Avaliados (F1-Score: 0.9991)

### 🗄️ [Banco de Dados](./databank/)
Projetos envolvendo SQL, PostgreSQL e análise de dados:
- **Work 1:** Análise de Alvarás de Construção
- **Work 2:** Análise Exploratória de Acidentes de Trânsito
- **Work 3:** Consultas SQL Avançadas
- **Work 6:** Artigo Científico - Análise de Acidentes em Rodovias Federais (67.794 acidentes)
- **Work 8:** Análise Espacial de Acidentes com PostGIS (73.156 acidentes, mapas interativos)

### 🤖 [Machine Learning](./ML/)
Projetos de aprendizado de máquina:
- **Work 1:** Regressão Linear - Previsão de Preços de Imóveis
- **Work 2:** Classificação Multiclasse - Indicadores Sociais Globais
- **Work 3:** Classificação de Sinais Vitais

### 🏥 [Análise de Dados em Saúde](./Trabalho/)
Projeto completo de análise de dados do Sistema E-Saúde de Curitiba:
- Análise temporal de atendimentos (Dez/2024 - Jul/2025)
- Análise geográfica por bairros
- Análise de profissionais de saúde
- Limpeza e preparação de dados (~46.000 registros/mês)

### 📖 [Tutoriais](./tutoriais/)
Materiais de estudo e tutoriais desenvolvidos durante o curso.

### 📝 [Exercícios](./exercicios/)
Exercícios práticos e notebooks de estudo.

---

## 🏆 Projetos em Destaque

### 1. 🗺️ [Análise Espacial de Acidentes com PostGIS](./databank/Work8/)
**Tecnologias:** PostgreSQL, PostGIS, Python, Folium, Geopandas  
**Resultado:** Artigo científico completo publicado  
**Destaque:** 
- Análise de **73.156 acidentes** em rodovias federais
- Mapeamento de **169 postos da PRF**
- Mapas interativos com análise de proximidade espacial
- Identificação de que 80% dos acidentes ocorrem fora da cobertura direta

**Impacto:** Metodologia replicável para análise geoespacial de segurança viária.

---

### 2. 🏅 [Competição Kaggle - Previsão de Locais](./data_mining/challenge/)
**Tecnologias:** Python, scikit-learn, Random Forest, XGBoost  
**Resultado:** **F1-Score de 0.9991** (Top performance)  
**Destaque:**
- Random Forest otimizado com Grid Search
- Validação cruzada estratificada (5-fold)
- Feature engineering completo
- Análise comparativa de múltiplos algoritmos

**Impacto:** Demonstração de capacidade de modelagem preditiva avançada em competições.

---

### 3. 📄 [Análise de Acidentes em Rodovias Federais](./databank/Work6/)
**Tecnologias:** PostgreSQL, Python, SQL, LaTeX  
**Resultado:** Artigo científico completo (padrão SBC)  
**Destaque:**
- Análise de **67.794 acidentes**
- Identificação de padrões temporais (picos em dezembro, outubro, julho)
- Horário crítico: 17h-19h
- Principais causas: Reação tardia (27,3%), Ausência de reação (22,4%)

**Impacto:** Insights valiosos para políticas públicas de segurança viária.

---

### 4. 🏥 [Análise do Sistema E-Saúde de Curitiba](./Trabalho/)
**Tecnologias:** Python, Pandas, Análise Temporal, Visualização  
**Resultado:** Projeto completo de análise em saúde pública  
**Destaque:**
- Processamento de **~46.000 registros mensais**
- Análise temporal (Dez/2024 - Jul/2025)
- Análise geográfica por bairros
- Limpeza e preparação de dados em larga escala

**Impacto:** Análise completa demonstrando capacidade de trabalhar com dados reais de saúde pública.

---

### 5. 💓 [Classificação de Sinais Vitais](./ML/Work3/)
**Tecnologias:** Python, scikit-learn, Classificação Multiclasse  
**Resultado:** Análise comparativa de múltiplos modelos  
**Destaque:**
- Comparação detalhada de métricas
- Análise de distribuições por classe
- Visualizações profissionais
- Feature importance e correlações

**Impacto:** Demonstração de capacidade de análise de dados médicos e classificação.

---

## 🛠️ Tecnologias Utilizadas

### Linguagens e Frameworks
- **Python** (pandas, numpy, scikit-learn, matplotlib, seaborn)
- **SQL** (PostgreSQL, PostGIS)
- **Jupyter Notebooks**
- **LaTeX** (artigos científicos)

### Bibliotecas Principais
- **Machine Learning:** scikit-learn, XGBoost, PyCaret
- **Visualização:** matplotlib, seaborn, plotly, folium
- **Análise:** pandas, numpy, scipy, statsmodels
- **Geoprocessamento:** geopandas, PostGIS
- **Web Scraping:** google-api-python-client

---

## 📈 Métricas e Resultados

### Modelos de Machine Learning
- **Regressão Linear:** RMSE otimizado para previsão de preços
- **Classificação:** F1-Score de até **0.9991** em competições
- **Clustering:** Análise de padrões em dados não supervisionados

### Análises Estatísticas
- Análise de **67.794+ acidentes** de trânsito
- Processamento de **46.000+ registros mensais** de saúde
- Análise temporal de múltiplos períodos
- Análise geoespacial de **73.156 acidentes**

---

## 🎓 Competências Demonstradas

### Técnicas
- ✅ Pré-processamento e limpeza de dados
- ✅ Feature Engineering
- ✅ Modelagem preditiva (regressão, classificação, clustering)
- ✅ Validação cruzada e otimização de hiperparâmetros
- ✅ Análise exploratória de dados (EDA)
- ✅ Visualização de dados profissional
- ✅ Análise estatística descritiva e inferencial
- ✅ Análise geoespacial com PostGIS
- ✅ Web Scraping e APIs
- ✅ Redação científica (LaTeX)

### Domínios
- ✅ Saúde Pública
- ✅ Segurança Viária
- ✅ Análise Geoespacial
- ✅ Análise Temporal
- ✅ Indicadores Sociais

---

## 🚀 Como Navegar

Cada pasta de trabalho contém:
- **README.md** com descrição detalhada do projeto
- **Notebooks Jupyter** (.ipynb) com análises completas
- **Scripts Python** (.py) quando aplicável
- **Dados** (quando permitido) ou instruções para obtenção
- **Visualizações** e resultados gerados

---

## 📦 Instalação

### Requisitos
```bash
# Instalar dependências Python
pip install -r requirements.txt

# Para trabalhos com PostgreSQL
# Instalar PostgreSQL e PostGIS separadamente
sudo apt-get install postgresql postgresql-contrib postgis

# Para compilar artigos LaTeX
sudo apt-get install texlive-latex-extra texlive-fonts-recommended texlive-lang-portuguese
```

---

## 📝 Estrutura de Pastas

```
datascience/
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos a ignorar
├── requirements.txt             # Dependências Python
│
├── data_mining/                 # Trabalhos de Data Mining
│   ├── README.md
│   ├── work1/                   # Web Scraping YouTube
│   ├── work2/                   # Regressão Linear
│   ├── work3/                   # Clustering
│   ├── work4/                   # Regras de Associação
│   └── challenge/               # Competição Kaggle
│
├── databank/                    # Trabalhos de Banco de Dados
│   ├── README.md
│   ├── Work1/                   # Alvarás
│   ├── Work2/                   # Acidentes Exploratória
│   ├── Work3/                   # SQL Avançado
│   ├── Work6/                   # Artigo Científico
│   └── Work8/                   # Análise Espacial
│
├── ML/                          # Trabalhos de Machine Learning
│   ├── README.md
│   ├── Work1/                   # Regressão Imóveis
│   ├── Work2/                   # Classificação Global
│   └── Work3/                   # Sinais Vitais
│
├── Trabalho/                    # Projeto E-Saúde
│   └── README.md
│
├── tutoriais/                   # Materiais de estudo
│   └── README.md
│
└── exercicios/                  # Exercícios práticos
    └── README.md
```

---

## 📧 Contato e Links

Para dúvidas, sugestões ou oportunidades de trabalho:

- **GitHub:** [@seu-usuario](https://github.com/seu-usuario)
- **LinkedIn:** [Seu perfil LinkedIn](https://linkedin.com/in/seu-perfil)
- **Email:** seu.email@exemplo.com

---

## 📚 Documentação Adicional

- [Guia Completo do GitHub](./GUIA_GITHUB.md) - Como publicar e organizar no GitHub
- [Passo a Passo GitHub](./PASSO_A_PASSO_GITHUB.md) - Tutorial detalhado de configuração
- [Resumo da Organização](./RESUMO_ORGANIZACAO.md) - O que foi organizado no portfólio

---

## 📄 Licença

Este portfólio é de uso educacional e acadêmico. Os dados utilizados são públicos ou foram fornecidos para fins acadêmicos.

---

**Última atualização:** 2025
