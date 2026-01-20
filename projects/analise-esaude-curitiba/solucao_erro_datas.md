#  Solução para o Erro de Criação de Datas no Pandas

## Problema Encontrado

O erro ocorreu ao tentar criar uma coluna de data a partir das colunas 'Ano' e 'Mes':

```python
#  CÓDIGO QUE CAUSA ERRO:
atendimentos_por_mes['Data'] = pd.to_datetime(atendimentos_por_mes[['Ano', 'Mes']].assign(day=1))
```

**Erro:** `ValueError: to assemble mappings requires at least that [year, month, day] be specified: [month,year] is missing`

## Causa do Problema

O pandas espera que as colunas tenham nomes específicos (`year`, `month`, `day`) quando usado com `.assign(day=1)`. Como as colunas se chamam 'Ano' e 'Mes', o pandas não consegue mapeá-las corretamente.

## Soluções Implementadas

###  Solução 1: Usando dicionário (RECOMENDADA)

```python
#  CÓDIGO CORRIGIDO:
atendimentos_por_mes['Data'] = pd.to_datetime({
 'year': atendimentos_por_mes['Ano'],
 'month': atendimentos_por_mes['Mes'],
 'day': 1
})
```

###  Solução 2: Usando string de data

```python
#  CÓDIGO CORRIGIDO:
atendimentos_por_mes['Data'] = pd.to_datetime(
 atendimentos_por_mes['Ano'].astype(str) + '-' +
 atendimentos_por_mes['Mes'].astype(str).str.zfill(2) + '-01'
)
```

###  Solução 3: Usando datetime diretamente

```python
#  CÓDIGO CORRIGIDO:
from datetime import datetime
atendimentos_por_mes['Data'] = atendimentos_por_mes.apply(
 lambda row: datetime(row['Ano'], row['Mes'], 1), axis=1
)
```

## Correções Aplicadas no Notebook

As seguintes linhas foram corrigidas no arquivo `analise_completa_temporal2.ipynb`:

1. **Linha com `evolucao_profissionais`**:
 ```python
 # Antes:
 evolucao_profissionais['Data'] = pd.to_datetime(evolucao_profissionais[['Ano', 'Mes']].assign(day=1))

 # Depois:
 evolucao_profissionais['Data'] = pd.to_datetime({'year': evolucao_profissionais['Ano'], 'month': evolucao_profissionais['Mes'], 'day': 1})
 ```

2. **Linha com `evolucao_bairros`**:
 ```python
 # Antes:
 evolucao_bairros['Data'] = pd.to_datetime(evolucao_bairros[['Ano', 'Mes']].assign(day=1))

 # Depois:
 evolucao_bairros['Data'] = pd.to_datetime({'year': evolucao_bairros['Ano'], 'month': evolucao_bairros['Mes'], 'day': 1})
 ```

3. **Linha com `atendimentos_por_mes`**:
 ```python
 # Antes:
 atendimentos_por_mes['Data'] = pd.to_datetime(atendimentos_por_mes[['Ano', 'Mes']].assign(day=1))

 # Depois:
 atendimentos_por_mes['Data'] = pd.to_datetime({'year': atendimentos_por_mes['Ano'], 'month': atendimentos_por_mes['Mes'], 'day': 1})
 ```

## Erro Adicional Corrigido

Também foi corrigido um erro de `KeyError: 'Ano'` que ocorreu porque a variável `df` não existia no contexto. A correção foi usar o nome correto da variável:

```python
#  Erro:
evolucao_bairros['Data'] = pd.to_datetime({'year': df['Ano'], 'month': df['Mes'], 'day': 1})

#  Correção:
evolucao_bairros['Data'] = pd.to_datetime({'year': evolucao_bairros['Ano'], 'month': evolucao_bairros['Mes'], 'day': 1})
```

## Recomendação

**Use a Solução 1 (dicionário)** pois é:
- Mais clara e legível
- Mais eficiente
- Menos propensa a erros
- Padrão recomendado pelo pandas

## Como Evitar no Futuro

1. **Sempre use nomes específicos** quando criar datas com pandas
2. **Verifique se as variáveis existem** antes de referenciá-las
3. **Teste o código** com dados pequenos antes de aplicar em datasets grandes
4. **Use a documentação do pandas** para verificar a sintaxe correta

---

**Status:**  Todos os erros foram corrigidos no notebook `analise_completa_temporal2.ipynb`