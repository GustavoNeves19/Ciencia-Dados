import os
import urllib.request
import streamlit as st
import joblib
from utils import preprocess_text

MODEL_URL = "https://drive.google.com/uc?export=download&id=1HO8VPMqEGOATPbw1GTIZOKlNBEOdbWMm"
MODEL_PATH = os.path.join("..", "models", "extra_tress.pkl")
VECTORIZER_PATH = os.path.join("..", "models", "model_vectorizer_tfidef.pkl")
ENCODER_PATH = os.path.join("..", "models", "label_encoder.pkl")

if not os.path.exists(MODEL_PATH):
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
label_encoder = joblib.load(ENCODER_PATH)

st.set_page_config(page_title="Análise de Sentimentos no Twitter")
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
