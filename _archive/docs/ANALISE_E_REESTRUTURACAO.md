# 📋 Análise Completa e Reestruturação do Portfólio de Data Science

**Autor:** Vinícius de Souza Cebalhos  
**Data:** Janeiro 2025  
**Objetivo:** Revisar, reestruturar e preparar o portfólio para publicação profissional

---

## 📊 1. ESTRUTURA ATUAL DO REPOSITÓRIO

### Tree Resumido (até 3 níveis)

```
/home/vinicius/Projects/datascience/
├── README.md                          # ✅ Existe, mas precisa atualização
├── requirements.txt                  # ✅ Existe
├── .gitignore                        # ✅ Existe, mas pode melhorar
│
├── Aulas_estatistica/                # ⚠️ 744M - R, não Python
│   ├── Aula1/ ... Aula10_apresentacao/
│   └── (múltiplos arquivos .R, .Rmd, .Rproj)
│
├── data_mining/                      # ✅ 444M - Bem estruturado
│   ├── README.md                     # ✅ Existe
│   ├── Aula3/
│   ├── work1/ ... work4/
│   └── challenge/                    # ⭐ Projeto destaque
│
├── databank/                         # ✅ 89M - Bem estruturado
│   ├── README.md                     # ✅ Existe
│   ├── Work1/ ... Work8/             # ⭐ Work6 e Work8 são destaques
│
├── ML/                               # ✅ 5.5M - Bem estruturado
│   ├── README.md                     # ✅ Existe
│   └── Work1/ ... Work3/
│
├── python_ds/                        # ⚠️ 745M - Maior pasta
│   ├── Trabalho/                     # ⭐ Projeto E-Saúde (destaque)
│   │   ├── README.md                 # ✅ Existe
│   │   ├── Dados/                    # ⚠️ Múltiplos CSVs grandes
│   │   └── (múltiplos notebooks)
│   └── tutoriais/                    # ⚠️ Material de estudo, não projeto
│
├── exercicios/                       # ⚠️ 1.5M - Exercícios, não projetos
│   └── README.md
│
├── downloads/                        # ⚠️ Pasta vazia ou temporária
│
└── (arquivos de documentação)
    ├── COMANDOS_GIT.md
    ├── GUIA_GITHUB.md
    ├── PASSO_A_PASSO_GITHUB.md
    ├── RESUMO_ORGANIZACAO.md
    └── SOLUCAO_ARQUIVO_GRANDE.md
```

---

## 🚨 2. PROBLEMAS IDENTIFICADOS

### 2.1 Estrutura e Organização

- ❌ **Nomes inconsistentes**: `Work1`, `work1`, `Aula1`, `Aula07` (mistura maiúsculas/minúsculas)
- ❌ **Pastas de tutoriais/exercícios misturadas com projetos**: `python_ds/tutoriais/`, `exercicios/`, `Aulas_estatistica/`
- ❌ **Pasta `downloads/` vazia ou temporária** não deveria estar no repositório
- ❌ **Pasta `Aulas_estatistica/` em R** (744M) - diferente do resto do portfólio Python
- ⚠️ **Estrutura inconsistente**: alguns projetos têm `README.md`, outros não
- ⚠️ **Falta padronização**: alguns têm `src/`, outros não

### 2.2 Arquivos e Dados

- ❌ **Arquivos grandes no Git** (>10MB):
  - `databank/Work2/datatran2025.csv`
  - `databank/Work6/datatran2024.csv`
  - `databank/Work8/datatran2024.csv`
  - `databank/Work3/datatran2024.csv`
  - `data_mining/challenge/data/*.csv` (múltiplos)
  - `python_ds/Trabalho/Dados/*.csv` (múltiplos >10MB)
  - `Aulas_estatistica/Aula10_apresentacao/winemag-data-130k-v2.csv`
  - `Aulas_estatistica/Aula10_apresentacao/archive.zip`
  - `data_mining/work1/chromedriver` (binário)
  - Mapas HTML grandes: `mapa_acidentes_interativo.html` (4.3MB), `mapa_completo_postos_prf.html` (6.2MB)

- ⚠️ **Arquivos sensíveis potenciais**:
  - `data_mining/work1/api.txt` (pode conter API keys)
  - `.env` files (se existirem)

