import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Função para pré-processamento dos dados. 
    - Seleção das colunas "Date" e "Close"
    - Conversão de "Date" para formato datetime
    - Normalização da coluna "Close"
    - Configuração de "Date" como índice
    
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

    # Transformando "Date" em Index
    df = df.set_index(pd.DatetimeIndex(df["Date"].values))
    
    # Dropando a Coluna "Date" após transformá-la em índice
    df = df.drop("Date", axis=1, inplace=False)

    # Criando um novo DataFrame para armazenar os dados normalizados
    df_scaler = df.copy()  # Fazendo uma cópia do DataFrame original
    
    # Normalizando a coluna "Close" usando StandardScaler
    scaler = StandardScaler()
    df_scaler['Close'] = scaler.fit_transform(df[['Close']])
    
    return df_scaler, df
    

