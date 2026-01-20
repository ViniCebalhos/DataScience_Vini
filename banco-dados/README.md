# Database & SQL Projects

Projetos demonstrando competências em PostgreSQL, PostGIS, SQL avançado, análise geoespacial e processamento de dados em larga escala.

---

## Projetos

### [Análise de Alvarás de Construção](./analise-alvaras/)
**Descrição:** Análise exploratória de dados de alvarás de construção usando SQL e Python.

**Tecnologias:**
- PostgreSQL
- Python (pandas)
- SQL para consultas

**Conteúdo:**
- Carregamento de dados em banco PostgreSQL
- Consultas SQL para análise exploratória
- Análise de padrões em alvarás de construção
- Estatísticas descritivas

**Arquivos principais:**
- `Work1.ipynb` - Notebook com análises
- `2023-05-22_Alvaras_-_Dicionario_de_Dados.csv` - Dicionário de dados

---

### [Análise Exploratória de Acidentes de Trânsito](./analise-acidentes-eda/)
**Descrição:** Análise exploratória de dados de acidentes de trânsito da PRF.

**Tecnologias:**
- PostgreSQL
- Python (pandas, matplotlib, seaborn)
- SQL para consultas

**Conteúdo:**
- Análise de acidentes em rodovias federais
- Estatísticas descritivas
- Visualizações de padrões temporais
- Identificação de causas principais

**Dataset:**
- `datatran2025.csv` - Dados da Polícia Rodoviária Federal

**Arquivos principais:**
- `Work2.ipynb` - Notebook com análises completas

---

### [Consultas SQL Avançadas](./consultas-sql-avancadas/)
**Descrição:** Aplicação de consultas SQL avançadas em dados de acidentes.

**Tecnologias:**
- PostgreSQL
- SQL (JOINs, agregações, subconsultas)

**Conteúdo:**
- Consultas SQL complexas
- Agregações e agrupamentos
- Análise de dados de acidentes

**Dataset:**
- `datatran2024.csv` - Dados da PRF

---

### [Artigo Científico - Análise de Acidentes em Rodovias Federais](../projects/analise-acidentes-rodovias/)
**Descrição:** Artigo científico completo sobre análise de acidentes de trânsito.

**Resultado:** Artigo científico completo publicado em formato SBC.

**Tecnologias:**
- PostgreSQL
- Python (pandas, matplotlib, seaborn)
- LaTeX para formatação do artigo
- SQL para consultas

**Conteúdo:**
- Análise de 67.794 acidentes em rodovias federais
- Identificação de padrões temporais (mensais e horários)
- Análise de causas principais
- Visualizações profissionais
- Artigo científico completo em LaTeX

**Principais Descobertas:**
- Picos de acidentes: Dezembro (6.587), Outubro (6.406), Julho (6.401)
- Horário crítico: 17h-19h
- Principais causas: Reação tardia (27,3%), Ausência de reação (22,4%), Desatenção (18,9%)

** Este projeto está em destaque em [`projects/analise-acidentes-rodovias/`](../projects/analise-acidentes-rodovias/)**

---

### [Análise Espacial de Acidentes com PostGIS](../projects/analise-espacial-acidentes/)
**Descrição:** Análise geoespacial de acidentes de trânsito usando PostGIS.

**Resultado:** Artigo científico completo com análise espacial.

**Tecnologias:**
- PostgreSQL + PostGIS
- Python (geopandas, folium)
- SQL espacial
- Visualizações interativas

**Conteúdo:**
- Análise de 73.156 acidentes em rodovias federais
- Mapeamento de 169 postos da PRF
- Análise de proximidade espacial
- Identificação de áreas críticas
- Mapas interativos com Folium

**Principais Descobertas:**
- 80% dos acidentes ocorrem fora da cobertura direta dos postos PRF
- Identificação de hotspots de acidentes
- Análise de eficiência da distribuição de postos

** Este projeto está em destaque em [`projects/analise-espacial-acidentes/`](../projects/analise-espacial-acidentes/)**

---

## Tecnologias e Bibliotecas Utilizadas

### Principais
- **PostgreSQL** - Banco de dados relacional
- **PostGIS** - Extensão geoespacial
- **Python** - Análise e visualização
- **Pandas** - Manipulação de dados
- **SQL** - Consultas e análises

### Específicas
- **Geopandas** - Dados geoespaciais
- **Folium** - Mapas interativos
- **Matplotlib/Seaborn** - Visualizações
- **LaTeX** - Formatação de artigos científicos

---

## Competências Demonstradas

- Modelagem de Banco de Dados
- Consultas SQL (básicas e avançadas)
- SQL Espacial (PostGIS)
- Análise Exploratória de Dados
- Análise Geoespacial
- Visualização de Dados
- Redação Científica (LaTeX)
- Análise Estatística

---

## Estrutura de Pastas

```
banco-dados/
 README.md                    # Este arquivo
 analise-alvaras/             # Análise de Alvarás
 analise-acidentes-eda/       # Análise Exploratória Acidentes
 consultas-sql-avancadas/     # Consultas SQL Avançadas

Nota: Os projetos Work6 e Work8 foram movidos para projects/ como projetos em destaque.
```

---

## Como Executar

### Para projetos com PostgreSQL:

1. Instale o PostgreSQL e PostGIS:
```bash
sudo apt-get install postgresql postgresql-contrib postgis
```

2. Crie o banco de dados:
```sql
CREATE DATABASE seu_banco;
\c seu_banco
CREATE EXTENSION postgis;
```

3. Instale as dependências Python:
```bash
pip install pandas psycopg2 geopandas folium matplotlib seaborn
```

4. Execute os notebooks ou scripts Python

### Para compilar artigos LaTeX:

1. Instale o LaTeX:
```bash
sudo apt-get install texlive-latex-extra texlive-fonts-recommended texlive-lang-portuguese
```

2. Compile o artigo:
```bash
cd Work6  # ou Work8
pdflatex artigo_sbc*.tex
```

---

## Notas

- Os datasets podem ser grandes e não estão incluídos no repositório
- Alguns projetos requerem configuração de banco de dados PostgreSQL
- Os artigos científicos estão em formato LaTeX (padrão SBC)
- Mapas interativos são gerados em HTML e podem ser visualizados no navegador

---

## Artigos Científicos

Este repositório contém dois artigos científicos completos:

1. **Análise de Acidentes em Rodovias Federais:** Artigo científico completo
2. **Análise Espacial de Acidentes:** Artigo científico com PostGIS

Ambos estão formatados conforme padrão SBC e prontos para submissão.

---

**Autor:** Vinícius de Souza Cebalhos

