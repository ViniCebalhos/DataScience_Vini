# 🔍 Web Scraping e Análise de Dados do YouTube

**Descrição:** Extração e análise de dados do YouTube usando a API oficial do Google.

---

## 📋 Descrição

Este projeto demonstra como:
- Utilizar a YouTube Data API v3
- Extrair dados de vídeos do YouTube
- Analisar estatísticas de vídeos
- Processar e estruturar dados de API

---

## 🛠️ Tecnologias

- **Python 3.x**
- **Google API Client** (`google-api-python-client`)
- **Pandas** - Manipulação de dados
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

---

## 🔑 Configuração da API

### 1. Obter Chave de API do YouTube

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative a **YouTube Data API v3**
4. Crie credenciais (API Key)
5. Copie a chave gerada

### 2. Configurar Variáveis de Ambiente

**Opção 1: Arquivo .env (Recomendado)**

Crie um arquivo `.env` na pasta `work1/`:

```bash
YOUTUBE_API_KEY=sua_chave_aqui
```

**Opção 2: Variável de Ambiente do Sistema**

```bash
export YOUTUBE_API_KEY="sua_chave_aqui"
```

### 3. Instalar Dependências

```bash
pip install google-api-python-client pandas python-dotenv
```

---

## 📁 Arquivos

- `first.ipynb` - Notebook principal de extração de dados
- `third.ipynb` - Análise dos dados extraídos
- `README.md` - Este arquivo
- `.env` - Arquivo de configuração (criar você mesmo, não commitado)

---

## 🚀 Como Executar

1. **Configure a chave de API** (veja seção acima)

2. **Abra o notebook:**
```bash
jupyter notebook first.ipynb
```

3. **Execute as células sequencialmente**

---

## 📊 Exemplo de Uso

O notebook demonstra como:
- Buscar vídeos por palavra-chave
- Filtrar por localização e período
- Extrair estatísticas (views, likes, comentários)
- Identificar vídeos mais populares

### Exemplo de Busca Implementado:
- **Palavra-chave:** "eleição"
- **Região:** Brasil
- **Localização:** São Paulo (raio de 50km)
- **Período:** 29-31 de outubro de 2022

---

## ⚠️ Importante

- **NUNCA** commite sua chave de API no repositório
- Use variáveis de ambiente ou arquivo `.env`
- O arquivo `.env` está no `.gitignore`
- Respeite os limites de quota da API do YouTube

---

## 📝 Limites da API

A YouTube Data API tem limites de quota:
- **Quota padrão:** 10.000 unidades por dia
- **Cada busca:** ~100 unidades
- **Cada lista de vídeos:** ~1 unidade

Para aumentar a quota, solicite no Google Cloud Console.

---

## 🔒 Segurança

- ✅ Chave de API removida do código
- ✅ Uso de variáveis de ambiente
- ✅ `.env` no `.gitignore`
- ✅ Instruções claras de configuração

---

**Autor:** Vinícius de Souza Cebalhos  
**Disciplina:** Data Mining

