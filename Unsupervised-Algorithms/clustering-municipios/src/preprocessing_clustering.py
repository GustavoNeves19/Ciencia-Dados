# src/data/preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def preprocess_data(df, features=None):
    """
    Aplica tratamento nos dados:
    - Seleciona features
    - Imputa valores ausentes com a média
    - Padroniza os dados

    Parâmetros:
        df (pd.DataFrame): DataFrame original
        features (list): Lista de colunas para manter (None = todas)

    Retorna:
        df_scaled (pd.DataFrame): DataFrame com variáveis padronizadas
    """
    df_proc = df.copy()

    if features is not None:
        df_proc = df_proc[features]

    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(imputer.fit_transform(df_proc), columns=df_proc.columns)

    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df_imputed), columns=df_imputed.columns)

    return df_scaled

def reduce_dimensions(df_scaled, n_components=5):
    """
    Aplica PCA para reduzir a dimensionalidade.

    Parâmetros:
        df_scaled (pd.DataFrame): Dados já padronizados
        n_components (int): Número de componentes principais

    Retorna:
        pca_data (np.ndarray): Dados transformados
        pca (PCA): Objeto PCA ajustado
    """
    pca = PCA(n_components=n_components)
    pca_data = pca.fit_transform(df_scaled)
    return pca_data, pca

def apply_kmeans(pca_data, n_clusters):
    """
    Aplica o algoritmo K-Means

    Parâmetros:
        pca_data (np.ndarray): Dados reduzidos por PCA
        n_clusters (int): Número de clusters desejado

    Retorna:
        labels (np.ndarray): Labels atribuídos a cada instância
        kmeans (KMeans): Modelo KMeans ajustado
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(pca_data)
    return labels, kmeans