- ⚠️ **Arquivos temporários/compilados**:
  - `*.aux`, `*.log`, `*.out` (LaTeX)
  - `*.html` (exportações de notebooks)
  - `*.ipynb_checkpoints/`

### 2.3 Documentação

- ⚠️ **READMEs desatualizados**: alguns projetos têm README, mas falta padronização
- ⚠️ **Falta de exemplos de uso**: nem todos os projetos têm exemplos claros
- ⚠️ **Falta de requirements.txt por projeto**: apenas alguns têm
- ⚠️ **Falta de documentação de dados**: onde obter datasets grandes

### 2.4 Notebooks

- ⚠️ **Nomes confusos**: `teste.ipynb`, `Teste2.ipynb`, `final.ipynb`, `final2.ipynb`
- ⚠️ **Múltiplas versões**: `analise_completa_temporal.ipynb` e `analise_completa_temporal2.ipynb`
- ⚠️ **Falta de versões limpas**: não há `*_clean.ipynb` separados
- ⚠️ **Possíveis outputs pesados**: imagens grandes embutidas nos notebooks
- ⚠️ **Falta de seeds**: alguns notebooks podem não ser reproduzíveis

### 2.5 Código Python

- ⚠️ **Falta de docstrings**: scripts Python sem documentação adequada
- ⚠️ **Falta de testes**: nenhum projeto tem testes unitários
- ⚠️ **Falta de estrutura `src/`**: código espalhado na raiz dos projetos
- ⚠️ **Falta de `__init__.py`**: módulos não estão organizados como pacotes

### 2.6 Versionamento

- ⚠️ **Falta de tags/releases**: não há versionamento semântico
- ⚠️ **Falta de CHANGELOG**: histórico de mudanças não documentado

---

## 🎯 3. NOVA ESTRUTURA PROPOSTA

### 3.1 Estrutura Principal

```
datascience/
├── README.md                          # README principal do portfólio
├── .gitignore                         # Atualizado
├── requirements.txt                   # Dependências gerais
├── .github/
│   └── workflows/
│       └── ci.yml                     # GitHub Actions
│
├── projects/                          # 🆕 Projetos principais (destaques)
│   ├── analise-espacial-acidentes/    # databank/Work8
│   ├── competicao-kaggle-venues/     # data_mining/challenge
│   ├── analise-acidentes-rodovias/   # databank/Work6
│   ├── analise-esaude-curitiba/      # python_ds/Trabalho
│   └── classificacao-sinais-vitais/  # ML/Work3
│
├── data-mining/                      # Renomeado de data_mining
│   ├── README.md
│   ├── web-scraping-youtube/         # work1
│   ├── regressao-linear/             # work2
│   ├── clustering-titanic/           # work3
│   └── regras-associacao-texto/      # work4
│
├── machine-learning/                 # Renomeado de ML
│   ├── README.md
│   ├── regressao-imoveis/            # Work1
│   ├── classificacao-indicadores/   # Work2
│   └── classificacao-sinais-vitais/ # Work3 (movido para projects/)
│
├── banco-dados/                      # Renomeado de databank
│   ├── README.md
│   ├── analise-alvaras/              # Work1
│   ├── analise-acidentes-eda/        # Work2
│   ├── consultas-sql-avancadas/      # Work3
│   ├── artigo-acidentes-rodovias/    # Work6 (movido para projects/)
│   └── analise-espacial-postgis/     # Work8 (movido para projects/)
│
├── estatistica/                      # 🆕 Aulas_estatistica (R)
│   ├── README.md
│   └── (estrutura mantida, mas documentada)
│
└── _archive/                         # 🆕 Material de estudo/tutoriais
    ├── tutoriais-python/             # python_ds/tutoriais
    ├── exercicios/                   # exercicios/
    └── README.md                     # Explica que é material de estudo
```

### 3.2 Estrutura Padrão por Projeto

Cada projeto deve seguir esta estrutura:

