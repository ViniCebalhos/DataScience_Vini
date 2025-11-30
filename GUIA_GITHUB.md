# 🚀 Guia Completo: Como Publicar Seu Portfólio no GitHub

Este guia contém recomendações profissionais baseadas em melhores práticas do mercado de trabalho em Ciência de Dados.

---

## 📋 Índice

1. [Preparação Antes de Publicar](#preparação)
2. [Estrutura Recomendada para GitHub](#estrutura)
3. [Configuração do Repositório](#configuração)
4. [Melhorias no README Principal](#readme)
5. [Badges e Visualizações](#badges)
6. [Organização de Projetos](#organização)
7. [Dicas de Mercado](#dicas)
8. [Checklist Final](#checklist)

---

## 🎯 Preparação Antes de Publicar {#preparação}

### 1. Limpeza de Arquivos

Antes de fazer o commit, certifique-se de:

- ✅ Remover dados sensíveis (chaves de API, senhas, tokens)
- ✅ Remover datasets grandes (usar `.gitignore`)
- ✅ Remover arquivos temporários (`.ipynb_checkpoints`, `__pycache__`)
- ✅ Remover arquivos de log e cache
- ✅ Manter apenas código, notebooks e documentação

### 2. Verificar Segurança

```bash
# Procurar por chaves de API ou tokens no código
cd /home/vinicius/Projects/datascience
grep -r "API_KEY\|api_key\|password\|secret" . --include="*.py" --include="*.ipynb" | grep -v ".git"
```

Se encontrar algo, remova ou use variáveis de ambiente.

---

## 📁 Estrutura Recomendada para GitHub {#estrutura}

### Estrutura Ideal para Portfólio

```
datascience/
├── README.md                    # ⭐ README principal (muito importante!)
├── .gitignore                    # Ignorar arquivos grandes
├── requirements.txt              # Dependências
│
├── data_mining/                  # Disciplina 1
│   ├── README.md                 # README da disciplina
│   ├── work1/
│   │   ├── README.md             # README do trabalho
│   │   ├── notebook.ipynb
│   │   └── results/              # Resultados (imagens, gráficos)
│   └── ...
│
├── databank/                     # Disciplina 2
│   └── ...
│
├── ML/                           # Disciplina 3
│   └── ...
│
└── Trabalho/                     # Projeto final
    └── ...
```

### Boas Práticas

1. **Um README por projeto** - Facilita navegação
2. **Pasta `results/` ou `outputs/`** - Para visualizações e resultados
3. **Pasta `data/` no `.gitignore`** - Dados grandes não devem ir para o GitHub
4. **Documentação clara** - Cada projeto deve ter objetivo, metodologia e resultados

---

## ⚙️ Configuração do Repositório {#configuração}

### Passo 1: Inicializar Git (se ainda não fez)

```bash
cd /home/vinicius/Projects/datascience

# Inicializar repositório Git
git init

# Verificar status
git status
```

### Passo 2: Configurar .gitignore

O arquivo `.gitignore` já foi criado. Verifique se está completo:

```bash
cat .gitignore
```

### Passo 3: Fazer Primeiro Commit

```bash
# Adicionar todos os arquivos
git add .

# Verificar o que será commitado
git status

# Fazer commit inicial
git commit -m "feat: Portfólio completo de Ciência de Dados - Pós-Graduação UTFPR

- Trabalhos de Data Mining, Banco de Dados e Machine Learning
- 2 artigos científicos completos
- Competição Kaggle (F1-Score: 0.9991)
- Projeto completo de análise em saúde pública
- Documentação profissional"
```

### Passo 4: Criar Repositório no GitHub

1. Acesse [GitHub.com](https://github.com)
2. Clique em **"New repository"** (ou **"+"** → **"New repository"**)
3. Configure:
   - **Repository name:** `portfolio-ciencia-dados` (ou outro nome profissional)
   - **Description:** `Portfólio de trabalhos de Ciência de Dados - Pós-Graduação UTFPR`
   - **Visibility:** Public (para portfólio, é melhor ser público)
   - **NÃO marque** "Add a README file" (já temos um)
   - **NÃO marque** "Add .gitignore" (já temos um)
4. Clique em **"Create repository"**

### Passo 5: Conectar Repositório Local ao GitHub

```bash
# Adicionar remote (substitua SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/portfolio-ciencia-dados.git

# Verificar
git remote -v

# Renomear branch principal para 'main' (padrão atual)
git branch -M main

# Fazer push
git push -u origin main
```

### Passo 6: Configurar GitHub Pages (Opcional mas Recomendado)

GitHub Pages permite criar um site para seu portfólio:

1. No repositório, vá em **Settings** → **Pages**
2. Em **Source**, selecione **"Deploy from a branch"**
3. Selecione branch **"main"** e pasta **"/ (root)"**
4. Clique em **Save**
5. Seu portfólio estará disponível em: `https://SEU_USUARIO.github.io/portfolio-ciencia-dados/`

---

## 📝 Melhorias no README Principal {#readme}

### Template Profissional de README

O README principal é a **primeira impressão** do seu portfólio. Deve incluir:

1. **Badge de Status** (ver seção Badges)
2. **Título e Descrição** clara
3. **Índice/Navegação**
4. **Destaques** (projetos principais)
5. **Tecnologias** utilizadas
6. **Como usar** o portfólio
7. **Contato** e links sociais
8. **Licença** (opcional)

### Exemplo de Seções Importantes

```markdown
## 🏆 Projetos em Destaque

### 1. [Análise Espacial de Acidentes](databank/Work8/)
**Tecnologias:** PostgreSQL, PostGIS, Python, Folium  
**Resultado:** Artigo científico completo, análise de 73.156 acidentes  
**Destaque:** Mapas interativos, análise de proximidade espacial

### 2. [Competição Kaggle - Previsão de Locais](data_mining/challenge/)
**Tecnologias:** Python, scikit-learn, Random Forest  
**Resultado:** F1-Score de 0.9991  
**Destaque:** Top performance na competição
```

---

## 🏅 Badges e Visualizações {#badges}

### Adicionar Badges ao README

Badges tornam o README mais profissional. Adicione no topo do README:

```markdown
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
```

### Gerar Badges Personalizados

Use [shields.io](https://shields.io/) para criar badges personalizados.

### Exemplo de Badges para Adicionar

```markdown
![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)
![PostgreSQL](https://img.shields.io/badge/postgresql-13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
```

---

## 📊 Organização de Projetos {#organização}

### Estrutura de Cada Projeto

Cada trabalho deve ter:

```
work1/
├── README.md              # Descrição completa do projeto
├── notebook.ipynb        # Notebook principal
├── requirements.txt      # Dependências específicas (opcional)
├── results/              # Resultados e visualizações
│   ├── grafico1.png
│   └── tabela1.csv
└── data/                 # Dados (se pequenos) ou link para dados
```

### README de Cada Projeto

Cada README deve conter:

1. **Título e Descrição**
2. **Objetivo**
3. **Metodologia**
4. **Tecnologias Utilizadas**
5. **Resultados Principais**
6. **Como Executar**
7. **Estrutura de Arquivos**
8. **Referências** (se houver)

---

## 💼 Dicas de Mercado de Trabalho {#dicas}

### 1. **Destaque os Projetos Mais Relevantes**

No README principal, coloque primeiro:
- Projetos com **resultados quantitativos** (métricas, scores)
- Projetos com **artigos científicos**
- Projetos com **aplicação prática** clara
- Projetos que demonstram **competências técnicas** avançadas

### 2. **Use Linguagem de Negócio**

Além de técnicas, mostre **impacto**:

❌ "Fiz um modelo de classificação"  
✅ "Desenvolvi modelo de classificação que alcançou F1-Score de 0.9991, demonstrando capacidade de modelagem preditiva avançada"

### 3. **Inclua Visualizações**

- Screenshots de dashboards
- Gráficos profissionais
- Mapas interativos (links)
- Resultados visuais

### 4. **Documente Decisões Técnicas**

Mostre que você **pensa criticamente**:

```markdown
## Decisões Técnicas

- **Escolha do algoritmo:** Random Forest foi escolhido após comparação
  com Logistic Regression e XGBoost, apresentando melhor balance
  entre performance e interpretabilidade.

- **Tratamento de dados desbalanceados:** Aplicado SMOTE após análise
  do balanceamento das classes, melhorando recall em 15%.
```

### 5. **Links para Resultados Interativos**

Se possível, hospede:
- Dashboards (Streamlit, Plotly Dash)
- Mapas interativos (Folium → HTML)
- Notebooks no Google Colab ou Binder

### 6. **Mantenha Atualizado**

- Commits regulares mostram atividade
- Atualize com novos projetos
- Responda a issues (se houver)

### 7. **Use Topics/Tags no GitHub**

Ao criar o repositório, adicione topics:
- `data-science`
- `machine-learning`
- `python`
- `jupyter-notebook`
- `data-analysis`
- `postgresql`
- `portfolio`

---

## ✅ Checklist Final {#checklist}

Antes de publicar, verifique:

### Segurança
- [ ] Nenhuma chave de API no código
- [ ] Nenhuma senha ou token
- [ ] `.gitignore` configurado corretamente
- [ ] Dados sensíveis removidos

### Documentação
- [ ] README principal completo e profissional
- [ ] README em cada disciplina
- [ ] README nos projetos principais
- [ ] Comentários no código quando necessário
- [ ] Instruções de como executar cada projeto

### Organização
- [ ] Estrutura de pastas clara
- [ ] Arquivos organizados
- [ ] Nomes de arquivos descritivos
- [ ] Sem arquivos temporários

### Qualidade
- [ ] Código limpo e organizado
- [ ] Notebooks executáveis
- [ ] Resultados documentados
- [ ] Visualizações de qualidade

### GitHub
- [ ] Repositório criado
- [ ] README com badges
- [ ] Description do repositório preenchida
- [ ] Topics/tags adicionados
- [ ] Branch principal renomeada para `main`

---

## 🎯 Próximos Passos Após Publicar

1. **Adicionar ao LinkedIn**
   - Link do repositório no perfil
   - Destaque projetos principais

2. **Criar README.md no Perfil do GitHub**
   - Crie um repositório com seu username
   - Adicione links para projetos principais
   - Adicione estatísticas e tecnologias

3. **Compartilhar**
   - Adicione link no currículo
   - Compartilhe em redes sociais profissionais
   - Mencione em entrevistas

---

## 📚 Recursos Adicionais

- [GitHub Docs](https://docs.github.com/)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Shields.io](https://shields.io/) - Badges
- [GitHub Pages](https://pages.github.com/)

---

**Boa sorte com seu portfólio!** 🚀

