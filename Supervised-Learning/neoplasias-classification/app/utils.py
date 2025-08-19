# utils.py
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

def load_data(path):
    """
    Carrega o dataset de neoplasias.

    Parâmetros:
        path (str): Caminho do arquivo CSV ou Excel

    Retorna:
        DataFrame: Dados carregados
    """
    return pd.read_csv(path)

def evaluate_model(model, X_train, y_train, X_test, y_test):
    """
    Avalia o modelo com métricas de classificação e imprime os resultados.

    Parâmetros:
        model: Modelo treinado
        X_train, y_train: Dados de treino
        X_test, y_test: Dados de teste
    """
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    print("🔎 Avaliação - Treinamento")
    print(f"Acurácia: {accuracy_score(y_train, y_train_pred):.4f}")
    print(f"Precisão: {precision_score(y_train, y_train_pred):.4f}")
    print(f"Recall: {recall_score(y_train, y_train_pred):.4f}")
    print(f"F1 Score: {f1_score(y_train, y_train_pred):.4f}\n")

    print("🔎 Avaliação - Teste")
    print(f"Acurácia: {accuracy_score(y_test, y_test_pred):.4f}")
    print(f"Precisão: {precision_score(y_test, y_test_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_test_pred):.4f}")
    print(f"F1 Score: {f1_score(y_test, y_test_pred):.4f}\n")

    print("📊 Classification Report:\n", classification_report(y_test, y_test_pred))
    print("📌 Matriz de Confusão:\n", confusion_matrix(y_test, y_test_pred))
