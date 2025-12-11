# 🔧 Comandos de Reorganização do Repositório

**Autor:** Vinícius de Souza Cebalhos  
**Data:** Janeiro 2025  
**Objetivo:** Comandos práticos para reorganizar o repositório

---

## ⚠️ IMPORTANTE: Antes de Executar

1. **Faça backup do repositório:**
```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados
git status
git branch backup-antes-reorganizacao
```

2. **Verifique se está em um branch limpo:**
```bash
git status
# Se houver mudanças não commitadas, faça commit ou stash
```

3. **Execute os comandos em ordem**

---

## 📋 1. REMOVER SUBPASTAS DESNECESSÁRIAS EM projects/

### 1.1 Analise Acidentes Rodovias

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/projects/analise-acidentes-rodovias

# Verificar conteúdo de Work6
ls -la Work6/

# Mover conteúdo para raiz
cd Work6
git mv * ../
git mv .* .. 2>/dev/null || true
cd ..

# Remover pasta vazia
rmdir Work6

# Verificar resultado
ls -la
```

### 1.2 Analise Espacial Acidentes

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/projects/analise-espacial-acidentes

# Verificar conteúdo de Work8
ls -la Work8/

# Mover conteúdo para raiz
cd Work8
git mv * ../
git mv .* .. 2>/dev/null || true
cd ..

# Remover pasta vazia
rmdir Work8

# Verificar resultado
ls -la
```

### 1.3 Classificacao Sinais Vitais

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/projects/classificacao-sinais-vitais

# Verificar conteúdo de Work3
ls -la Work3/

# Mover conteúdo para raiz
cd Work3
git mv * ../
git mv .* .. 2>/dev/null || true
cd ..

# Remover pasta vazia
rmdir Work3

# Verificar resultado
ls -la
```

### 1.4 Competicao Kaggle

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/projects/competicao-kaggle-venues

# Verificar conteúdo de challenge
ls -la challenge/

# Mover conteúdo para raiz
cd challenge
git mv * ../
git mv .* .. 2>/dev/null || true
cd ..

# Remover pasta vazia
rmdir challenge

# Verificar resultado
ls -la
```

---

## 🧹 2. LIMPAR NOTEBOOKS DUPLICADOS

### 2.1 Analise E-Saude Curitiba

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/projects/analise-esaude-curitiba

# Verificar notebooks e datas de modificação
ls -lt *.ipynb

# Decisão: Manter analise_completa_temporal.ipynb como principal
# Se analise_completa_temporal2.ipynb for mais recente e completo:
# git mv analise_completa_temporal2.ipynb analise_completa_temporal.ipynb

# Remover notebooks de teste/duplicados
git rm teste.ipynb Teste2.ipynb final.ipynb limpeza_dados2.ipynb 2>/dev/null || echo "Alguns arquivos podem não existir"

# Verificar resultado
ls -la *.ipynb
```

### 2.2 Competicao Kaggle

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/projects/competicao-kaggle-venues

# Verificar notebooks e datas de modificação
ls -lt *.ipynb

# Decisão: Manter challenge_final.ipynb como principal (ou o mais completo)
# Se houver múltiplos, verificar qual é o mais completo:
# jupyter nbconvert --to script challenge_final.ipynb --stdout | wc -l
# jupyter nbconvert --to script challenge.ipynb --stdout | wc -l

# Remover notebooks duplicados (após verificação)
# git rm challenge.ipynb final.ipynb final2.ipynb 2>/dev/null || echo "Alguns arquivos podem não existir"

# Verificar resultado
ls -la *.ipynb
```

---

## 📁 3. REORGANIZAR DATA MINING

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/data-mining

# Renomear Aula3 para nome mais descritivo
if [ -d "Aula3" ]; then
    git mv Aula3 conceitos-fundamentais
    echo "Aula3 renomeado para conceitos-fundamentais"
fi

# Verificar resultado
ls -la
```

---

## 🧹 4. LIMPAR MACHINE LEARNING

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados/machine-learning

# Verificar se Work2 é duplicado de classificacao-indicadores
if [ -d "Work2" ] && [ -d "classificacao-indicadores" ]; then
    echo "Work2 encontrado. Verificar se é duplicado antes de remover:"
    echo "Conteúdo de Work2:"
    ls -la Work2/
    echo ""
    echo "Conteúdo de classificacao-indicadores:"
    ls -la classificacao-indicadores/
    echo ""
    echo "Se Work2 for duplicado, execute:"
    echo "git rm -r Work2"
fi
```

