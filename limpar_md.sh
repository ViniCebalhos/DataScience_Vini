#!/bin/bash
# Script para limpar arquivos .md da raiz, movendo documentos internos para _archive/docs/

cd /home/vinicius/Projects/11111/ciencia_de_dados

echo "🧹 Limpando arquivos .md da raiz..."

# Garantir que _archive/docs/ existe
mkdir -p _archive/docs

# Lista de arquivos para mover (documentos internos)
ARQUIVOS_PARA_MOVER=(
    "ANALISE_CRITICA_COMPLETA.md"
    "ANALISE_E_REESTRUTURACAO.md"
    "COMANDOS_REORGANIZACAO.md"
    "CHECKLIST_FINAL_PUBLICACAO.md"
    "RESUMO_EXECUTIVO.md"
    "RESUMO_EXECUTIVO_REVISAO.md"
    "RESUMO_LIMPEZA_DOCUMENTACAO.md"
    "RESUMO_REORGANIZACAO_COMPLETA.md"
    "INDICE_DOCUMENTACAO.md"
    "TEXTOS_LINKEDIN_PORTFOLIO.md"
    "ENTREGAVEIS_REVISAO.md"
    "LIMPEZA_ARQUIVOS_MD.md"
)

# Mover arquivos
for arquivo in "${ARQUIVOS_PARA_MOVER[@]}"; do
    if [ -f "$arquivo" ]; then
        echo "📦 Movendo $arquivo para _archive/docs/"
        git mv "$arquivo" _archive/docs/ 2>/dev/null || mv "$arquivo" _archive/docs/
    else
        echo "⚠️  Arquivo $arquivo não encontrado (pode já ter sido movido)"
    fi
done

echo ""
echo "✅ Limpeza concluída!"
echo ""
echo "📊 Arquivos .md restantes na raiz:"
ls -1 *.md 2>/dev/null || echo "Nenhum arquivo .md encontrado (além do README.md que deve ser mantido)"

echo ""
echo "📁 Arquivos movidos para _archive/docs/:"
ls -1 _archive/docs/*.md 2>/dev/null | wc -l | xargs echo "Total:"

echo ""
echo "💡 Próximo passo:"
echo "   git commit -m 'docs(organizacao): mover documentos internos para _archive/docs/'"

