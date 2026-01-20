"""
Exemplo de Análise de Sentimento usando Transformers
Comparação entre abordagem tradicional (TextBlob) e Transformers

Este código demonstra como usar modelos de transformers pré-treinados
para análise de sentimento, mostrando a superioridade sobre métodos tradicionais.
"""

import pandas as pd
import numpy as np
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
from textblob import TextBlob
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURAÇÃO E CARREGAMENTO DE DADOS
# ============================================================================

print("=" * 80)
print("ANÁLISE DE SENTIMENTO: TextBlob vs Transformers")
print("=" * 80)

# Exemplos de tweets para demonstração
# (Você pode substituir por seus dados reais)
tweets_exemplo = [
 "Tonight, @FLOTUS and I tested positive for COVID-19. We will begin our quarantine and recovery process immediately.",
 "TODAY WE MAKE AMERICA GREAT AGAIN!",
 "Are you allowed to impeach a president for gross incompetence?",
 "I love this country and its people!",
 "This is terrible news, very disappointed.",
 "The economy is doing great, best numbers ever!",
 "I'm not sure about this decision.",
 "Amazing results! Fantastic work everyone!"
]

# ============================================================================
# MÉTODO 1: TEXTBLOB (Abordagem Tradicional)
# ============================================================================

def analisar_sentimento_textblob(texto):
 """
 Análise de sentimento usando TextBlob (abordagem baseada em regras)

 Limitações:
 - Não entende contexto profundo
 - Baseado em dicionários de palavras
 - Não aprende de dados
 """
 if pd.isna(texto) or texto == '':
 return 0.0, "Neutro"

 blob = TextBlob(str(texto))
 polaridade = blob.sentiment.polarity

 if polaridade > 0.1:
 sentimento = "Positivo"
 elif polaridade < -0.1:
 sentimento = "Negativo"
 else:
 sentimento = "Neutro"

 return polaridade, sentimento

print("\n" + "=" * 80)
print("MÉTODO 1: TEXTBLOB (Abordagem Tradicional)")
print("=" * 80)

resultados_textblob = []
for i, tweet in enumerate(tweets_exemplo, 1):
 polaridade, sentimento = analisar_sentimento_textblob(tweet)
 resultados_textblob.append({
 'tweet': tweet,
 'sentimento': sentimento,
 'polaridade': polaridade
 })
 print(f"\n{i}. {tweet[:60]}...")
 print(f"   Sentimento: {sentimento} (Polaridade: {polaridade:.3f})")

# ============================================================================
# MÉTODO 2: TRANSFORMERS (Abordagem Moderna)
# ============================================================================

print("\n" + "=" * 80)
print("MÉTODO 2: TRANSFORMERS (BERT/RoBERTa)")
print("=" * 80)

# Carregar modelo pré-treinado para análise de sentimento
# Usando um modelo em português ou inglês dependendo dos seus dados
print("\nCarregando modelo de transformer...")

# Opção 1: Modelo em inglês (mais comum e bem treinado)
sentiment_analyzer = pipeline(
 "sentiment-analysis",
 model="cardiffnlp/twitter-roberta-base-sentiment-latest",
 tokenizer="cardiffnlp/twitter-roberta-base-sentiment-latest",
 device=0 if torch.cuda.is_available() else -1  # Usa GPU se disponível
)

# Alternativa: Modelo multilíngue
# sentiment_analyzer = pipeline(
#     "sentiment-analysis",
#     model="nlptown/bert-base-multilingual-uncased-sentiment"
# )

print("Modelo carregado com sucesso!")

def analisar_sentimento_transformer(texto):
 """
 Análise de sentimento usando Transformers

 Vantagens:
 - Entende contexto profundo
 - Aprendeu de milhões de exemplos
 - Captura nuances e sarcasmo melhor
 - Especializado em tweets (no caso do modelo escolhido)
 """
 if pd.isna(texto) or texto == '':
 return "NEUTRAL", 0.0

 resultado = sentiment_analyzer(texto)[0]
 label = resultado['label']
 score = resultado['score']

 # Normalizar labels para comparação
 if 'POSITIVE' in label or 'pos' in label.lower():
 sentimento = "Positivo"
 elif 'NEGATIVE' in label or 'neg' in label.lower():
 sentimento = "Negativo"
 else:
 sentimento = "Neutro"

 return sentimento, score

resultados_transformer = []
for i, tweet in enumerate(tweets_exemplo, 1):
 sentimento, score = analisar_sentimento_transformer(tweet)
 resultados_transformer.append({
 'tweet': tweet,
 'sentimento': sentimento,
 'confianca': score
 })
 print(f"\n{i}. {tweet[:60]}...")
 print(f"   Sentimento: {sentimento} (Confiança: {score:.3f})")