---

## 🗑️ 5. LIMPAR ARQUIVOS TEMPORÁRIOS

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados

# Remover checkpoints do Jupyter
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null
echo "Checkpoints do Jupyter removidos"

# Remover arquivos LaTeX temporários
find . -name "*.aux" -delete
find . -name "*.log" -delete
find . -name "*.out" -delete
find . -name "*.synctex.gz" -delete
find . -name "*.fdb_latexmk" -delete
find . -name "*.fls" -delete
echo "Arquivos LaTeX temporários removidos"
```

---

## 🔒 6. VERIFICAR DADOS SENSÍVEIS

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados

# Verificar arquivos com possíveis API keys
echo "=== Verificando possíveis API keys ==="
grep -r "api_key\|API_KEY\|secret\|SECRET" --include="*.txt" --include="*.py" --include="*.ipynb" . | grep -v ".git" | grep -v "placeholder\|exemplo\|example" || echo "Nenhum arquivo com API keys encontrado"

# Verificar arquivos .env
echo ""
echo "=== Verificando arquivos .env ==="
find . -name ".env" -o -name "*.env" | grep -v ".git" || echo "Nenhum arquivo .env encontrado"

# Verificar preparar_postos_prf_banco.py
echo ""
echo "=== Verificando preparar_postos_prf_banco.py ==="
grep -n "password\|senha" projects/analise-espacial-acidentes/preparar_postos_prf_banco.py || echo "Arquivo não encontrado"
```

---

## 📝 7. COMMITS SUGERIDOS

Após executar cada seção, faça commits descritivos:

```bash
# Commit 1: Remover subpastas
git add projects/
git commit -m "refactor(estrutura): remover subpastas desnecessárias em projects/

- Remover Work6/ de analise-acidentes-rodovias
- Remover Work8/ de analise-espacial-acidentes
- Remover Work3/ de classificacao-sinais-vitais
- Remover challenge/ de competicao-kaggle-venues"

# Commit 2: Limpar notebooks duplicados
git add projects/
git commit -m "chore(notebooks): limpar notebooks duplicados

- Consolidar notebooks em analise-esaude-curitiba
- Remover versões de teste e duplicadas
- Manter apenas versões principais e completas"

# Commit 3: Reorganizar data-mining
git add data-mining/
git commit -m "refactor(data-mining): renomear Aula3 para conceitos-fundamentais

- Melhorar nomenclatura descritiva
- Padronizar nomes de pastas"

# Commit 4: Limpar arquivos temporários
git add .
git commit -m "chore(limpeza): remover arquivos temporários

- Remover .ipynb_checkpoints
- Remover arquivos LaTeX temporários (*.aux, *.log, *.out)"
```

---

## ✅ 8. VERIFICAÇÃO FINAL

```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados

# Verificar estrutura final
echo "=== Estrutura de projects/ ==="
tree -L 2 projects/ || find projects/ -maxdepth 2 -type d

# Verificar se há subpastas desnecessárias
echo ""
echo "=== Verificando subpastas desnecessárias ==="
find projects/ -type d -name "Work*" -o -name "challenge" | grep -v ".git" || echo "Nenhuma subpasta desnecessária encontrada"

# Verificar notebooks duplicados
echo ""
echo "=== Verificando notebooks duplicados ==="
find projects/ -name "*teste*.ipynb" -o -name "*Teste*.ipynb" -o -name "*final*.ipynb" | grep -v ".git" || echo "Nenhum notebook duplicado encontrado"

# Verificar status do git
echo ""
echo "=== Status do Git ==="
git status
```

---

## 🚨 TROUBLESHOOTING

### Erro: "fatal: not a git repository"
```bash
cd /home/vinicius/Projects/11111/ciencia_de_dados
git init  # Apenas se não for um repositório git ainda
```

### Erro: "fatal: pathspec did not match any files"
- O arquivo pode não existir ou já ter sido removido
- Verifique com `ls -la` antes de executar `git mv` ou `git rm`

### Erro ao remover pasta não vazia
```bash
# Se rmdir falhar, verifique se há arquivos ocultos
ls -la pasta/
# Remova manualmente arquivos restantes
```

### Reverter mudanças
```bash
# Se precisar reverter um commit
git log --oneline -5
git revert <hash-do-commit>

# Se precisar voltar ao estado anterior
git reset --hard backup-antes-reorganizacao
```

---

**Última atualização:** Janeiro 2025

