# 🚀 Guia Completo: Configurar Sincronização Automática com GitHub Actions

Este guia vai te ajudar a configurar a sincronização automática entre o repositório privado e o público usando GitHub Actions.

## 📋 O que é GitHub Actions?

GitHub Actions é uma ferramenta que permite automatizar tarefas no GitHub. Neste caso, vamos usar para sincronizar automaticamente a branch `main` do repositório privado para o repositório público sempre que você fizer push.

## 🎯 O que vamos fazer?

1. Criar um **Personal Access Token (PAT)** no GitHub
2. Adicionar esse token como **Secret** no repositório privado
3. O workflow vai executar automaticamente quando você fizer push na `main`

## 📝 Passo a Passo Detalhado

### Passo 1: Criar um Personal Access Token (PAT)

1. **Acesse as configurações do GitHub:**
   - Clique na sua foto de perfil (canto superior direito)
   - Clique em **Settings** (Configurações)
   - Ou acesse diretamente: https://github.com/settings/profile

2. **Navegue até Developer settings:**
   - No menu lateral esquerdo, role até o final
   - Clique em **Developer settings**
   - Ou acesse diretamente: https://github.com/settings/apps

3. **Acesse Personal access tokens:**
   - Clique em **Tokens (classic)**
   - Ou acesse diretamente: https://github.com/settings/tokens

4. **Criar novo token:**
   - Clique em **Generate new token** → **Generate new token (classic)**
   - Dê um nome descritivo: `DataScience_Vini-Sync` ou `Portfolio-Sync`
   - Selecione a validade:
     - **90 days** (recomendado para começar)
     - Ou **No expiration** (se preferir não renovar)

5. **Selecionar permissões (scopes):**
   
   Marque **APENAS** a seguinte permissão:
   - ✅ **repo** (acesso completo aos repositórios)
     - Isso inclui automaticamente todas as sub-permissões necessárias
     - ⚠️ **NÃO** marque outras permissões desnecessárias por segurança

6. **Gerar o token:**
   - Role até o final e clique em **Generate token**
   - ⚠️ **IMPORTANTE:** Copie o token imediatamente! Você não poderá vê-lo novamente.
   - O token será algo como: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - 💡 **Dica:** Cole em um editor de texto temporário para não perder

### Passo 2: Adicionar o Token como Secret no Repositório Privado

1. **Acesse o repositório privado:**
   - Vá para: https://github.com/ViniCebalhos/ciencia_de_dados

2. **Acesse as configurações do repositório:**
   - Clique na aba **Settings** (no topo do repositório, ao lado de "Code", "Issues", etc.)

3. **Navegue até Secrets:**
   - No menu lateral esquerdo, clique em **Secrets and variables** → **Actions**
   - Ou acesse diretamente: https://github.com/ViniCebalhos/ciencia_de_dados/settings/secrets/actions

4. **Criar novo secret:**
   - Clique no botão **New repository secret** (canto superior direito)
   - **Name:** Digite exatamente: `PUBLIC_REPO_TOKEN`
     - ⚠️ O nome deve ser exatamente este (case-sensitive)
   - **Secret:** Cole o token que você copiou no Passo 1
   - Clique em **Add secret**

5. **Verificar:**
   - Você deve ver o secret `PUBLIC_REPO_TOKEN` listado
   - ✅ Pronto! O token está configurado

### Passo 3: Verificar se o Workflow está Configurado

O arquivo `.github/workflows/sync-to-public.yml` já está criado e configurado. Ele vai:
- ✅ Executar automaticamente quando você fizer push na branch `main`
- ✅ Sincronizar apenas a branch `main` para o repositório público
- ✅ Permitir execução manual pela interface do GitHub (workflow_dispatch)

### Passo 4: Testar a Configuração

1. **Fazer um commit de teste na main:**
   ```bash
   git checkout main
   # Faça uma pequena alteração (ex: atualize o README)
   echo "# Teste de sincronização automática" >> README.md
   git add README.md
   git commit -m "test: verificar sincronização automática"
   git push origin main
   ```

