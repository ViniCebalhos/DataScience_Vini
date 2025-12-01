# 🔧 Comandos Git Essenciais para o Portfólio

Guia rápido de comandos Git mais usados para gerenciar seu portfólio.

---

## 📋 Comandos Básicos

### Verificar Status
```bash
git status
```
Mostra arquivos modificados, adicionados ou não rastreados.

### Adicionar Arquivos
```bash
git add .                    # Adiciona todos os arquivos
git add arquivo.py          # Adiciona arquivo específico
git add pasta/              # Adiciona pasta inteira
git add *.ipynb             # Adiciona todos os notebooks
```

### Fazer Commit
```bash
git commit -m "mensagem descritiva"
```

**Boas práticas de mensagens:**
```bash
git commit -m "feat: Adicionar análise de acidentes"
git commit -m "docs: Atualizar README do Work 6"
git commit -m "fix: Corrigir erro no notebook de clustering"
git commit -m "refactor: Reorganizar estrutura de pastas"
```

**Convenções:**
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Documentação
- `refactor:` - Refatoração de código
- `style:` - Formatação
- `test:` - Testes

### Ver Histórico
```bash
git log                     # Histórico completo
git log --oneline           # Histórico resumido (1 linha)
git log --graph             # Com gráfico de branches
git log -5                  # Últimos 5 commits
```

### Ver Diferenças
```bash
git diff                    # Diferenças não commitadas
git diff arquivo.py         # Diferenças em arquivo específico
git diff HEAD~1             # Diferenças com commit anterior
```

---

## 🔄 Trabalhando com GitHub

### Fazer Push
```bash
git push                    # Push para branch atual
git push origin main        # Push específico
git push -u origin main     # Primeira vez (configura upstream)
```

### Atualizar do GitHub
```bash
git pull                    # Atualizar do GitHub
git fetch                   # Buscar sem mesclar
git pull origin main        # Pull específico
```

### Verificar Remotes
```bash
git remote -v               # Listar remotes
git remote add origin URL   # Adicionar remote
git remote remove origin    # Remover remote
```

---

## 🌿 Trabalhando com Branches

### Criar e Mudar de Branch
```bash
git branch                  # Listar branches
git branch nova-branch      # Criar branch
git checkout nova-branch    # Mudar para branch
git checkout -b nova-branch # Criar e mudar
git switch nova-branch      # Mudar (Git 2.23+)
```

### Mesclar Branches
```bash
git merge outra-branch      # Mesclar branch atual
git merge --no-ff branch    # Mesclar sem fast-forward
```

### Deletar Branch
```bash
git branch -d branch        # Deletar local
git push origin --delete branch  # Deletar no GitHub
```

---

## 🔍 Buscar e Explorar

### Buscar no Histórico
```bash
git log --grep="palavra"    # Buscar por mensagem
git log --author="nome"     # Buscar por autor
git log --since="2024-01-01" # Desde data
git log --until="2024-12-31" # Até data
```

### Buscar no Código
```bash
git grep "palavra"         # Buscar no código
git grep -n "palavra"      # Com números de linha
git grep -i "palavra"      # Case insensitive
```

---

## ⚙️ Configuração

### Configurações Globais
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
git config --global init.defaultBranch main
```

### Ver Configurações
```bash
git config --list           # Todas as configurações
git config user.name        # Nome configurado
git config user.email       # Email configurado
```

### Editor Padrão
```bash
git config --global core.editor "nano"
git config --global core.editor "vim"
git config --global core.editor "code --wait"  # VS Code
```

---

## 🗂️ Gerenciar Arquivos

### Remover Arquivos
```bash
git rm arquivo.py           # Remover e fazer commit
git rm -r pasta/            # Remover pasta
git rm --cached arquivo     # Remover do Git mas manter local
```

### Renomear/Mover
```bash
git mv arquivo_antigo.py novo_nome.py
git mv arquivo.py pasta/arquivo.py
```

### Desfazer Mudanças
```bash
git restore arquivo.py      # Desfazer mudanças não commitadas
git restore --staged arquivo.py  # Remover do stage
git checkout -- arquivo.py # Desfazer (Git antigo)
```

---

## 📦 Trabalhar com Commits

### Modificar Último Commit
```bash
git commit --amend          # Modificar mensagem
git commit --amend --no-edit  # Adicionar arquivos ao último commit
```

### Desfazer Commit (mantendo mudanças)
```bash
git reset --soft HEAD~1     # Desfazer commit, manter mudanças staged
git reset --mixed HEAD~1    # Desfazer commit, manter mudanças não staged
git reset --hard HEAD~1     # Desfazer commit e mudanças (CUIDADO!)
```

### Ver Commit Específico
```bash
git show HEAD               # Último commit
git show HEAD~1             # Penúltimo commit
git show abc123             # Commit específico
```

---

## 🔐 Autenticação

### Configurar SSH
```bash
# Gerar chave SSH
ssh-keygen -t ed25519 -C "seu.email@exemplo.com"

# Copiar chave pública
cat ~/.ssh/id_ed25519.pub

# Testar conexão
ssh -T git@github.com
```

### Personal Access Token
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Selecionar escopos: `repo`
4. Copiar token
5. Usar token como senha ao fazer push

---

## 🚨 Situações Comuns

### Atualizar Repositório Local
```bash
git fetch origin
git merge origin/main
# ou
git pull origin main
```

### Resolver Conflitos
```bash
# Ver arquivos em conflito
git status

# Editar arquivos manualmente
# Depois:
git add arquivo_resolvido.py
git commit -m "fix: Resolver conflitos"
```

### Descartar Mudanças Locais
```bash
git checkout -- arquivo.py  # Descartar mudanças
git reset --hard HEAD       # Descartar todas (CUIDADO!)
```

### Limpar Arquivos Não Rastreados
```bash
git clean -n                # Ver o que será removido (dry-run)
git clean -f                # Remover arquivos
git clean -fd               # Remover arquivos e pastas
```

---

## 📊 Estatísticas e Informações

### Estatísticas do Repositório
```bash
git shortlog -sn            # Commits por autor
git log --stat              # Estatísticas de commits
git diff --stat             # Estatísticas de mudanças
```

### Tamanho do Repositório
```bash
du -sh .git                 # Tamanho do .git
git count-objects -vH       # Detalhes dos objetos
```

---

## 🎯 Workflow Recomendado para Portfólio

### 1. Antes de Trabalhar
```bash
git pull                    # Atualizar do GitHub
git status                  # Verificar status
```

### 2. Fazer Mudanças
```bash
# Trabalhar nos arquivos...
```

### 3. Adicionar e Commitar
```bash
git add .
git commit -m "feat: Descrição clara das mudanças"
```

### 4. Publicar
```bash
git push
```

### 5. Verificar
```bash
# Acessar GitHub e verificar se está tudo certo
```

---

## 💡 Dicas

1. **Commite frequentemente** - Commits pequenos e frequentes são melhores
2. **Mensagens descritivas** - Explique o que e por quê
3. **Pull antes de Push** - Sempre atualize antes de publicar
4. **Use branches** - Para experimentos ou features grandes
5. **Não commite dados grandes** - Use .gitignore

---

## 📚 Recursos

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials)

---

**Última atualização:** 2025

