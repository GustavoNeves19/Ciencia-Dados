import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from preprocessing import preprocess_data
from model import predict_next_5_days
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam

# Caminho para o modelo
MODEL_PATH = os.path.join("..", "models", "modelo_lstm.h5")

# Carregar o modelo sem compilar
model = load_model(MODEL_PATH, compile=False)

# Compilando o modelo manualmente
model.compile(optimizer=Adam(), loss=MeanSquaredError(), metrics=['mse'])

# Exibindo título na interface Streamlit
st.title("Previsão de Preços de Ações da NVIDIA")

# Carregar o DataFrame com o arquivo CSV
uploaded_file = st.file_uploader("Carregue o arquivo de dados", type=["csv"])

if uploaded_file is not None:
    # Leitura do arquivo CSV
    df = pd.read_csv(uploaded_file)
    
    # Exibição dos dados carregados
    st.write("### Dados Carregados")
    st.write(df.head())
    
    # Pré-processamento dos dados
    df_processed = preprocess_data(df)
    
    # Exibindo os dados processados
    st.write("### Dados Processados")
    st.write(df_processed.head())
    
    # Realizando a previsão usando o modelo LSTM
    predictions, dates = predict_next_5_days(df_processed, model)
    
    # Exibindo as previsões
    st.write("### Previsões para os Próximos Dias")
    st.write(predictions)
    
    dates = pd.to_datetime(dates)  # Converte as datas para o formato datetime

    # Agora, plote os dados
    plt.figure(figsize=(10, 6))
    plt.plot(dates, predictions, label='Preço Previsto', linestyle='dashed')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (USD)')
    plt.title('Preço Real vs Previsão de Fechamento das Ações da NVIDIA')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Exibindo o gráfico no Streamlit
    st.pyplot(plt)
