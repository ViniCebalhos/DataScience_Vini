#!/bin/bash

# Script para sincronizar a branch main do repositório privado para o público
# Uso: ./sync-to-public.sh

set -e  # Parar em caso de erro

echo "🔄 Sincronizando repositório privado → público..."

# Verificar se o remote 'public' existe
if ! git remote | grep -q "^public$"; then
    echo "❌ Erro: Remote 'public' não encontrado!"
    echo "💡 Execute: git remote add public <url-do-repositorio-publico>"
    exit 1
fi

# Verificar se estamos em uma branch válida
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "⚠️  Você está na branch '$CURRENT_BRANCH'"
    read -p "Deseja continuar mesmo assim? (s/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        echo "❌ Operação cancelada."
        exit 1
    fi
fi

# Atualizar branch main do repositório privado
echo "📥 Atualizando branch main do repositório privado..."
git fetch origin main

# Verificar se há mudanças locais não commitadas
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  Você tem mudanças não commitadas!"
    read -p "Deseja continuar mesmo assim? (s/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        echo "❌ Operação cancelada. Faça commit ou stash das mudanças primeiro."
        exit 1
    fi
fi

# Garantir que estamos na main e atualizada
echo "🔀 Mudando para branch main..."
git checkout main
git pull origin main

# Fazer push para o repositório público
echo "📤 Enviando para repositório público..."
git push public main

echo "✅ Sincronização concluída!"
echo "🌐 Repositório público atualizado: $(git remote get-url public)"
