# 🤖 Machine Learning - Trabalhos e Projetos

Esta pasta contém todos os trabalhos desenvolvidos na disciplina de **Machine Learning** da pós-graduação em Ciência de Dados.

---

## 📚 Trabalhos Desenvolvidos

### 🏠 [Regressão Linear - Previsão de Preços de Imóveis](./regressao-imoveis/)
**Objetivo:** Ajustar um modelo de regressão linear para prever preços de imóveis.

**Tecnologias:**
- Python (scikit-learn, pandas, numpy)
- Regressão Linear
- Métricas de avaliação (RMSE)

**Conteúdo:**
- Análise exploratória de dados de imóveis
- Treinamento de modelo de regressão linear
- Avaliação com Erro Quadrático Médio (RMSE)
- Análise de resíduos

**Datasets:**
- `Imoveis_Fabro_treino.csv` - Dataset de treino
- `Imoveis_Fabro_teste.csv` - Dataset de teste

**Arquivos principais:**
- `regressao_linear_imoveis.py` - Script Python completo
- `tarefa1.txt` - Enunciado do trabalho

**Métricas:**
- RMSE otimizado no conjunto de teste
- Análise de performance do modelo

---

### 🌍 [Classificação Multiclasse - Indicadores Sociais Globais](./classificacao-indicadores/)
**Objetivo:** Classificar países em categorias baseadas em indicadores sociais globais.

**Tecnologias:**
- Python (scikit-learn, pandas, numpy, matplotlib, seaborn)
- Logistic Regression
- Random Forest
- XGBoost (Gradient Boosting)
- Validação cruzada estratificada
- SMOTE para balanceamento

**Conteúdo:**
- Análise exploratória completa (EDA)
- Auditoria inicial de dados
- Pré-processamento e feature engineering
- Teste de múltiplos algoritmos
- Otimização de hiperparâmetros
- Análise de feature importance
- Partial Dependence Plots
- Visualizações profissionais

**Dataset:**
- `gdp-and-homicides-vs-happiness-vs-hdi_FabroClassification2025OK_4classes.csv`
- Indicadores: GDP, Homicides, Happiness, HDI, Cantrill Ladder

**Arquivos principais:**
- `Vinicius_Cebalhos_classificacao.ipynb` - Notebook completo (47 células)
- `VERIFICACAO_COMPLETA.md` - Checklist de implementação
- Visualizações: boxplots, histogramas, heatmaps, matrizes de confusão, ROC curves, feature importance

**Metodologia:**
1. **Carregamento e Auditoria:** Verificação de qualidade dos dados
2. **EDA Completa:** Estatísticas descritivas, distribuições, correlações
3. **Preparação:** Tratamento de valores ausentes, normalização, encoding
4. **Modelagem:** Teste de 3 algoritmos com validação cruzada
5. **Interpretação:** Feature importance e análise de resultados

**Métricas Avaliadas:**
- Accuracy
- Precision
- Recall
- F1-Score
- Matriz de Confusão
- ROC Curve + AUC (One-vs-Rest para multiclasse)

**Resultados:**
- Comparação detalhada entre modelos
- Identificação do melhor modelo e justificativa
- Análise de variáveis mais relevantes

---

### 💓 [Classificação de Sinais Vitais](../projects/classificacao-sinais-vitais/)
**Objetivo:** Classificar sinais vitais em diferentes categorias usando machine learning.

**Tecnologias:**
- Python (scikit-learn, pandas, numpy, matplotlib, seaborn)
- Algoritmos de classificação
- Análise de métricas comparativas
- Visualizações profissionais

**Conteúdo:**
- Análise exploratória de sinais vitais
- Pré-processamento de dados
- Treinamento de modelos de classificação
- Comparação de métricas entre modelos
- Análise de correlações entre features
- Distribuições por classe
- Matrizes de confusão comparativas

**Datasets:**
- `treino_sinais_vitais_com_label_1500.txt` - Dataset de treino
- `teste_cego_com_classe.csv` - Dataset de teste (com classe para validação)
- `predicoes_teste_cego.csv` - Predições geradas

**Arquivos principais:**
- `Vinicius_Cebalhos_classificacao_sinais_vitais.ipynb` - Notebook completo
- `Enunciado_Sinais_Vitais_CDA2025.pdf` - Enunciado do trabalho
- Visualizações: `comparacao_metricas.png`, `correlacao_features.png`, `distribuicoes_por_classe.png`, `matrizes_confusao_comparacao.png`

**📍 Este projeto está em destaque em [`projects/classificacao-sinais-vitais/`](../projects/classificacao-sinais-vitais/)**

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

### Principais
- **Python 3.x**
- **Scikit-learn** - Machine Learning
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **Matplotlib/Seaborn** - Visualização

### Específicas
- **XGBoost** - Gradient Boosting
- **Imbalanced-learn** - SMOTE para balanceamento
- **Scipy** - Estatísticas avançadas

---

## 📊 Competências Demonstradas

- ✅ Regressão Linear
- ✅ Classificação (binária e multiclasse)
- ✅ Pré-processamento de dados
- ✅ Feature Engineering
- ✅ Validação Cruzada
- ✅ Otimização de Hiperparâmetros
- ✅ Análise de Feature Importance
- ✅ Avaliação de Modelos (múltiplas métricas)
- ✅ Tratamento de Dados Desbalanceados
- ✅ Visualização de Resultados

---

## 📁 Estrutura de Pastas

```
machine-learning/
├── README.md                    # Este arquivo
├── regressao-imoveis/           # Regressão Linear - Imóveis
└── classificacao-indicadores/   # Classificação - Indicadores Globais

Nota: O projeto Work3 foi movido para projects/ como projeto em destaque.
```

---

## 🚀 Como Executar

### Para Regressão Linear:
```bash
cd regressao-imoveis
python regressao_linear_imoveis.py
```

### Para Classificação de Indicadores:
```bash
# Instale as dependências
pip install pandas numpy scikit-learn matplotlib seaborn xgboost imbalanced-learn

# Abra o notebook
jupyter notebook classificacao-indicadores/Vinicius_Cebalhos_classificacao.ipynb
```

---

## 📊 Resultados e Métricas

### Work 1
- Modelo de regressão linear otimizado
- RMSE calculado no conjunto de teste

### Work 2
- Comparação de 3 algoritmos (Logistic Regression, Random Forest, XGBoost)
- Validação cruzada estratificada (k=5)
- Análise completa de métricas
- Feature importance detalhada

### Work 3
- Classificação de sinais vitais
- Comparação de múltiplas métricas
- Análise de distribuições por classe
- Visualizações comparativas

---

## 📝 Notas

- Os datasets podem precisar ser baixados separadamente
- Alguns trabalhos requerem dados específicos fornecidos pelo professor
- Os notebooks estão completamente documentados
- Visualizações são geradas automaticamente e salvas em PNG

---

## 🎯 Destaques

### Work 2 - Classificação Multiclasse
- **Notebook completo** com 47 células
- **Checklist de implementação** completo
- **Metodologia defensável** e justificada
- **Visualizações profissionais** (300 DPI)
- **Análise comparativa** detalhada de modelos

### Work 3 - Sinais Vitais
- **Análise comparativa** de múltiplos modelos
- **Visualizações comparativas** profissionais
- **Análise de correlações** entre features
- **Distribuições por classe** detalhadas

---

**Disciplina:** Machine Learning  
**Autor:** Vinícius de Souza Cebalhos  
**Instituição:** UTFPR

