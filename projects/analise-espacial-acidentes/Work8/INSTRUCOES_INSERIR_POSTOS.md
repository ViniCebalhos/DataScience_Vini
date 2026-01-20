#  Instruções para Adicionar Postos PRF no SGBD PostgreSQL

##  Arquivos Gerados

1. **`criar_tabela_postos_prf.sql`** (899 bytes)
 - SQL para criar a tabela `postos_prf`
 - Inclui índices espaciais (GIST)
 - Sistema de coordenadas: EPSG:4326 (WGS84)

2. **`inserir_postos_prf.sql`** (34 KB)
 - SQL para inserir 169 postos PRF
 - Dados baixados do portal ANTT (dados.antt.gov.br)

3. **`postos_prf.csv`** (24 KB)
 - Dados dos postos em formato CSV
 - Útil para importação via COPY ou ferramentas GUI

4. **`preparar_postos_prf_banco.py`**
 - Script Python para gerar os arquivos SQL
 - Opção de inserção direta no banco

##  Métodos de Inserção

### **Método 1: Via psql (Linha de Comando)**

```bash
# 1. Conectar ao banco
psql -U seu_usuario -h localhost -d nome_do_banco

# 2. Executar o CREATE TABLE
\i criar_tabela_postos_prf.sql

# 3. Executar os INSERTs
\i inserir_postos_prf.sql

# 4. Verificar os dados
SELECT COUNT(*) FROM postos_prf;
SELECT nome_posto, rodovia, uf FROM postos_prf LIMIT 10;
```

### **Método 2: Via PGAdmin ou DBeaver**

1. Abra a ferramenta gráfica (PGAdmin, DBeaver, etc.)
2. Conecte ao banco PostgreSQL
3. Execute os arquivos SQL na seguinte ordem:
 - `criar_tabela_postos_prf.sql` (cria a tabela)
 - `inserir_postos_prf.sql` (insere os dados)

### **Método 3: Via Python (Script Automatizado)**

```bash
# Executar o script Python
python preparar_postos_prf_banco.py

# Opção 2 - Inserção direta
# O script perguntará os dados de conexão
```

### **Método 4: Via PostgreSQL COPY (Mais Rápido)**

```bash
# 1. Criar a tabela primeiro
psql -U seu_usuario -d nome_do_banco -f criar_tabela_postos_prf.sql

# 2. Importar via COPY
psql -U seu_usuario -d nome_do_banco -c "
COPY postos_prf FROM '/caminho/completo/postos_prf.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',');
"
```

##  Estrutura da Tabela

```sql
CREATE TABLE postos_prf (
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
```

### **Campos Importantes:**
- `nome_posto`: Nome do posto PRF
- `rodovia`: Rodovia (ex: BR-116, BR-101)
- `uf`: Sigla do estado
- `municipio`: Município onde está o posto
- `latitude/longitude`: Coordenadas geográficas
- `geom`: Geometria espacial (Point) - PostGIS

### **Índices Criados:**
1. Índice espacial GIST na coluna `geom`
2. Índice na coluna `uf`
3. Índice na coluna `rodovia`

##  Queries Úteis

### **Verificar Dados Inseridos**
```sql
-- Contar total de postos
SELECT COUNT(*) AS total_postos FROM postos_prf;

-- Listar postos por estado
SELECT uf, COUNT(*) AS quantidade
FROM postos_prf
GROUP BY uf
ORDER BY quantidade DESC;

-- Postos por rodovia
SELECT rodovia, COUNT(*) AS quantidade
FROM postos_prf
GROUP BY rodovia
ORDER BY quantidade DESC;
```

### **Converter para SIRGAS 2000 (EPSG:4674)**
```sql
-- Adicionar coluna com geometria em SIRGAS 2000
ALTER TABLE postos_prf
ADD COLUMN geom_sirgas GEOMETRY(POINT, 4674);

UPDATE postos_prf
SET geom_sirgas = ST_Transform(geom, 4674);
```

### **Exemplo de Análise Espacial**
```sql
-- Encontrar postos próximos a um ponto específico (São Paulo)
SELECT nome_posto, municipio, rodovia, uf,
 ST_Distance(
 geom,
 ST_SetSRID(ST_MakePoint(-46.633309, -23.550520), 4326)
 ) AS distancia_km
FROM postos_prf
ORDER BY distancia_km
LIMIT 10;

-- Criar buffers de 10 km ao redor de cada posto
SELECT
 nome_posto,
 uf,
 ST_Buffer(ST_Transform(geom, 4674), 10000) AS buffer_10km
FROM postos_prf;
```

##  Notas Importantes

1. **Sistema de Coordenadas**:
 - Coordenadas originais: WGS84 (EPSG:4326)
 - Para usar com SIRGAS 2000, converter com `ST_Transform`

2. **Total de Postos**:
 - 169 postos ativos mapeados
 - Dados atualizados do portal ANTT

3. **Campos Geográficos**:
 - Latitude/Longitude: em decimal (WGS84)
 - `geom`: geometria PostGIS (Point)
 - Coordenadas brasileiras (latitude negativa)

##  Troubleshooting

### **Erro: Extensão PostGIS não habilitada**
```sql
-- Habilitar extensão PostGIS
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
```

### **Erro: Permissões insuficientes**
```sql
-- Verificar permissões do usuário
SELECT * FROM information_schema.role_table_grants
WHERE table_name='postos_prf';

-- Dar permissões necessárias (como superuser)
GRANT ALL PRIVILEGES ON TABLE postos_prf TO seu_usuario;
```

### **Verificar se PostGIS está instalado**
```sql
SELECT PostGIS_full_version();
SELECT PostGIS_version();
```

##  Informações dos Dados

- **Fonte**: Portal ANTT (Agência Nacional de Transportes Terrestres)
- **URL**: https://dados.antt.gov.br/dataset/postos-prf
- **Última atualização**: Dados de 2024
- **Formato**: JSON → CSV → PostgreSQL
- **Licença**: Dados abertos do governo federal

##  Integração com Tabela de Acidentes

Uma vez que os postos estiverem no banco, você pode fazer análises como:

```sql
-- Análise de acidentes próximos aos postos
SELECT
 p.nome_posto,
 p.uf,
 COUNT(a.id) AS acidentes_proximos
FROM postos_prf p
LEFT JOIN especializacao_vinicius_acidentes a
 ON ST_DWithin(
 a.geom,
 ST_Transform(p.geom, 4674),
 10000  -- 10 km em metros
 )
GROUP BY p.id, p.nome_posto, p.uf
ORDER BY acidentes_proximos DESC;
```

##  Checklist de Verificação

Após inserir os dados, verifique:
- [ ] Tabela `postos_prf` criada
- [ ] 169 registros inseridos
- [ ] Índices criados
- [ ] Geometria espacial funcionando (`SELECT ST_AsText(geom) FROM postos_prf LIMIT 1`)
- [ ] Postos distribuídos no Brasil
- [ ] Coordenadas válidas (latitude entre -35 e 5, longitude entre -75 e -30)

##  Suporte

Para dúvidas:
1. Verificar logs do PostgreSQL
2. Verificar sintaxe SQL com `EXPLAIN`
3. Testar queries isoladamente
4. Consultar documentação PostGIS: https://postgis.net/

---

**Desenvolvido por**: Vinicius de Souza Cebalhos
**Data**: Outubro 2024
**Universidade**: UTFPR



