# Análise Exploratória - Dados de Reclamações/Solicitações
# Resolução dos exercícios do notebook em formato .py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurações iniciais
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 50)

# 1. Leitura e análise inicial dos dados
print("\n--- Leitura dos dados ---")
df = pd.read_csv('../data/2017-02-01_156_-_Base_de_Dados_sample-limpo.csv')
print(f"Dimensões: {df.shape}")
print(f"Colunas: {list(df.columns)}")

# Média, máxima e valores únicos
print("\n--- Estatísticas de idade e bairros ---")
print(f"Média das idades: {df['IDADE'].mean():.2f}")
print(f"Idade máxima: {df['IDADE'].max()}")
print(f"Valores únicos em BAIRRO_ASS: {df['BAIRRO_ASS'].nunique()}")

# Visualização das primeiras linhas
display(df.head())

# Informações dos tipos de dados
df.info()

# Estatísticas descritivas
display(df.describe())

# 2. Visualização da distribuição das variáveis
print("\n--- Distribuição de idades por sexo ---")
print(df['SEXO'].value_counts())

# Histogramas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
df_m = df[df['SEXO'] == 'M']
df_f = df[df['SEXO'] == 'F']
ax1.hist(df_m['IDADE'], bins=20, alpha=0.7, color='blue', edgecolor='black')
ax1.set_title('Homens')
ax2.hist(df_f['IDADE'], bins=20, alpha=0.7, color='pink', edgecolor='black')
ax2.set_title('Mulheres')
plt.show()

# Histograma sobreposto
plt.figure(figsize=(12, 6))
plt.hist(df_m['IDADE'], bins=20, alpha=0.6, color='blue', label='Homens', edgecolor='black')
plt.hist(df_f['IDADE'], bins=20, alpha=0.6, color='pink', label='Mulheres', edgecolor='black')
plt.legend()
plt.title('Distribuição de Idades por Sexo')
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
df.boxplot(column='IDADE', by='SEXO')
plt.title('Boxplot de Idades por Sexo')
plt.suptitle('')
plt.show()

# 3. Seleção dos dados
print("\n--- Seleção dos assuntos mais comuns ---")
# Usando groupby para contagem dos assuntos mais comuns
assuntos_grouped = df.groupby('ASSUNTO').size().reset_index(name='count')
assuntos_grouped = assuntos_grouped.sort_values('count', ascending=False)
print("Top 20 assuntos mais comuns:")
print(assuntos_grouped.head(20))

# Criando lista com assuntos que têm mais de 60 registros
assuntos_top = assuntos_grouped[assuntos_grouped['count'] > 60]['ASSUNTO'].tolist()
print(f"\nAssuntos com mais de 60 registros: {len(assuntos_top)}")
print("Lista dos assuntos:")
for i, assunto in enumerate(assuntos_top, 1):
    print(f"{i}. {assunto}")

# Filtrando DataFrame usando isin()
df_filtered = df[df['ASSUNTO'].isin(assuntos_top)]
print(f"\nDataFrame filtrado: {df_filtered.shape}")
print(f"Registros mantidos: {len(df_filtered)} de {len(df)} ({len(df_filtered)/len(df)*100:.1f}%)")

# 4. Análise de similaridades entre bairros
print("\n--- Similaridade entre bairros ---")
# Usando crosstab() para gerar DataFrame com bairros nas colunas e assuntos nas linhas
crosstab_data = pd.crosstab(df_filtered['ASSUNTO'], df_filtered['BAIRRO_ASS'])
print("Dimensões da tabela cruzada:")
print(f"Linhas (assuntos): {crosstab_data.shape[0]}")
print(f"Colunas (bairros): {crosstab_data.shape[1]}")
print("\nPrimeiras 10 linhas e 10 colunas da tabela cruzada:")
print(crosstab_data.iloc[:10, :10])

# Usando corr() para gerar matriz de correlações entre bairros
correlation_matrix = crosstab_data.corr()
print(f"\nDimensões da matriz de correlação: {correlation_matrix.shape}")
print(f"Correlação máxima: {correlation_matrix.max().max():.3f}")
print(f"Correlação mínima: {correlation_matrix.min().min():.3f}")
print(f"Média das correlações: {correlation_matrix.mean().mean():.3f}")

# Heatmap para exibir as correlações com cores
plt.figure(figsize=(20, 16))
sns.heatmap(correlation_matrix, cmap='RdBu_r', center=0, annot=False, square=True, cbar_kws={'shrink': 0.8})
plt.title('Matriz de Correlação entre Bairros')
plt.xlabel('Bairros')
plt.ylabel('Bairros')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# 5. Análise de bairros mais problemáticos
print("\n--- Bairros com mais registros ---")
# Criando DataFrame com contagem de registros por bairro usando BAIRRO_ASS
bairros_grouped = df.groupby('BAIRRO_ASS').size().reset_index(name='TOTAL_REGISTROS')
bairros_grouped = bairros_grouped.sort_values('TOTAL_REGISTROS', ascending=False)
print("Top 20 bairros com mais registros:")
print(bairros_grouped.head(20))

