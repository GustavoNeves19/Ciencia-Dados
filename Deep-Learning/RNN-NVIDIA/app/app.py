# app.py
import argparse
import random
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

from Config import (
    DATA_CSV, MODELS_DIR, REPORTS_DIR, SCALER_PATH, MODEL_PATH,
    HISTORY_PLOT, FORECAST_PLOT, TARGET_COL,
    WINDOW, HORIZON, TRAIN_RATIO, VAL_RATIO,
    EPOCHS, BATCH_SIZE, LR, RANDOM_SEED
)
from model import build_lstm, default_callbacks


# ------------------------ utils ------------------------

def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

def ensure_dirs(*paths: Path):
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)

def plot_training(history, out_path: Path):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(9,5))
    plt.plot(history.history["loss"], label="loss")
    if "val_loss" in history.history:
        plt.plot(history.history["val_loss"], label="val_loss")
    plt.xlabel("Epoch"); plt.ylabel("MSE"); plt.title("Training history (LSTM)")
    plt.legend(); plt.tight_layout()
    plt.savefig(out_path, dpi=140)
    plt.close()

def plot_forecast(dates, true_series, pred_series, out_path: Path, title="5-day Forecast"):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10,5))
    plt.plot(dates, true_series, label="True", linewidth=2)
    plt.plot(dates, pred_series, label="Forecast", linestyle="--")
    plt.title(title); plt.xlabel("Date"); plt.ylabel("Close")
    plt.legend(); plt.tight_layout()
    plt.savefig(out_path, dpi=140)
    plt.close()


# ------------------------ data prep ------------------------

def load_series(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    if "Adj Close" in df.columns and "AdjClose" not in df.columns:
        df.rename(columns={"Adj Close": "AdjClose"}, inplace=True)
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df.sort_values("Date", inplace=True)
        df.reset_index(drop=True, inplace=True)
    return df

def split_time_series(values: np.ndarray, train_ratio=TRAIN_RATIO, val_ratio=VAL_RATIO):
    n = len(values)
    n_train = int(n * train_ratio)
    n_val   = int(n * val_ratio)
    train = values[:n_train]
    val   = values[n_train:n_train+n_val]
    test  = values[n_train+n_val:]
    return train, val, test

def build_sequences(series_1d: np.ndarray, window: int):
    X, y = [], []
    for i in range(len(series_1d) - window):
        X.append(series_1d[i:i+window])
        y.append(series_1d[i+window])
    X = np.array(X)[..., np.newaxis]  # (samples, window, 1)
    y = np.array(y)
    return X, y

def prepare_datasets(df: pd.DataFrame, target_col: str, scaler_path: Path):
    close = df[target_col].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    close_scaled = scaler.fit_transform(close)
    ensure_dirs(Path(scaler_path).parent)
    joblib.dump(scaler, scaler_path)

    train, val, test = split_time_series(close_scaled)
    X_train, y_train = build_sequences(train.flatten(), WINDOW)
    X_val, y_val     = build_sequences(val.flatten(), WINDOW)
    X_test, y_test   = build_sequences(test.flatten(), WINDOW)

    # datas alinhadas aos pontos de y_test para plot
    if "Date" in df.columns:
        dates = df["Date"]
        start_idx = len(train) + len(val)
        test_dates = dates[start_idx + WINDOW:].reset_index(drop=True)
    else:
        test_dates = pd.RangeIndex(len(y_test))

    return {
        "X_train": X_train, "y_train": y_train,
        "X_val": X_val,     "y_val": y_val,
        "X_test": X_test,   "y_test": y_test,
        "test_dates": test_dates
    }


# ------------------------ train ------------------------

def train():
    set_seed(RANDOM_SEED)
    ensure_dirs(MODELS_DIR, REPORTS_DIR.parent)

    df = load_series(DATA_CSV)
    data = prepare_datasets(df, TARGET_COL, SCALER_PATH)

    model = build_lstm(WINDOW, lr=LR)
    history = model.fit(
        data["X_train"], data["y_train"],
        validation_data=(data["X_val"], data["y_val"]),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        callbacks=default_callbacks(),
        verbose=1
    )

    ensure_dirs(MODELS_DIR)
    model.save(MODEL_PATH)
    plot_training(history, HISTORY_PLOT)

    print(f"✅ Modelo salvo em: {MODEL_PATH}")
    print(f"✅ Scaler salvo em: {SCALER_PATH}")
    print(f"✅ Histórico salvo em: {HISTORY_PLOT}")


# ------------------------ predict ------------------------

def _recursive_forecast(last_window_scaled: np.ndarray, model, horizon: int) -> np.ndarray:
    """Prevê multi-step recursivo com a última janela escalada (shape: (WINDOW,))."""
    window = last_window_scaled.copy().reshape(1, WINDOW, 1)
    preds = []
    for _ in range(horizon):
        yhat = model.predict(window, verbose=0)[0, 0]
        preds.append(yhat)
        window = np.append(window[:, 1:, :], [[[yhat]]], axis=1)
    return np.array(preds)

def predict():
    ensure_dirs(REPORTS_DIR)

    # carregar tudo
    df = load_series(DATA_CSV)
    scaler = joblib.load(SCALER_PATH)
    model  = tf.keras.models.load_model(MODEL_PATH)

    close = df[TARGET_COL].values.reshape(-1, 1)
    close_scaled = scaler.transform(close)

    last_window_scaled = close_scaled[-WINDOW:].flatten()
    preds_scaled = _recursive_forecast(last_window_scaled, model, HORIZON)
    preds = scaler.inverse_transform(preds_scaled.reshape(-1, 1)).flatten()

    # Para plot: últimos WINDOW reais + previsões futuras
    history = close[-WINDOW:].flatten()
    if "Date" in df.columns:
        idx_history = df["Date"].iloc[-WINDOW:]
        future_idx = pd.date_range(start=idx_history.iloc[-1] + pd.Timedelta(days=1),
                                   periods=HORIZON, freq="B")
        plot_dates = pd.Index(idx_history).append(pd.Index(future_idx))
    else:
        plot_dates = pd.RangeIndex(WINDOW + HORIZON)

    plot_true = np.concatenate([history, [np.nan]*HORIZON])
    plot_pred = np.concatenate([history, preds])

    plot_forecast(plot_dates, plot_true, plot_pred, FORECAST_PLOT, title="NVIDIA Close - 5-day Forecast")

    print("✅ Previsões (5 dias à frente):", np.round(preds, 4).tolist())
    print(f"✅ Gráfico salvo em: {FORECAST_PLOT}")


# ------------------------ cli ------------------------

def main():
    parser = argparse.ArgumentParser(description="LSTM NVIDIA - treino e previsão (5 dias)")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Treina o modelo e salva .h5 + scaler")
    sub.add_parser("predict", help="Gera previsão de 5 dias e salva gráfico")

    args = parser.parse_args()
    if args.cmd == "train":
        train()
    elif args.cmd == "predict":
        predict()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
