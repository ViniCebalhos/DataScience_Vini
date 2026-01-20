#  Artigo Científico - Análise de Acidentes em Rodovias Federais

**Título:** Análise de Acidentes em Rodovias Federais Brasileiras com Dados da PRF: Um Estudo Exploratório

---

##  Sobre o Projeto

Artigo científico completo sobre análise de acidentes de trânsito em rodovias federais brasileiras, utilizando dados da Polícia Rodoviária Federal (PRF).

---

##  Resultados Principais

### Estatísticas
- **Total de Acidentes Analisados:** 67.794
- **Média Mensal:** 5.649,5 acidentes
- **Desvio Padrão:** 594,1 acidentes

### Padrões Temporais
- **Picos Mensais:**
 - Dezembro: 6.587 acidentes
 - Outubro: 6.406 acidentes
 - Julho: 6.401 acidentes

- **Horário Crítico:** 17h-19h (coincide com horários de pico de tráfego)

### Principais Causas
1. **Reação tardia:** 18.500 casos (27,3%)
2. **Ausência de reação:** 15.200 casos (22,4%)
3. **Desatenção:** 12.800 casos (18,9%)

**Total das 3 principais causas:** 68,6% do total de acidentes

---

##  Metodologia

### 1. Fonte dos Dados
- Dados da Polícia Rodoviária Federal (PRF)
- Formato CSV processado e inserido em PostgreSQL
- Tabela: `especializacao_vinicius_acidentes`

### 2. Análises Realizadas
- Consultas SQL para agregações
- Análise exploratória com Python
- Visualizações profissionais
- Estatísticas descritivas

### 3. Visualizações Geradas
- Gráfico de barras: Acidentes por mês
- Gráfico horizontal: Principais causas
- Gráfico de linha: Distribuição por hora

---

##  Arquivos

### Artigo
- `artigo_sbc_simples.tex` - Código LaTeX do artigo
- `artigo_sbc_simples.pdf` - Artigo compilado em PDF
- `artigo_sbc.tex` - Versão alternativa

### Scripts
- `anexos.py` - Script para gerar visualizações
- `compilar_simples.sh` - Script de compilação automática
- `compilar_artigo.sh` - Script alternativo

### Visualizações
- `acidentes_por_mes.png` - Gráfico de acidentes por mês
- `causas_acidentes.png` - Gráfico de principais causas
- `acidentes_por_hora.png` - Gráfico de distribuição horária

### Dados
- `tabela_acidentes_por_mes.csv` - Dados mensais
- `tabela_causas_acidentes.csv` - Dados de causas
- `estatisticas_descritivas.txt` - Estatísticas geradas

### Documentação
- `README_compilacao.md` - Guia completo de compilação
- `guia_visualizacao.md` - Guia do tema visual
- `tabelas_artigo.md` - Tabelas formatadas

---

##  Como Compilar o Artigo

### Opção 1: Compilação Automática (Recomendada)
```bash
chmod +x compilar_simples.sh
./compilar_simples.sh
```

### Opção 2: Compilação Manual
```bash
pdflatex artigo_sbc_simples.tex
pdflatex artigo_sbc_simples.tex  # Segunda compilação para referências
```

### Pré-requisitos
```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-extra texlive-fonts-recommended texlive-lang-portuguese
```

---

##  Estrutura do Artigo

1. **Resumo** - Objetivo, metodologia e principais achados
2. **Introdução** - Contextualização do problema
3. **Trabalhos Relacionados** - 4 referências acadêmicas
4. **Descrição e Análise dos Dados**
 - Fonte dos dados
 - Estrutura da tabela
 - Qualidade dos dados
 - Análises realizadas
5. **Conclusão** - Síntese e recomendações
6. **Referências** - Bibliografia formatada

---

##  Visualizações

### Gráfico 1: Acidentes por Mês
- Tipo: Gráfico de barras
- Destaque: Picos em dezembro, outubro e julho
- Arquivo: `acidentes_por_mes.png`

### Gráfico 2: Principais Causas
- Tipo: Gráfico de barras horizontal
- Destaque: Reação tardia, ausência de reação, desatenção
- Arquivo: `causas_acidentes.png`

### Gráfico 3: Distribuição por Hora
- Tipo: Gráfico de linha
- Destaque: Pico entre 17h e 19h
- Arquivo: `acidentes_por_hora.png`

---

##  Principais Descobertas

1. **Sazonalidade:** Picos em meses de férias e feriados prolongados
2. **Horário Crítico:** Concentração no horário de pico (17h-19h)
3. **Causas Humanas:** 68,6% dos acidentes relacionados a comportamento do condutor
4. **Padrões Temporais:** Identificação clara de períodos de maior risco

---

##  Gerar Visualizações

Para gerar as visualizações novamente:

```bash
python anexos.py
```

O script gera automaticamente:
- Gráficos em PNG (alta resolução)
- Tabelas em CSV
- Estatísticas descritivas

---

##  Notas

- O dataset completo não está incluído (tamanho)
- As visualizações foram geradas com matplotlib/seaborn
- O artigo segue o padrão SBC (Sociedade Brasileira de Computação)
- Formato: 4 páginas (limite SBC)

---

##  Referências do Artigo

1. Chuerubim et al. (2019) - Limitação de modelos de árvore de decisão
2. Dias et al. (2023) - Evolução da frota e legislação brasileira
3. Melo (2020) - Revisão bibliométrica
4. Velazquez et al. (2021) - Percepção de segurança viária

---

**Autor:** Vinícius de Souza Cebalhos
**Instituição:** UTFPR
**Formato:** Artigo Científico (SBC)
**Status:** Completo e pronto para submissão

