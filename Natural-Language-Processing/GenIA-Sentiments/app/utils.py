import nltk
import string
import pandas as pd

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
