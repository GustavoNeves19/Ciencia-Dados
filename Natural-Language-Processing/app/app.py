import os
import urllib.request
import streamlit as st
import joblib
from utils import preprocess_text


# Carregar arquivos necessários

MODEL_PATH = "models/extra_tress.pkl"
MODEL_URL = "https://drive.google.com/uc?export=download&id=1HO8VPMqEGOATPbw1GTIZOKlNBEOdbWMm"

# Verifica se o modelo já está salvo localmente
if not os.path.exists(MODEL_PATH):
    os.makedirs("models", exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

# Carrega o modelo
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load("models/model_vectorizer_tfidef.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

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