# Gráfico de barras para visualizar bairros com mais registros
plt.figure(figsize=(15, 8))
top_15_bairros = bairros_grouped.head(15)
bars = plt.bar(range(len(top_15_bairros)), top_15_bairros['TOTAL_REGISTROS'], 
               color='skyblue', edgecolor='navy', alpha=0.7)
plt.title('Top 15 Bairros com Mais Registros')
plt.xlabel('Bairros')
plt.ylabel('Número de Registros')
plt.xticks(range(len(top_15_bairros)), top_15_bairros['BAIRRO_ASS'], rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')

# Adicionando valores nas barras
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{int(height)}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

# 6. Taxa de registros por habitante
print("\n--- Taxa de registros por habitante ---")
# Criando DataFrame a partir dos dados do arquivo dados_bairros.csv
df_populacao = pd.read_csv('../data/dados_bairros.csv')
print("Dados de população dos bairros:")
print(df_populacao.head())
print(f"Dimensões: {df_populacao.shape}")

# Convertendo nomes dos bairros para caixa-baixo (minúsculo)
df_populacao['BAIRRO_LOWER'] = df_populacao['Bairro'].str.lower()
bairros_grouped['BAIRRO_LOWER'] = bairros_grouped['BAIRRO_ASS'].str.lower()

print("\nExemplos de conversão para minúsculo:")
print("Dados de população:")
print(df_populacao[['Bairro', 'BAIRRO_LOWER']].head())
print("\nDados de registros:")
print(bairros_grouped[['BAIRRO_ASS', 'BAIRRO_LOWER']].head())

# Fazendo junção usando merge com left_on e right_on
df_merged = bairros_grouped.merge(df_populacao, 
                                 left_on='BAIRRO_LOWER', 
                                 right_on='BAIRRO_LOWER', 
                                 how='left')
print(f"\nResultado da junção: {df_merged.shape}")

# Verificando bairros que não foram encontrados
bairros_nao_encontrados = df_merged[df_merged['Total'].isna()]
print(f"\nBairros sem dados de população: {len(bairros_nao_encontrados)}")
if len(bairros_nao_encontrados) > 0:
    print("Bairros:")
    for bairro in bairros_nao_encontrados['BAIRRO_ASS']:
        print(f"  - {bairro}")

# Criando coluna taxa usando a coluna 'Total' (população total)
df_merged['TAXA'] = df_merged['TOTAL_REGISTROS'] / df_merged['Total']
df_merged_sorted = df_merged.sort_values('TAXA', ascending=False)
print("\nTop 10 bairros com maior taxa de registros:")
print(df_merged_sorted[['BAIRRO_ASS', 'TOTAL_REGISTROS', 'Total', 'TAXA']].head(10))

# Gráfico de barras da taxa de registros
plt.figure(figsize=(15, 8))
top_15_taxa = df_merged_sorted.head(15)
bars = plt.bar(range(len(top_15_taxa)), top_15_taxa['TAXA'], 
               color='lightcoral', edgecolor='darkred', alpha=0.7)
plt.title('Top 15 Bairros com Maior Taxa de Registros por Habitante')
plt.xlabel('Bairros')
plt.ylabel('Taxa de Registros por Habitante')
plt.xticks(range(len(top_15_taxa)), top_15_taxa['BAIRRO_ASS'], rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')

# Adicionando valores nas barras
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.001,
             f'{height:.3f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

# 7. Tendências temporais
print("\n--- Tendências temporais ---")
# Convertendo coluna DATA para datetime
df['DATA'] = pd.to_datetime(df['DATA'])
print(f"Tipo da coluna DATA: {df['DATA'].dtype}")
print(f"Data mínima: {df['DATA'].min()}")
print(f"Data máxima: {df['DATA'].max()}")

# Agrupando linhas contando registros por mês
df['MES_ANO'] = df['DATA'].dt.to_period('M')
registros_por_mes = df.groupby('MES_ANO').size().reset_index(name='TOTAL_REGISTROS')
registros_por_mes['MES_ANO'] = registros_por_mes['MES_ANO'].astype(str)
print("\nRegistros por mês:")
print(registros_por_mes)
print(f"\nTotal de meses: {len(registros_por_mes)}")
print(f"Média de registros por mês: {registros_por_mes['TOTAL_REGISTROS'].mean():.1f}")

# Gráfico de linha com evolução da contagem
plt.figure(figsize=(15, 8))
plt.plot(range(len(registros_por_mes)), registros_por_mes['TOTAL_REGISTROS'], 
         marker='o', linewidth=2, markersize=6, color='darkblue')
plt.title('Evolução do Número de Registros por Mês')
plt.xlabel('Meses')
plt.ylabel('Número de Registros')
plt.grid(True, alpha=0.3)
plt.xticks(range(len(registros_por_mes)), registros_por_mes['MES_ANO'], rotation=45, ha='right')

# Adicionando valores nos pontos
for i, valor in enumerate(registros_por_mes['TOTAL_REGISTROS']):
    plt.text(i, valor + 5, str(valor), ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show() 