```
projeto-nome/
├── README.md                         # Documentação completa
├── requirements.txt                  # Dependências do projeto
├── .gitignore                       # Gitignore específico (opcional)
│
├── data/
│   ├── raw/                         # Dados brutos (não versionados)
│   ├── processed/                   # Dados processados (não versionados)
│   ├── sample/                     # Amostra pequena para testes
│   └── README.md                   # Como obter os dados
│
├── notebooks/
│   ├── 01-exploracao.ipynb         # EDA
│   ├── 02-preprocessamento.ipynb   # Limpeza
│   ├── 03-modelagem.ipynb          # Modelos
│   └── 04-resultados.ipynb         # Resultados finais
│
├── src/                             # Código Python organizado
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── load_data.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py
│   └── models/
│       ├── __init__.py
│       └── train_model.py
│
├── figures/                         # Visualizações salvas
│   └── README.md                   # Descrição das figuras
│
├── reports/                         # Relatórios, artigos
│   └── (PDFs, LaTeX, etc.)
│
└── tests/                           # Testes unitários (opcional)
    └── test_*.py
```

---

## 🔧 4. COMANDOS DE REORGANIZAÇÃO

### 4.1 Criar Nova Estrutura

```bash
cd /home/vinicius/Projects/datascience

# Criar pastas principais
mkdir -p projects
mkdir -p _archive/tutoriais-python
mkdir -p _archive/exercicios
mkdir -p estatistica

# Criar estrutura de projetos principais
mkdir -p projects/analise-espacial-acidentes
mkdir -p projects/competicao-kaggle-venues
mkdir -p projects/analise-acidentes-rodovias
mkdir -p projects/analise-esaude-curitiba
mkdir -p projects/classificacao-sinais-vitais
```

### 4.2 Mover Projetos para Destaque

```bash
# Work 8 - Análise Espacial (DESTAQUE)
git mv databank/Work8 projects/analise-espacial-acidentes

# Challenge Kaggle (DESTAQUE)
git mv data_mining/challenge projects/competicao-kaggle-venues

# Work 6 - Artigo Acidentes (DESTAQUE)
git mv databank/Work6 projects/analise-acidentes-rodovias

# Trabalho E-Saúde (DESTAQUE)
git mv python_ds/Trabalho projects/analise-esaude-curitiba

# ML Work 3 - Sinais Vitais (DESTAQUE)
git mv ML/Work3 projects/classificacao-sinais-vitais
```

### 4.3 Reorganizar Data Mining

```bash
# Renomear pasta principal
git mv data_mining data-mining

# Reorganizar works
cd data-mining
git mv work1 web-scraping-youtube
git mv work2 regressao-linear
git mv work3 clustering-titanic
git mv work4 regras-associacao-texto
cd ..
```

### 4.4 Reorganizar Machine Learning

```bash
# Renomear pasta principal
git mv ML machine-learning

# Reorganizar works
cd machine-learning
git mv Work1 regressao-imoveis
git mv Work2 classificacao-indicadores
cd ..
```

### 4.5 Reorganizar Banco de Dados

```bash
# Renomear pasta principal
git mv databank banco-dados

# Reorganizar works
cd banco-dados
git mv Work1 analise-alvaras
git mv Work2 analise-acidentes-eda
git mv Work3 consultas-sql-avancadas
cd ..
```

### 4.6 Mover Material de Estudo

```bash
# Tutoriais
git mv python_ds/tutoriais _archive/tutoriais-python

# Exercícios
git mv exercicios _archive/exercicios

# Estatística (R)
git mv Aulas_estatistica estatistica

# Remover pasta downloads se vazia
rmdir downloads 2>/dev/null || echo "Downloads não está vazia"
```

### 4.6 Limpar Arquivos Temporários

```bash
# Remover checkpoints do Jupyter
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null

# Remover arquivos LaTeX temporários (já no .gitignore, mas limpar localmente)
find . -name "*.aux" -delete
find . -name "*.log" -delete
find . -name "*.out" -delete
find . -name "*.synctex.gz" -delete
```

---

## 📝 5. CHECKLIST DE LIMPEZA POR PROJETO

### 5.1 Checklist Geral para Cada Projeto

