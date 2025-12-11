---
marp: true
theme: default
paginate: true
---

# 🤖 Transformers
## Como as máquinas aprendem a entender linguagem

Uma explicação simples para leigos

---

## O Problema

**Como fazer uma máquina entender texto?**

- Computadores só entendem números (0 e 1)
- Mas nós falamos em palavras
- Como converter palavras em números que façam sentido?

> **Analogia:** É como traduzir português para uma linguagem que só tem números!

---

## De Onde Vieram os Transformers?

### Começou com Redes Neurais

**1940s:** Primeiras ideias - Neurônios artificiais (inspirados no cérebro humano)

**1980s:** Redes Neurais - Múltiplas camadas de neurônios conectados

**2010s:** Deep Learning - Redes muito profundas com muitas camadas

---

## Evolução no Processamento de Texto

**Anos 2000:** Métodos Estatísticos - Contagem de palavras, regras simples

**2010-2015:** Word Embeddings - Palavras viram vetores (números)
- Ex: "rei" - "homem" + "mulher" = "rainha"

**2015-2017:** RNNs/LSTMs - Processavam texto palavra por palavra (sequencial)

---

## 2017: O Nascimento dos Transformers

### Paper: "Attention Is All You Need"
Google publicou uma nova arquitetura revolucionária

- **Problema anterior:** Processar palavra por palavra era lento
- **Solução:** Processar TODAS as palavras ao mesmo tempo!
- **Inovação:** Mecanismo de Atenção

> **Antes:** Ler um livro palavra por palavra  
> **Agora:** Ver o livro inteiro de uma vez e entender tudo!

---

## Word Embedding: Convertendo Palavras em Números

### Como funciona?

Cada palavra vira um **vetor** (lista de números)

```
"gato" → [0.2, -0.5, 0.8, 0.1, ...]
"cachorro" → [0.3, -0.4, 0.7, 0.2, ...]
"animal" → [0.25, -0.45, 0.75, 0.15, ...]
```

> **Analogia:** É como criar um "mapa" onde palavras similares ficam próximas.  
> "Gato" e "cachorro" têm números parecidos porque são ambos animais!

---

## Mecanismo de Atenção: O Coração dos Transformers

### O que é?

O modelo "presta atenção" em todas as palavras ao mesmo tempo

**Exemplo:**
- **Frase:** "O banco está fechado"
- Qual "banco"? Banco de sentar ou banco financeiro?
- Atenção olha para "fechado" → Ah, é banco financeiro!

> **Analogia:** É como quando você lê uma frase e seu cérebro automaticamente conecta todas as palavras para entender o significado completo.

---

## Como o Mecanismo de Atenção Funciona?

### Passo a Passo:

1. Cada palavra olha para **TODAS** as outras palavras
2. Calcula "quanto" cada palavra é importante para entender as outras
3. Cria uma "rede de conexões" entre todas as palavras
4. Usa essas conexões para entender o contexto completo

> **Visual:** Imagine uma teia de aranha conectando todas as palavras!

---

## Arquitetura: Encoder e Decoder

### Encoder (Codificador)
- 📥 Recebe o texto de entrada
- 🔍 Processa e entende o texto
- 💾 Cria uma representação interna

### Decoder (Decodificador)
- 📤 Pega a representação do encoder
- 🎯 Gera a saída (tradução, resposta, etc.)
- ✨ Produz o resultado final

> **Analogia:** Encoder = tradutor que entende português  
> Decoder = tradutor que fala inglês e produz a tradução

---

## Fluxo Completo: Do Texto ao Resultado

1. **Word Embedding**
   - "Olá mundo" → [números, números, ...]

2. **Encoder**
   - Processa com Attention → Entende contexto

3. **Decoder**
   - Gera resposta → "Hello world"

> **Tudo isso acontece simultaneamente!**  
> Não precisa processar palavra por palavra

---

## Por que Transformers são Melhores?

- ⚡ **Mais Rápido:** Processa tudo ao mesmo tempo
- 🧠 **Entende Contexto:** Vê o texto completo
- 📚 **Aprende Melhor:** Treinado em milhões de textos
- 🔄 **Reutilizável:** Um modelo serve para várias tarefas

> **Comparação:**  
> **Antes:** Como ler um livro página por página  
> **Agora:** Como ter uma visão aérea de todo o livro de uma vez!

---

## Onde Você Já Viu Transformers?

- 💬 **ChatGPT:** Conversa com você
- 🌐 **Google Translate:** Traduz textos
- 🔍 **Busca Google:** Entende o que você procura
- 📱 **Assistentes Virtuais:** Siri, Alexa, etc.
- 📊 **Análise de Sentimento:** Entende se texto é positivo/negativo

> **Transformers estão em todo lugar!**  
> Você provavelmente já usou sem saber!

---

## Resumo: Como Funciona?

**Texto de Entrada**
- "O gato está no tapete"

↓

**Word Embedding**
- Palavras → Vetores (números)

↓

**Encoder + Attention**
- Entende contexto e relações

↓

**Decoder**
- Gera resultado (tradução, análise, etc.)

> **Em uma frase:** Transformers convertem palavras em números, entendem o contexto completo usando atenção, e produzem resultados inteligentes!

---

## Conclusão

### Transformers são:

- Uma evolução das redes neurais
- Usam mecanismo de atenção para entender contexto
- Convertem palavras em números (word embeddings)
- Têm encoder (entende) e decoder (gera resposta)
- Revolucionaram como máquinas processam linguagem

> **Em resumo:** Transformers são como dar "superpoderes" de compreensão de linguagem para computadores!

---

## Obrigado!

### Perguntas?


