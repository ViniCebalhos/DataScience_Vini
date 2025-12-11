"""
Script para testar vários exemplos e encontrar casos onde
TextBlob e Transformers discordam
"""

from textblob import TextBlob
from transformers import pipeline
import torch
import pandas as pd

# Carregar modelo
print("Carregando modelo de transformer...")
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    device=0 if torch.cuda.is_available() else -1
)
print("Modelo carregado!\n")

def analisar_textblob(texto):
    blob = TextBlob(str(texto))
    polaridade = blob.sentiment.polarity
    if polaridade > 0.1:
        return "Positivo", polaridade
    elif polaridade < -0.1:
        return "Negativo", polaridade
    else:
        return "Neutro", polaridade

def analisar_transformer(texto):
    resultado = sentiment_analyzer(texto)[0]
    label = resultado['label']
    score = resultado['score']
    if 'POSITIVE' in label or 'pos' in label.lower():
        return "Positivo", score
    elif 'NEGATIVE' in label or 'neg' in label.lower():
        return "Negativo", score
    else:
        return "Neutro", score

# Lista de exemplos para testar
exemplos = [
    # Construções com "not bad"
    ("The movie was not bad, actually quite good.", "Positivo"),
    ("It's not the worst thing I've seen.", "Positivo"),
    ("Not bad at all, I'm impressed.", "Positivo"),
    
    # Sarcasmo explícito
    ("Great! My flight was cancelled and I'm stuck at the airport.", "Negativo"),
    ("Perfect! Just what I needed - another problem to solve.", "Negativo"),
    ("Wonderful! I lost my keys again.", "Negativo"),
    ("Excellent! The internet is down.", "Negativo"),
    ("I love waiting in line for 2 hours. Best customer service ever!", "Negativo"),
    ("Oh great, another amazing decision. Just what we needed.", "Negativo"),
    ("Sure, let's have another meeting about meetings. That's productive.", "Negativo"),
    
    # Dupla negação
    ("I can't say I'm unhappy with the results, they exceeded expectations.", "Positivo"),
    ("I'm not disappointed, actually quite pleased.", "Positivo"),
    ("Can't complain, it was better than expected.", "Positivo"),
    
    # Contexto negativo com palavras positivas
    ("Thanks for the help. Really helpful.", "Negativo"),  # sarcástico
    ("Wow, this is exactly what I wanted. Not.", "Negativo"),
    ("Because clearly, that's the solution we need.", "Negativo"),
    ("Right, because that makes total sense.", "Negativo"),
    
    # Construções complexas
    ("The food was okay, nothing special.", "Neutro"),
    ("It's fine, I guess.", "Neutro"),
    ("Could be better, could be worse.", "Neutro"),
    
    # Casos claros para comparação
    ("I hate this product, it's terrible", "Negativo"),
    ("This is the worst service I've ever experienced", "Negativo"),
    ("I love this country and its people!", "Positivo"),
    ("Amazing results! Fantastic work everyone!", "Positivo"),
]

print("=" * 80)
print("TESTANDO EXEMPLOS - Procurando Discordâncias")
print("=" * 80)

resultados = []
discordancias = []

for texto, esperado in exemplos:
    tb, pol_tb = analisar_textblob(texto)
    tr, score_tr = analisar_transformer(texto)
    
    resultado = {
        'texto': texto,
        'esperado': esperado,
        'textblob': tb,
        'polaridade_tb': pol_tb,
        'transformer': tr,
        'confianca_tr': score_tr,
        'tb_correto': tb == esperado,
        'tr_correto': tr == esperado,
        'discordam': tb != tr
    }
    
    resultados.append(resultado)
    
    if tb != tr:
        discordancias.append(resultado)

print(f"\n📊 Total de exemplos testados: {len(resultados)}")
print(f"📊 Discordâncias encontradas: {len(discordancias)}")
print(f"📊 TextBlob acertou: {sum(1 for r in resultados if r['tb_correto'])} ({sum(1 for r in resultados if r['tb_correto'])/len(resultados)*100:.1f}%)")
print(f"📊 Transformer acertou: {sum(1 for r in resultados if r['tr_correto'])} ({sum(1 for r in resultados if r['tr_correto'])/len(resultados)*100:.1f}%)")

print("\n\n" + "=" * 80)
print("MELHORES EXEMPLOS DE DISCORDÂNCIA")
print("=" * 80)

# Filtrar casos onde transformer acertou e textblob errou
melhores = [r for r in discordancias if r['tr_correto'] and not r['tb_correto']]

if melhores:
    print(f"\n✅ Encontrados {len(melhores)} exemplos onde Transformer ACERTOU e TextBlob ERROU:\n")
    for i, r in enumerate(melhores, 1):
        print(f"{'='*80}")
        print(f"Exemplo {i}:")
        print(f"Texto: {r['texto']}")
        print(f"Esperado: {r['esperado']}")
        print(f"TextBlob: {r['textblob']} (Polaridade: {r['polaridade_tb']:.3f}) ❌")
        print(f"Transformer: {r['transformer']} (Confiança: {r['confianca_tr']:.3f}) ✅")
        print()
else:
    print("\n⚠️ Não encontramos exemplos onde Transformer acertou e TextBlob errou.")
    print("Mostrando todas as discordâncias encontradas:\n")
    for i, r in enumerate(discordancias[:10], 1):
        print(f"{'='*80}")
        print(f"Exemplo {i}:")
        print(f"Texto: {r['texto']}")
        print(f"Esperado: {r['esperado']}")
        print(f"TextBlob: {r['textblob']} (Polaridade: {r['polaridade_tb']:.3f})")
        print(f"Transformer: {r['transformer']} (Confiança: {r['confianca_tr']:.3f})")
        print(f"TextBlob correto: {r['tb_correto']}")
        print(f"Transformer correto: {r['tr_correto']}")
        print()

# Salvar resultados em CSV
df = pd.DataFrame(resultados)
df_discordam = df[df['discordam'] == True]
print(f"\n💾 Salvando {len(df_discordam)} discordâncias em 'discordancias.csv'...")
df_discordam.to_csv('discordancias.csv', index=False)
print("✅ Salvo!")