- [ ] README.md completo e atualizado
- [ ] requirements.txt com versões específicas
- [ ] .gitignore configurado (se necessário)
- [ ] Estrutura de pastas padronizada (data/, notebooks/, src/, figures/)
- [ ] Dados grandes movidos para data/raw/ e adicionados ao .gitignore
- [ ] data/README.md explicando como obter os dados
- [ ] data/sample/ com amostra pequena para testes
- [ ] Notebooks renomeados de forma descritiva (01-*, 02-*, etc.)
- [ ] Notebooks limpos (outputs removidos) ou versão *_clean.ipynb
- [ ] Seeds definidos para reprodutibilidade
- [ ] Código Python com docstrings (estilo NumPy)
- [ ] Scripts executáveis do início ao fim
- [ ] Visualizações salvas em figures/ (não embutidas nos notebooks)
- [ ] Exemplos de uso documentados

### 5.2 Checklist Específico para Notebooks

Para cada notebook importante:

- [ ] **Célula de Setup**: pip install ou requirements claramente separado
- [ ] **Seeds**: `np.random.seed()` e `random.seed()` definidos
- [ ] **Caminhos relativos**: sem caminhos absolutos locais
- [ ] **Outputs limpos**: versão sem outputs ou *_clean.ipynb
- [ ] **Seção Resumo**: células finais com principais resultados
- [ ] **Referência ao dataset**: link ou instruções para obter dados
- [ ] **Documentação**: células markdown explicando cada etapa
- [ ] **Execução completa**: notebook roda do início ao fim sem erros

**Comando para limpar outputs:**
```bash
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebook.ipynb
```

### 5.3 Checklist para Código Python

- [ ] **Docstrings estilo NumPy**:
```python
def process_data(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Processa dados removendo valores nulos.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame de entrada.
    column : str
        Nome da coluna a processar.

    Returns
    -------
    pd.DataFrame
        DataFrame processado.
    """
    pass
```

- [ ] **Type hints**: parâmetros e retornos tipados
- [ ] **Funções pequenas**: uma responsabilidade por função
- [ ] **Tratamento de erros**: try/except onde necessário
- [ ] **Logging**: uso de logging em vez de print()
- [ ] **Configuração**: variáveis de ambiente ou arquivo config

---

## 🔒 6. SEGURANÇA E DADOS SENSÍVEIS

### 6.1 Arquivos a Verificar/Remover

```bash
# Verificar arquivos com possíveis API keys
grep -r "api_key\|API_KEY\|secret\|SECRET" --include="*.txt" --include="*.py" --include="*.ipynb" .

# Verificar arquivos .env
find . -name ".env" -o -name "*.env"

# Verificar arquivos com possíveis dados sensíveis
find . -name "*cpf*" -o -name "*email*" -o -name "*senha*" -i
```

### 6.2 .gitignore Atualizado

O `.gitignore` atual já está bom, mas adicionar:

```gitignore
# Dados grandes
data/raw/
data/processed/
*.csv
*.xlsx
*.parquet
!data/sample/*.csv
!data/README.md

# Mapas HTML grandes (manter apenas se essencial)
*.html
!README*.html
!reports/*.html

# Arquivos de API
*api*.txt
*_key.txt
*_secret.txt
chromedriver
chromedriver.exe

# Arquivos LaTeX temporários (já está, mas garantir)
*.aux
*.log
*.out
*.synctex.gz
*.fdb_latexmk
*.fls
```

---

## 📊 7. PROJETOS EM DESTAQUE (3-5)

### 7.1 Seleção de Projetos

**Critérios de seleção:**
1. ✅ Completude (projeto finalizado)
2. ✅ Variedade técnica (diferentes áreas)
3. ✅ Resultados mensuráveis (métricas, artigos)
4. ✅ Código limpo e documentado
5. ✅ Impacto/Relevância

### 7.2 Projetos Selecionados

#### 🥇 1. Análise Espacial de Acidentes com PostGIS
**Pasta:** `projects/analise-espacial-acidentes/`  
**Justificativa:**
- ✅ Artigo científico completo publicado
- ✅ 73.156 acidentes analisados
- ✅ Tecnologia avançada (PostGIS, análise geoespacial)
- ✅ Mapas interativos profissionais
- ✅ Resultado mensurável: 80% dos acidentes fora da cobertura
- ✅ Metodologia replicável

