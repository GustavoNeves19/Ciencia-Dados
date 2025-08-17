import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def create_df(df, steps=10):
    """
    Função para criar os dados de entrada (X) e saída (Y) com base no fechamento da ação.
    
    Parâmetros:
    df (DataFrame): Dados históricos da ação.
    steps (int): Número de passos para previsão (ex: 10 dias de dados).
    
    Retorno:
    dataX, dataY: Dados de entrada e saída para o modelo.
    """
    dataX, dataY = [], []
    for i in range(len(df) - steps - 1):
        a = df[i:(i + steps), 0]
        dataX.append(a)
        dataY.append(df[i + steps, 0])
    return np.array(dataX), np.array(dataY)

def predict_next_5_days(df, model, scaler, steps=10):
    """
    Função para prever os próximos 5 dias de preço de fechamento da ação.
    
    Parâmetros:
    df (DataFrame): Dados históricos da ação.
    model (keras.Model): Modelo LSTM treinado.
    scaler (scaler): Scaler utilizado para normalização dos dados.
    steps (int): Número de passos para previsão (número de dias passados para fazer a previsão).
    
    Retorno:
    predictions (array): Previsões para os próximos 5 dias.
    dates (list): Datas correspondentes às previsões.
    """
    # Inicializa a lista de previsões
    pred_output = []  # Lista para armazenar as previsões
    list_output = df['Close'].values[-steps:].tolist()  # Últimos 10 valores para previsão

    # Previsão para os próximos 5 dias
    n_future = 5
    i = 0

    while i < n_future:
        # Se houver dados suficientes, faz a previsão
        if len(list_output) > steps:
            # Cria os dados de entrada para o modelo
            inputs_steps = np.array(list_output[1:])
            inputs_steps = inputs_steps.reshape(1, -1)
            inputs_steps = inputs_steps.reshape(1, steps, 1)

            # Realiza a previsão
            pred = model.predict(inputs_steps, verbose=0)
            pred_output.append(pred[0, 0])

            # Atualiza os dados de entrada
            list_output.extend(pred[0].tolist())
            list_output = list_output[1:]
            i += 1
        else:
            # Se não houver dados suficientes, faz a previsão com os dados iniciais
            inputs_steps = np.array(list_output).reshape((1, steps, 1))
            pred = model.predict(inputs_steps, verbose=0)
            pred_output.append(pred[0, 0])
            list_output.extend(pred[0].tolist())
            i += 1
    
    # Desnormalizando as previsões
    predictions = scaler.inverse_transform(np.array(pred_output).reshape(-1, 1)).flatten()

    # Geração das datas de previsão
    last_date = df.index[-1]
    future_dates = pd.date_range(last_date + pd.DateOffset(1), periods=5, freq="B")

     # Cria o DataFrame com as previsões e suas respectivas datas
    df_forecast = pd.DataFrame({
        'Date': future_dates,
        'Close': predictions
    })

    # Definindo a coluna "Date" como índice
    df_forecast.set_index('Date', inplace=True)

    return df_forecast

