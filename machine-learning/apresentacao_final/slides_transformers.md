---
marp: true
theme: default
paginate: true
---

# Transformers em Machine Learning
## Análise de Sentimento com Deep Learning

---

## O que são Transformers?

- Arquitetura de **Deep Learning** para Processamento de Linguagem Natural (NLP)
- Baseada em **Attention Mechanism** (Mecanismo de Atenção)
- Revolucionaram o campo de NLP a partir de 2017
- Modelos famosos: **BERT**, **GPT**, **RoBERTa**

---

## Por que "Transformers"?

- **Transformam** sequências de texto em representações numéricas
- Permitem que o modelo **preste atenção** em todas as palavras simultaneamente
- Diferente de métodos antigos que processam palavra por palavra

---

## Attention Mechanism (Mecanismo de Atenção)

### Como funciona?

- O modelo "presta atenção" em **todas as palavras** ao mesmo tempo
- Entende **relações** entre palavras distantes
- Captura **contexto profundo** do texto

### Analogia:
> É como ler um texto inteiro de uma vez, em vez de palavra por palavra

---

## Comparação: Métodos Tradicionais vs Transformers

### Métodos Tradicionais (ex: TextBlob)
- ❌ Baseados em **dicionários** de palavras
- ❌ Não entendem **contexto profundo**
- ❌ Dificuldade com **sarcasmo** e **ironia**
- ❌ Processam palavras **isoladamente**

### Transformers
- ✅ Entendem **contexto completo**
- ✅ Treinados em **milhões de exemplos**
- ✅ Capturam **nuances** linguísticas
- ✅ Processam **todo o texto** simultaneamente

---

## Exemplo Prático: Análise de Sentimento

### Tweet: 
> "Great! My flight was cancelled and I'm stuck at the airport."

### TextBlob (Tradicional):
- Vê "Great!" → **Positivo** ❌
- Ignora o contexto negativo

### Transformers:
- Analisa todo o texto → **Negativo** ✅
- Entende o sarcasmo

---

## Vantagens dos Transformers

1. **Contexto Profundo**
   - Entendem significado completo, não apenas palavras isoladas

2. **Aprendizado**
   - Treinados em milhões de exemplos de dados reais

3. **Nuances**
   - Capturam sarcasmo, ironia e contexto cultural

4. **Confiança**
   - Fornecem scores de confiança para cada predição

---

## Arquitetura dos Transformers

### Componentes principais:

1. **Encoder** - Processa o texto de entrada
2. **Attention Layers** - Calcula atenção entre palavras
3. **Feed-Forward Networks** - Processa as representações
4. **Output Layer** - Gera a predição final

---

## Modelos Pré-treinados

### Vantagem:
- Modelos já **treinados** em grandes volumes de dados
- Podem ser **reutilizados** para diferentes tarefas
- **Fine-tuning** para tarefas específicas

### Exemplos:
- BERT (Google)
- GPT (OpenAI)
- RoBERTa (Facebook)
- T5 (Google)

---

## Aplicações dos Transformers

- 📱 **Análise de Sentimento** em redes sociais
- 📝 **Tradução Automática**
- 💬 **Chatbots** e assistentes virtuais
- 📊 **Análise de Reviews** de produtos
- 🔍 **Busca Semântica**
- 📰 **Resumo Automático** de textos

---

## Como Usar Transformers?

### Biblioteca Hugging Face

```python
from transformers import pipeline

# Carregar modelo pré-treinado
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

# Usar o modelo
resultado = sentiment_analyzer("I love this product!")
```

---

## Resultados: TextBlob vs Transformers

### Estatísticas dos Testes:

- **TextBlob acertou:** 33.3% dos casos
- **Transformers acertou:** 41.7% dos casos

### Casos de Discordância:

- Transformers são **superiores** em:
  - Sarcasmo e ironia
  - Contexto negativo com palavras positivas
  - Construções linguísticas complexas

---

## Exemplo Real: Sarcasmo

### Tweet:
> "This is the worst service I've ever experienced"

### TextBlob:
- **Neutro** (polaridade -0.1) ❌
- Não detecta sentimento negativo forte

### Transformers:
- **Negativo** (confiança 0.95) ✅
- Entende corretamente o sentimento

---

## Por que Transformers são Melhores?

### 1. Entendimento de Contexto
- Não apenas palavras, mas **relações** entre elas

### 2. Aprendizado Profundo
- Treinados em **milhões** de exemplos

### 3. Especialização
- Podem ser treinados para **domínios específicos**
- Ex: Análise de tweets, reviews, etc.

---

## Limitações dos Transformers

- ⚠️ Requerem **muito poder computacional** para treinar
- ⚠️ Modelos grandes podem ser **lentos** para inferência
- ⚠️ Sarcasmo muito sutil ainda é **desafiador**
- ⚠️ Dependem da **qualidade dos dados** de treinamento

---

## Impacto dos Transformers

### Revolução no NLP:

- **2017:** Paper "Attention Is All You Need"
- **2018:** BERT lançado pelo Google
- **2019:** GPT-2 demonstra capacidades impressionantes
- **2020+:** GPT-3, GPT-4, e outros modelos grandes

### Hoje:
- Transformers são **essenciais** para NLP moderno
- Usados em produtos do dia a dia (Google, ChatGPT, etc.)

---

## Conclusão

### Transformers são:

✅ **Superiores** a métodos tradicionais  
✅ **Entendem contexto** profundo  
✅ **Capturam nuances** linguísticas  
✅ **Fáceis de usar** com bibliotecas modernas  

### Para análise de sentimento:
- Transformers são a **melhor escolha** atual
- Especialmente para dados de redes sociais
- Melhor precisão e entendimento de contexto

---

## Obrigado!

### Perguntas?

---

## Referências

- Paper original: "Attention Is All You Need" (Vaswani et al., 2017)
- Hugging Face: https://huggingface.co/
- Modelo usado: `cardiffnlp/twitter-roberta-base-sentiment-latest`


