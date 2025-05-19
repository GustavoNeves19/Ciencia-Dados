
import streamlit as st
import joblib
from app.utils import preprocess_text

# Carregar arquivos necessários
model = joblib.load("Natural Language Processing\models\extra_tress.pkl")
vectorizer = joblib.load("Natural Language Processing\models\model_vectorizer_tfidef.pkl")
label_encoder = joblib.load("Natural Language Processing\models\label_encoder.pkl")

# Interface do usuário
st.set_page_config(page_title="Análise de Sentimentos no Twitter", layout="centered")
st.title("🧠 Análise de Sentimentos no Twitter")

tweet = st.text_area("Digite o conteúdo do tweet a ser analisado:")

if st.button("Analisar"):
    if tweet.strip():
        texto_limpo = preprocess_text(tweet)
        texto_vectorizado = vectorizer.transform([texto_limpo])
        predicao = model.predict(texto_vectorizado)
        sentimento = label_encoder.inverse_transform(predicao)[0]
        st.success(f"💬 Sentimento identificado: **{sentimento}**")
    else:
        st.warning("Por favor, insira um texto antes de clicar em 'Analisar'.")
