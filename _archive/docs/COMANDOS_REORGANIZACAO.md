# 🔧 Comandos de Reorganização do Repositório

Este documento contém todos os comandos sugeridos para reorganizar o repositório conforme a nova estrutura proposta.

**⚠️ IMPORTANTE:** Execute estes comandos em ordem e faça commits intermediários para facilitar rollback se necessário.

---

## 📋 Pré-requisitos

```bash
# Certifique-se de estar na raiz do repositório
cd /home/vinicius/Projects/datascience

# Verifique o status do Git
git status

# Faça backup (opcional, mas recomendado)
git branch backup-antes-reorganizacao
```

---

## 1️⃣ Criar Nova Estrutura de Pastas

```bash
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

---

## 2️⃣ Mover Projetos para Destaque

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

# Commit intermediário
git commit -m "refactor(estrutura): mover projetos em destaque para pasta projects/"
```

---

## 3️⃣ Reorganizar Data Mining

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

# Commit intermediário
git commit -m "refactor(data-mining): reorganizar estrutura e renomear works"
```

---

## 4️⃣ Reorganizar Machine Learning

```bash
# Renomear pasta principal
git mv ML machine-learning

# Reorganizar works
cd machine-learning
git mv Work1 regressao-imoveis
git mv Work2 classificacao-indicadores
cd ..

# Commit intermediário
git commit -m "refactor(machine-learning): reorganizar estrutura e renomear works"
```

---

## 5️⃣ Reorganizar Banco de Dados

```bash
# Renomear pasta principal
git mv databank banco-dados

# Reorganizar works
cd banco-dados
git mv Work1 analise-alvaras
git mv Work2 analise-acidentes-eda
git mv Work3 consultas-sql-avancadas
cd ..

# Commit intermediário
git commit -m "refactor(banco-dados): reorganizar estrutura e renomear works"
```

---

## 6️⃣ Mover Material de Estudo

```bash
# Tutoriais
git mv python_ds/tutoriais _archive/tutoriais-python

# Exercícios
git mv exercicios _archive/exercicios

# Estatística (R)
git mv Aulas_estatistica estatistica

# Remover pasta downloads se vazia
rmdir downloads 2>/dev/null || echo "Downloads não está vazia - verificar manualmente"

# Commit intermediário
git commit -m "refactor(estrutura): mover material de estudo para _archive/"
```

---

## 7️⃣ Limpar Arquivos Temporários

```bash
# Remover checkpoints do Jupyter (já no .gitignore, mas limpar localmente)
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null

# Remover arquivos LaTeX temporários (já no .gitignore)
find . -name "*.aux" -delete
find . -name "*.log" -delete
find . -name "*.out" -delete
find . -name "*.synctex.gz" -delete

# Commit (se houver mudanças)
git add -A
git commit -m "chore: remover arquivos temporários" || echo "Nenhum arquivo temporário para remover"
```

---

## 8️⃣ Atualizar .gitignore

```bash
# Verificar se .gitignore está atualizado
# Adicionar se necessário:
cat >> .gitignore << 'EOF'

# Dados grandes (adicionar se ainda não estiver)
data/raw/
data/processed/
*.csv
*.xlsx
*.parquet
!data/sample/*.csv
!data/README.md

# Mapas HTML grandes
*.html
!README*.html
!reports/*.html
EOF

git add .gitignore
git commit -m "chore(gitignore): atualizar para ignorar dados grandes e arquivos temporários"
```

---

## 9️⃣ Criar Estrutura Padrão nos Projetos

Para cada projeto em `projects/`, criar estrutura padrão:

```bash
# Exemplo para um projeto
cd projects/analise-espacial-acidentes

# Criar estrutura padrão
mkdir -p data/raw data/processed data/sample figures reports

# Criar data/README.md
cat > data/README.md << 'EOF'
# Dados do Projeto

## Como Obter os Dados

[Instruções para obter os dados]

## Estrutura

- `raw/` - Dados brutos (não versionados)
- `processed/` - Dados processados (não versionados)
- `sample/` - Amostra pequena para testes
EOF

cd ../..
```

---

## 🔟 Renomear Notebooks (Opcional, mas Recomendado)

```bash
# Exemplo: renomear notebooks em um projeto
cd projects/analise-espacial-acidentes

# Renomear notebooks descritivamente
# (Ajustar nomes conforme necessário)
# git mv "notebook_antigo.ipynb" "01-exploracao.ipynb"
# git mv "outro_notebook.ipynb" "02-modelagem.ipynb"

cd ../..
```

---

## 1️⃣1️⃣ Atualizar README Principal

```bash
# Substituir README.md atual pelo novo
git mv README.md README_OLD.md
cp README_PRINCIPAL.md README.md

git add README.md
git commit -m "docs(readme): atualizar README principal com nova estrutura"
```

---

## 1️⃣2️⃣ Commit Final

```bash
# Verificar status
git status

# Adicionar todos os arquivos novos
git add .

# Commit final
git commit -m "refactor(estrutura): reorganização completa do portfólio

- Mover projetos em destaque para pasta projects/
- Reorganizar disciplinas com nomes consistentes
- Mover material de estudo para _archive/
- Atualizar estrutura de pastas
- Limpar arquivos temporários
- Atualizar documentação"

# Push (quando estiver pronto)
# git push origin main
```

---

## ⚠️ Notas Importantes

1. **Faça commits intermediários** após cada seção para facilitar rollback
2. **Teste localmente** antes de fazer push
3. **Verifique links** nos READMEs após reorganização
4. **Atualize caminhos** em notebooks que referenciam outros arquivos
5. **Verifique .gitignore** para garantir que dados grandes não sejam commitados

---

## 🔄 Rollback (Se Necessário)

Se precisar reverter as mudanças:

```bash
# Voltar para o branch de backup
git checkout backup-antes-reorganizacao

# Ou reverter commits específicos
git revert HEAD
```

---

## ✅ Verificação Final

Após reorganização, verificar:

```bash
# Estrutura de pastas
tree -L 2 -d

# Arquivos não rastreados
git status

# Links quebrados (verificar manualmente nos READMEs)
```

---

**Última atualização:** Janeiro 2025

