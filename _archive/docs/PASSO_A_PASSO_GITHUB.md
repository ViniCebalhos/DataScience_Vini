# 📖 Passo a Passo: Configurar GitHub do Zero

Este guia é um tutorial passo a passo detalhado para configurar seu portfólio no GitHub.

---

## 🎯 Pré-requisitos

- Conta no GitHub (crie em [github.com](https://github.com) se não tiver)
- Git instalado no seu computador
- Terminal/linha de comando acessível

---

## 📝 Passo 1: Verificar Instalação do Git

Abra o terminal e execute:

```bash
git --version
```

Se não estiver instalado:

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install git
```

**Verificar configuração:**
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

---

## 📝 Passo 2: Preparar o Repositório Local

### 2.1 Navegar até a pasta do portfólio

```bash
cd /home/vinicius/Projects/datascience
```

### 2.2 Verificar se já é um repositório Git

```bash
ls -la | grep .git
```

Se não aparecer `.git`, inicialize:

```bash
git init
```

### 2.3 Verificar status

```bash
git status
```

Você verá todos os arquivos que ainda não foram adicionados.

---

## 📝 Passo 3: Configurar .gitignore

O arquivo `.gitignore` já foi criado. Verifique se está presente:

```bash
cat .gitignore | head -20
```

Se estiver tudo certo, continue. Caso contrário, o arquivo já foi criado anteriormente.

---

## 📝 Passo 4: Fazer Primeiro Commit

### 4.1 Adicionar todos os arquivos

```bash
git add .
```

### 4.2 Verificar o que será commitado

```bash
git status
```

Você deve ver uma lista de arquivos em verde (staged).

### 4.3 Fazer o commit

```bash
git commit -m "feat: Portfólio completo de Ciência de Dados

- Trabalhos de Data Mining, Banco de Dados e Machine Learning
- 2 artigos científicos completos
- Competição Kaggle (F1-Score: 0.9991)
- Projeto completo de análise em saúde pública
- Documentação profissional"
```

**Dica:** Mensagens de commit descritivas são importantes!

---

## 📝 Passo 5: Criar Conta/Login no GitHub

1. Acesse [github.com](https://github.com)
2. Se não tem conta, clique em **"Sign up"**
3. Preencha os dados e crie a conta
4. Verifique seu email
5. Faça login

---

## 📝 Passo 6: Criar Novo Repositório no GitHub

### 6.1 Criar repositório

1. No canto superior direito, clique no **"+"** → **"New repository"**
2. Ou acesse diretamente: [github.com/new](https://github.com/new)

### 6.2 Configurar repositório

Preencha os campos:

- **Repository name:** `portfolio-ciencia-dados`
  - Use letras minúsculas e hífens
  - Nome descritivo e profissional

- **Description:** `Portfólio de trabalhos de Ciência de Dados - Pós-Graduação UTFPR. Inclui projetos de Data Mining, Banco de Dados, Machine Learning e análise em saúde pública.`

- **Visibility:**
  - ✅ **Public** (recomendado para portfólio)
  - ⚠️ **Private** (se preferir manter privado)

- **NÃO marque:**
  - ❌ "Add a README file" (já temos)
  - ❌ "Add .gitignore" (já temos)
  - ❌ "Choose a license" (pode adicionar depois)

### 6.3 Criar repositório

Clique em **"Create repository"**

---

## 📝 Passo 7: Conectar Repositório Local ao GitHub

Após criar o repositório, o GitHub mostrará instruções. Siga estas:

### 7.1 Adicionar remote

```bash
# Substitua SEU_USUARIO pelo seu username do GitHub
git remote add origin https://github.com/SEU_USUARIO/portfolio-ciencia-dados.git
```

**Exemplo:**
```bash
git remote add origin https://github.com/viniciuscebalhos/portfolio-ciencia-dados.git
```

### 7.2 Verificar remote

```bash
git remote -v
```

Deve mostrar:
```
origin  https://github.com/SEU_USUARIO/portfolio-ciencia-dados.git (fetch)
origin  https://github.com/SEU_USUARIO/portfolio-ciencia-dados.git (push)
```

### 7.3 Renomear branch principal

```bash
git branch -M main
```

### 7.4 Fazer push

```bash
git push -u origin main
```

**Nota:** Na primeira vez, o GitHub pedirá autenticação:
- Se usar HTTPS: pedirá username e token (não senha)
- Se usar SSH: configure chaves SSH primeiro

---

## 📝 Passo 8: Autenticação no GitHub

### Opção A: Usar Personal Access Token (HTTPS)

1. No GitHub, vá em **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Clique em **"Generate new token"**
3. Dê um nome (ex: "Portfolio Local")
4. Selecione escopos: `repo` (todos)
5. Clique em **"Generate token"**
6. **Copie o token** (só aparece uma vez!)
7. Quando o Git pedir senha, use o **token** (não sua senha do GitHub)

### Opção B: Configurar SSH (Recomendado para uso contínuo)

```bash
# Gerar chave SSH
ssh-keygen -t ed25519 -C "seu.email@exemplo.com"

# Copiar chave pública
cat ~/.ssh/id_ed25519.pub
```

1. Copie a chave gerada
2. No GitHub: **Settings** → **SSH and GPG keys** → **New SSH key**
3. Cole a chave e salve
4. Use URL SSH ao invés de HTTPS:
   ```bash
   git remote set-url origin git@github.com:SEU_USUARIO/portfolio-ciencia-dados.git
   ```

---

## 📝 Passo 9: Verificar Upload

1. Acesse seu repositório no GitHub: `https://github.com/SEU_USUARIO/portfolio-ciencia-dados`
2. Verifique se todos os arquivos estão lá
3. Verifique se o README.md está sendo exibido corretamente

---

## 📝 Passo 10: Melhorar o Repositório

### 10.1 Adicionar Description e Topics

1. No repositório, clique em **⚙️ Settings** (ou vá em **About**)
2. Adicione uma **description** mais detalhada
3. Adicione **Topics** (tags):
   - `data-science`
   - `machine-learning`
   - `python`
   - `jupyter-notebook`
   - `portfolio`
   - `postgresql`
   - `data-analysis`

### 10.2 Adicionar Badges ao README

Edite o `README.md` e adicione no topo:

```markdown
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
```

### 10.3 Fazer commit das melhorias

```bash
git add README.md
git commit -m "docs: Adicionar badges e melhorar README"
git push
```

---

## 📝 Passo 11: Configurar GitHub Pages (Opcional)

GitHub Pages permite criar um site para seu portfólio:

1. No repositório: **Settings** → **Pages**
2. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/ (root)`
3. Clique em **Save**
4. Aguarde alguns minutos
5. Seu site estará em: `https://SEU_USUARIO.github.io/portfolio-ciencia-dados/`

---

## 📝 Passo 12: Criar README no Perfil do GitHub

Crie um repositório especial com seu username do GitHub:

1. Crie novo repositório: `SEU_USUARIO` (exatamente seu username)
2. Adicione um `README.md` com:

```markdown
# Olá, eu sou [Seu Nome] 👋

## 🎓 Sobre Mim

Cientista de Dados em formação, especializando-me em Machine Learning, Análise de Dados e Banco de Dados.

## 📊 Portfólio

Confira meu portfólio completo: [portfolio-ciencia-dados](https://github.com/SEU_USUARIO/portfolio-ciencia-dados)

## 🛠️ Tecnologias

- Python
- SQL (PostgreSQL)
- Machine Learning
- Data Analysis

## 📈 Estatísticas GitHub

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=SEU_USUARIO&show_icons=true)
```

Este README aparecerá na página do seu perfil!

---

## 🔄 Comandos Git Úteis

### Ver status
```bash
git status
```

### Adicionar arquivos
```bash
git add .                    # Todos os arquivos
git add arquivo.py           # Arquivo específico
```

### Fazer commit
```bash
git commit -m "mensagem descritiva"
```

### Ver histórico
```bash
git log --oneline
```

### Fazer push
```bash
git push
```

### Atualizar do GitHub
```bash
git pull
```

### Ver diferenças
```bash
git diff
```

---

## 🐛 Solução de Problemas

### Erro: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/SEU_USUARIO/portfolio-ciencia-dados.git
```

### Erro: "failed to push"
```bash
# Verificar remote
git remote -v

# Forçar push (cuidado!)
git push -u origin main --force
```

### Erro de autenticação
- Use Personal Access Token ao invés de senha
- Ou configure SSH

---

## ✅ Checklist Final

- [ ] Git instalado e configurado
- [ ] Repositório local inicializado
- [ ] Primeiro commit feito
- [ ] Conta GitHub criada
- [ ] Repositório criado no GitHub
- [ ] Remote configurado
- [ ] Push realizado com sucesso
- [ ] README visível no GitHub
- [ ] Description e Topics adicionados
- [ ] Badges adicionados ao README

---

## 🎉 Pronto!

Seu portfólio está no GitHub! Agora:

1. Compartilhe o link no LinkedIn
2. Adicione ao seu currículo
3. Continue atualizando com novos projetos
4. Responda a issues (se houver)

**Boa sorte!** 🚀

---

**Dúvidas?** Consulte a [documentação oficial do GitHub](https://docs.github.com/)

