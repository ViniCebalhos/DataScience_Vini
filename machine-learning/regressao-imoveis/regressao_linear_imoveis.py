"""
Script de Regressão Linear para Previsão de Preços de Imóveis
Atividade de Machine Learning - Pós-graduação

Este script:
1. Carrega os dados de treino e teste
2. Treina um modelo de Regressão Linear
3. Exibe os coeficientes, intercepto e equação do modelo
4. Faz previsões no conjunto de teste
5. Calcula e exibe o Erro Quadrático Médio (MSE)
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder


def carregar_dados(caminho_arquivo):
    """
    Carrega os dados de um arquivo CSV.
    
    Parâmetros:
    -----------
    caminho_arquivo : str
        Caminho para o arquivo CSV a ser carregado
    
    Retorna:
    --------
    pd.DataFrame
        DataFrame com os dados carregados
    """
    print(f"\n{'='*60}")
    print(f"Carregando dados de: {caminho_arquivo}")
    print(f"{'='*60}")
    
    # Carrega o arquivo CSV usando ponto e vírgula como separador
    dados = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')
    
    print(f"Dados carregados com sucesso!")
    print(f"Shape do dataset: {dados.shape}")
    print(f"\nPrimeiras linhas do dataset:")
    print(dados.head())
    
    return dados


def preparar_dados(dados, conjunto='treino'):
    """
    Prepara os dados separando features e target, e codificando variáveis categóricas.
    
    Parâmetros:
    -----------
    dados : pd.DataFrame
        DataFrame com os dados brutos
    conjunto : str
        'treino' ou 'teste' - indica qual conjunto está sendo preparado
    
    Retorna:
    --------
    X : pd.DataFrame
        DataFrame com as features (variáveis de entrada)
    y : pd.Series
        Série com a variável alvo (Valor de Venda)
    label_encoders : dict
        Dicionário com os encoders usados (apenas para treino)
    """
    print(f"\n{'='*60}")
    print(f"Preparando dados do conjunto de {conjunto}")
    print(f"{'='*60}")
    
    # Faz uma cópia para não modificar o original
    dados_prep = dados.copy()
    
    # Remove a coluna 'Índice' se existir (não é uma feature útil)
    if 'Índice' in dados_prep.columns:
        dados_prep = dados_prep.drop('Índice', axis=1)
    
    # Separa a variável alvo (target)
    y = dados_prep['Valor de Venda']
    
    # Separa as features (todas as colunas exceto a variável alvo)
    X = dados_prep.drop('Valor de Venda', axis=1)
    
    print(f"\nVariáveis de entrada (features):")
    print(X.columns.tolist())
    print(f"\nVariável alvo: Valor de Venda")
    print(f"\nShape de X: {X.shape}")
    print(f"Shape de y: {y.shape}")
    
    # Identifica variáveis categóricas
    variaveis_categoricas = X.select_dtypes(include=['object']).columns.tolist()
    
    if variaveis_categoricas:
        print(f"\nVariáveis categóricas encontradas: {variaveis_categoricas}")
        
        # Para o conjunto de treino, cria os encoders
        if conjunto == 'treino':
            label_encoders = {}
            
            # Usa One-Hot Encoding para variáveis categóricas
            # Isso cria colunas dummy para cada categoria
            X_encoded = pd.get_dummies(X, columns=variaveis_categoricas, drop_first=False)
            
            print(f"\nApós codificação:")
            print(f"Shape de X: {X_encoded.shape}")
            print(f"Novas colunas criadas: {X_encoded.columns.tolist()}")
            
            return X_encoded, y, variaveis_categoricas
        
        else:  # conjunto de teste
            # Para teste, precisamos garantir que temos as mesmas colunas do treino
            # Isso será tratado na função treinar_modelo
            X_encoded = pd.get_dummies(X, columns=variaveis_categoricas, drop_first=False)
            return X_encoded, y, None
    
    else:
        print("\nNenhuma variável categórica encontrada.")
        return X, y, None


def treinar_modelo(X_treino, y_treino):
    """
    Treina um modelo de Regressão Linear.
    
    Parâmetros:
    -----------
    X_treino : pd.DataFrame
        Features do conjunto de treino
    y_treino : pd.Series
        Valores alvo do conjunto de treino
    
    Retorna:
    --------
    model : LinearRegression
        Modelo treinado
    """
    print(f"\n{'='*60}")
    print("Treinando modelo de Regressão Linear")
    print(f"{'='*60}")
    
    # Cria e treina o modelo
    model = LinearRegression()
    model.fit(X_treino, y_treino)
    
    print("Modelo treinado com sucesso!")
    
    return model


def exibir_informacoes_modelo(model, X_treino):
    """
    Exibe os coeficientes, intercepto e equação do modelo.
    
    Parâmetros:
    -----------
    model : LinearRegression
        Modelo treinado
    X_treino : pd.DataFrame
        Features do conjunto de treino (para obter nomes das colunas)
    """
    print(f"\n{'='*60}")
    print("INFORMAÇÕES DO MODELO")
    print(f"{'='*60}")
    
    # Obtém o intercepto
    intercepto = model.intercept_
    print(f"\nIntercepto (b0): {intercepto:.2f}")
    
    # Obtém os coeficientes
    coeficientes = model.coef_
    nomes_features = X_treino.columns.tolist()
    
    print(f"\nCoeficientes da regressão:")
    print("-" * 60)
    for i, (nome, coef) in enumerate(zip(nomes_features, coeficientes), 1):
        print(f"b{i} ({nome}): {coef:.2f}")
    
    # Constrói a equação do modelo
    print(f"\n{'='*60}")
    print("EQUAÇÃO DO MODELO:")
    print(f"{'='*60}")
    print("\npreco = b0 + b1*x1 + b2*x2 + ... + bn*xn\n")
    print("Onde:")
    print(f"b0 = {intercepto:.2f}")
    
    equacao = f"preco = {intercepto:.2f}"
    for i, (nome, coef) in enumerate(zip(nomes_features, coeficientes), 1):
        sinal = "+" if coef >= 0 else ""
        equacao += f" {sinal}{coef:.2f}*{nome}"
        print(f"b{i} = {coef:.2f}  (variável: {nome})")
    
    print(f"\n{'-'*60}")
    print("Equação completa:")
    print(f"{equacao}")
    print(f"{'='*60}\n")


def alinhar_colunas_teste(X_treino, X_teste):
    """
    Alinha as colunas do conjunto de teste com as do conjunto de treino.
    Isso é necessário porque o One-Hot Encoding pode criar colunas diferentes.
    
    Parâmetros:
    -----------
    X_treino : pd.DataFrame
        Features do conjunto de treino
    X_teste : pd.DataFrame
        Features do conjunto de teste
    
    Retorna:
    --------
    X_teste_alinhado : pd.DataFrame
        Features do teste com colunas alinhadas ao treino
    """
    # Obtém as colunas do treino
    colunas_treino = X_treino.columns.tolist()
    
    # Adiciona colunas faltantes no teste (com zeros)
    for col in colunas_treino:
        if col not in X_teste.columns:
            X_teste[col] = 0
    
    # Remove colunas extras do teste (que não existem no treino)
    X_teste_alinhado = X_teste[colunas_treino]
    
    return X_teste_alinhado


def avaliar_modelo(model, X_teste, y_teste):
    """
    Faz previsões no conjunto de teste e calcula o MSE.
    
    Parâmetros:
    -----------
    model : LinearRegression
        Modelo treinado
    X_teste : pd.DataFrame
        Features do conjunto de teste
    y_teste : pd.Series
        Valores alvo reais do conjunto de teste
    
    Retorna:
    --------
    y_pred : np.array
        Valores previstos
    mse : float
        Erro Quadrático Médio
    """
    print(f"\n{'='*60}")
    print("Avaliando modelo no conjunto de teste")
    print(f"{'='*60}")
    
    # Faz as previsões
    y_pred = model.predict(X_teste)
    
    print(f"\nPrevisões realizadas para {len(y_pred)} amostras")
    print(f"\nPrimeiras 5 previsões:")
    for i in range(min(5, len(y_pred))):
        print(f"  Amostra {i+1}: Valor real = {y_teste.iloc[i]:.2f}, "
              f"Valor previsto = {y_pred[i]:.2f}")
    
    # Calcula o MSE
    mse = mean_squared_error(y_teste, y_pred)
    
    print(f"\n{'='*60}")
    print("RESULTADO DA AVALIAÇÃO")
    print(f"{'='*60}")
    print(f"\nErro Quadrático Médio (MSE): {mse:.2f}")
    print(f"{'='*60}\n")
    
    return y_pred, mse


def main():
    """
    Função principal que executa todo o pipeline de machine learning.
    """
    print("\n" + "="*60)
    print("SCRIPT DE REGRESSÃO LINEAR - PREVISÃO DE PREÇOS DE IMÓVEIS")
    print("="*60)
    
    # 1. Carregar dados de treino
    dados_treino = carregar_dados("Imoveis_Fabro_treino.csv")
    
    # 2. Preparar dados de treino
    X_treino, y_treino, variaveis_categoricas = preparar_dados(dados_treino, conjunto='treino')
    
    # 3. Treinar o modelo
    model = treinar_modelo(X_treino, y_treino)
    
    # 4. Exibir informações do modelo
    exibir_informacoes_modelo(model, X_treino)
    
    # 5. Carregar dados de teste
    dados_teste = carregar_dados("Imoveis_Fabro_teste.csv")
    
    # 6. Preparar dados de teste
    X_teste, y_teste, _ = preparar_dados(dados_teste, conjunto='teste')
    
    # 7. Alinhar colunas do teste com as do treino
    X_teste_alinhado = alinhar_colunas_teste(X_treino, X_teste)
    
    # 8. Avaliar o modelo
    y_pred, mse = avaliar_modelo(model, X_teste_alinhado, y_teste)
    
    print("\n" + "="*60)
    print("PROCESSO CONCLUÍDO COM SUCESSO!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()

