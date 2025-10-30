import os
import sys
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import string

# --- Dependências de Pré-Processamento (Copiadas de utils.py) ---
# Em um ambiente de produção real, você garantiria que essas dependências fossem instaladas.
# A NLTK pode ser lenta para baixar em ambientes de servidor, então é melhor pré-instalar.
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import PorterStemmer
    
    # Tentativa de download de recursos (garante que funcionará se não existirem)
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except nltk.downloader.DownloadError:
        print("Recursos NLTK não encontrados. Tentando download...")
        nltk.download('punkt')
        nltk.download('stopwords')
        
    STOPWORDS = set(stopwords.words('english'))
    STEMMER = PorterStemmer()

    def preprocess_text(text: str) -> str:
        """Realiza o pré-processamento de um texto (lowercase, tokenização, remoção de stopwords/pontuação, stemming)."""
        if not isinstance(text, str): return ""
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word not in STOPWORDS and word not in string.punctuation]
        tokens = [STEMMER.stem(word) for word in tokens]
        return ' '.join(tokens)
    
except ImportError:
    print("NLTK ou suas dependências não instaladas. A API não funcionará corretamente.")
    def preprocess_text(text: str) -> str: return text # Fallback dummy
    

# --- Configuração de Caminhos ---
# Ajuste estes caminhos se o seu 'models' estiver em um local diferente
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

MODEL_PATH = os.path.join(MODEL_DIR, "extra_tress.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "model_vectorizer_tfidef.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")

# --- Inicialização do FastAPI ---
app = FastAPI(
    title="GenAI Sentiment API",
    description="API para Classificação de Sentimentos de Holdings usando Modelos de ML",
    version="1.0.0"
)

# --- Carregamento de Modelos ---
model = None
vectorizer = None
label_encoder = None

@app.on_event("startup")
async def load_all_models():
    """Carrega todos os modelos de ML e o vetorizador na inicialização do servidor."""
    global model, vectorizer, label_encoder
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        label_encoder = joblib.load(ENCODER_PATH)
        print("Modelos ML carregados com sucesso!")
    except FileNotFoundError as e:
        print(f"ERRO: Arquivo de modelo não encontrado: {e}")
        # É crucial que o servidor não inicie se os modelos não estiverem lá
        sys.exit(1)
    except Exception as e:
        print(f"ERRO ao carregar modelos: {e}")
        sys.exit(1)


# --- Esquema de Dados (Pydantic) ---
class Comment(BaseModel):
    """Define a estrutura de um único comentário para o consumidor da API."""
    content: str
    entity: str
    
    class Config: # Adicionado na última interação para gerar o exemplo no docs
        json_schema_extra = {
            "example": {
                "content": "Estou muito satisfeito com o serviço, a equipe da EmpresaA foi muito ágil.",
                "entity": "EmpresaA"
            }
        }

class PredictionOutput(BaseModel):
    """Define a estrutura de saída da previsão."""
    content: str
    entity: str
    sentiment: str

class HealthCheck(BaseModel):
    """Resposta de verificação de saúde."""
    status: str
    models_ready: bool
    
# --- Endpoints ---

@app.get("/health", response_model=HealthCheck, tags=["Monitoramento"])
async def health_check():
    """Verifica se a API está de pé e se os modelos foram carregados."""
    return {
        "status": "online",
        "models_ready": model is not None and vectorizer is not None and label_encoder is not None
    }

@app.post("/predict/sentiment", response_model=list[PredictionOutput], tags=["Predição"])
async def predict_sentiment(comments: list[Comment]):
    """
    Recebe uma lista de comentários e entidades, classifica o sentimento 
    (Positivo, Negativo, Neutro, Irrelevant) e retorna a lista rotulada.
    """
    if model is None or vectorizer is None or label_encoder is None:
        raise HTTPException(status_code=503, detail="Modelos ML não carregados. Serviço indisponível.")

    # 1. Preparação dos dados
    df_raw = pd.DataFrame([c.dict() for c in comments])
    
    # 2. Pré-processamento
    df_raw['content_processed'] = df_raw['content'].apply(preprocess_text)
    
    # 3. Combinação de texto (como feito no treinamento)
    df_raw['text_combined'] = df_raw['content_processed'] + ' ' + df_raw['entity']

    # 4. Vetorização e Predição
    X = vectorizer.transform(df_raw["text_combined"])
    pred = model.predict(X)
    
    # 5. Decodificação do Sentimento
    df_raw["sentiment"] = label_encoder.inverse_transform(pred)

    # 6. Preparação da resposta
    response_list = [
        PredictionOutput(
            content=row['content'],
            entity=row['entity'],
            sentiment=row['sentiment']
        )
        for index, row in df_raw.iterrows()
    ]
    
    return response_list
