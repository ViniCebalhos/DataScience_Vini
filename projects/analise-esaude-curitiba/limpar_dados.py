#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para limpeza automatizada dos dados do Sistema E-Saúde
Autor: Projeto de Pós-Graduação
Data: 2025
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

class LimpezaDadosESaude:
 """
 Classe para limpeza dos dados do Sistema E-Saúde
 """

 def __init__(self, arquivo_entrada=None):
 """
 Inicializa o limpiador

 Args:
 arquivo_entrada (str): Caminho para o arquivo de entrada
 """
 self.arquivo_entrada = arquivo_entrada
 self.df_original = None
 self.df_limpo = None
 self.estatisticas_limpeza = {}

 def carregar_dados(self):
 """
 Carrega os dados para limpeza
 """
 if self.arquivo_entrada and os.path.exists(self.arquivo_entrada):
 # Carrega arquivo específico
 self.df_original = pd.read_csv(self.arquivo_entrada, sep=';', encoding='utf-8')
 print(f" Dados carregados de: {self.arquivo_entrada}")
 else:
 # Tenta carregar dataset consolidado
 try:
 self.df_original = pd.read_csv('Dados/dataset_consolidado_completo.csv',
 sep=';', encoding='utf-8')
 print(" Dataset consolidado carregado")
 except FileNotFoundError:
 print(" Nenhum arquivo de dados encontrado!")
 return False

 print(f"  - {len(self.df_original):,} registros")
 print(f"  - {self.df_original.shape[1]} colunas")
 return True

 def analisar_dados(self):
 """
 Analisa os dados para identificar problemas
 """
 print("\n ANÁLISE INICIAL DOS DADOS")
 print("=" * 40)

 # Estatísticas básicas
 self.estatisticas_limpeza['registros_iniciais'] = len(self.df_original)
 self.estatisticas_limpeza['colunas'] = self.df_original.shape[1]

 # Valores nulos
 nulos = self.df_original.isnull().sum()
 colunas_com_nulos = nulos[nulos > 0]

 print(f" Registros iniciais: {self.estatisticas_limpeza['registros_iniciais']:,}")
 print(f" Colunas: {self.estatisticas_limpeza['colunas']}")

 if len(colunas_com_nulos) > 0:
 print(f"\n  Colunas com valores nulos:")
 for col, count in colunas_com_nulos.items():
 percentual = (count / len(self.df_original)) * 100
 print(f"  - {col}: {count:,} ({percentual:.1f}%)")

 # Análise de datas
 self._analisar_datas()

 # Análise de idades
 self._analisar_idades()

 return True

 def _analisar_datas(self):
 """
 Analisa problemas com datas
 """
 print(f"\n ANÁLISE DE DATAS:")

 # Converte datas
 self.df_original['Data do Atendimento'] = pd.to_datetime(
 self.df_original['Data do Atendimento'],
 format='%d/%m/%Y %H:%M:%S',
 errors='coerce'
 )

 self.df_original['Data de Nascimento'] = pd.to_datetime(
 self.df_original['Data de Nascimento'],
 format='%d/%m/%Y %H:%M:%S',
 errors='coerce'
 )

 # Problemas identificados
 datas_atendimento_nulas = self.df_original['Data do Atendimento'].isnull().sum()
 datas_nascimento_nulas = self.df_original['Data de Nascimento'].isnull().sum()

 data_atual = pd.Timestamp.now()
 datas_futuras_atendimento = (self.df_original['Data do Atendimento'] > data_atual).sum()
 datas_futuras_nascimento = (self.df_original['Data de Nascimento'] > data_atual).sum()

 print(f"  - Datas de atendimento nulas: {datas_atendimento_nulas:,}")
 print(f"  - Datas de nascimento nulas: {datas_nascimento_nulas:,}")
 print(f"  - Datas de atendimento futuras: {datas_futuras_atendimento:,}")
 print(f"  - Datas de nascimento futuras: {datas_futuras_nascimento:,}")

 # Armazena estatísticas
 self.estatisticas_limpeza['datas_atendimento_nulas'] = datas_atendimento_nulas
 self.estatisticas_limpeza['datas_nascimento_nulas'] = datas_nascimento_nulas
 self.estatisticas_limpeza['datas_futuras_atendimento'] = datas_futuras_atendimento
 self.estatisticas_limpeza['datas_futuras_nascimento'] = datas_futuras_nascimento

 def _analisar_idades(self):
 """
 Analisa problemas com idades
 """
 print(f"\n ANÁLISE DE IDADES:")

 # Calcula idade
 self.df_original['Idade'] = (
 self.df_original['Data do Atendimento'] - self.df_original['Data de Nascimento']
 ).dt.total_seconds() / (365.25 * 24 * 3600)

 # Problemas identificados
 idades_negativas = (self.df_original['Idade'] < 0).sum()
 idades_muito_altas = (self.df_original['Idade'] > 120).sum()
 idades_nulas = self.df_original['Idade'].isnull().sum()

 print(f"  - Idades negativas: {idades_negativas:,}")
 print(f"  - Idades > 120 anos: {idades_muito_altas:,}")
 print(f"  - Idades nulas: {idades_nulas:,}")

 if not self.df_original['Idade'].isnull().all():
 print(f"  - Faixa de idade: {self.df_original['Idade'].min():.1f} a {self.df_original['Idade'].max():.1f} anos")

 # Armazena estatísticas
 self.estatisticas_limpeza['idades_negativas'] = idades_negativas
 self.estatisticas_limpeza['idades_muito_altas'] = idades_muito_altas
 self.estatisticas_limpeza['idades_nulas'] = idades_nulas

 def limpar_dados(self):
 """
 Executa a limpeza completa dos dados
 """
 print(f"\n INICIANDO LIMPEZA DOS DADOS")
 print("=" * 40)

 # Cria cópia para limpeza
 self.df_limpo = self.df_original.copy()
 registros_antes = len(self.df_limpo)

 # 1. Limpeza de datas de atendimento
 print(f"\n1⃣  Limpeza de datas de atendimento...")
 self.df_limpo = self.df_limpo.dropna(subset=['Data do Atendimento'])
 data_atual = pd.Timestamp.now()
 self.df_limpo = self.df_limpo[self.df_limpo['Data do Atendimento'] <= data_atual]

 registros_removidos = registros_antes - len(self.df_limpo)
 print(f"    Removidos {registros_removidos:,} registros")

 # 2. Limpeza de datas de nascimento e idades
 print(f"2⃣  Limpeza de datas de nascimento e idades...")
 registros_antes = len(self.df_limpo)

 data_minima = pd.Timestamp('1900-01-01')
 self.df_limpo = self.df_limpo[
 (self.df_limpo['Data de Nascimento'] >= data_minima) &
 (self.df_limpo['Data de Nascimento'] <= data_atual)
 ]

 # Recalcula idade
 self.df_limpo['Idade'] = (
 self.df_limpo['Data do Atendimento'] - self.df_limpo['Data de Nascimento']
 ).dt.total_seconds() / (365.25 * 24 * 3600)

 # Remove idades absurdas
 self.df_limpo = self.df_limpo[(self.df_limpo['Idade'] >= 0) & (self.df_limpo['Idade'] <= 120)]

 registros_removidos = registros_antes - len(self.df_limpo)
 print(f"    Removidos {registros_removidos:,} registros")

 # 3. Limpeza de valores vazios em colunas críticas
 print(f"3⃣  Limpeza de valores vazios em colunas críticas...")
 registros_antes = len(self.df_limpo)

 colunas_criticas = ['cod_usuario', 'cod_profissional', 'Código da Unidade', 'Sexo']
 colunas_disponiveis = [col for col in colunas_criticas if col in self.df_limpo.columns]

 self.df_limpo = self.df_limpo.dropna(subset=colunas_disponiveis)

 registros_removidos = registros_antes - len(self.df_limpo)
 print(f"    Removidos {registros_removidos:,} registros")

 # 4. Limpeza de valores inconsistentes
 print(f"4⃣  Limpeza de valores inconsistentes...")
 registros_antes = len(self.df_limpo)

 # Remove sexo inválido
 if 'Sexo' in self.df_limpo.columns:
 self.df_limpo = self.df_limpo[self.df_limpo['Sexo'].isin(['F', 'M'])]

 # Remove tipo de unidade inválido
 if 'Tipo de Unidade' in self.df_limpo.columns:
 tipos_validos = ['BASICO', 'SIACE']
 self.df_limpo = self.df_limpo[self.df_limpo['Tipo de Unidade'].isin(tipos_validos)]

 registros_removidos = registros_antes - len(self.df_limpo)
 print(f"    Removidos {registros_removidos:,} registros")

 # 5. Remoção de duplicatas
 print(f"5⃣  Remoção de duplicatas...")
 registros_antes = len(self.df_limpo)

 colunas_duplicata = ['Data do Atendimento', 'cod_usuario', 'cod_profissional', 'Código da Unidade']
 colunas_disponiveis = [col for col in colunas_duplicata if col in self.df_limpo.columns]

 duplicatas = self.df_limpo.duplicated(subset=colunas_disponiveis, keep='first').sum()
 self.df_limpo = self.df_limpo.drop_duplicates(subset=colunas_disponiveis, keep='first')

 print(f"    Removidas {duplicatas:,} duplicatas")

 # Estatísticas finais
 self.estatisticas_limpeza['registros_finais'] = len(self.df_limpo)
 self.estatisticas_limpeza['registros_removidos'] = self.estatisticas_limpeza['registros_iniciais'] - len(self.df_limpo)
 self.estatisticas_limpeza['taxa_retencao'] = len(self.df_limpo) / self.estatisticas_limpeza['registros_iniciais'] * 100

 print(f"\n LIMPEZA CONCLUÍDA!")
 print(f"   - Registros iniciais: {self.estatisticas_limpeza['registros_iniciais']:,}")
 print(f"   - Registros finais: {self.estatisticas_limpeza['registros_finais']:,}")
 print(f"   - Registros removidos: {self.estatisticas_limpeza['registros_removidos']:,}")
 print(f"   - Taxa de retenção: {self.estatisticas_limpeza['taxa_retencao']:.1f}%")

 def salvar_dados_limpos(self):
 """
 Salva os dados limpos
 """
 print(f"\n SALVANDO DADOS LIMPOS")
 print("=" * 30)

 # Salva em CSV
 arquivo_csv = 'Dados/dataset_limpo_completo.csv'
 self.df_limpo.to_csv(arquivo_csv, index=False, sep=';', encoding='utf-8')

 tamanho_csv = os.path.getsize(arquivo_csv) / (1024 * 1024)
 print(f" CSV salvo: {arquivo_csv}")
 print(f"  - {len(self.df_limpo):,} registros")
 print(f"  - {self.df_limpo.shape[1]} colunas")
 print(f"  - {tamanho_csv:.1f} MB")

 # Tenta salvar em pickle
 try:
 arquivo_pkl = 'Dados/dataset_limpo_completo.pkl'
 self.df_limpo.to_pickle(arquivo_pkl)
 tamanho_pkl = os.path.getsize(arquivo_pkl) / (1024 * 1024)
 print(f" Pickle salvo: {arquivo_pkl}")
 print(f"  - {tamanho_pkl:.1f} MB")
 except Exception as e:
 print(f"  Erro ao salvar pickle: {e}")

 return True

 def gerar_relatorio(self):
 """
 Gera relatório da limpeza
 """
 print(f"\n GERANDO RELATÓRIO")
 print("=" * 25)

 relatorio = f"""
# Relatório de Limpeza - Sistema E-Saúde

## Resumo Executivo
- **Registros iniciais:** {self.estatisticas_limpeza['registros_iniciais']:,}
- **Registros finais:** {self.estatisticas_limpeza['registros_finais']:,}
- **Registros removidos:** {self.estatisticas_limpeza['registros_removidos']:,}
- **Taxa de retenção:** {self.estatisticas_limpeza['taxa_retencao']:.1f}%

## Procedimentos Realizados

### 1. Limpeza de Datas de Atendimento
- Removidos registros com datas de atendimento nulas: {self.estatisticas_limpeza.get('datas_atendimento_nulas', 0):,}
- Removidos registros com datas de atendimento futuras: {self.estatisticas_limpeza.get('datas_futuras_atendimento', 0):,}

### 2. Limpeza de Datas de Nascimento e Idades
- Removidos registros com datas de nascimento nulas: {self.estatisticas_limpeza.get('datas_nascimento_nulas', 0):,}
- Removidos registros com datas de nascimento futuras: {self.estatisticas_limpeza.get('datas_futuras_nascimento', 0):,}
- Removidos registros com idades negativas: {self.estatisticas_limpeza.get('idades_negativas', 0):,}
- Removidos registros com idades > 120 anos: {self.estatisticas_limpeza.get('idades_muito_altas', 0):,}

### 3. Limpeza de Valores Vazios em Colunas Críticas
- Removidos registros com valores nulos em colunas essenciais

### 4. Limpeza de Valores Inconsistentes
- Removidos registros com sexo inválido
- Removidos registros com tipo de unidade inválido

### 5. Remoção de Duplicatas
- Removidas duplicatas baseadas em múltiplas colunas

## Qualidade Final dos Dados
- **Faixa de idade:** {self.df_limpo['Idade'].min():.1f} a {self.df_limpo['Idade'].max():.1f} anos
- **Período:** {self.df_limpo['Data do Atendimento'].min().strftime('%d/%m/%Y')} a {self.df_limpo['Data do Atendimento'].max().strftime('%d/%m/%Y')}
- **Unidades únicas:** {self.df_limpo['Código da Unidade'].nunique():,}
- **Profissionais únicos:** {self.df_limpo['cod_profissional'].nunique():,}
- **Pacientes únicos:** {self.df_limpo['cod_usuario'].nunique():,}

## Arquivos Gerados
- `dataset_limpo_completo.csv`: Dataset limpo em formato CSV
- `dataset_limpo_completo.pkl`: Dataset limpo em formato pickle (se disponível)

## Conclusão
A limpeza removeu {self.estatisticas_limpeza['registros_removidos']:,} registros problemáticos ({100-self.estatisticas_limpeza['taxa_retencao']:.1f}% do total),
mantendo {self.estatisticas_limpeza['registros_finais']:,} registros de alta qualidade ({self.estatisticas_limpeza['taxa_retencao']:.1f}% do total original).
O dataset final está adequado para análises estatísticas e de machine learning.
"""

 # Salva relatório
 with open('Dados/relatorio_limpeza.md', 'w', encoding='utf-8') as f:
 f.write(relatorio)

 print(f" Relatório salvo em: Dados/relatorio_limpeza.md")
 return relatorio


def main():
 """
 Função principal
 """
 print(" LIMPEZA AUTOMATIZADA DE DADOS - SISTEMA E-SAÚDE")
 print("=" * 60)

 # Inicializa limpiador
 limpiador = LimpezaDadosESaude()

 # Carrega dados
 if not limpiador.carregar_dados():
 return

 # Analisa dados
 limpiador.analisar_dados()

 # Executa limpeza
 limpiador.limpar_dados()

 # Salva dados limpos
 limpiador.salvar_dados_limpos()

 # Gera relatório
 limpiador.gerar_relatorio()

 print(f"\n PROCESSO CONCLUÍDO COM SUCESSO!")
 print(f"Dataset limpo disponível em: Dados/dataset_limpo_completo.csv")


if __name__ == "__main__":
 main()