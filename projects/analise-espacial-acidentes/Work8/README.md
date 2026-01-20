# 📊 Resultados da Análise Espacial de Acidentes em Rodovias Federais

## Arquivos Gerados

### 📄 Documentos Acadêmicos
1. **`artigo_sbc_analise_espacial.pdf`** (748 KB)
   - Artigo completo no formato SBC
   - 12 páginas com análise espacial completa
   - Inclui metodologia PostGIS, resultados e conclusões

2. **`artigo_analise_espacial_acidentes_sbc.md`** (Markdown)
   - Versão em Markdown do artigo
   - Inclui todos os SQLs utilizados no anexo

### Visualizações

1. **`mapa_densidade_acidentes.png`** (595 KB)
   - Mapa estático da distribuição de acidentes
   - 73.156 pontos de acidentes georreferenciados
   - Coordenadas: SIRGAS 2000 (EPSG:4674)

2. **`mapa_acidentes_interativo.html`** (4.3 MB)
   - Mapa interativo com heatmap
   - Visualização Folium com clusters
   - Pode ser aberto em qualquer navegador

3. **`mapa_completo_postos_prf.html`** (6.2 MB)
   - Mapa completo com acidentes, postos PRF e buffers de 10 km
   - Inclui 169 postos da PRF georreferenciados
   - 169 buffers de 10 km ao redor de cada posto
   - Camada de satélite incluída

4. **`acidentes_por_estado.png`** (186 KB)
   - Gráfico de barras horizontal
   - Top 10 estados por número de acidentes
   - MG em 1º lugar (9.296 acidentes)

### Análises e Estatísticas

1. **`estatisticas_acidentes.txt`**
   - Estatísticas descritivas completas
   - Top 10 estados e principais causas

2. **`resultados_analise_postos_prf.txt`**
   - Resultados da análise de proximidade
   - Estatísticas dos postos PRF
   - Interpretação dos resultados

### 💻 Scripts Python

1. **`gerar_mapa_analise_espacial.py`**
   - Geração de mapas de densidade
   - Análise estatística por estado
   - Visualizações com GeoPandas e Folium

2. **`analise_postos_prf.py`**
   - Download automático de dados dos postos PRF (ANTT)
   - Cálculo de buffers de 10 km
   - Análise de proximidade acidentes-postos
   - Geração de mapa completo interativo

## Principais Descobertas

### Dados Gerais
- **Total de acidentes analisados**: 73.156
- **Período**: Ano de 2024
- **Acidentes com vítimas fatais**: 5.222 (7,14%)

### Top 10 Estados (por número de acidentes)
1. **Minas Gerais (MG)**: 9.296 acidentes (12,7%)
2. **Santa Catarina (SC)**: 8.381 acidentes (11,5%)
3. **Paraná (PR)**: 7.576 acidentes (10,4%)
4. **Rio de Janeiro (RJ)**: 6.389 acidentes (8,7%)
5. **Rio Grande do Sul (RS)**: 5.206 acidentes (7,1%)
6. **São Paulo (SP)**: 4.883 acidentes (6,7%)
7. **Bahia (BA)**: 4.151 acidentes (5,7%)
8. **Goiás (GO)**: 3.305 acidentes (4,5%)
9. **Pernambuco (PE)**: 3.230 acidentes (4,4%)
10. **Mato Grosso (MT)**: 2.554 acidentes (3,5%)

### Top 10 Causas de Acidentes
1. **Reação tardia ou ineficiente**: 10.920 acidentes (14,9%)
2. **Ausência de reação**: 10.664 acidentes (14,6%)
3. **Acesso indevido à via**: 6.958 acidentes (9,5%)
4. **Distância insuficiente**: 4.460 acidentes (6,1%)
5. **Velocidade Incompatível**: 4.347 acidentes (5,9%)
6. **Manobra indevida**: 4.213 acidentes (5,8%)
7. **Ingestão de álcool**: 3.854 acidentes (5,3%)
8. **Falhas mecânicas**: 3.390 acidentes (4,6%)
9. **Contramão**: 2.461 acidentes (3,4%)
10. **Condutor Dormindo**: 2.136 acidentes (2,9%)

### Análise de Proximidade aos Postos PRF

**Resultados da Análise de Amostra (10.000 acidentes):**
- **Acidentes dentro dos buffers (10 km)**: 2.019 (20,19%)
- **Acidentes fora dos buffers**: 7.981 (79,81%)

**Interpretação:**
- ~80% dos acidentes ocorrem em áreas com menor cobertura direta da PRF
- Apenas ~20% dos acidentes estão dentro do raio de 10 km dos postos
- **Recomendação**: Estratégias complementares são necessárias (patrulhamento móvel, monitoramento remoto)

### Postos PRF Mapeados
- **Total de postos ativos**: 169
- **Área coberta pelos buffers**: ~53.000 km²
- **Cobertura do território nacional**: 0,62%

**Distribuição de Postos (Top 5 Estados):**
1. RJ: 29 postos
2. MG: 27 postos
3. SP: 26 postos
4. PR: 17 postos
5. GO: 13 postos

