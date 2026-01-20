#  Configuração de Repositórios: Privado (Dev) e Público (Portfólio)

##  Estrutura Proposta

### Repositório Privado (Atual)
- **Nome:** `ciencia_de_dados` (ou `ciencia_de_dados-dev`)
- **Visibilidade:**  Privado
- **Branches:** `dev`, `main`, `backup-antes-reorganizacao`, e outras branches de desenvolvimento
- **Uso:** Desenvolvimento, experimentos, trabalho em progresso

### Repositório Público (Novo)
- **Nome:** `DataScience_Vini`
- **URL:** https://github.com/ViniCebalhos/DataScience_Vini
- **Visibilidade:**  Público
- **Branches:** Apenas `main` (produção)
- **Uso:** Portfólio público, projetos finalizados

##  Passo a Passo

### 1. Criar o Repositório Público no GitHub

1. Acesse: https://github.com/new
2. **Nome:** `ciencia_de_dados` (ou outro nome)
3. **Visibilidade:**  Public
4. **NÃO inicialize** com README, .gitignore ou license
5. Clique em "Create repository"

### 2. Configurar Remotes Locais

Após criar o repositório público, execute:

```bash
# Adicionar o repositório público como 'public'
git remote add public git@github.com:ViniCebalhos/DataScience_Vini.git

# Verificar remotes
git remote -v
```

### 3. Sincronizar Branch Main para o Repositório Público

```bash
# Garantir que está na branch main e atualizada
git checkout main
git pull origin main

# Fazer push apenas da main para o repositório público
git push public main
```

### 4. Configurar Sincronização Automática (Opcional)

Use o script `sync-to-public.sh` para sincronizar automaticamente.

##  Workflow de Trabalho

### Desenvolvimento Normal (Privado)
```bash
# Trabalhar na branch dev (privada)
git checkout dev
# ... fazer commits ...
git push origin dev
```

### Publicar no Portfólio (Público)
```bash
# Quando quiser atualizar o portfólio público:
git checkout main
git merge dev  # ou fazer merge via PR
git push origin main      # Atualiza repositório privado
git push public main      # Atualiza repositório público
```

##  Sincronização Automática

Execute o script `sync-to-public.sh` sempre que quiser sincronizar:

```bash
./sync-to-public.sh
```

Ou adicione um alias:
```bash
git config alias.sync-public '!./sync-to-public.sh'
git sync-public
```

##  Importante

- **Nunca** faça push da branch `dev` para o repositório público
- **Sempre** revise o que está na `main` antes de sincronizar
- Use **tags** para marcar versões públicas importantes
- Considere usar **GitHub Actions** para automatizar a sincronização

##  Tags e Releases

Para marcar versões importantes no repositório público:

```bash
git tag -a v1.0.0 -m "Primeira versão pública do portfólio"
git push public v1.0.0
```
