import streamlit as st
import pandas as pd
import joblib
import os
import plotly.express as px
from utils import process_validation_data

# Caminhos para os modelos
MODEL_PATH = os.path.join("..", "models", "extra_tress.pkl")
VECTORIZER_PATH = os.path.join("..", "models", "model_vectorizer_tfidef.pkl")
ENCODER_PATH = os.path.join("..", "models", "label_encoder.pkl")

# Cores para os sentimentos
COLOR_MAP = {
    "Positive": "green",
    "Negative": "red",
    "Neutral": "gray",
    "Irrelevant": "orange"
}

# Carregar modelos
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
label_encoder = joblib.load(ENCODER_PATH)

# Configuração da página
st.set_page_config(page_title="Análise de Sentimentos - Holding", layout="wide")
st.title("📊 Análise de Sentimentos sobre Empresas do Holding")
st.markdown("Envie um arquivo `.csv` com as colunas `tweetid`, `entity`, `target`, `content` para gerar insights estratégicos.")

# Upload do arquivo
uploaded_file = st.file_uploader("Envie o CSV com os comentários:", type="csv")

if uploaded_file is not None:
    with st.spinner("Processando os comentários e classificações..."):
        df = process_validation_data(uploaded_file)
        X = vectorizer.transform(df["text_combined"])
        pred = model.predict(X)
        df["Sentimento"] = label_encoder.inverse_transform(pred)

    st.success("Classificação concluída!")

    # Filtro por empresa
    empresas = ["Todas"] + sorted(df["entity"].unique().tolist())
    empresa_selecionada = st.selectbox("Filtrar por Empresa", empresas)
    df_filtrado = df if empresa_selecionada == "Todas" else df[df["entity"] == empresa_selecionada]

    # Painel de storytelling
    st.subheader("📈 Resumo dos Dados")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total de Comentários", len(df_filtrado))
    with col2:
        st.metric("Empresas Distintas", df_filtrado["entity"].nunique())

    st.markdown("---")
    st.subheader("🎯 Distribuição Geral dos Sentimentos")
    pie_fig = px.pie(df_filtrado, names="Sentimento", title="Distribuição Geral dos Sentimentos",
                     color="Sentimento", color_discrete_map=COLOR_MAP)
    st.plotly_chart(pie_fig, use_container_width=True)

    st.markdown("---")
    st.subheader("🏆 Top 5 Empresas com Mais Comentários")
    top_empresas = df_filtrado["entity"].value_counts().nlargest(5).reset_index()
    top_empresas.columns = ["Empresa", "Quantidade"]
    bar_top = px.bar(top_empresas, x="Empresa", y="Quantidade", title="Top 5 Empresas com Mais Comentários")
    st.plotly_chart(bar_top, use_container_width=True)

    st.markdown("---")
    st.subheader("📌 Ranking de Sentimentos por Empresa")
    sentiment_counts = df_filtrado.groupby(["entity", "Sentimento"]).size().reset_index(name="Quantidade")
    bar_sent = px.bar(sentiment_counts, x="entity", y="Quantidade", color="Sentimento",
                      title="Sentimentos por Empresa", barmode="group", color_discrete_map=COLOR_MAP)
    st.plotly_chart(bar_sent, use_container_width=True)

    st.markdown("---")
    st.subheader("📋 Comentários Classificados")
    st.dataframe(df_filtrado[["entity", "content", "Sentimento"]])

    # Download do CSV rotulado
    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar CSV com Sentimentos",
        data=csv,
        file_name="comentarios_classificados.csv",
        mime="text/csv"
    )
