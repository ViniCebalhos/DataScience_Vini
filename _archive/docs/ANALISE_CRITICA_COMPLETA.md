# 📊 Análise Crítica Completa do Portfólio de Ciência de Dados

**Autor:** Vinícius de Souza Cebalhos  
**Data:** Janeiro 2025  
**Objetivo:** Revisão completa, crítica e prática para transformar o repositório em portfólio profissional

---

## 📁 1. TREE RESUMIDO DO REPOSITÓRIO (Atual)

```
/home/vinicius/Projects/11111/ciencia_de_dados/
├── README.md                          # ✅ Existe, mas precisa atualização
├── requirements.txt                  # ✅ Existe, mas versões genéricas (>=)
├── .gitignore                         # ✅ Existe, bem configurado
├── .github/
│   └── workflows/                     # ⚠️ Verificar se existe ci.yml
│
├── projects/                          # ✅ Estrutura criada
│   ├── analise-acidentes-rodovias/
│   │   └── Work6/                     # ⚠️ Subpasta desnecessária
│   ├── analise-espacial-acidentes/
│   │   └── Work8/                     # ⚠️ Subpasta desnecessária
│   ├── analise-esaude-curitiba/       # ⚠️ Muitos notebooks duplicados
│   ├── classificacao-sinais-vitais/
│   │   └── Work3/                     # ⚠️ Subpasta desnecessária
│   └── competicao-kaggle-venues/
│       └── challenge/                 # ⚠️ Subpasta desnecessária
│
├── data-mining/                       # ✅ Bem estruturado
│   ├── README.md
│   ├── Aula3/                         # ⚠️ Nome genérico
│   ├── clustering-titanic/
│   ├── regressao-linear/
│   ├── regras-associacao-texto/
│   └── web-scraping-youtube/
│
├── machine-learning/                  # ✅ Bem estruturado
│   ├── README.md
│   ├── classificacao-indicadores/
│   │   ├── README.md
│   │   └── Vinicius_Cebalhos_classificacao.ipynb
│   ├── regressao-imoveis/
│   └── Work2/                         # ⚠️ Pasta duplicada (deveria estar em classificacao-indicadores)
│
├── banco-dados/                       # ✅ Bem estruturado
│   ├── README.md
│   ├── analise-acidentes-eda/
│   ├── analise-alvaras/
│   └── consultas-sql-avancadas/
│
├── estatistica/                       # ⚠️ 79M - R, não Python
│   ├── Aula01/ ... Aula10_apresentacao/
│   └── (múltiplos arquivos .R, .Rmd, .Rproj)
│
└── _archive/                          # ✅ Material de estudo
    ├── docs/
    ├── exercicios/
    └── tutoriais-python/
```

**Tamanhos por pasta:**
- `estatistica/`: 79M (maior)
- `_archive/`: 31M
- `machine-learning/`: 5.6M
- `projects/`: 4.7M
- `data-mining/`: 2.7M
- `banco-dados/`: 248K

---

## 🚨 2. PROBLEMAS IDENTIFICADOS

### 2.1 Estrutura e Organização

#### ❌ Problemas Críticos