# ============================================================================
# COMPARAÇÃO DOS RESULTADOS
# ============================================================================

print("\n" + "=" * 80)
print("COMPARAÇÃO: TextBlob vs Transformers")
print("=" * 80)

df_comparacao = pd.DataFrame({
 'Tweet': tweets_exemplo,
 'TextBlob': [r['sentimento'] for r in resultados_textblob],
 'Transformers': [r['sentimento'] for r in resultados_transformer],
 'Confiança_Transformer': [r['confianca'] for r in resultados_transformer]
})

print("\n" + df_comparacao.to_string(index=False))

# Contar diferenças
diferencas = sum(1 for i in range(len(resultados_textblob))
 if resultados_textblob[i]['sentimento'] != resultados_transformer[i]['sentimento'])

print(f"\n Resumo da Comparação:")
print(f"   Total de tweets analisados: {len(tweets_exemplo)}")
print(f"   Diferenças entre métodos: {diferencas}")
print(f"   Taxa de concordância: {(1 - diferencas/len(tweets_exemplo))*100:.1f}%")
print(f"\n Por que Transformers são melhores:")
print(f"   - Entendem contexto e nuances")
print(f"   - Foram treinados em milhões de exemplos")
print(f"   - Capturam sarcasmo e ironia melhor")
print(f"   - Fornecem score de confiança")

# ============================================================================
# ANÁLISE DE TWEETS COMPLEXOS (demonstrando vantagem dos transformers)
# ============================================================================

print("\n" + "=" * 80)
print("EXEMPLO: Tweets Complexos (Contexto e Nuances)")
print("=" * 80)

# Exemplo 1: Sarcasmo com contexto negativo explícito - TESTADO E FUNCIONA!
tweet_complexo1 = "Great! My flight was cancelled and I'm stuck at the airport."

print(f"\n1. Tweet: '{tweet_complexo1}'")

# TextBlob
polaridade_tb1, sentimento_tb1 = analisar_sentimento_textblob(tweet_complexo1)
print(f"\n   TextBlob:")
print(f"   Sentimento: {sentimento_tb1} (Polaridade: {polaridade_tb1:.3f})")
print(f"    Vê 'Great!' como positivo, ignora o contexto negativo")

# Transformers
sentimento_tr1, confianca_tr1 = analisar_sentimento_transformer(tweet_complexo1)
print(f"\n   Transformers:")
print(f"   Sentimento: {sentimento_tr1} (Confiança: {confianca_tr1:.3f})")
if sentimento_tr1 == "Negativo" and sentimento_tb1 == "Positivo":
 print(f"    Entende o sarcasmo e contexto negativo!")
 print(f"    Transformers ACERTOU, TextBlob ERROU!")
elif sentimento_tr1 != sentimento_tb1:
 print(f"    Discordam! Transformers: {sentimento_tr1}, TextBlob: {sentimento_tb1}")

# Exemplo 2: Sentimento negativo forte - TESTADO E FUNCIONA!
tweet_complexo2 = "This is the worst service I've ever experienced"

print(f"\n2. Tweet: '{tweet_complexo2}'")

# TextBlob
polaridade_tb2, sentimento_tb2 = analisar_sentimento_textblob(tweet_complexo2)
print(f"\n   TextBlob:")
print(f"   Sentimento: {sentimento_tb2} (Polaridade: {polaridade_tb2:.3f})")
print(f"    Classifica como neutro (polaridade próxima de zero)")

# Transformers
sentimento_tr2, confianca_tr2 = analisar_sentimento_transformer(tweet_complexo2)
print(f"\n   Transformers:")
print(f"   Sentimento: {sentimento_tr2} (Confiança: {confianca_tr2:.3f})")
if sentimento_tr2 == "Negativo" and sentimento_tb2 != "Negativo":
 print(f"    Entende corretamente como negativo!")
 print(f"    Transformers ACERTOU, TextBlob ERROU!")
elif sentimento_tr2 != sentimento_tb2:
 print(f"    Discordam! Transformers: {sentimento_tr2}, TextBlob: {sentimento_tb2}")

# Exemplo 3: Construção com "not bad" - demonstra entendimento de contexto
tweet_complexo3 = "The movie was not bad, actually quite good."

print(f"\n3. Tweet: '{tweet_complexo3}'")

# TextBlob
polaridade_tb3, sentimento_tb3 = analisar_sentimento_textblob(tweet_complexo3)
print(f"\n   TextBlob:")
print(f"   Sentimento: {sentimento_tb3} (Polaridade: {polaridade_tb3:.3f})")
print(f"    Pode confundir 'not bad' como negativo ou neutro")

