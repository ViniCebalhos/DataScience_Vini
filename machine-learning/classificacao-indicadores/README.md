# 🌍 Classificação Multiclasse - Indicadores Sociais Globais

**Disciplina:** Machine Learning  
**Trabalho:** Work 2

---

## 🎯 Objetivo

Classificar países em categorias baseadas em indicadores sociais globais.

---

## 📊 Dataset

- **Arquivo:** `gdp-and-homicides-vs-happiness-vs-hdi_FabroClassification2025OK_4classes.csv`
- **Indicadores:**
  - GDP (Produto Interno Bruto)
  - Homicides (Taxa de homicídios)
  - Happiness (Índice de felicidade)
  - HDI (Índice de Desenvolvimento Humano)
  - Cantrill Ladder

---

## 🛠️ Tecnologias

- Python (scikit-learn, pandas, numpy, matplotlib, seaborn)
- Logistic Regression
- Random Forest
- XGBoost (Gradient Boosting)
- Validação cruzada estratificada
- SMOTE para balanceamento

---

## 📁 Arquivos

- `Vinicius_Cebalhos_classificacao.ipynb` - Notebook completo (47 células)
- `VERIFICACAO_COMPLETA.md` - Checklist de implementação
- Visualizações: boxplots, histogramas, heatmaps, matrizes de confusão, ROC curves, feature importance

---

## 🚀 Como Executar

1. Instale as dependências:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn xgboost imbalanced-learn
```

2. Abra o notebook:
```bash
jupyter notebook Vinicius_Cebalhos_classificacao.ipynb
```

---

## 📝 Metodologia

1. **Carregamento e Auditoria:** Verificação de qualidade dos dados
2. **EDA Completa:** Estatísticas descritivas, distribuições, correlações
3. **Preparação:** Tratamento de valores ausentes, normalização, encoding
4. **Modelagem:** Teste de 3 algoritmos com validação cruzada
5. **Interpretação:** Feature importance e análise de resultados

---

## 📊 Métricas Avaliadas

- Accuracy
- Precision
- Recall
- F1-Score
- Matriz de Confusão
- ROC Curve + AUC (One-vs-Rest para multiclasse)

---

## 🎯 Destaques

- **Notebook completo** com 47 células
- **Checklist de implementação** completo
- **Metodologia defensável** e justificada
- **Visualizações profissionais** (300 DPI)
- **Análise comparativa** detalhada de modelos