1. **Subpastas desnecessárias em projects/**
   - `projects/analise-acidentes-rodovias/Work6/` → deveria ser `projects/analise-acidentes-rodovias/`
   - `projects/analise-espacial-acidentes/Work8/` → deveria ser `projects/analise-espacial-acidentes/`
   - `projects/classificacao-sinais-vitais/Work3/` → deveria ser `projects/classificacao-sinais-vitais/`
   - `projects/competicao-kaggle-venues/challenge/` → deveria ser `projects/competicao-kaggle-venues/`

2. **Nomes inconsistentes e genéricos**
   - `Aula3/` em data-mining (nome genérico)
   - `Work2/` em machine-learning (duplicado, já existe classificacao-indicadores)
   - Múltiplos notebooks com nomes genéricos: `teste.ipynb`, `final.ipynb`, `final2.ipynb`, `Teste2.ipynb`

3. **Notebooks duplicados/versões múltiplas**
   - `analise-esaude-curitiba/`: 8 notebooks, muitos duplicados
     - `analise_completa_temporal.ipynb` e `analise_completa_temporal2.ipynb`
     - `teste.ipynb`, `Teste2.ipynb`, `final.ipynb`
   - `competicao-kaggle-venues/`: 4 notebooks similares
     - `challenge.ipynb`, `challenge_final.ipynb`, `final.ipynb`, `final2.ipynb`

4. **Estrutura inconsistente entre projetos**
   - Alguns têm `README.md`, outros não
   - Alguns têm `requirements.txt`, outros não
   - Falta padronização de pastas (data/, notebooks/, src/, figures/)

### 2.2 Arquivos e Dados

#### ❌ Problemas Críticos

1. **Arquivos grandes no Git (potencial)**
   - `estatistica/Aula10_apresentacao/archive/winemag-data-130k-v2.json` (>10MB)
   - `.git/objects/pack/` (normal, mas verificar histórico)

2. **Dados sensíveis potenciais**
   - `preparar_postos_prf_banco.py` contém string de conexão com placeholder de senha
   - Verificar se há arquivos `.env` ou `api.txt` com chaves reais

3. **Arquivos temporários/compilados**
   - Verificar se há `*.aux`, `*.log`, `*.out` (LaTeX) versionados
   - Verificar `.ipynb_checkpoints/` (já no .gitignore, mas limpar localmente)

### 2.3 Documentação

#### ⚠️ Problemas Moderados

1. **READMEs desatualizados ou incompletos**
   - README principal existe mas pode melhorar
   - Alguns projetos em `projects/` não têm README específico
   - Falta `data/README.md` explicando como obter datasets

2. **Falta de exemplos de uso**
   - Nem todos os projetos têm exemplos claros de execução
   - Falta documentação de como obter dados grandes

3. **Falta de requirements.txt por projeto**
   - Apenas alguns projetos têm `requirements.txt` específico
   - `requirements.txt` raiz usa versões genéricas (>=) em vez de fixas (==)

### 2.4 Notebooks

#### ⚠️ Problemas Moderados

1. **Nomes confusos e duplicados**
   - `teste.ipynb`, `Teste2.ipynb`, `final.ipynb`, `final2.ipynb`
   - `analise_completa_temporal.ipynb` e `analise_completa_temporal2.ipynb`

2. **Falta de versões limpas**
   - Não há `*_clean.ipynb` separados
   - Outputs podem estar embutidos (pesados)

3. **Possíveis problemas de reprodutibilidade**
   - Verificar se todos têm seeds definidos
   - Verificar se há caminhos absolutos locais

4. **Falta de estrutura padronizada**
   - Não há separação clara: EDA → Preprocessamento → Modelagem → Resultados
   - Falta seção "Resumo" com principais resultados

### 2.5 Código Python

#### ⚠️ Problemas Moderados

1. **Falta de docstrings**
   - Scripts Python sem documentação adequada (estilo NumPy)

2. **Falta de testes**
   - Nenhum projeto tem testes unitários

3. **Falta de estrutura `src/`**
   - Código espalhado na raiz dos projetos
   - Falta `__init__.py` para organização como pacotes

### 2.6 Versionamento

#### ⚠️ Problemas Menores

1. **Falta de tags/releases**
   - Não há versionamento semântico

2. **Falta de CHANGELOG**
   - Histórico de mudanças não documentado

---

## 🎯 3. NOVA ESTRUTURA PROPOSTA

### 3.1 Estrutura Principal (Corrigida)

```
ciencia_de_dados/
├── README.md                          # README principal do portfólio
├── .gitignore                         # Atualizado
├── requirements.txt                   # Versões fixas (==)
├── .github/
│   ├── workflows/
│   │   └── ci.yml                     # GitHub Actions
│   └── pull_request_template.md       # Template de PR
│
├── projects/                          # 🆕 Projetos principais (destaques)
│   ├── analise-espacial-acidentes/    # ⬆️ Remover Work8/
│   ├── competicao-kaggle-venues/      # ⬆️ Remover challenge/
│   ├── analise-acidentes-rodovias/    # ⬆️ Remover Work6/
│   ├── analise-esaude-curitiba/       # ⬆️ Limpar notebooks duplicados
│   └── classificacao-sinais-vitais/   # ⬆️ Remover Work3/
│
├── data-mining/                       # ✅ Manter
│   ├── README.md
│   ├── conceitos-fundamentais/        # ⬆️ Renomear Aula3/
│   ├── web-scraping-youtube/
│   ├── regressao-linear/
│   ├── clustering-titanic/
│   └── regras-associacao-texto/
│
├── machine-learning/                  # ✅ Manter
│   ├── README.md
│   ├── regressao-imoveis/
│   └── classificacao-indicadores/     # ⬆️ Remover Work2/ duplicado
│
├── banco-dados/                       # ✅ Manter
│   ├── README.md
│   ├── analise-alvaras/
│   ├── analise-acidentes-eda/
│   └── consultas-sql-avancadas/
│
├── estatistica/                       # ⚠️ Manter (R)
│   ├── README.md                      # ⬆️ Criar
│   └── (estrutura mantida)
│
└── _archive/                          # ✅ Manter
    ├── README.md                      # ⬆️ Criar
    ├── docs/
    ├── exercicios/
    └── tutoriais-python/
```

### 3.2 Estrutura Padrão por Projeto (Recomendada)

Cada projeto em `projects/` deve seguir:

```
projeto-nome/
├── README.md                         # Documentação completa
├── requirements.txt                  # Dependências específicas
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
│   ├── 02-preprocessamento.ipynb  # Limpeza
│   ├── 03-modelagem.ipynb         # Modelos
│   └── 04-resultados.ipynb        # Resultados finais
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

### 4.1 Remover Subpastas Desnecessárias em projects/

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados

# Analise Acidentes Rodovias
cd projects/analise-acidentes-rodovias/Work6
git mv * ../
git mv .* .. 2>/dev/null || true
cd ..
rmdir Work6

# Analise Espacial Acidentes
cd projects/analise-espacial-acidentes/Work8
git mv * ../
git mv .* .. 2>/dev/null || true
cd ..
rmdir Work8

# Classificacao Sinais Vitais
cd projects/classificacao-sinais-vitais/Work3
git mv * ../
git mv .* .. 2>/dev/null || true
cd ..
rmdir Work3

# Competicao Kaggle
cd projects/competicao-kaggle-venues/challenge
git mv * ../
git mv .* .. 2>/dev/null || true
cd ..
rmdir challenge
```

### 4.2 Limpar Notebooks Duplicados

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados

# Analise E-Saude: Manter apenas os principais
cd projects/analise-esaude-curitiba

# Manter: analise_exploratoria_esaude.ipynb, analise_completa_temporal.ipynb
# Remover ou arquivar: teste.ipynb, Teste2.ipynb, final.ipynb, limpeza_dados2.ipynb
# Decisão: manter analise_completa_temporal.ipynb como principal
# Se analise_completa_temporal2.ipynb for mais recente, substituir

# Verificar qual é mais recente
ls -lt *.ipynb | head -5

# Se temporal2 for mais recente:
# git mv analise_completa_temporal2.ipynb analise_completa_temporal.ipynb
# git rm analise_completa_temporal.ipynb  # versão antiga

# Competicao Kaggle: Manter apenas challenge_final.ipynb
cd ../competicao-kaggle-venues
# Manter: challenge_final.ipynb (ou o mais completo)
# Remover: challenge.ipynb, final.ipynb, final2.ipynb
```

### 4.3 Reorganizar Data Mining

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/data-mining

# Renomear Aula3
git mv Aula3 conceitos-fundamentais
```

### 4.4 Limpar Machine Learning

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/machine-learning

# Verificar se Work2 é duplicado de classificacao-indicadores
# Se sim, remover Work2
if [ -d "Work2" ] && [ -d "classificacao-indicadores" ]; then
    echo "Work2 parece ser duplicado. Verificar conteúdo antes de remover."
    # git rm -r Work2  # Apenas após verificação
fi
```

### 4.5 Limpar Arquivos Temporários

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados

# Remover checkpoints do Jupyter
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null

# Remover arquivos LaTeX temporários (já no .gitignore, mas limpar localmente)
find . -name "*.aux" -delete
find . -name "*.log" -delete
find . -name "*.out" -delete
find . -name "*.synctex.gz" -delete
find . -name "*.fdb_latexmk" -delete
find . -name "*.fls" -delete
```

### 4.6 Verificar e Remover Dados Sensíveis

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados

# Verificar arquivos com possíveis API keys
grep -r "api_key\|API_KEY\|secret\|SECRET" --include="*.txt" --include="*.py" --include="*.ipynb" . | grep -v ".git" | grep -v "placeholder\|exemplo\|example"

# Verificar arquivos .env
find . -name ".env" -o -name "*.env" | grep -v ".git"

# Verificar preparar_postos_prf_banco.py
# Já identificado: contém placeholder, mas verificar se há senhas reais
grep -n "password\|senha" projects/analise-espacial-acidentes/preparar_postos_prf_banco.py
```

---

## 📝 5. CHECKLIST DE LIMPEZA POR PROJETO

### 5.1 Checklist Geral para Cada Projeto em `projects/`

- [ ] **README.md** completo e atualizado
- [ ] **requirements.txt** com versões específicas (==)
- [ ] **.gitignore** configurado (se necessário)
- [ ] Estrutura de pastas padronizada (data/, notebooks/, src/, figures/)
- [ ] Dados grandes movidos para `data/raw/` e adicionados ao `.gitignore`
- [ ] `data/README.md` explicando como obter os dados
- [ ] `data/sample/` com amostra pequena para testes
- [ ] Notebooks renomeados de forma descritiva (01-*, 02-*, etc.)
- [ ] Notebooks limpos (outputs removidos) ou versão `*_clean.ipynb`
- [ ] Seeds definidos para reprodutibilidade
- [ ] Código Python com docstrings (estilo NumPy)
- [ ] Scripts executáveis do início ao fim
- [ ] Visualizações salvas em `figures/` (não embutidas nos notebooks)
- [ ] Exemplos de uso documentados

### 5.2 Checklist Específico para Notebooks

Para cada notebook importante:

- [ ] **Célula de Setup**: pip install ou requirements claramente separado
- [ ] **Seeds**: `np.random.seed()` e `random.seed()` definidos
- [ ] **Caminhos relativos**: sem caminhos absolutos locais
- [ ] **Outputs limpos**: versão sem outputs ou `*_clean.ipynb`
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

### 6.1 Arquivos Identificados

1. **`preparar_postos_prf_banco.py`**
   - Linha 178: string de conexão com placeholder `password=sua_senha`
   - Linha 274: input de senha (seguro, não versionado)
   - **Ação:** Manter como está (usa input, não hardcoded)

2. **Verificar arquivos com possíveis API keys**
   - Executar: `grep -r "api_key\|API_KEY" --include="*.txt" .`
   - Se encontrar, remover ou usar variáveis de ambiente

### 6.2 .gitignore - Melhorias Sugeridas

O `.gitignore` atual está bom, mas adicionar:

```gitignore
# Dados grandes (específicos)
data/raw/
data/processed/
!data/sample/*.csv
!data/README.md

# Arquivos de API (específicos)
*api*.txt
!*api*example*.txt
```

---

## 📊 7. PROJETOS EM DESTAQUE (3-5)

### 7.1 Critérios de Seleção

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

**⚠️ Ação necessária:** Limpar notebooks duplicados antes de destacar

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
git commit -m "refactor(estrutura): remover subpastas desnecessárias em projects/

- Remover Work6/ de analise-acidentes-rodovias
- Remover Work8/ de analise-espacial-acidentes
- Remover Work3/ de classificacao-sinais-vitais
- Remover challenge/ de competicao-kaggle-venues"

# Limpeza de notebooks
git commit -m "chore(notebooks): limpar notebooks duplicados em analise-esaude-curitiba

- Manter analise_completa_temporal.ipynb como principal
- Remover teste.ipynb, Teste2.ipynb, final.ipynb
- Consolidar versões duplicadas"

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

## ✅ 10. CHECKLIST FINAL PARA PUBLICAÇÃO

### 10.1 Segurança e Privacidade

- [ ] Arquivos sensíveis removidos (API keys, senhas, CPFs)
- [ ] `.gitignore` configurado corretamente
- [ ] Dados pessoais anonimizados (se houver)
- [ ] Arquivos `.env` não versionados
- [ ] Histórico do Git limpo (se necessário, usar `git filter-branch`)

### 10.2 Estrutura e Organização

- [ ] Estrutura de pastas padronizada
- [ ] Nomes de arquivos descritivos e consistentes
- [ ] Projetos em destaque na pasta `projects/`
- [ ] Material de estudo em `_archive/`
- [ ] Sem pastas vazias ou temporárias
- [ ] Subpastas desnecessárias removidas (Work6/, Work8/, etc.)

### 10.3 Documentação

- [ ] README.md principal completo e atualizado
- [ ] README.md em cada projeto principal
- [ ] README.md em cada disciplina
- [ ] `data/README.md` explicando como obter dados
- [ ] Exemplos de uso documentados
- [ ] Contato atualizado (ou "sob demanda")

### 10.4 Código e Notebooks

- [ ] Notebooks limpos (outputs removidos) ou versões `*_clean.ipynb`
- [ ] Seeds definidos para reprodutibilidade
- [ ] Caminhos relativos (sem caminhos absolutos locais)
- [ ] Docstrings em funções Python (estilo NumPy)
- [ ] Scripts executáveis do início ao fim
- [ ] Células de setup claramente separadas
- [ ] Notebooks duplicados removidos ou consolidados

### 10.5 Dependências

- [ ] `requirements.txt` na raiz atualizado
- [ ] `requirements.txt` em cada projeto (quando necessário)
- [ ] Versões específicas de pacotes (não `>=`, usar `==`)
- [ ] Instruções de instalação claras

### 10.6 Dados

- [ ] Datasets grandes (>10MB) no `.gitignore`
- [ ] `data/sample/` com amostras pequenas para testes
- [ ] `data/README.md` com links/instruções para obter dados
- [ ] Sem dados sensíveis versionados

### 10.7 Visualizações

- [ ] Figuras salvas em `figures/` (não embutidas nos notebooks)
- [ ] Figuras principais documentadas
- [ ] Screenshots/plots para projetos em destaque

### 10.8 Projetos em Destaque

- [ ] 3-5 projetos selecionados e documentados
- [ ] README específico para cada projeto em destaque
- [ ] Resultados mensuráveis documentados
- [ ] Links funcionando

### 10.9 Versionamento

- [ ] Commits com mensagens descritivas
- [ ] Branches organizadas (se aplicável)
- [ ] Tags para releases (opcional)

### 10.10 CI/CD (Opcional)

- [ ] GitHub Actions configurado
- [ ] Lint passando
- [ ] Testes passando (se houver)

---

**Última atualização:** Janeiro 2025