2. **Verificar se o workflow executou:**
   - Acesse: https://github.com/ViniCebalhos/ciencia_de_dados/actions
   - Você deve ver um workflow chamado **"Sincronizar para Repositório Público"** em execução
   - Clique nele para ver os logs em tempo real
   - ✅ Se aparecer um ✅ verde, funcionou!

3. **Verificar o repositório público:**
   - Acesse: https://github.com/ViniCebalhos/DataScience_Vini
   - Verifique se o commit apareceu automaticamente
   - Compare os commits entre os dois repositórios

## 🔍 Como Verificar se Está Funcionando

### Ver logs do workflow:
1. Acesse: https://github.com/ViniCebalhos/ciencia_de_dados/actions
2. Clique no workflow mais recente (deve ter um ícone de relógio ⏱️ ou check ✅)
3. Clique no job "sync"
4. Expanda cada step para ver os logs detalhados

### Verificar sincronização:
- Compare os commits entre os dois repositórios
- O repositório público deve ter os mesmos commits da `main` privada
- Os timestamps devem ser muito próximos (alguns segundos de diferença)

### Executar manualmente (se necessário):
1. Acesse: https://github.com/ViniCebalhos/ciencia_de_dados/actions
2. Clique em **"Sincronizar para Repositório Público"** no menu lateral
3. Clique em **"Run workflow"** (botão no canto superior direito)
4. Selecione a branch `main` e clique em **"Run workflow"**

## ⚠️ Troubleshooting (Solução de Problemas)

### ❌ Workflow não executa:
- ✅ Verifique se o arquivo `.github/workflows/sync-to-public.yml` está na branch `main`
- ✅ Verifique se o nome do repositório no workflow está correto: `ViniCebalhos/ciencia_de_dados`
- ✅ Verifique se você fez push na branch `main` (não em outras branches)

### ❌ Erro de autenticação:
- ✅ Verifique se o secret `PUBLIC_REPO_TOKEN` está configurado corretamente
- ✅ Verifique se o nome do secret está exatamente `PUBLIC_REPO_TOKEN` (case-sensitive)
- ✅ Verifique se o token tem permissões de `repo`
- ✅ Gere um novo token se necessário

### ❌ Erro "repository not found":
- ✅ Verifique se o nome do repositório público no workflow está correto: `ViniCebalhos/DataScience_Vini`
- ✅ Verifique se o token tem acesso ao repositório público
- ✅ Verifique se o repositório público existe e você tem acesso

### ❌ Erro "refusing to allow a Personal Access Token":
- ✅ O token precisa ter permissão `repo` completa
- ✅ Gere um novo token com todas as permissões de `repo`

### ❌ Workflow executa mas não sincroniza:
- ✅ Verifique os logs do workflow para ver mensagens de erro específicas
- ✅ Verifique se o repositório público está acessível
- ✅ Tente executar manualmente pelo workflow_dispatch

## 🔒 Segurança

- ⚠️ **Nunca** compartilhe seu token publicamente
- ⚠️ **Nunca** commite o token no código
- ⚠️ **Nunca** coloque o token em mensagens de commit
- ✅ O token está seguro como Secret do GitHub (criptografado)
- ✅ Apenas workflows autorizados podem acessar os secrets
- ✅ Você pode revogar o token a qualquer momento nas configurações

## 📚 Recursos Adicionais

- [Documentação do GitHub Actions](https://docs.github.com/en/actions)
- [Criar Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Secrets do GitHub Actions](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## 🎉 Pronto!

Depois de configurar, toda vez que você fizer push na `main` do repositório privado, o repositório público será atualizado automaticamente em alguns segundos!

### Resumo do que acontece:
1. Você faz push na `main` do repositório privado
2. GitHub Actions detecta o push
3. O workflow executa automaticamente
4. O código é sincronizado para o repositório público
5. ✅ Pronto! Seu portfólio está atualizado

### Dúvidas?
Se tiver algum problema, verifique:
1. Os logs do workflow em: https://github.com/ViniCebalhos/ciencia_de_dados/actions
2. Se o secret está configurado corretamente
3. Se o token tem as permissões corretas
