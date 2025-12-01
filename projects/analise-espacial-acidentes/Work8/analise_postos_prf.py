"""
Script para análise de proximidade entre acidentes e postos PRF
Download e processamento dos dados dos postos da PRF
"""

import json
import requests
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import folium
from folium import plugins
import numpy as np

def baixar_dados_postos():
    """
    Baixa os dados dos postos PRF do portal da ANTT
    """
    print("Baixando dados dos postos PRF...")
    
    url = "https://dados.antt.gov.br/dataset/87c613a5-af73-445f-bc35-5fe816e70935/resource/69444e48-599e-4384-a1e4-9318701f5590/download/dados_dos_postos_prfs.json"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        print(f"Dados baixados com sucesso!")
        
        return data
    except Exception as e:
        print(f"Erro ao baixar dados: {e}")
        return None

def processar_postos(data):
    """
    Processa os dados dos postos PRF
    """
    print("Processando dados dos postos...")
    
    postos = []
    
    for posto in data.get('prf', []):
        # Converter coordenadas (substituir vírgula por ponto)
        try:
            lat = float(posto['latitude'].replace(',', '.'))
            lon = float(posto['longitude'].replace(',', '.'))
            
            postos.append({
                'nome_posto': posto['nome_posto_prf'],
                'rodovia': posto['rodovia'],
                'uf': posto['uf'],
                'municipio': posto['municipio'],
                'latitude': lat,
                'longitude': lon,
                'situacao': posto['situacao'],
                'concessionaria': posto['concessionaria']
            })
        except:
            continue
    
    df_postos = pd.DataFrame(postos)
    
    # Filtrar apenas postos ativos
    df_postos = df_postos[df_postos['situacao'] == 'Ativo']
    
    print(f"Postos processados: {len(df_postos)}")
    print(f"Postos únicos: {df_postos['nome_posto'].nunique()}")
    
    # Criar GeoDataFrame
    geometry = [Point(xy) for xy in zip(df_postos['longitude'], df_postos['latitude'])]
    gdf_postos = gpd.GeoDataFrame(df_postos, geometry=geometry, crs='EPSG:4326')
    
    return gdf_postos

def processar_acidentes():
    """
    Processa os dados de acidentes
    """
    print("Carregando dados de acidentes...")
    
    df = pd.read_csv(
        'datatran2024.csv',
        sep=';',
        encoding='latin-1',
        low_memory=False
    )
    
    # Limpar dados
    df = df[df['latitude'].notna()]
    df = df[df['longitude'].notna()]
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df = df[df['latitude'].between(-90, 90)]
    df = df[df['longitude'].between(-180, 180)]
    
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    gdf_acidentes = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')
    
    # Converter para SIRGAS 2000 (mesmo sistema dos postos)
    gdf_acidentes = gdf_acidentes.to_crs('EPSG:4674')
    
    print(f"Acidentes processados: {len(gdf_acidentes):,}")
    
    return gdf_acidentes

def calcular_proximidade(gdf_acidentes, gdf_postos):
    """
    Calcula a distância entre acidentes e postos PRF mais próximos
    """
    print("Calculando distâncias...")
    
    # Converter postos para CRS UTM (para criar buffers corretos)
    gdf_postos_utm = gdf_postos.to_crs('EPSG:5880')  # UTM Zone 23S (Brasil)
    
    # Criar buffers de 10 km ao redor dos postos
    buffers = gdf_postos_utm.geometry.buffer(10000)
    
    # Converter de volta para SIRGAS
    buffers_sirgas = gpd.GeoSeries(buffers, crs='EPSG:5880').to_crs('EPSG:4674')
    
    # Criar GeoDataFrame de buffers
    gdf_buffers = gpd.GeoDataFrame(
        gdf_postos[['nome_posto', 'municipio', 'rodovia', 'uf']],
        geometry=buffers_sirgas,
        crs='EPSG:4674'
    )
    
    print(f"Buffers de 10 km criados para {len(gdf_buffers)} postos")
    
    # Verificar acidentes dentro dos buffers
    acidentes_dentro = 0
    acidentes_fora = 0
    
    # Análise mais eficiente: amostra para demo
    sample_acidentes = gdf_acidentes.sample(n=min(10000, len(gdf_acidentes)))
    
    for idx, acidente in sample_acidentes.iterrows():
        dentro = False
        for jdx, buffer in gdf_buffers.iterrows():
            if acidente.geometry.within(buffer.geometry):
                dentro = True
                break
        
        if dentro:
            acidentes_dentro += 1
        else:
            acidentes_fora += 1
    
    total = acidentes_dentro + acidentes_fora
    percentual_dentro = (acidentes_dentro / total * 100) if total > 0 else 0
    
    print(f"\n=== RESULTADOS DA ANÁLISE ===")
    print(f"Amostra analisada: {total:,} acidentes")
    print(f"Acidentes dentro dos buffers (10 km): {acidentes_dentro:,} ({percentual_dentro:.2f}%)")
    print(f"Acidentes fora dos buffers: {acidentes_fora:,} ({100-percentual_dentro:.2f}%)")
    
    return gdf_buffers, acidentes_dentro, acidentes_fora

