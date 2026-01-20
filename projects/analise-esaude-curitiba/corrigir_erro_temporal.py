#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir o erro de criação de datas no pandas
Problema: pd.to_datetime com colunas 'Ano' e 'Mes' não funciona corretamente
Solução: Usar método alternativo para criar datas
"""

import pandas as pd
import numpy as np
from datetime import datetime

def corrigir_criacao_data():
 """
 Demonstra como corrigir o erro de criação de datas
 """

 # Simula dados como no dataset real
 dados_exemplo = {
 'Ano': [2024, 2024, 2025, 2025],
 'Mes': [12, 12, 1, 1],
 'Atendimentos': [1000, 1200, 1100, 1300]
 }

 df_exemplo = pd.DataFrame(dados_exemplo)
 print("Dados de exemplo:")
 print(df_exemplo)
 print()

 #  MÉTODO QUE CAUSA ERRO
 print(" MÉTODO QUE CAUSA ERRO:")
 print("atendimentos_por_mes['Data'] = pd.to_datetime(atendimentos_por_mes[['Ano', 'Mes']].assign(day=1))")
 print("Erro: ValueError: to assemble mappings requires at least that [year, month, day] be specified")
 print()

 #  MÉTODOS CORRETOS

 print(" MÉTODO 1 - Usando pd.to_datetime com formato:")
 try:
 # Método 1: Criar string de data primeiro
 df_exemplo['Data_String'] = df_exemplo['Ano'].astype(str) + '-' + df_exemplo['Mes'].astype(str).str.zfill(2) + '-01'
 df_exemplo['Data'] = pd.to_datetime(df_exemplo['Data_String'])
 print(" Funcionou!")
 print(df_exemplo[['Ano', 'Mes', 'Data_String', 'Data']])
 except Exception as e:
 print(f" Erro: {e}")
 print()

 print(" MÉTODO 2 - Usando pd.to_datetime com dicionário:")
 try:
 # Método 2: Criar dicionário com year, month, day
 df_exemplo['Data2'] = pd.to_datetime({
 'year': df_exemplo['Ano'],
 'month': df_exemplo['Mes'],
 'day': 1
 })
 print(" Funcionou!")
 print(df_exemplo[['Ano', 'Mes', 'Data2']])
 except Exception as e:
 print(f" Erro: {e}")
 print()

 print(" MÉTODO 3 - Usando datetime diretamente:")
 try:
 # Método 3: Usar datetime diretamente
 df_exemplo['Data3'] = df_exemplo.apply(
 lambda row: datetime(row['Ano'], row['Mes'], 1), axis=1
 )
 print(" Funcionou!")
 print(df_exemplo[['Ano', 'Mes', 'Data3']])
 except Exception as e:
 print(f" Erro: {e}")
 print()

 return df_exemplo

def solucao_para_notebook():
 """
 Retorna o código corrigido para usar no notebook
 """

 print(" CÓDIGO CORRIGIDO PARA O NOTEBOOK:")
 print("=" * 50)

 print("""
#  CÓDIGO QUE CAUSA ERRO:
atendimentos_por_mes = df_completo.groupby(['Ano', 'Mes']).size().reset_index(name='Atendimentos')
atendimentos_por_mes['Data'] = pd.to_datetime(atendimentos_por_mes[['Ano', 'Mes']].assign(day=1))

#  CÓDIGO CORRIGIDO - OPÇÃO 1:
atendimentos_por_mes = df_completo.groupby(['Ano', 'Mes']).size().reset_index(name='Atendimentos')
atendimentos_por_mes['Data'] = pd.to_datetime({
 'year': atendimentos_por_mes['Ano'],
 'month': atendimentos_por_mes['Mes'],
 'day': 1
})

#  CÓDIGO CORRIGIDO - OPÇÃO 2:
atendimentos_por_mes = df_completo.groupby(['Ano', 'Mes']).size().reset_index(name='Atendimentos')
atendimentos_por_mes['Data'] = atendimentos_por_mes.apply(
 lambda row: datetime(row['Ano'], row['Mes'], 1), axis=1
)

#  CÓDIGO CORRIGIDO - OPÇÃO 3:
atendimentos_por_mes = df_completo.groupby(['Ano', 'Mes']).size().reset_index(name='Atendimentos')
atendimentos_por_mes['Data'] = pd.to_datetime(
 atendimentos_por_mes['Ano'].astype(str) + '-' +
 atendimentos_por_mes['Mes'].astype(str).str.zfill(2) + '-01'
)
""")

def corrigir_todas_ocorrencias():
 """
 Lista todas as ocorrências que precisam ser corrigidas no notebook
 """

 print(" OCORRÊNCIAS QUE PRECISAM SER CORRIGIDAS NO NOTEBOOK:")
 print("=" * 60)

 ocorrencias = [
 "evolucao_profissionais['Data'] = pd.to_datetime(evolucao_profissionais[['Ano', 'Mes']].assign(day=1))",
 "evolucao_bairros['Data'] = pd.to_datetime(evolucao_bairros[['Ano', 'Mes']].assign(day=1))",
 "atendimentos_por_mes['Data'] = pd.to_datetime(atendimentos_por_mes[['Ano', 'Mes']].assign(day=1))"
 ]

 for i, ocorrencia in enumerate(ocorrencias, 1):
 print(f"{i}. {ocorrencia}")
 print(f"   → Substituir por:")
 print(f"   → pd.to_datetime({{'year': df['Ano'], 'month': df['Mes'], 'day': 1}})")
 print()

if __name__ == "__main__":
 print(" CORREÇÃO DO ERRO DE CRIAÇÃO DE DATAS NO PANDAS")
 print("=" * 60)
 print()

 # Demonstra o erro e as soluções
 df_corrigido = corrigir_criacao_data()

 # Mostra o código corrigido
 solucao_para_notebook()

 # Lista todas as ocorrências
 corrigir_todas_ocorrencias()

 print(" RECOMENDAÇÃO:")
 print("Use o MÉTODO 2 (pd.to_datetime com dicionário) pois é mais claro e eficiente.")
 print("Substitua todas as ocorrências no notebook pelo código corrigido.")