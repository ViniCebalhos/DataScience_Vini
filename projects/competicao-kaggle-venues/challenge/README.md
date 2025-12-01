# 🏆 Challenge: Previsão de Locais Altamente Avaliados

**Competição:** Predict Highly Rated Venues CDA UTFPR 2024  
**Plataforma:** Kaggle-style Competition  
**Dataset:** Yelp Toronto Reviews

---

## 🎯 Objetivo

Prever se um local será altamente avaliado (1) ou não (0) na cidade de Toronto, ON, Canadá, utilizando dados do Yelp.

---

## 📊 Resultados

### Melhor Modelo
- **Algoritmo:** Random Forest
- **F1-Score:** 0.9991
- **Score CV:** 0.9991 +/- 0.0003
- **Validação Cruzada:** 5-fold estratificada

### Modelos Testados
1. **Logistic Regression** - Baseline
2. **Random Forest** - Melhor performance ⭐
3. **Gradient Boosting** - Alternativa testada

---

## 🛠️ Metodologia

### 1. Análise Exploratória de Dados (EDA)
- Carregamento e mesclagem de datasets
- Análise de distribuições
- Identificação de padrões
- Tratamento de valores ausentes

### 2. Pré-processamento
- Limpeza de dados
- Feature engineering
- Codificação de variáveis categóricas
- Normalização/padronização

### 3. Modelagem
- Teste de múltiplos algoritmos
- Validação cruzada estratificada
- Otimização de hiperparâmetros (Grid Search)
- Avaliação com múltiplas métricas

### 4. Otimização
- Teste de diferentes thresholds
- Análise de trade-off precision/recall
- Seleção do melhor modelo

---

## 📁 Arquivos

### Notebooks
- `challenge_final.ipynb` - Notebook final com melhor modelo
- `challenge.ipynb` - Notebook de desenvolvimento
- `final.ipynb`, `final2.ipynb` - Versões intermediárias

### Submissões
- `submission_best_model.csv` - Submissão final (melhor resultado)
- `submission_rf_optimized.csv` - Random Forest otimizado
- `submission_rf_ideal_threshold_0.59.csv` - Threshold otimizado
- Outras submissões com diferentes thresholds (0.3, 0.4, 0.5)

### Dados
- `data/reviewsTrainToronto.csv` - Reviews de treino
- `data/reviewsTestToronto.csv` - Reviews de teste
- `data/X_trainToronto.csv` - Features de treino
- `data/X_testToronto.csv` - Features de teste
- `data/sampleResposta.csv` - Formato de submissão

---

## 🚀 Como Executar

1. **Instale as dependências:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

2. **Abra o notebook:**
```bash
jupyter notebook challenge_final.ipynb
```

3. **Execute as células sequencialmente**

4. **Para gerar submissão:**
   - Execute todas as células
   - O arquivo `submission_best_model.csv` será gerado automaticamente

---

## 📈 Métricas Avaliadas

- **F1-Score** (métrica principal)
- **Accuracy**
- **Precision**
- **Recall**
- **AUC-ROC**

---

## 💡 Insights e Decisões

### Feature Engineering
- Combinação de features de reviews e características dos locais
- Tratamento de valores ausentes
- Normalização de features numéricas

### Seleção de Modelo
- Random Forest escolhido por melhor balance entre performance e interpretabilidade
- Validação cruzada para garantir robustez
- Threshold otimizado para maximizar F1-Score

### Otimizações
- Teste de múltiplos thresholds (0.3 a 0.59)
- Grid Search para hiperparâmetros
- Análise de feature importance

---

## 📝 Notas

- O dataset não está incluído no repositório (tamanho)
- As submissões foram testadas na plataforma da competição
- O modelo final foi escolhido baseado em validação cruzada

---

**Autor:** Vinícius de Souza Cebalhos  
**Data:** 2024  
**Competição:** CDA UTFPR 2024