**Rodovias com Mais Postos:**
1. **BR-116**: 46 postos
2. **BR-101**: 32 postos
3. **BR-163**: 17 postos
4. **BR-153**: 15 postos
5. **BR-381**: 9 postos

## Metodologia Utilizada

### Ferramentas
- **Banco de Dados**: PostgreSQL com extensão PostGIS
- **Sistema de Coordenadas**: SIRGAS 2000 (EPSG:4674)
- **Análise Espacial**: PostGIS (ST_Buffer, ST_Distance, ST_Within)
- **Visualização**: Python (GeoPandas, Folium, Matplotlib)
- **Fontes de Dados**:
  - Acidentes: Polícia Rodoviária Federal (PRF)
  - Postos: Agência Nacional de Transportes Terrestres (ANTT)

### Funções PostGIS Utilizadas
1. **ST_MakePoint**: Conversão de coordenadas em geometrias POINT
2. **ST_SetSRID**: Definição do sistema de coordenadas
3. **ST_Buffer**: Criação de buffers de 10 km
4. **ST_Distance**: Cálculo de distância entre acidentes e postos
5. **ST_Within**: Verificação de acidentes dentro dos buffers

## Como Usar

### 1. Visualizar os Mapas
```bash
# Abra os mapas interativos no navegador
firefox mapa_acidentes_interativo.html
firefox mapa_completo_postos_prf.html
```

### 2. Ler o Artigo
```bash
# Visualizar o PDF
xdg-open artigo_sbc_analise_espacial.pdf

# Ou abrir no editor de texto
xdg-open artigo_analise_espacial_acidentes_sbc.md
```

### 3. Reexecutar as Análises
```bash
# Ativar o ambiente conda
source ~/anaconda3/etc/profile.d/conda.sh
conda activate ds

# Executar os scripts
python gerar_mapa_analise_espacial.py
python analise_postos_prf.py
```

## Estrutura do Artigo

1. **Introdução**: Contextualização do problema
2. **Trabalhos Relacionados**: 4 artigos relevantes citados
3. **Metodologia**: 5 etapas de análise espacial
4. **Resultados**: 
   - Distribuição geográfica
   - Análise de proximidade (20% dentro, 80% fora)
   - Principais causas
   - Estatísticas dos postos PRF
5. **Conclusão**: Achados e trabalhos futuros
6. **Referências**: 8 trabalhos citados
7. **Anexos**: Códigos SQL utilizados

## Principais Contribuições

1. Mapeamento completo de 73.156 acidentes em rodovias federais
2. Análise espacial de proximidade aos postos PRF
3. Identificação de que 80% dos acidentes ocorrem fora da cobertura direta
4. Mapeamento de 169 postos ativos da PRF
5. Geração de visualizações interativas com Folium
6. Metodologia replicável com PostGIS

## Referências Utilizadas

1. OMS (2018) - Global status report on road safety
2. Silva et al. (2018) - Análise espacial com SIG
3. Santos e Oliveira (2019) - PostgreSQL/PostGIS para proximidade
4. Costa et al. (2020) - Funções espaciais em rodovias
5. Chuerubim et al. (2019) - Modelos de classificação
6. Dias et al. (2023) - Evolução da frota e legislação
7. Melo (2020) - Revisão bibliométrica
8. Velazquez et al. (2021) - Percepção de segurança

## 🚀 Trabalhos Futuros Sugeridos

1. **Clusterização Espacial (DBSCAN)**: Identificação automática de hotspots
2. **Modelos Preditivos**: Machine learning para predição de acidentes
3. **Análise Temporal-Espacial**: Tendências temporais combinadas com padrões espaciais
4. **Análise de Redes**: Fluxos de tráfego e pontos críticos
5. **Integração com Dados Climáticos**: Fatores ambientais
6. **Otimização da Cobertura**: Modelos para posicionamento de novos postos


---

## Estrutura de Arquivos

```
Work8/
├── artigo_sbc_analise_espacial.pdf          # Artigo PDF (748 KB)
├── artigo_analise_espacial_acidentes_sbc.md # Artigo Markdown
├── artigo_sbc_analise_espacial.tex          # Código LaTeX
├── mapa_densidade_acidentes.png             # Mapa estático
├── mapa_acidentes_interativo.html           # Mapa interativo (4.3 MB)
├── mapa_completo_postos_prf.html           # Mapa com buffers (6.2 MB)
├── acidentes_por_estado.png                 # Gráfico por estado
├── estatisticas_acidentes.txt               # Estatísticas
├── resultados_analise_postos_prf.txt        # Análise de proximidade
├── datatran2024.csv                         # Dados originais (73K registros)
├── gerar_mapa_analise_espacial.py          # Script de análise 1
├── analise_postos_prf.py                    # Script de análise 2
└── README_RESULTADOS.md                     # Este arquivo
```

---

**Desenvolvido com Python, PostGIS e LaTeX** 



