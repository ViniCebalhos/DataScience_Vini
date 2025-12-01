
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
    