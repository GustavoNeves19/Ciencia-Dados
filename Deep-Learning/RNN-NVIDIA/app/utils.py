# utils.py
from pathlib import Path
import random
import numpy as np
import matplotlib.pyplot as plt
import joblib
import tensorflow as tf


# ------------------------ reprodutibilidade ------------------------

def set_seed(seed: int = 42):
    """Configura seeds para resultados reproduzíveis."""
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


# ------------------------ filesystem ------------------------

def ensure_dirs(*paths: Path):
    """Garante que os diretórios existam (cria se necessário)."""
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)


# ------------------------ persistência ------------------------

def save_scaler(scaler, path: Path):
    """Salva um scaler (ex.: MinMaxScaler) em disco."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(scaler, path)

def load_scaler(path: Path):
    """Carrega um scaler salvo em disco."""
    return joblib.load(path)


# ------------------------ visualizações ------------------------

def plot_training(history, out_path: Path, title: str = "Training history (LSTM)"):
    """
    Plota e salva o histórico de treinamento (loss/val_loss).
    history: objeto History do Keras.
    """
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))
    plt.plot(history.history.get("loss", []), label="loss")
    if "val_loss" in history.history:
        plt.plot(history.history["val_loss"], label="val_loss")
    plt.xlabel("Epoch")
    plt.ylabel("MSE")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=140)
    plt.close()


def plot_forecast(dates, true_series, pred_series, out_path: Path, title: str = "5-day Forecast"):
    """
    Plota a série real (histórico) + previsão (linha tracejada) e salva a figura.
    - dates: index/array de datas (histórico + futuro)
    - true_series: array com históricos + NaNs nos pontos previstos
    - pred_series: array com histórico + previsões substituindo o trecho futuro
    """
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, true_series, label="True", linewidth=2)
    plt.plot(dates, pred_series, label="Forecast", linestyle="--")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Close")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=140)
    plt.close()
