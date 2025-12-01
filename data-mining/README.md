# 📊 Data Mining - Trabalhos e Projetos

Esta pasta contém todos os trabalhos desenvolvidos na disciplina de **Data Mining** da pós-graduação em Ciência de Dados.

---

## 📚 Trabalhos Desenvolvidos

### 🔍 [Web Scraping e Análise de Dados do YouTube](./web-scraping-youtube/)
**Objetivo:** Extrair e analisar dados do YouTube usando a API oficial do Google.

**Tecnologias:**
- Python (googleapiclient)
- YouTube Data API v3
- Pandas para análise

**Conteúdo:**
- Extração de dados de vídeos do YouTube
- Análise de estatísticas de vídeos
- Processamento de dados de API

**Arquivos principais:**
- `first.ipynb` - Notebook principal de extração
- `third.ipynb` - Análise dos dados extraídos

---

### 📈 [Regressão Linear e Análise de Dados](./regressao-linear/)
**Objetivo:** Aplicar conceitos fundamentais de dados e regressão linear em datasets reais.

**Tecnologias:**
- Python (pandas, numpy, scikit-learn)
- Regressão Linear
- Análise exploratória de dados

**Conteúdo:**
- Análise do dataset Iris
- Análise do dataset Titanic
- Regressão linear em dados de carros
- Estatísticas descritivas

**Datasets utilizados:**
- Iris.csv
- titanic.csv
- datasetCarros.csv

**Arquivos principais:**
- `Exercicio_Conceitos_fundamentais_de_dados_e_Regressão_Linear.ipynb`
- `Exercicio_Conceitos_fundamentais_de_dados_e_Regressão_Linear2.ipynb`

---

### 🎯 [Classificação e Agrupamento (Clustering)](./clustering-titanic/)
**Objetivo:** Aplicar técnicas de classificação e clustering em dados do Titanic.

**Tecnologias:**
- Python (scikit-learn)
- K-Means Clustering
- Algoritmos de Classificação

**Conteúdo:**
- Clustering de passageiros do Titanic
- Análise de grupos identificados
- Visualizações de clusters

**Arquivos principais:**
- `exercicio_titanic_clustering.ipynb`
- `ExercicioClassificacao_e_Agrupamento.pdf` - Enunciado do trabalho

---

### 🔗 [Regras de Associação e Mineração de Texto](./regras-associacao-texto/)
**Objetivo:** Aplicar técnicas de regras de associação e análise de texto.

**Tecnologias:**
- Python (mlxtend, nltk)
- Apriori Algorithm
- Processamento de Linguagem Natural

**Conteúdo:**
- Regras de associação em dados de supermercado
- Análise de sentimento em tweets
- Mineração de texto em dados do Twitter

**Datasets utilizados:**
- supermercado.csv
- tweets_trump.csv

**Arquivos principais:**
- `work4.ipynb` - Notebook principal
- `work4.html` - Versão HTML exportada

---

### 🏆 [Competição Kaggle - Previsão de Locais](../projects/competicao-kaggle-venues/)
**Objetivo:** Prever locais altamente avaliados em Toronto usando dados do Yelp.

**Competição:** Predict Highly Rated Venues CDA UTFPR 2024

**Resultados:**
- **Melhor Modelo:** Random Forest
- **F1-Score:** 0.9991
- **Score CV:** 0.9991 +/- 0.0003

**Tecnologias:**
- Python (scikit-learn, pandas, numpy)
- Random Forest Classifier
- Gradient Boosting
- Logistic Regression
- Grid Search para otimização

**Metodologia:**
1. Análise Exploratória de Dados (EDA)
2. Pré-processamento e feature engineering
3. Teste de múltiplos algoritmos
4. Otimização de hiperparâmetros
5. Validação cruzada

**📍 Este projeto está em destaque em [`projects/competicao-kaggle-venues/`](../projects/competicao-kaggle-venues/)**

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

### Principais
- **Python 3.x**
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Scikit-learn** - Machine Learning
- **Matplotlib/Seaborn** - Visualização

### Específicas
- **Google API Client** - Web scraping do YouTube
- **MLxtend** - Regras de associação (Apriori)
- **NLTK** - Processamento de linguagem natural
- **XGBoost** - Gradient Boosting

---

## 📊 Competências Demonstradas

- ✅ Web Scraping e APIs
- ✅ Análise Exploratória de Dados (EDA)
- ✅ Regressão Linear
- ✅ Classificação e Clustering
- ✅ Regras de Associação
- ✅ Mineração de Texto
- ✅ Feature Engineering
- ✅ Otimização de Modelos
- ✅ Validação Cruzada

---

## 📁 Estrutura de Pastas

```
data-mining/
├── README.md                    # Este arquivo
├── Aula3/                       # Exercícios de aula
├── web-scraping-youtube/        # Web Scraping YouTube
├── regressao-linear/            # Regressão Linear
├── clustering-titanic/           # Classificação e Clustering
├── regras-associacao-texto/     # Regras de Associação e Texto
└── lib/                         # Bibliotecas auxiliares

Nota: O projeto challenge foi movido para projects/ como projeto em destaque.
```

---

## 🚀 Como Executar

Cada trabalho possui seus próprios notebooks Jupyter. Para executar:

1. Instale as dependências:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

2. Abra o notebook desejado:
```bash
jupyter notebook [nome-do-projeto]/[nome_do_notebook].ipynb
```

3. Execute as células sequencialmente

---

## 📝 Notas

- Alguns datasets podem precisar ser baixados separadamente
- APIs podem requerer chaves de acesso (YouTube API)
- Os notebooks estão documentados em português
- Resultados e visualizações são gerados automaticamente

---

**Disciplina:** Data Mining  
**Autor:** Vinícius de Souza Cebalhos  
**Instituição:** UTFPR

