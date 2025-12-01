# 📄 Compilação do Artigo SBC - LaTeX

## 🎯 Arquivos Gerados

Este diretório contém todos os arquivos necessários para gerar o PDF do artigo SBC:

### 📝 Documentos LaTeX
- **`artigo_sbc.tex`** - Arquivo principal do artigo em LaTeX
- **`compilar_artigo.sh`** - Script para compilação automática

### 📊 Figuras e Tabelas
- **`acidentes_por_mes.png`** - Gráfico de acidentes por mês
- **`causas_acidentes.png`** - Gráfico de causas de acidentes  
- **`acidentes_por_hora.png`** - Gráfico de acidentes por hora
- **`tabela_acidentes_por_mes.csv`** - Dados mensais
- **`tabela_causas_acidentes.csv`** - Dados de causas

### 📋 Documentos de Apoio
- **`artigo_sbc_acidentes_rodovias.md`** - Artigo em Markdown
- **`tabelas_artigo.md`** - Tabelas formatadas
- **`guia_visualizacao.md`** - Guia do tema visual

## 🚀 Como Compilar

### Opção 1: Compilação Automática (Recomendada)
```bash
# Tornar o script executável
chmod +x compilar_artigo.sh

# Executar a compilação
./compilar_artigo.sh
```

### Opção 2: Compilação Manual
```bash
# Primeira compilação
pdflatex artigo_sbc.tex

# Segunda compilação (para referências)
pdflatex artigo_sbc.tex
```

## 📦 Pré-requisitos

### Instalação do LaTeX (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install texlive-latex-extra texlive-fonts-recommended texlive-lang-portuguese
```

### Instalação do LaTeX (Ubuntu/Debian - Completa)
```bash
sudo apt-get install texlive-full
```

### Instalação do LaTeX (macOS)
```bash
brew install --cask mactex
```

### Instalação do LaTeX (Windows)
1. Baixe o MiKTeX: https://miktex.org/download
2. Instale o pacote completo
3. Use o TeXworks ou editor similar

## 📊 Estrutura do Artigo

O artigo LaTeX inclui:

1. **Cabeçalho SBC** - Título, autor, resumo
2. **Introdução** - Contextualização do problema
3. **Trabalhos Relacionados** - 4 referências acadêmicas
4. **Descrição e Análise dos Dados** - Metodologia e resultados
5. **Tabelas** - Dados formatados em tabelas LaTeX
6. **Figuras** - 3 gráficos profissionais incluídos
7. **Conclusão** - Síntese e recomendações
8. **Referências** - Bibliografia formatada

## 🎨 Características Visuais

- **Formatação SBC** - Padrão acadêmico brasileiro
- **Figuras Profissionais** - Gráficos com tema unificado
- **Tabelas Formatadas** - Dados organizados e legíveis
- **Tipografia** - Fonte adequada para impressão
- **Cores** - Paleta profissional (azul, rosa, laranja)

## 📈 Dados Incluídos

### Estatísticas Principais
- **Total de Acidentes**: 67.794
- **Média Mensal**: 5.649,5 acidentes
- **Picos Sazonais**: Dez (6.587), Out (6.406), Jul (6.401)
- **Horário Crítico**: 17h-19h
- **Principais Causas**: Reação tardia (27,3%), Ausência de reação (22,4%), Desatenção (18,9%)

### Visualizações
1. **Gráfico de Barras** - Acidentes por mês
2. **Gráfico Horizontal** - Principais causas
3. **Gráfico de Linha** - Distribuição por hora

## 🔧 Solução de Problemas

### Erro: "pdflatex não encontrado"
```bash
sudo apt-get install texlive-latex-extra
```

### Erro: "Figura não encontrada"
- Verifique se os arquivos PNG estão no mesmo diretório
- Execute o script `anexos.py` para gerar as figuras

### Erro: "Caracteres especiais"
```bash
sudo apt-get install texlive-lang-portuguese
```

### Erro: "Fonte não encontrada"
```bash
sudo apt-get install texlive-fonts-recommended
```

## 📄 Resultado Final

Após a compilação bem-sucedida, você terá:
- **`artigo_sbc.pdf`** - Artigo completo em PDF
- **4 páginas** - Conforme limite SBC
- **Alta qualidade** - Pronto para submissão
- **Formatação profissional** - Padrão acadêmico

## 🎯 Próximos Passos

1. **Revisar o PDF** - Verificar formatação e conteúdo
2. **Ajustar se necessário** - Modificar o arquivo .tex
3. **Recompilar** - Executar novamente o script
4. **Submeter** - Enviar para conferência/revista

## 📞 Suporte

Para dúvidas ou problemas:
- Verifique os logs de compilação
- Consulte a documentação do LaTeX
- Execute o script de diagnóstico

---

**Desenvolvido por**: Vinícius de Souza Cebalhos  
**Data**: Outubro 2025  
**Versão**: 1.0