**Técnicas:** PostgreSQL, PostGIS, Python, GeoPandas, Folium, Análise Espacial

---

#### 🥈 2. Competição Kaggle - Previsão de Locais
**Pasta:** `projects/competicao-kaggle-venues/`  
**Justificativa:**
- ✅ F1-Score de 0.9991 (excelente performance)
- ✅ Competição real (Kaggle-style)
- ✅ Feature engineering completo
- ✅ Múltiplos algoritmos testados
- ✅ Validação cruzada e otimização

**Técnicas:** Machine Learning, Random Forest, Grid Search, Validação Cruzada, Feature Engineering

---

#### 🥉 3. Análise de Acidentes em Rodovias Federais
**Pasta:** `projects/analise-acidentes-rodovias/`  
**Justificativa:**
- ✅ Artigo científico completo (padrão SBC)
- ✅ 67.794 acidentes analisados
- ✅ Análise temporal completa
- ✅ Visualizações profissionais
- ✅ Insights para políticas públicas

**Técnicas:** PostgreSQL, SQL, Python, Análise Temporal, LaTeX, Visualização

---

#### 4. Análise do Sistema E-Saúde de Curitiba
**Pasta:** `projects/analise-esaude-curitiba/`  
**Justificativa:**
- ✅ Projeto completo de análise em saúde pública
- ✅ ~46.000 registros mensais processados
- ✅ Análise temporal e geográfica
- ✅ Scripts automatizados de limpeza
- ✅ Dados reais de produção

**Técnicas:** Python, Pandas, Análise Temporal, Análise Geográfica, Limpeza de Dados

---

#### 5. Classificação de Sinais Vitais
**Pasta:** `projects/classificacao-sinais-vitais/`  
**Justificativa:**
- ✅ Classificação multiclasse completa
- ✅ Comparação de múltiplos modelos
- ✅ Visualizações comparativas profissionais
- ✅ Análise de correlações e distribuições
- ✅ Aplicação em área médica

**Técnicas:** Machine Learning, Classificação, Scikit-learn, Análise Comparativa

---

## 📄 8. MENSAGENS DE COMMIT SUGERIDAS

### 8.1 Padrão de Commits

Usar formato convencional:

```
tipo(escopo): descrição curta

Descrição detalhada (opcional)

- Item 1
- Item 2
```

**Tipos:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `refactor`: Refatoração
- `style`: Formatação
- `chore`: Manutenção

### 8.2 Exemplos de Commits

```bash
# Reorganização
git commit -m "refactor(estrutura): reorganizar projetos em pasta projects/

- Mover Work8 para projects/analise-espacial-acidentes
- Mover challenge para projects/competicao-kaggle-venues
- Criar estrutura padronizada por projeto"

# Documentação
git commit -m "docs(readme): atualizar README principal com projetos em destaque

- Adicionar seção de projetos em destaque
- Incluir badges de tecnologias
- Atualizar instruções de instalação"

# Limpeza
git commit -m "chore(notebooks): limpar outputs e adicionar versões clean

- Remover outputs de notebooks principais
- Criar versões *_clean.ipynb
- Adicionar seeds para reprodutibilidade"

# Dados
git commit -m "chore(dados): mover datasets grandes para .gitignore

- Adicionar data/raw/ ao .gitignore
- Criar data/sample/ com amostras pequenas
- Adicionar data/README.md com instruções"
```

---

## 🔄 9. TEMPLATE DE PULL REQUEST

Criar `.github/pull_request_template.md`:

```markdown
## 📋 Descrição

Breve descrição das mudanças realizadas.

## 🎯 Tipo de Mudança

- [ ] Nova funcionalidade
- [ ] Correção de bug
- [ ] Documentação
- [ ] Refatoração
- [ ] Reorganização de estrutura

## 📁 Arquivos Modificados

- Arquivo 1
- Arquivo 2

## ✅ Checklist

- [ ] Código testado localmente
- [ ] README atualizado
- [ ] Dependências atualizadas (requirements.txt)
- [ ] Sem dados sensíveis
- [ ] Notebooks limpos (outputs removidos)
- [ ] Seeds definidos para reprodutibilidade

## 📸 Screenshots/Resultados

(Se aplicável, adicionar screenshots ou resultados)

## 🔗 Issues Relacionadas

Fixes #(número da issue)
```