def gerar_mapa_completo(gdf_acidentes, gdf_postos, gdf_buffers, output_file='mapa_completo_postos_prf.html'):
    """
    Gera mapa completo com acidentes, postos PRF e buffers
    """
    print("Gerando mapa completo...")
    
    # Converter para WGS84 para visualização
    gdf_postos_wgs84 = gdf_postos.to_crs('EPSG:4326')
    gdf_acidentes_wgs84 = gdf_acidentes.to_crs('EPSG:4326')
    gdf_buffers_wgs84 = gdf_buffers.to_crs('EPSG:4326')
    
    # Centro do mapa (Brasil)
    center_lat = -15.0
    center_lon = -47.0
    
    # Criar mapa
    mapa = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=5,
        tiles='OpenStreetMap'
    )
    
    # Adicionar layer de satélite
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='ESRI',
        name='Satélite',
        overlay=False,
        control=True
    ).add_to(mapa)
    
    # Adicionar acidentes (amostra)
    sample = gdf_acidentes_wgs84.sample(n=min(5000, len(gdf_acidentes_wgs84)))
    
    # MarkerCluster para acidentes
    marker_cluster = plugins.MarkerCluster(
        name='Acidentes (5.000 amostra)',
        overlay=True
    ).add_to(mapa)
    
    for idx, row in sample.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=f"Data: {row.get('data_inversa', 'N/A')}<br>UF: {row.get('uf', 'N/A')}<br>Causa: {row.get('causa_acidente', 'N/A')[:50]}",
            icon=folium.Icon(color='red', icon='warning-sign', prefix='glyphicon')
        ).add_to(marker_cluster)
    
    # Adicionar buffers (apenas alguns para não sobrecarregar)
    gdf_buffers_wgs84_sample = gdf_buffers_wgs84.sample(n=min(50, len(gdf_buffers_wgs84)))
    
    for idx, row in gdf_buffers_wgs84_sample.iterrows():
        try:
            folium.GeoJson(
                row.geometry,
                style_function=lambda feature: {
                    'fillColor': 'lightblue',
                    'color': 'blue',
                    'weight': 2,
                    'fillOpacity': 0.2,
                }
            ).add_to(mapa)
        except:
            continue
    
    # Adicionar postos PRF
    for idx, row in gdf_postos_wgs84.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=f"<b>{row.nome_posto}</b><br>Município: {row.municipio}<br>Rodovia: {row.rodovia}",
            icon=folium.Icon(color='blue', icon='shield', prefix='glyphicon'),
            tooltip=row.nome_posto
        ).add_to(mapa)
    
    # Controle de camadas
    folium.LayerControl().add_to(mapa)
    
    # Legenda
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 200px; height: 150px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px">
    <h4 style="margin-top: 0">Legenda</h4>
    <p><span style="color:blue;">🔵</span> Postos PRF</p>
    <p><span style="color:lightblue;">█</span> Buffer 10 km</p>
    <p><span style="color:red;">🔴</span> Acidentes</p>
    </div>
    '''
    mapa.get_root().html.add_child(folium.Element(legend_html))
    
    mapa.save(output_file)
    print(f"Mapa completo salvo em: {output_file}")

def gerar_estatisticas_postos(gdf_postos, gdf_acidentes):
    """
    Gera estatísticas sobre os postos PRF
    """
    print("\n=== ESTATÍSTICAS DOS POSTOS PRF ===")
    print(f"Total de postos ativos: {len(gdf_postos)}")
    print(f"\nDistribuição por Estado:")
    print(gdf_postos['uf'].value_counts())
    print(f"\nTop 10 Rodovias com mais postos:")
    print(gdf_postos['rodovia'].value_counts().head(10))
    
    # Estimar cobertura
    # Criar buffer de 10 km ao redor de cada posto
    gdf_postos_utm = gdf_postos.to_crs('EPSG:5880')  # UTM
    
    # Área aproximada dos buffers
    area_buffers = gdf_postos_utm.geometry.buffer(10000).area.sum() / 1e6  # km²
    
    # Área aproximada do Brasil: 8.5 milhão km²
    area_brasil = 8_500_000
    
    cobertura = (area_buffers / area_brasil) * 100
    
    print(f"\nÁrea coberta pelos buffers (aprox): {area_buffers:,.0f} km²")
    print(f"Cobertura teórica: {cobertura:.2f}% do território nacional")

def main():
    """
    Função principal
    """
    print("=" * 70)
    print("ANÁLISE DE PROXIMIDADE: ACIDENTES E POSTOS PRF")
    print("=" * 70)
    
    # 1. Baixar dados dos postos
    data = baixar_dados_postos()
    if data is None:
        print("Não foi possível baixar os dados dos postos.")
        return
    
    # 2. Processar postos
    gdf_postos = processar_postos(data)
    
    # 3. Processar acidentes
    gdf_acidentes = processar_acidentes()
    
    # 4. Calcular proximidade
    gdf_buffers, dentro, fora = calcular_proximidade(gdf_acidentes, gdf_postos)
    
    # 5. Gerar mapa completo
    gerar_mapa_completo(gdf_acidentes, gdf_postos, gdf_buffers)
    
    # 6. Estatísticas
    gerar_estatisticas_postos(gdf_postos, gdf_acidentes)
    
    print("\n" + "=" * 70)
    print("PROCESSO CONCLUÍDO!")
    print("=" * 70)

if __name__ == "__main__":
    main()

