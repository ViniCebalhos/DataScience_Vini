#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir o problema do parquet no notebook
Substitui o código problemático por uma versão que trata a ausência das dependências
"""

def corrigir_codigo_parquet():
 """
 Retorna o código corrigido para substituir no notebook
 """

 codigo_corrigido = '''
# Salva o dataset consolidado para uso futuro
print("Salvando dataset consolidado...")

# Remove colunas temporárias criadas para análise
colunas_para_remover = ['Ano', 'Mes', 'Dia', 'DiaSemana', 'Hora', 'Semana']
df_consolidado_final = df_completo.drop(columns=colunas_para_remover, errors='ignore')

# Salva em formato CSV
arquivo_saida = 'Dados/dataset_consolidado_completo.csv'
df_consolidado_final.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8')

print(f" Dataset consolidado salvo em: {arquivo_saida}")
print(f"  - {len(df_consolidado_final):,} registros")
print(f"  - {df_consolidado_final.shape[1]} colunas")
print(f"  - Tamanho do arquivo: {os.path.getsize(arquivo_saida) / (1024*1024):.1f} MB")

# Tenta salvar em formato parquet (mais eficiente)
try:
 arquivo_parquet = 'Dados/dataset_consolidado_completo.parquet'
 df_consolidado_final.to_parquet(arquivo_parquet, index=False)
 print(f" Dataset também salvo em formato parquet: {arquivo_parquet}")
 print(f"  - Tamanho do arquivo: {os.path.getsize(arquivo_parquet) / (1024*1024):.1f} MB")
except ImportError as e:
 print("  Formato parquet não disponível (pyarrow ou fastparquet não instalados)")
 print("   Para instalar: pip install pyarrow fastparquet")
 print("   Dataset salvo apenas em formato CSV")
except Exception as e:
 print(f"  Erro ao salvar em parquet: {e}")
 print("   Dataset salvo apenas em formato CSV")
'''

 return codigo_corrigido

def instrucoes_instalacao():
 """
 Retorna instruções para instalar as dependências do parquet
 """

 instrucoes = '''
 INSTRUÇÕES PARA INSTALAR DEPENDÊNCIAS DO PARQUET:

1. **Instalar pyarrow (recomendado):**
 ```bash
 pip install pyarrow
 ```

2. **Ou instalar fastparquet (alternativa):**
 ```bash
 pip install fastparquet
 ```

3. **Ou instalar ambas (mais seguro):**
 ```bash
 pip install pyarrow fastparquet
 ```

4. **Se estiver usando conda:**
 ```bash
 conda install pyarrow
 # ou
 conda install -c conda-forge pyarrow
 ```

5. **Verificar se foi instalado:**
 ```python
 import pyarrow
 print("pyarrow instalado com sucesso!")
 ```

 **NOTA:** Se não conseguir instalar, o dataset será salvo apenas em formato CSV,
que também funciona perfeitamente para a análise.
'''

 return instrucoes

def solucao_alternativa():
 """
 Retorna uma solução alternativa que não depende do parquet
 """

 solucao = '''
 SOLUÇÃO ALTERNATIVA (SEM PARQUET):

Se você não conseguir instalar pyarrow ou fastparquet, use este código:

```python
# Salva o dataset consolidado para uso futuro
print("Salvando dataset consolidado...")

# Remove colunas temporárias criadas para análise
colunas_para_remover = ['Ano', 'Mes', 'Dia', 'DiaSemana', 'Hora', 'Semana']
df_consolidado_final = df_completo.drop(columns=colunas_para_remover, errors='ignore')

# Salva em formato CSV
arquivo_saida = 'Dados/dataset_consolidado_completo.csv'
df_consolidado_final.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8')

print(f" Dataset consolidado salvo em: {arquivo_saida}")
print(f"  - {len(df_consolidado_final):,} registros")
print(f"  - {df_consolidado_final.shape[1]} colunas")
print(f"  - Tamanho do arquivo: {os.path.getsize(arquivo_saida) / (1024*1024):.1f} MB")

# Salva também em formato pickle (alternativa ao parquet)
try:
 arquivo_pickle = 'Dados/dataset_consolidado_completo.pkl'
 df_consolidado_final.to_pickle(arquivo_pickle)
 print(f" Dataset também salvo em formato pickle: {arquivo_pickle}")
 print(f"  - Tamanho do arquivo: {os.path.getsize(arquivo_pickle) / (1024*1024):.1f} MB")
except Exception as e:
 print(f"  Erro ao salvar em pickle: {e}")
 print("   Dataset salvo apenas em formato CSV")
```

 **Vantagens do CSV:**
- Formato universal, funciona em qualquer sistema
- Pode ser aberto em Excel, Google Sheets, etc.
- Não requer dependências especiais
- Fácil de compartilhar e versionar

 **Desvantagens do CSV:**
- Arquivo maior que parquet
- Leitura mais lenta para datasets grandes
- Não preserva tipos de dados complexos
'''

 return solucao

if __name__ == "__main__":
 print(" CORREÇÃO DO PROBLEMA DO PARQUET")
 print("=" * 50)
 print()

 print(" PROBLEMA:")
 print("ImportError: Unable to find a usable engine; tried using: 'pyarrow', 'fastparquet'")
 print()

 print(" SOLUÇÃO:")
 print("Substitua o código problemático no notebook por:")
 print()
 print(corrigir_codigo_parquet())

 print(" INSTRUÇÕES DE INSTALAÇÃO:")
 print(instrucoes_instalacao())

 print(" SOLUÇÃO ALTERNATIVA:")
 print(solucao_alternativa())

 print(" RECOMENDAÇÃO:")
 print("1. Tente instalar pyarrow primeiro")
 print("2. Se não conseguir, use a solução alternativa com CSV + pickle")
 print("3. O formato CSV é suficiente para a maioria das análises")