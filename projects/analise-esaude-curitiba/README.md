# Análise do Sistema E-Saúde - Profissionais de Nível Superior

## Descrição do Projeto

Este projeto de pós-graduação analisa dados do Sistema E-Saúde de Curitiba, focando nos atendimentos realizados por profissionais de nível superior (exceto médicos) nas unidades municipais de saúde.

## Estrutura do Projeto

```
Trabalho/
 Dados/                                    # Arquivos de dados
 *.csv                                # Datasets mensais (Dez/2024 - Jul/2025)
 *_Dicionario_de_Dados.csv           # Dicionário de dados
 dataset_consolidado_completo.csv    # Dataset consolidado (gerado)
 dataset_consolidado_completo.parquet # Dataset consolidado (formato eficiente)
 dataset_limpo_completo.csv          # Dataset limpo (gerado)
 dataset_limpo_completo.pkl          # Dataset limpo (formato eficiente)
 relatorio_limpeza.md                # Relatório de limpeza (gerado)
 documentacao_limpeza.md             # Documentação de limpeza (gerado)
 descricao_dataset.md                     # Descrição detalhada do dataset
 carregar_dados_completos.py             # Script para carregar todos os datasets
 limpar_dados.py                         # Script para limpeza automatizada
 limpeza_dados.ipynb                     # Notebook de limpeza detalhada
 analise_completa_temporal.ipynb         # Notebook de análise temporal completa
 exemplo_uso_completo.ipynb              # Exemplo de uso do script
 requirements.txt                         # Dependências do projeto
 README.md                               # Este arquivo
```

## Dataset

### Características Principais
- **Fonte**: Sistema E-Saúde da Prefeitura Municipal de Curitiba
- **Período**: Dezembro de 2024 a Julho de 2025
- **Volume**: ~46.000 registros por mês
- **Localização**: Município de Curitiba, Paraná

### Profissionais Abrangidos
- Fisioterapeutas
- Psicólogos
- Nutricionistas
- Educadores Físicos
- Outros profissionais de nível superior (exceto médicos)

### Tipos de Unidades
- **BASICO**: Unidades básicas de saúde
- **SIACE**: Centros de especialidades médicas

## Instalação e Configuração

1. **Clone ou baixe o projeto**
2. **Instale as dependências**:
 ```bash
 pip install -r requirements.txt
 ```

3. **Opções de execução**:

 **Opção A - Script Python:**
 ```bash
 python3 carregar_dados_completos.py
 ```

 **Opção B - Jupyter Notebook:**
 ```bash
 jupyter notebook exemplo_uso_completo.ipynb
 ```

 **Opção C - Limpeza de dados:**
 ```bash
 python3 limpar_dados.py
 # ou
 jupyter notebook limpeza_dados.ipynb
 ```

 **Opção D - Análise temporal completa:**
 ```bash
 jupyter notebook analise_completa_temporal.ipynb
 ```

## Análises Realizadas

### 1. Carregamento e Consolidação
- **Script automatizado** para carregar todos os datasets mensais
- **Consolidação temporal** de 8 meses de dados (Dez/2024 - Jul/2025)
- **Preparação de dados temporais** (datas, idades, períodos)
- **Geração de estatísticas básicas** automáticas

### 2. Limpeza e Qualidade dos Dados
- **Identificação automática** de valores inconsistentes e absurdos
- **Remoção de registros problemáticos** (datas futuras, idades negativas, etc.)
- **Eliminação de duplicatas** baseada em múltiplas colunas
- **Validação de integridade** dos dados críticos
- **Geração de relatórios** detalhados da limpeza

### 3. Análise Exploratória Inicial
- Carregamento e limpeza dos dados
- Estatísticas descritivas básicas
- Identificação de valores nulos e outliers

### 4. Análise Temporal Completa
- **Evolução mensal** de atendimentos
- Distribuição por dia da semana
- Padrões horários de atendimento
- **Sazonalidade** e tendências temporais
- **Correlações temporais** entre variáveis

### 5. Análise Geográfica
- Distribuição por bairros de Curitiba
- Concentração de atendimentos por região
- Análise de acessibilidade
- **Evolução geográfica** ao longo do tempo

### 6. Análise de Profissionais
- Perfil dos profissionais mais ativos
- Distribuição por especialidade
- Padrões de atendimento por categoria
- **Evolução temporal** dos profissionais

### 7. Análise Socioeconômica
- Condições habitacionais dos pacientes
- Acesso a serviços básicos
- Características demográficas

## Funcionalidades Principais

### Script de Carregamento (`carregar_dados_completos.py`)
- **Carregamento automático** de todos os datasets mensais
- **Consolidação inteligente** com identificação de períodos
- **Preparação de dados temporais** (datas, idades, períodos)
- **Geração de estatísticas** automáticas
- **Salvamento em múltiplos formatos** (CSV e Parquet)

### Script de Limpeza (`limpar_dados.py`)
- **Limpeza automatizada** de dados inconsistentes
- **Remoção de valores absurdos** (datas futuras, idades negativas, etc.)
- **Eliminação de duplicatas** baseada em múltiplas colunas
- **Validação de integridade** dos dados críticos
- **Geração de relatórios** detalhados da limpeza

### Notebooks de Análise
- **`exemplo_uso_completo.ipynb`**: Tutorial completo de uso
- **`limpeza_dados.ipynb`**: Limpeza detalhada com visualizações
- **`analise_completa_temporal.ipynb`**: Análise temporal detalhada
- **Visualizações interativas** e gráficos informativos
- **Análises estatísticas** avançadas

### Análises Disponíveis
- **Evolução temporal** de atendimentos
- **Distribuição geográfica** por bairros
- **Perfil dos profissionais** mais ativos
- **Padrões temporais** (dias da semana, horários)
- **Análise de sazonalidade** mensal
- **Correlações** entre variáveis

## Próximos Passos

1. **Análise de Correlações**: Identificar relações entre variáveis
2. **Análise de Clusters**: Segmentação de pacientes e profissionais
3. **Modelagem Preditiva**: Previsão de demanda por serviços
4. **Análise de Eficiência**: Avaliação de performance das unidades
5. **Dashboard Interativo**: Visualização dinâmica dos resultados

## Variáveis Principais

### Informações do Atendimento
- Data e hora do atendimento
- Tipo de unidade e código
- Procedimento realizado
- Diagnóstico (CID)

### Informações do Paciente
- Dados demográficos (idade, sexo, nacionalidade)
- Localização (município, bairro)
- Condições socioeconômicas
- Condições habitacionais

### Informações do Profissional
- Código CBO e descrição
- Área de atuação
- Código único do profissional

### Informações Farmacêuticas
- Medicamentos prescritos e dispensados
- Quantidade de medicamentos não padronizados

### Informações de Encaminhamento
- Solicitação de exames
- Encaminhamento para especialistas
- Internamentos (se aplicável)

## Contribuições

Este projeto visa contribuir para:
- Melhoria da gestão em saúde pública
- Identificação de padrões de atendimento
- Otimização da distribuição de recursos
- Análise de eficiência dos serviços
- Planejamento estratégico em saúde

## Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato através do repositório.

---

**Projeto de Pós-Graduação em Ciência de Dados**
*Análise de Dados em Saúde Pública*