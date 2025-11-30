"""
Script para gerar mapas de análise espacial de acidentes de trânsito
utilizando dados da PRF (Polícia Rodoviária Federal)
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from shapely.geometry import Point
import contextily as ctx
import folium
from folium import plugins
import numpy as np
import seaborn as sns

# Configuração de estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 12

def carregar_dados():
    """Carrega os dados de acidentes do CSV"""
    print("Carregando dados de acidentes...")
    df = pd.read_csv(
        'datatran2024.csv',
        sep=';',
        encoding='latin-1',
        low_memory=False
    )
    
    # Limpar dados inválidos
    df = df[df['latitude'].notna()]
    df = df[df['longitude'].notna()]
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df = df[df['latitude'].between(-90, 90)]
    df = df[df['longitude'].between(-180, 180)]
    
    print(f"Total de registros carregados: {len(df):,}")
    
    return df

def criar_geodataframe(df):
    """Converte o DataFrame em GeoDataFrame"""
    print("Convertendo para GeoDataFrame...")
    
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')
    
    # Converter para SIRGAS 2000 (EPSG:4674) - Brasil
    gdf = gdf.to_crs('EPSG:4674')
    
    print(f"GeoDataFrame criado com {len(gdf):,} pontos")
    
    return gdf

def calcular_densidade_espacial(gdf, cell_size=50000):
    """
    Calcula densidade espacial usando grid
    cell_size está em metros (50km)
    """
    print(f"Calculando densidade espacial (grid de {cell_size/1000:.0f}km)...")
    
    bounds = gdf.total_bounds
    minx, miny, maxx, maxy = bounds
    
    # Criar grid
    x_cells = int((maxx - minx) / cell_size) + 1
    y_cells = int((maxy - miny) / cell_size) + 1
    
    density_grid = []
    
    for i in range(x_cells):
        for j in range(y_cells):
            cell_minx = minx + i * cell_size
            cell_miny = miny + j * cell_size
            cell_maxx = minx + (i + 1) * cell_size
            cell_maxy = miny + (j + 1) * cell_size
            
            cell = gdf.cx[cell_minx:cell_maxx, cell_miny:cell_maxy]
            count = len(cell)
            
            if count > 0:
                density_grid.append({
                    'geometry': Point(cell_minx + cell_size/2, cell_miny + cell_size/2),
                    'count': count,
                    'density': count / (cell_size / 1000)**2  # acidentes por km²
                })
    
    density_gdf = gpd.GeoDataFrame(density_grid, crs=gdf.crs)
    
    print(f"Grid de densidade criado com {len(density_gdf)} células")
    
    return density_gdf

def gerar_mapa_densidade(gdf, density_gdf, output_file='mapa_densidade_acidentes.png'):
    """
    Gera mapa de densidade de acidentes
    """
    print("Gerando mapa de densidade...")
    
    fig, ax = plt.subplots(figsize=(20, 16))
    
    # Plotar densidade se houver dados
    if len(density_gdf) > 0:
        try:
            density_gdf.plot(
                ax=ax,
                column='count',
                cmap='YlOrRd',
                alpha=0.6,
                edgecolor='none',
                linewidth=0,
                legend=True,
                legend_kwds={'shrink': 0.8, 'label': 'Número de Acidentes'}
            )
        except:
            print("Aviso: Não foi possível plotar o grid de densidade")
    
    # Converter para WGS84 para melhor visualização
    gdf_wgs84 = gdf.to_crs('EPSG:4326')
    
    # Plotar pontos (amostra para não sobrecarregar)
    sample = gdf_wgs84.sample(n=min(5000, len(gdf_wgs84)))
    sample.plot(ax=ax, markersize=0.5, color='darkred', alpha=0.3, label='Acidentes')
    
    ax.set_title(
        'Mapa de Densidade de Acidentes de Trânsito em Rodovias Federais - 2024\n' +
        f'Total de acidentes: {len(gdf):,}',
        fontsize=18,
        fontweight='bold',
        pad=20
    )
    
    ax.set_xlabel('Longitude (WGS84)', fontsize=14)
    ax.set_ylabel('Latitude (WGS84)', fontsize=14)
    
    # Adicionar grid
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Ajustar aspecto para latitude média do Brasil
    ax.set_aspect(1.0)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Mapa salvo em: {output_file}")
    
    plt.close()
    
def gerar_mapa_interativo(gdf, output_file='mapa_acidentes_interativo.html'):
    """
    Gera mapa interativo com Folium
    """
    print("Gerando mapa interativo...")
    
    # Converter para WGS84 para Folium
    gdf_wgs84 = gdf.to_crs('EPSG:4326')
    
    # Calcular centro do mapa
    center_lat = gdf_wgs84.geometry.y.mean()
    center_lon = gdf_wgs84.geometry.x.mean()
    
    # Criar mapa
    mapa = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=5,
        tiles='OpenStreetMap'
    )
    
    # Adicionar camada de calor
    heat_data = [[row.geometry.y, row.geometry.x] for idx, row in gdf_wgs84.iterrows()]
    
    plugins.HeatMap(
        heat_data,
        radius=15,
        blur=10,
        max_zoom=1,
        gradient={
            0.2: 'blue',
            0.4: 'cyan',
            0.6: 'lime',
            0.8: 'yellow',
            1: 'red'
        }
    ).add_to(mapa)
    
    # Adicionar clusters de pontos
    sample = gdf_wgs84.sample(n=min(2000, len(gdf_wgs84)))
    
    marker_cluster = plugins.MarkerCluster(
        name='Acidentes',
        overlay=True,
        control=True
    ).add_to(mapa)
    
    for idx, row in sample.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=f"UF: {row.get('uf', 'N/A')}<br>" +
                  f"Causa: {row.get('causa_acidente', 'N/A')}<br>" +
                  f"Data: {row.get('data_inversa', 'N/A')}",
            icon=folium.Icon(color='red', icon='warning-sign', prefix='glyphicon')
        ).add_to(marker_cluster)
    
    # Adicionar controle de camadas
    folium.LayerControl().add_to(mapa)
    
    # Salvar mapa
    mapa.save(output_file)
    print(f"Mapa interativo salvo em: {output_file}")

def analise_por_estado(gdf):
    """Gera análise de acidentes por estado"""
    print("Gerando análise por estado...")
    
    gdf_wgs84 = gdf.to_crs('EPSG:4326')
    
    # Contagem por UF - ordenado do MAIOR para o MENOR
    contagem_uf = gdf_wgs84['uf'].value_counts().head(10)
    
    # Reverter a ordem para ter o maior no topo (barh mostra de cima para baixo)
    # Maior valor = maior índice = maior cor
    contagem_uf = contagem_uf.iloc[::-1]
    
    # Gráfico de barras
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Gerar cores do mais forte (vermelho) para o mais fraco (rosa claro)
    # Valor mais alto = índice 0 = posição superior = cor mais forte
    cores = plt.cm.Reds(np.linspace(0.4, 0.95, len(contagem_uf)))
    # Inverter as cores para que o maior valor (topo) tenha cor mais forte
    cores = cores[::-1]
    
    ax.barh(contagem_uf.index, contagem_uf.values, color=cores)
    
    ax.set_xlabel('Número de Acidentes', fontsize=14, fontweight='bold')
    ax.set_ylabel('Estado (UF)', fontsize=14, fontweight='bold')
    ax.set_title(
        'Top 10 Estados com Maior Número de Acidentes em Rodovias Federais - 2024',
        fontsize=16,
        fontweight='bold',
        pad=20
    )
    
    # Adicionar valores nas barras
    for i, v in enumerate(contagem_uf.values):
        ax.text(v + 50, i, f'{v:,}', va='center', fontsize=11, fontweight='bold')
    
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('acidentes_por_estado.png', dpi=300, bbox_inches='tight')
    print("Gráfico de acidentes por estado salvo em: acidentes_por_estado.png")
    
    plt.close()
    
    return contagem_uf.iloc[::-1]  # Retornar na ordem original

def gerar_estatisticas_descriptivas(gdf):
    """Gera estatísticas descritivas dos acidentes"""
    print("\n=== ESTATÍSTICAS DESCRITIVAS ===\n")
    
    print(f"Total de acidentes analisados: {len(gdf):,}")
    
    # Distribuição por UF
    print("\nTop 10 Estados:")
    print(gdf['uf'].value_counts().head(10))
    
    # Distribuição por causa
    print("\nTop 10 Causas de Acidentes:")
    print(gdf['causa_acidente'].value_counts().head(10))
    
    # Acidentes com vítimas fatais
    fatal = gdf['classificacao_acidente'].str.contains('Fatais', na=False).sum()
    print(f"\nAcidentes com vítimas fatais: {fatal:,} ({fatal/len(gdf)*100:.2f}%)")
    
    # Salvar em arquivo
    with open('estatisticas_acidentes.txt', 'w', encoding='utf-8') as f:
        f.write("=== ESTATÍSTICAS DE ACIDENTES DE TRÂNSITO 2024 ===\n\n")
        f.write(f"Total de acidentes: {len(gdf):,}\n\n")
        f.write("Distribuição por Estado:\n")
        f.write(gdf['uf'].value_counts().to_string())
        f.write("\n\nTop 10 Causas de Acidentes:\n")
        f.write(gdf['causa_acidente'].value_counts().head(10).to_string())
        f.write("\n\n")
        
    print("\nEstatísticas salvas em: estatisticas_acidentes.txt")

def main():
    """Função principal"""
    print("=" * 70)
    print("GERAÇÃO DE MAPAS E ANÁLISES ESPACIAIS DE ACIDENTES")
    print("=" * 70)
    
    # 1. Carregar dados
    df = carregar_dados()
    
    # 2. Criar GeoDataFrame
    gdf = criar_geodataframe(df)
    
    # 3. Calcular densidade
    density_gdf = calcular_densidade_espacial(gdf)
    
    # 4. Gerar mapas
    gerar_mapa_densidade(gdf, density_gdf)
    gerar_mapa_interativo(gdf)
    
    # 5. Análise por estado
    analise_por_estado(gdf)
    
    # 6. Estatísticas descritivas
    gerar_estatisticas_descriptivas(gdf)
    
    print("\n" + "=" * 70)
    print("PROCESSO CONCLUÍDO!")
    print("=" * 70)
    print("\nArquivos gerados:")
    print("- mapa_densidade_acidentes.png")
    print("- mapa_acidentes_interativo.html")
    print("- acidentes_por_estado.png")
    print("- estatisticas_acidentes.txt")

if __name__ == "__main__":
    main()

