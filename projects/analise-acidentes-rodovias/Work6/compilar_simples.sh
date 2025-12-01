#!/bin/bash

# Script para compilar o artigo LaTeX simplificado
echo "🚀 Compilando artigo SBC (versão simplificada)..."
echo "================================================"

# Verificar se pdflatex está disponível
if ! command -v pdflatex &> /dev/null; then
    echo "❌ pdflatex não encontrado. Instalando..."
    sudo apt-get update
    sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-lang-portuguese
fi

# Compilar o LaTeX
echo "📝 Compilando LaTeX..."
pdflatex -interaction=nonstopmode artigo_sbc_simples.tex

if [ $? -eq 0 ]; then
    echo "✅ Compilação bem-sucedida!"
    echo "📄 PDF gerado: artigo_sbc_simples.pdf"
    
    # Mostrar informações do arquivo
    if [ -f "artigo_sbc_simples.pdf" ]; then
        echo ""
        echo "📊 Informações do arquivo:"
        ls -lh artigo_sbc_simples.pdf
        echo ""
        echo "🎉 Artigo pronto para uso!"
    fi
else
    echo "❌ Erro na compilação. Verifique os logs acima."
fi








