"""
Script para preparar e inserir dados dos postos PRF no PostgreSQL
Baixa dados do portal ANTT e cria tabela com geometria PostGIS
"""

import json
import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import psycopg2
from psycopg2 import sql
import sys

def baixar_dados_postos():
    """Baixa os dados dos postos PRF do portal da ANTT"""
    print("Baixando dados dos postos PRF...")
    
    url = "https://dados.antt.gov.br/dataset/87c613a5-af73-445f-bc35-5fe816e70935/resource/69444e48-599e-4384-a1e4-9318701f5590/download/dados_dos_postos_prfs.json"
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        print(f"✓ Dados baixados com sucesso ({len(data.get('prf', []))} postos)")
        return data
    except Exception as e:
        print(f"✗ Erro ao baixar dados: {e}")
        return None

def processar_dados_postos(data):
    """Processa os dados dos postos e cria GeoDataFrame"""
    print("Processando dados dos postos...")
    
    postos = []
    
    for posto in data.get('prf', []):
        try:
            # Converter coordenadas (substituir vírgula por ponto)
            lat = float(posto['latitude'].replace(',', '.'))
            lon = float(posto['longitude'].replace(',', '.'))
            km = str(posto.get('km_m', '0')).replace(',', '.')
            
            # Filtrar apenas postos ativos
            if posto.get('situacao', '').upper() == 'ATIVO':
                postos.append({
                    'nome_posto': posto['nome_posto_prf'],
                    'rodovia': posto['rodovia'],
                    'uf': posto['uf'],
                    'municipio': posto['municipio'],
                    'km': km,
                    'latitude': lat,
                    'longitude': lon,
                    'concessionaria': posto.get('concessionaria', ''),
                    'situacao': posto.get('situacao', ''),
                    'tipo_pista': posto.get('tipo_pista', ''),
                    'sentido': posto.get('sentido', '')
                })
        except Exception as e:
            print(f"Aviso: Posto '{posto.get('nome_posto_prf', 'N/A')}' ignorado: {e}")
            continue
    
    # Criar DataFrame
    df_postos = pd.DataFrame(postos)
    
    # Criar geometria
    geometry = [Point(xy) for xy in zip(df_postos['longitude'], df_postos['latitude'])]
    gdf_postos = gpd.GeoDataFrame(df_postos, geometry=geometry, crs='EPSG:4326')
    
    print(f"✓ Processados {len(gdf_postos)} postos ativos")
    return gdf_postos

def gerar_sql_create_table():
    """Gera SQL para criar a tabela de postos PRF"""
    sql_create = """
-- Criação da tabela de postos PRF
CREATE TABLE IF NOT EXISTS postos_prf (
    id SERIAL PRIMARY KEY,
    nome_posto VARCHAR(255) NOT NULL,
    rodovia VARCHAR(20),
    uf VARCHAR(2),
    municipio VARCHAR(100),
    km VARCHAR(20),
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    concessionaria VARCHAR(255),
    situacao VARCHAR(50),
    tipo_pista VARCHAR(50),
    sentido VARCHAR(50),
    geom GEOMETRY(POINT, 4326)  -- WGS84
);

-- Criação de índices para melhor performance
CREATE INDEX IF NOT EXISTS idx_postos_prf_geom 
ON postos_prf USING GIST (geom);

CREATE INDEX IF NOT EXISTS idx_postos_prf_uf 
ON postos_prf(uf);

CREATE INDEX IF NOT EXISTS idx_postos_prf_rodovia 
ON postos_prf(rodovia);

COMMENT ON TABLE postos_prf IS 'Postos da Polícia Rodoviária Federal - Dados do portal ANTT';
COMMENT ON COLUMN postos_prf.geom IS 'Geometria Point em WGS84 (EPSG:4326)';
    """
    
    return sql_create

def gerar_sql_inserts(gdf_postos):
    """Gera comandos SQL INSERT para os postos"""
    print("Gerando comandos SQL INSERT...")
    
    sql_commands = []
    sql_commands.append("-- Dados dos postos PRF\n")
    sql_commands.append("INSERT INTO postos_prf (nome_posto, rodovia, uf, municipio, km, latitude, longitude, concessionaria, situacao, tipo_pista, sentido, geom) VALUES\n")
    
    for idx, row in gdf_postos.iterrows():
        # Converter geometria para WKT
        geom_wkt = row.geometry.wkt
        
        # Escapar aspas simples no nome
        nome_escape = row['nome_posto'].replace("'", "''")
        municipio_escape = row['municipio'].replace("'", "''")
        
        insert = f"""('{nome_escape}', '{row['rodovia']}', '{row['uf']}', 
'{municipio_escape}', '{row['km']}', {row['latitude']}, {row['longitude']}, 
'{row['concessionaria']}', '{row['situacao']}', '{row['tipo_pista']}', 
'{row['sentido']}', ST_GeomFromText('{geom_wkt}', 4326))"""
        
        sql_commands.append(insert)
        
        # Adicionar vírgula exceto no último
        if idx < len(gdf_postos) - 1:
            sql_commands.append(",\n")
        else:
            sql_commands.append(";\n")
    
    return ''.join(sql_commands)

