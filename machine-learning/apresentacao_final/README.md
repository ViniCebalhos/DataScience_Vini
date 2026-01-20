# Apresentação: Transformers para Análise de Sentimento

Este projeto demonstra o uso de Transformers para análise de sentimento, comparando com métodos tradicionais como TextBlob.

## Sobre o Projeto

Este trabalho foi desenvolvido para a disciplina de Machine Learning, apresentando:
- Conceitos de Transformers
- Comparação entre abordagens tradicionais e modernas
- Exemplo prático de análise de sentimento em tweets

## Como Usar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o Exemplo

```bash
python transformers_sentiment_analysis.py
```

## Estrutura do Código

O código demonstra:

1. **Análise com TextBlob** (método tradicional)
   - Baseado em regras e dicionários
   - Limitações em contexto e nuances

2. **Análise com Transformers** (método moderno)
   - Modelo pré-treinado: `cardiffnlp/twitter-roberta-base-sentiment-latest`
   - Entende contexto profundo
   - Melhor para sarcasmo e ironia

3. **Comparação dos Resultados**
   - Mostra diferenças entre os métodos
   - Demonstra vantagens dos transformers

## Pontos para a Apresentação

### Por que Transformers são melhores?

1. **Contexto Profundo**: Entendem o significado completo, não apenas palavras isoladas
2. **Aprendizado**: Treinados em milhões de exemplos
3. **Nuances**: Capturam sarcasmo, ironia e contexto cultural
4. **Confiança**: Fornecem scores de confiança para cada predição

### Exemplo de Caso de Uso

O exemplo usa análise de sentimento em tweets, demonstrando:
- Como transformers superam métodos tradicionais
- Aplicação prática em dados reais
- Facilidade de uso com bibliotecas modernas


## Modelos Disponíveis

O código usa `cardiffnlp/twitter-roberta-base-sentiment-latest` que é:
- Especializado em tweets
- Treinado em dados do Twitter
- Multilíngue (principalmente inglês)

Alternativas:
- `nlptown/bert-base-multilingual-uncased-sentiment` (multilíngue)
- `distilbert-base-uncased-finetuned-sst-2-english` (mais leve)

## Referências

- Hugging Face Transformers: https://huggingface.co/transformers/
- Paper original: "Attention Is All You Need" (Vaswani et al., 2017)
- Modelo usado: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest

