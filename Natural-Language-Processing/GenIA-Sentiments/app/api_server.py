import os
import sys
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import string

# --- Dependências e Funções de Pré-Processamento (Essenciais para o Modelo ML) ---
# A API precisa realizar o pré-processamento exato usado no treinamento do modelo.
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import PorterStemmer
    
    # Garante que os recursos NLTK essenciais estejam disponíveis
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
        """Aplica o pré-processamento completo: lowercase, tokenização, remoção de stopwords/pontuação e stemming."""
        if not isinstance(text, str): return "" # Retorna vazio se não for string
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word not in STOPWORDS and word not in string.punctuation]
        tokens = [STEMMER.stem(word) for word in tokens]
        return ' '.join(tokens)
    
except ImportError:
    print("ERRO: NLTK ou suas dependências não instaladas. A API não funcionará corretamente.")
    def preprocess_text(text: str) -> str: return text # Fallback (A API falhará se não tiver as dependências)
    

# --- Configuração de Caminhos ---
# Define o caminho relativo para a pasta 'models/' (um nível acima da pasta 'app/')
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

MODEL_PATH = os.path.join(MODEL_DIR, "extra_tress.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "model_vectorizer_tfidef.pkl")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")

# --- Inicialização do FastAPI ---
app = FastAPI(
    title="GenAI Sentiment API",
    description="Serviço REST para Classificação de Sentimentos de Holdings usando Modelos de ML",
    version="1.0.0"
)

# --- Variáveis Globais para Modelos ---
model = None
vectorizer = None
label_encoder = None

@app.on_event("startup")
async def load_all_models():
    """Hook de inicialização: Carrega todos os artefatos de ML (modelo, vetorizador e encoder) antes de aceitar requisições."""
    global model, vectorizer, label_encoder
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        label_encoder = joblib.load(ENCODER_PATH)
        print("Modelos ML carregados com sucesso!")
    except FileNotFoundError as e:
        print(f"ERRO CRÍTICO: Arquivo de modelo não encontrado. {e}")
        sys.exit(1) # Impede a inicialização do servidor se os modelos estiverem faltando
    except Exception as e:
        print(f"ERRO CRÍTICO ao carregar modelos: {e}")
        sys.exit(1)


# --- Esquema de Dados (Pydantic) ---
class Comment(BaseModel):
    """Estrutura esperada para cada comentário na requisição de entrada."""
    content: str # O texto do comentário
    entity: str  # A entidade/empresa à qual o comentário se refere
    
    class Config: # Usado pelo FastAPI para gerar a documentação interativa
        json_schema_extra = {
            "example": {
                "content": "Estou muito satisfeito com o serviço, a equipe da EmpresaA foi muito ágil.",
                "entity": "EmpresaA"
            }
        }

class PredictionOutput(BaseModel):
    """Estrutura de saída: inclui o sentimento predito."""
    content: str
    entity: str
    sentiment: str # Sentimento classificado (Positive, Negative, Neutral, etc.)

class HealthCheck(BaseModel):
    """Resposta do endpoint de verificação de saúde."""
    status: str
    models_ready: bool
    
# --- Endpoints da API ---

@app.get("/health", response_model=HealthCheck, tags=["Monitoramento"])
async def health_check():
    """Verifica o status da API e confirma se os modelos de ML estão carregados e prontos para uso."""
    ready = model is not None and vectorizer is not None and label_encoder is not None
    return {
        "status": "online",
        "models_ready": ready
    }

@app.post("/predict/sentiment", response_model=list[PredictionOutput], tags=["Predição"])
async def predict_sentiment(comments: list[Comment]):
    """
    Recebe uma lista de comentários, aplica o pipeline ML (pré-processamento + vetorização)
    e classifica o sentimento de cada um.
    """
    # Verifica se os modelos estão prontos antes de processar
    if model is None or vectorizer is None or label_encoder is None:
        raise HTTPException(status_code=503, detail="Modelos ML não carregados. Serviço indisponível.")

    # 1. Converte a lista de Pydantic Models em DataFrame
    df_raw = pd.DataFrame([c.model_dump() for c in comments])
    
    # 2. Pré-processamento e Combinação de Texto (simulando a etapa de treinamento)
    df_raw['content_processed'] = df_raw['content'].apply(preprocess_text)
    df_raw['text_combined'] = df_raw['content_processed'] + ' ' + df_raw['entity']

    # 3. Vetorização e Predição
    X = vectorizer.transform(df_raw["text_combined"])
    pred = model.predict(X)
    
    # 4. Decodificação do Sentimento e Geração da Coluna 'sentiment'
    df_raw["sentiment"] = label_encoder.inverse_transform(pred)

    # 5. Prepara a lista de resposta no formato Pydantic
    response_list = [
        PredictionOutput(
            content=row['content'],
            entity=row['entity'],
            sentiment=row['sentiment']
        )
        for index, row in df_raw.iterrows()
    ]
    
    return response_list
