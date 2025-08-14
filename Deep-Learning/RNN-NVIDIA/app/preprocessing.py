import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Função para pré-processamento dos dados. 
    - Seleção das colunas "Date" e "Close"
    - Conversão de "Date" para formato datetime
    - Normalização da coluna "Close"
    
    Parâmetros:
    df (DataFrame): DataFrame contendo os dados históricos.

    Retorno:
    df_processed (DataFrame): DataFrame com as colunas processadas.
    """
    
    # Selecionando as colunas "Date" e "Close"
    df = df[['Date', 'Close']]
    
    # Convertendo a coluna "Date" para datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Ordenando os dados pela data
    df = df.sort_values('Date')
    
    # Normalizando a coluna "Close" usando MinMaxScaler (opcional, mas útil para redes neurais)
    scaler = StandardScaler()
    df['Close'] = scaler.fit_transform(df[['Close']])
    
    return df
