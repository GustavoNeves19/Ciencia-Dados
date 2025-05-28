import nltk
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Baixando recursos necessários do NLTK (apenas na primeira execução)
nltk.download('punkt')
nltk.download('stopwords')

# Configurações globais
STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()
COLS = ['tweetid', 'entity', 'target', 'content']  # Nomes esperados no CSV original

def preprocess_text(text: str) -> str:
    """
    Realiza o pré-processamento de um texto:
    - Lowercase
    - Tokenização
    - Remoção de pontuação e stopwords
    - Stemming

    Args:
        text (str): Texto original.

    Returns:
        str: Texto pré-processado.
    """
    # 1. Coloca o texto em minúsculas e faz a tokenização
    tokens = word_tokenize(text.lower())

    # 2. Remove stopwords e pontuações
    tokens = [word for word in tokens if word not in STOPWORDS and word not in string.punctuation]

    # 3. Aplica stemming
    tokens = [STEMMER.stem(word) for word in tokens]

    # 4. Reconstrói a frase
    return ' '.join(tokens)

def process_validation_data(csv_file) -> pd.DataFrame:
    """
    Carrega e trata um CSV contendo dados de comentários.

    O tratamento inclui:
    - Remoção de colunas desnecessárias
    - Exclusão de registros com valores ausentes
    - Aplicação do pré-processamento de texto
    - Combinação das colunas 'content' e 'entity'

    Args:
        csv_file: Arquivo CSV enviado via interface Streamlit.

    Returns:
        pd.DataFrame: DataFrame com texto combinado e pronto para vetorização.
    """
    df = pd.read_csv(csv_file, names=COLS)

    # Remove colunas não utilizadas
    df.drop(columns=['tweetid', 'target'], inplace=True)

    # Remove registros incompletos
    df.dropna(inplace=True)

    # Aplica pré-processamento no campo de texto
    df['content'] = df['content'].apply(preprocess_text)

    # Combina conteúdo com o nome da entidade
    df['text_combined'] = df['content'] + ' ' + df['entity']

    return df
