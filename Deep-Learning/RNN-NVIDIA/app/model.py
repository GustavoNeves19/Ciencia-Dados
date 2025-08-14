from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd

def predict_next_5_days(df, model, steps=10):
    """
    Função para prever os próximos 5 dias de preço de fechamento da ação.
    
    Parâmetros:
    df (DataFrame): Dados históricos da ação.
    model (keras.Model): Modelo LSTM treinado.
    steps (int): Número de passos para previsão, neste caso 10 dias de dados.
    
    Retorno:
    predictions (array): Previsões para os próximos 5 dias.
    dates (list): Datas correspondentes às previsões.
    """
    # Utiliza os últimos 10 dias de dados para previsão
    X_input = df['Close'].values[-steps:]  # Últimos 10 valores para previsão
    X_input = X_input.reshape((1, steps, 1))  # Redimensiona para formato adequado (1, steps, 1)
    
    # Fazendo previsões para os próximos 5 dias
    predictions = []
    for _ in range(5):
        pred = model.predict(X_input, verbose=0)
        predictions.append(pred[0, 0])  # Adiciona a previsão
        
        # Atualiza os dados de entrada para o próximo dia
        # Garantindo que 'pred' tenha o formato correto para concatenar com 'X_input'
        pred = pred.reshape(1, 1, 1)  # Redimensiona para (1, 1, 1)
        X_input = np.append(X_input[:, 1:, :], pred, axis=1)

    # Gera as datas das previsões (incrementando a data de fechamento)
    last_date = df['Date'].iloc[-1]
    dates = [last_date + pd.Timedelta(days=i + 1) for i in range(5)]  # Adiciona os 5 próximos dias

    return predictions, dates