def salvar_arquivos_sql():
    """Salva os arquivos SQL gerados"""
    print("Salvando arquivos SQL...")
    
    # 1. Gerar CREATE TABLE
    with open('criar_tabela_postos_prf.sql', 'w', encoding='utf-8') as f:
        f.write(gerar_sql_create_table())
    
    print("✓ Arquivo criado: criar_tabela_postos_prf.sql")
    
    # 2. Baixar e processar dados
    data = baixar_dados_postos()
    if data is None:
        print("✗ Não foi possível baixar os dados")
        return
    
    gdf_postos = processar_dados_postos(data)
    
    # 3. Gerar INSERTs
    sql_inserts = gerar_sql_inserts(gdf_postos)
    
    with open('inserir_postos_prf.sql', 'w', encoding='utf-8') as f:
        f.write(sql_inserts)
    
    print("✓ Arquivo criado: inserir_postos_prf.sql")
    
    # 4. Salvar CSV também
    gdf_postos.to_csv('postos_prf.csv', index=False, encoding='utf-8')
    print("✓ Arquivo criado: postos_prf.csv")
    
    return gdf_postos

def inserir_direto_banco(connection_string):
    """
    Insere os dados diretamente no banco PostgreSQL
    
    Parâmetros:
    connection_string: String de conexão no formato:
                      "host=localhost dbname=seu_banco user=seu_user password=sua_senha"
    """
    print(f"Conectando ao banco PostgreSQL...")
    
    try:
        # Conectar ao banco
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
        
        # 1. Criar tabela
        print("Criando tabela postos_prf...")
        cur.execute(gerar_sql_create_table())
        
        # 2. Baixar e processar dados
        print("Baixando dados dos postos PRF...")
        data = baixar_dados_postos()
        if data is None:
            print("✗ Erro ao baixar dados")
            conn.rollback()
            return False
        
        gdf_postos = processar_dados_postos(data)
        
        # 3. Limpar tabela se já existir
        cur.execute("TRUNCATE TABLE postos_prf CASCADE;")
        
        # 4. Inserir dados
        print(f"Inserindo {len(gdf_postos)} postos...")
        
        for idx, row in gdf_postos.iterrows():
            geom_wkt = row.geometry.wkt
            
            cur.execute("""
                INSERT INTO postos_prf 
                (nome_posto, rodovia, uf, municipio, km, latitude, longitude, 
                 concessionaria, situacao, tipo_pista, sentido, geom)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                        ST_GeomFromText(%s, 4326))
            """, (
                row['nome_posto'],
                row['rodovia'],
                row['uf'],
                row['municipio'],
                row['km'],
                float(row['latitude']),
                float(row['longitude']),
                row['concessionaria'],
                row['situacao'],
                row['tipo_pista'],
                row['sentido'],
                geom_wkt
            ))
        
        # Commit
        conn.commit()
        cur.close()
        conn.close()
        
        print(f"✓ Sucesso! {len(gdf_postos)} postos inseridos na tabela 'postos_prf'")
        return True
        
    except Exception as e:
        print(f"✗ Erro ao inserir no banco: {e}")
        if conn:
            conn.rollback()
        return False

def main():
    """
    Menu principal
    """
    print("=" * 70)
    print("PREPARAÇÃO DE DADOS DOS POSTOS PRF PARA POSTGRESQL")
    print("=" * 70)
    print()
    print("Escolha uma opção:")
    print("1 - Gerar arquivos SQL (para executar manualmente)")
    print("2 - Inserir diretamente no banco PostgreSQL")
    print()
    
    opcao = input("Digite sua opção (1 ou 2): ").strip()
    
    if opcao == '1':
        print("\n=== GERANDO ARQUIVOS SQL ===\n")
        salvar_arquivos_sql()
        print("\n✓ Arquivos SQL gerados com sucesso!")
        print("\nPara executar no banco:")
        print("psql -U seu_usuario -d seu_banco -f criar_tabela_postos_prf.sql")
        print("psql -U seu_usuario -d seu_banco -f inserir_postos_prf.sql")
        
    elif opcao == '2':
        print("\n=== INSERÇÃO DIRETA NO BANCO ===\n")
        print("Informe os dados de conexão:")
        host = input("Host [localhost]: ").strip() or "localhost"
        dbname = input("Nome do banco: ").strip()
        user = input("Usuário: ").strip()
        password = input("Senha: ").strip()
        port = input("Porta [5432]: ").strip() or "5432"
        
        connection_string = f"host={host} dbname={dbname} user={user} password={password} port={port}"
        
        inserir_direto_banco(connection_string)
        
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()



