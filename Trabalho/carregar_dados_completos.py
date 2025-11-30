#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para carregar e consolidar todos os datasets do Sistema E-Saúde
Autor: Projeto de Pós-Graduação
Data: 2025
"""

import pandas as pd
import numpy as np
import glob
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class CarregadorDadosESaude:
    """
    Classe para carregar e processar dados do Sistema E-Saúde
    """
    
    def __init__(self, pasta_dados='Dados/'):
        """
        Inicializa o carregador
        
        Args:
            pasta_dados (str): Caminho para a pasta com os arquivos CSV
        """
        self.pasta_dados = pasta_dados
        self.datasets_mensais = {}
        self.df_consolidado = None
        
    def listar_arquivos(self):
        """
        Lista todos os arquivos CSV disponíveis
        
        Returns:
            list: Lista de arquivos CSV encontrados
        """
        arquivos_csv = glob.glob(os.path.join(self.pasta_dados, '*.csv'))
        arquivos_csv = [f for f in arquivos_csv if 'Dicionario' not in f]
        arquivos_csv.sort()
        
        print(f"Encontrados {len(arquivos_csv)} arquivos de dados:")
        for arquivo in arquivos_csv:
            tamanho_mb = os.path.getsize(arquivo) / (1024 * 1024)
            print(f"  - {os.path.basename(arquivo)} ({tamanho_mb:.1f} MB)")
            
        return arquivos_csv
    
    def carregar_dataset(self, arquivo):
        """
        Carrega um dataset individual
        
        Args:
            arquivo (str): Caminho do arquivo CSV
            
        Returns:
            pd.DataFrame: Dataset carregado
        """
        try:
            # Extrai período do nome do arquivo
            nome_arquivo = os.path.basename(arquivo)
            periodo = nome_arquivo.split('_')[0]
            
            print(f"Carregando {nome_arquivo}...")
            
            # Carrega o dataset
            df = pd.read_csv(arquivo, sep=';', encoding='latin1')
            
            # Adiciona coluna de período
            df['Periodo'] = periodo
            
            print(f"  ✓ {len(df):,} registros carregados")
            
            return df, periodo
            
        except Exception as e:
            print(f"  ✗ Erro ao carregar {arquivo}: {e}")
            return None, None
    
    def carregar_todos_datasets(self):
        """
        Carrega todos os datasets e cria o consolidado
        
        Returns:
            tuple: (dicionário de datasets mensais, dataframe consolidado)
        """
        arquivos = self.listar_arquivos()
        
        if not arquivos:
            print("Nenhum arquivo CSV encontrado!")
            return {}, None
        
        # Carrega cada dataset
        for arquivo in arquivos:
            df, periodo = self.carregar_dataset(arquivo)
            if df is not None:
                self.datasets_mensais[periodo] = df
        
        # Concatena todos os datasets
        if self.datasets_mensais:
            self.df_consolidado = pd.concat(self.datasets_mensais.values(), ignore_index=True)
            print(f"\n✓ Dataset consolidado criado com {len(self.df_consolidado):,} registros totais")
        else:
            print("\n✗ Nenhum dataset foi carregado com sucesso")
        
        return self.datasets_mensais, self.df_consolidado
    
    def preparar_dados_temporais(self):
        """
        Prepara dados temporais para análise
        
        Returns:
            pd.DataFrame: Dataset com dados temporais preparados
        """
        if self.df_consolidado is None:
            print("Nenhum dataset carregado!")
            return None
        
        print("Preparando dados temporais...")
        
        # Converte datas
        self.df_consolidado['Data do Atendimento'] = pd.to_datetime(
            self.df_consolidado['Data do Atendimento'], 
            format='%d/%m/%Y %H:%M:%S', 
            errors='coerce'
        )
        
        self.df_consolidado['Data de Nascimento'] = pd.to_datetime(
            self.df_consolidado['Data de Nascimento'], 
            format='%d/%m/%Y %H:%M:%S', 
            errors='coerce'
        )
        
        # Extrai informações temporais
        self.df_consolidado['Ano'] = self.df_consolidado['Data do Atendimento'].dt.year
        self.df_consolidado['Mes'] = self.df_consolidado['Data do Atendimento'].dt.month
        self.df_consolidado['Dia'] = self.df_consolidado['Data do Atendimento'].dt.day
        self.df_consolidado['DiaSemana'] = self.df_consolidado['Data do Atendimento'].dt.day_name()
        self.df_consolidado['Hora'] = self.df_consolidado['Data do Atendimento'].dt.hour
        self.df_consolidado['Semana'] = self.df_consolidado['Data do Atendimento'].dt.isocalendar().week
        
        # Calcula idade
        self.df_consolidado['Idade'] = (
            self.df_consolidado['Data do Atendimento'] - self.df_consolidado['Data de Nascimento']
        ).dt.total_seconds() / (365.25 * 24 * 3600)
        
        print("✓ Dados temporais preparados")
        return self.df_consolidado
    
    def gerar_estatisticas_basicas(self):
        """
        Gera estatísticas básicas do dataset consolidado
        
        Returns:
            dict: Dicionário com estatísticas
        """
        if self.df_consolidado is None:
            print("Nenhum dataset carregado!")
            return {}
        
        stats = {
            'total_registros': len(self.df_consolidado),
            'periodo_inicio': self.df_consolidado['Data do Atendimento'].min(),
            'periodo_fim': self.df_consolidado['Data do Atendimento'].max(),
            'unidades_unicas': self.df_consolidado['Código da Unidade'].nunique(),
            'profissionais_unicos': self.df_consolidado['cod_profissional'].nunique(),
            'pacientes_unicos': self.df_consolidado['cod_usuario'].nunique(),
            'bairros_unicos': self.df_consolidado['Bairro'].nunique(),
            'procedimentos_unicos': self.df_consolidado['Código do Procedimento'].nunique(),
            'cbo_unicos': self.df_consolidado['Descrição do CBO'].nunique()
        }
        
        # Calcula duração em dias
        stats['duracao_dias'] = (stats['periodo_fim'] - stats['periodo_inicio']).days
        stats['media_diaria'] = stats['total_registros'] / stats['duracao_dias']
        
        return stats
    
    def salvar_dataset_consolidado(self, formato='csv'):
        """
        Salva o dataset consolidado
        
        Args:
            formato (str): Formato de saída ('csv' ou 'parquet')
        """
        if self.df_consolidado is None:
            print("Nenhum dataset para salvar!")
            return
        
        # Remove colunas temporárias criadas para análise
        colunas_para_remover = ['Ano', 'Mes', 'Dia', 'DiaSemana', 'Hora', 'Semana']
        df_final = self.df_consolidado.drop(columns=colunas_para_remover, errors='ignore')
        
        if formato.lower() == 'csv':
            arquivo_saida = os.path.join(self.pasta_dados, 'dataset_consolidado_completo.csv')
            df_final.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8')
        elif formato.lower() == 'parquet':
            arquivo_saida = os.path.join(self.pasta_dados, 'dataset_consolidado_completo.parquet')
            df_final.to_parquet(arquivo_saida, index=False)
        else:
            print(f"Formato {formato} não suportado!")
            return
        
        tamanho_mb = os.path.getsize(arquivo_saida) / (1024 * 1024)
        print(f"✓ Dataset consolidado salvo em: {arquivo_saida}")
        print(f"  - {len(df_final):,} registros")
        print(f"  - {df_final.shape[1]} colunas")
        print(f"  - Tamanho: {tamanho_mb:.1f} MB")
    
    def obter_evolucao_mensal(self):
        """
        Obtém evolução mensal dos atendimentos
        
        Returns:
            pd.DataFrame: DataFrame com evolução mensal
        """
        if self.df_consolidado is None:
            print("Nenhum dataset carregado!")
            return None
        
        evolucao = self.df_consolidado.groupby(['Ano', 'Mes']).size().reset_index(name='Atendimentos')
        evolucao['Data'] = pd.to_datetime(evolucao[['Ano', 'Mes']].assign(day=1))
        return evolucao.sort_values('Data')
    
    def obter_top_profissionais(self, top_n=10):
        """
        Obtém os profissionais mais ativos
        
        Args:
            top_n (int): Número de profissionais a retornar
            
        Returns:
            pd.Series: Série com os profissionais mais ativos
        """
        if self.df_consolidado is None:
            print("Nenhum dataset carregado!")
            return None
        
        return self.df_consolidado['Descrição do CBO'].value_counts().head(top_n)
    
    def obter_top_bairros(self, top_n=10):
        """
        Obtém os bairros com mais atendimentos
        
        Args:
            top_n (int): Número de bairros a retornar
            
        Returns:
            pd.Series: Série com os bairros mais atendidos
        """
        if self.df_consolidado is None:
            print("Nenhum dataset carregado!")
            return None
        
        return self.df_consolidado['Bairro'].value_counts().head(top_n)


def main():
    """
    Função principal para demonstração do uso
    """
    print("=" * 60)
    print("CARREGADOR DE DADOS - SISTEMA E-SAÚDE")
    print("=" * 60)
    
    # Inicializa o carregador
    carregador = CarregadorDadosESaude()
    
    # Carrega todos os datasets
    datasets_mensais, df_consolidado = carregador.carregar_todos_datasets()
    
    if df_consolidado is not None:
        # Prepara dados temporais
        carregador.preparar_dados_temporais()
        
        # Gera estatísticas
        stats = carregador.gerar_estatisticas_basicas()
        
        print("\n" + "=" * 60)
        print("ESTATÍSTICAS BÁSICAS")
        print("=" * 60)
        print(f"Total de registros: {stats['total_registros']:,}")
        print(f"Período: {stats['periodo_inicio'].strftime('%d/%m/%Y')} a {stats['periodo_fim'].strftime('%d/%m/%Y')}")
        print(f"Duração: {stats['duracao_dias']} dias")
        print(f"Média diária: {stats['media_diaria']:.0f} atendimentos")
        print(f"Unidades únicas: {stats['unidades_unicas']}")
        print(f"Profissionais únicos: {stats['profissionais_unicos']}")
        print(f"Pacientes únicos: {stats['pacientes_unicos']}")
        print(f"Bairros únicos: {stats['bairros_unicos']}")
        
        # Salva dataset consolidado
        print("\nSalvando dataset consolidado...")
        carregador.salvar_dataset_consolidado('csv')
        carregador.salvar_dataset_consolidado('parquet')
        
        print("\n" + "=" * 60)
        print("CARREGAMENTO CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        
        return carregador
    else:
        print("Falha no carregamento dos dados!")
        return None


if __name__ == "__main__":
    carregador = main() 