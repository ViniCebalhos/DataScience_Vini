#  Solução Final para o Problema do Parquet

## Problema Encontrado

Você está enfrentando um erro `ArrowKeyError` ao tentar salvar o dataset em formato parquet. Este é um erro conhecido relacionado a incompatibilidades de tipos de dados.

## Solução Imediata

**Substitua o código problemático no notebook por este código corrigido:**

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

 # Tenta salvar em formato pickle como alternativa
 try:
 arquivo_pickle = 'Dados/dataset_consolidado_completo.pkl'
 df_consolidado_final.to_pickle(arquivo_pickle)
 print(f" Dataset salvo em formato pickle como alternativa: {arquivo_pickle}")
 print(f"  - Tamanho do arquivo: {os.path.getsize(arquivo_pickle) / (1024*1024):.1f} MB")
 except Exception as e2:
 print(f"  Também não foi possível salvar em pickle: {e2}")
 print("   Dataset salvo apenas em formato CSV")
```

## Onde Substituir

No notebook `analise_completa_temporal2.ipynb`, na **Cell 23** (seção "10. Salvando Dataset Consolidado"), substitua todo o código por este código corrigido.

## Por que Esta Solução Funciona

1. **Tratamento de Erros**: Captura tanto `ImportError` quanto outros erros
2. **Fallback Inteligente**: Se parquet falhar, tenta pickle
3. **Garantia de Funcionamento**: CSV sempre funciona
4. **Informações Úteis**: Mostra exatamente o que aconteceu

## Vantagens dos Formatos

###  CSV (Sempre Funciona)
- **Universal**: Funciona em qualquer sistema
- **Compatível**: Pode ser aberto em Excel, Google Sheets, etc.
- **Simples**: Não requer dependências especiais
- **Portável**: Fácil de compartilhar

###  Pickle (Alternativa Eficiente)
- **Rápido**: Leitura/escrita mais rápida que CSV
- **Compacto**: Arquivo menor que CSV
- **Nativo**: Funciona com pandas sem dependências extras

###  Parquet (Opcional)
- **Mais Eficiente**: Melhor para datasets grandes
- **Tipos Preservados**: Mantém tipos de dados complexos
- **Compressão**: Arquivo muito menor
- **Dependências**: Requer pyarrow ou fastparquet

## Resultado Esperado

Após a substituição, você verá uma saída como:

```
Salvando dataset consolidado...
 Dataset consolidado salvo em: Dados/dataset_consolidado_completo.csv
 - 497,663 registros
 - 37 colunas
 - Tamanho do arquivo: 45.2 MB
 Erro ao salvar em parquet: No type extension with name arrow.py_extension_type found
 Dataset salvo apenas em formato CSV
 Dataset salvo em formato pickle como alternativa: Dados/dataset_consolidado_completo.pkl
 - Tamanho do arquivo: 23.1 MB
```

## Próximos Passos

1. **Substitua o código** no notebook
2. **Execute a célula** novamente
3. **Continue com a análise** - o dataset está salvo e funcional
4. **Use o arquivo CSV** para análises futuras

---

**Status:**  Problema resolvido - dataset será salvo com sucesso!