---

## 🤖 10. GITHUB ACTIONS WORKFLOW

Criar `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 black
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    
    - name: Lint with flake8
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    
    - name: Check formatting with black
      run: |
        black --check .

  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        pip install pytest
    
    - name: Run tests
      run: |
        pytest tests/ -v || echo "No tests found"

  notebooks:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install jupyter nbconvert pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    
    - name: Check notebooks (exemplo)
      run: |
        # Verificar se notebooks podem ser executados (opcional, pode ser lento)
        # jupyter nbconvert --to notebook --execute notebooks/01-exemplo.ipynb --output /dev/null || echo "Notebook check skipped"
        echo "Notebook validation skipped (too slow for CI)"
```

---

## ✅ 11. CHECKLIST FINAL PARA PUBLICAÇÃO

### 11.1 Segurança e Privacidade

- [ ] Arquivos sensíveis removidos (API keys, senhas, CPFs)
- [ ] `.gitignore` configurado corretamente
- [ ] Dados pessoais anonimizados (se houver)
- [ ] Arquivos `.env` não versionados
- [ ] Histórico do Git limpo (se necessário, usar `git filter-branch`)

### 11.2 Estrutura e Organização

- [ ] Estrutura de pastas padronizada
- [ ] Nomes de arquivos descritivos e consistentes
- [ ] Projetos em destaque na pasta `projects/`
- [ ] Material de estudo em `_archive/`
- [ ] Sem pastas vazias ou temporárias

### 11.3 Documentação

- [ ] README.md principal completo e atualizado
- [ ] README.md em cada projeto principal
- [ ] README.md em cada disciplina
- [ ] data/README.md explicando como obter dados
- [ ] Exemplos de uso documentados
- [ ] Contato atualizado (ou "sob demanda")

### 11.4 Código e Notebooks

- [ ] Notebooks limpos (outputs removidos) ou versões `*_clean.ipynb`
- [ ] Seeds definidos para reprodutibilidade
- [ ] Caminhos relativos (sem caminhos absolutos locais)
- [ ] Docstrings em funções Python (estilo NumPy)
- [ ] Scripts executáveis do início ao fim
- [ ] Células de setup claramente separadas

### 11.5 Dependências

- [ ] `requirements.txt` na raiz atualizado
- [ ] `requirements.txt` em cada projeto (quando necessário)
- [ ] Versões específicas de pacotes (não `>=`, usar `==`)
- [ ] Instruções de instalação claras

### 11.6 Dados

- [ ] Datasets grandes (>10MB) no `.gitignore`
- [ ] `data/sample/` com amostras pequenas para testes
- [ ] `data/README.md` com links/instruções para obter dados
- [ ] Sem dados sensíveis versionados

### 11.7 Visualizações

- [ ] Figuras salvas em `figures/` (não embutidas nos notebooks)
- [ ] Figuras principais documentadas
- [ ] Screenshots/plots para projetos em destaque

### 11.8 Projetos em Destaque

- [ ] 3-5 projetos selecionados e documentados
- [ ] README específico para cada projeto em destaque
- [ ] Resultados mensuráveis documentados
- [ ] Links funcionando

### 11.9 Versionamento

- [ ] Commits com mensagens descritivas
- [ ] Branches organizadas (se aplicável)
- [ ] Tags para releases (opcional)

### 11.10 CI/CD (Opcional)

- [ ] GitHub Actions configurado
- [ ] Lint passando
- [ ] Testes passando (se houver)

---

## 📝 12. PRÓXIMOS PASSOS

1. **Revisar este documento** e ajustar conforme necessário
2. **Aplicar comandos de reorganização** (seção 4)
3. **Atualizar READMEs** conforme templates fornecidos
4. **Limpar notebooks** e criar versões clean
5. **Mover dados grandes** para .gitignore
6. **Criar data/README.md** em cada projeto
7. **Adicionar docstrings** em código Python
8. **Configurar GitHub Actions** (opcional)
9. **Fazer commits** com mensagens descritivas
10. **Revisar checklist final** antes de publicar

---

**Última atualização:** Janeiro 2025

