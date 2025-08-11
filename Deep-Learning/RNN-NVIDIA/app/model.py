# model.py
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks, optimizers

def build_lstm(window: int, lr: float = 1e-3) -> tf.keras.Model:
    """Modelo LSTM simples para previsão univariada."""
    model = models.Sequential([
        layers.Input(shape=(window, 1)),
        layers.LSTM(64, return_sequences=True),
        layers.LSTM(32),
        layers.Dense(16, activation="relu"),
        layers.Dense(1)
    ])
    model.compile(optimizer=optimizers.Adam(learning_rate=lr), loss="mse")
    return model

def default_callbacks(patience_es: int = 7, patience_rlr: int = 3):
    """Conjunto padrão de callbacks para treino estável."""
    return [
        callbacks.EarlyStopping(
            monitor="val_loss", patience=patience_es, restore_best_weights=True
        ),
        callbacks.ReduceLROnPlateau(
            monitor="val_loss", factor=0.5, patience=patience_rlr, min_lr=1e-5, verbose=1
        )
    ]
