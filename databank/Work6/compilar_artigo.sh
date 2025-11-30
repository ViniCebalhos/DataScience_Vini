#!/bin/bash

# Script para compilar o artigo LaTeX e gerar o PDF
# Autor: Vinícius de Souza Cebalhos

echo "🚀 Iniciando compilação do artigo SBC..."
echo "================================================"

# Verificar se o LaTeX está instalado
if ! command -v pdflatex &> /dev/null; then
    echo "❌ Erro: pdflatex não está instalado!"
    echo "Instale o LaTeX com: sudo apt-get install texlive-full"
    exit 1
fi

# Verificar se os arquivos necessários existem
if [ ! -f "artigo_sbc.tex" ]; then
    echo "❌ Erro: arquivo artigo_sbc.tex não encontrado!"
    exit 1
fi

if [ ! -f "acidentes_por_mes.png" ]; then
    echo "❌ Erro: arquivo acidentes_por_mes.png não encontrado!"
    exit 1
fi

if [ ! -f "causas_acidentes.png" ]; then
    echo "❌ Erro: arquivo causas_acidentes.png não encontrado!"
    exit 1
fi

if [ ! -f "acidentes_por_hora.png" ]; then
    echo "❌ Erro: arquivo acidentes_por_hora.png não encontrado!"
    exit 1
fi

echo "✅ Todos os arquivos necessários encontrados!"

# Compilar o LaTeX (primeira passagem)
echo "📝 Compilando LaTeX (primeira passagem)..."
pdflatex -interaction=nonstopmode artigo_sbc.tex

if [ $? -ne 0 ]; then
    echo "❌ Erro na primeira compilação!"
    exit 1
fi

# Compilar o LaTeX (segunda passagem para referências)
echo "📝 Compilando LaTeX (segunda passagem)..."
pdflatex -interaction=nonstopmode artigo_sbc.tex

if [ $? -ne 0 ]; then
    echo "❌ Erro na segunda compilação!"
    exit 1
fi

# Verificar se o PDF foi gerado
if [ -f "artigo_sbc.pdf" ]; then
    echo "✅ PDF gerado com sucesso: artigo_sbc.pdf"
    
    # Mostrar informações do arquivo
    echo ""
    echo "📊 Informações do arquivo:"
    ls -lh artigo_sbc.pdf
    
    echo ""
    echo "🎉 Compilação concluída com sucesso!"
    echo "📄 O arquivo artigo_sbc.pdf está pronto para uso!"
    
    # Limpar arquivos auxiliares (opcional)
    echo ""
    read -p "🧹 Deseja limpar os arquivos auxiliares? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -f *.aux *.log *.out *.toc *.fdb_latexmk *.fls *.synctex.gz
        echo "✅ Arquivos auxiliares removidos!"
    fi
    
else
    echo "❌ Erro: PDF não foi gerado!"
    exit 1
fi

echo ""
echo "================================================"
echo "✅ Processo de compilação finalizado!"