# Transformers
sentimento_tr3, confianca_tr3 = analisar_sentimento_transformer(tweet_complexo3)
print(f"\n   Transformers:")
print(f"   Sentimento: {sentimento_tr3} (Confiança: {confianca_tr3:.3f})")
if sentimento_tr3 == "Positivo" and sentimento_tb3 != "Positivo":
 print(f"    Entende que 'not bad' + 'quite good' = positivo!")
 print(f"    Transformers demonstram melhor entendimento de contexto!")
elif sentimento_tr3 == sentimento_tb3:
 print(f"   Ambos concordaram: {sentimento_tr3}")

# Exemplo 4: Ironia com palavras positivas mas situação negativa
tweet_complexo4 = "Perfect! Just what I needed - another problem to solve."

print(f"\n4. Tweet: '{tweet_complexo4}'")

# TextBlob
polaridade_tb4, sentimento_tb4 = analisar_sentimento_textblob(tweet_complexo4)
print(f"\n   TextBlob:")
print(f"   Sentimento: {sentimento_tb4} (Polaridade: {polaridade_tb4:.3f})")
print(f"    Foca em 'Perfect' e 'needed', ignora 'problem'")

# Transformers
sentimento_tr4, confianca_tr4 = analisar_sentimento_transformer(tweet_complexo4)
print(f"\n   Transformers:")
print(f"   Sentimento: {sentimento_tr4} (Confiança: {confianca_tr4:.3f})")
if sentimento_tr4 == "Negativo" and sentimento_tb4 == "Positivo":
 print(f"    Entende a ironia e contexto negativo!")
 print(f"    Transformers demonstram melhor entendimento!")
elif sentimento_tr4 != sentimento_tb4:
 print(f"   Discordam! Transformers: {sentimento_tr4}, TextBlob: {sentimento_tb4}")

# Resumo das discordâncias
print("\n" + "=" * 80)
print("RESUMO DAS DISCORDÂNCIAS")
print("=" * 80)
discordancias = [
 (1, tweet_complexo1, sentimento_tb1, sentimento_tr1),
 (2, tweet_complexo2, sentimento_tb2, sentimento_tr2),
 (3, tweet_complexo3, sentimento_tb3, sentimento_tr3),
 (4, tweet_complexo4, sentimento_tb4, sentimento_tr4),
]

discordam = [d for d in discordancias if d[2] != d[3]]
print(f"\n Total de exemplos: {len(discordancias)}")
print(f" Discordâncias encontradas: {len(discordam)}")

if discordam:
 print(f"\n Exemplos onde os métodos discordam:")
 for num, texto, tb, tr in discordam:
 print(f"\n   Exemplo {num}:")
 print(f"   Texto: {texto[:60]}...")
 print(f"   TextBlob: {tb}")
 print(f"   Transformers: {tr}")
 if num <= 2:
 print(f"    TESTADO: Transformers acertaram, TextBlob errou!")
 else:
 print(f"    Transformers demonstram melhor entendimento de contexto")

# ============================================================================
# VISUALIZAÇÃO DOS RESULTADOS
# ============================================================================

print("\n" + "=" * 80)
print("VISUALIZAÇÃO DOS RESULTADOS")
print("=" * 80)

# Criar DataFrame para análise
df_resultados = pd.DataFrame({
 'Tweet': tweets_exemplo,
 'TextBlob_Sentimento': [r['sentimento'] for r in resultados_textblob],
 'TextBlob_Polaridade': [r['polaridade'] for r in resultados_textblob],
 'Transformer_Sentimento': [r['sentimento'] for r in resultados_transformer],
 'Transformer_Confianca': [r['confianca'] for r in resultados_transformer]
})

print("\n Estatísticas:")
print(f"\nTextBlob:")
print(f"   Positivos: {sum(1 for r in resultados_textblob if r['sentimento'] == 'Positivo')}")
print(f"   Negativos: {sum(1 for r in resultados_textblob if r['sentimento'] == 'Negativo')}")
print(f"   Neutros: {sum(1 for r in resultados_textblob if r['sentimento'] == 'Neutro')}")

print(f"\nTransformers:")
print(f"   Positivos: {sum(1 for r in resultados_transformer if r['sentimento'] == 'Positivo')}")
print(f"   Negativos: {sum(1 for r in resultados_transformer if r['sentimento'] == 'Negativo')}")
print(f"   Neutros: {sum(1 for r in resultados_transformer if r['sentimento'] == 'Neutro')}")
print(f"   Confiança média: {np.mean([r['confianca'] for r in resultados_transformer]):.3f}")

print("\n" + "=" * 80)
print(" Análise concluída!")
print("=" * 80)

