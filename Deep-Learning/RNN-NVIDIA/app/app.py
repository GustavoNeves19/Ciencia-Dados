import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
from preprocessing import preprocess_data
from model import predict_next_5_days  # Função para previsões com o modelo
from tensorflow.keras.models import load_model
import joblib

# Caminho para o modelo e scaler
MODEL_PATH = os.path.join("..", "models", "modelo_lstm.h5")
SCALER_PATH = os.path.join("..", "models", "scaler.pkl")

# Carregar o modelo e o scaler já treinados
model = load_model(MODEL_PATH, compile=False)
scaler = joblib.load(SCALER_PATH)

# Compilando o modelo manualmente
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])

# Exibindo título na interface Streamlit
st.title("Previsão de Preços de Ações da NVIDIA")

# Carregar o DataFrame com o arquivo CSV
uploaded_file = st.file_uploader("Carregue o arquivo de dados", type=["csv"])

if uploaded_file is not None:
    # Leitura do arquivo CSV
    df = pd.read_csv(uploaded_file)

    df_processed, df_close = preprocess_data(df)
    
    # Exibição dos dados carregados
    st.write("### Dados Carregados")
    st.write(df.head())

    st.write("### Distribuição dos Valores de Fechamento")
    # Plotando o gráfico de dados reais
    plt.figure(figsize=(10, 6))
    plt.plot(df_close.index, df_close['Close'], label='Preço Real', linestyle='solid')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (USD)')
    plt.title('Preço Real das Ações da NVIDIA')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    
    # Exibindo os dados processados
    st.write("### Dados Processados")
    st.write(df_processed.head())
    
    #Exibindo os Ultimos 10 dias do DataFrame
    st.write("### Ultimos 10 dias")
    st.write(df_close.tail(10))
    
    # Realizando a previsão usando o modelo LSTM
    df_forecast = predict_next_5_days(df_processed, model, scaler)

    # Exibindo o DataFrame com os 5 dias futuros e as previsões
    st.write("### Previsões para os Próximos 5 Dias")
    st.write(df_forecast)


    # Plotando o gráfico de dados reais e previstos para os últimos 10 dias + 5 previsões
    plt.figure(figsize=(16,8))
    plt.plot(df_close['Close'].tail(10), label='Preço Real', linestyle='solid')
    plt.plot(df_forecast['Close'], label='Preço Previsto', linestyle='dashed')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (USD)')
    plt.title('REAL X PREVISÃO (Últimos 10 dias + Previsões)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
