# pipeline.py
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier


def build_pipeline(best_params=None):
    """
    Constrói um pipeline com padronização e modelo LGBM.

    Parâmetros:
        best_params (dict): Parâmetros ajustados via GridSearchCV

    Retorna:
        sklearn.pipeline.Pipeline
    """
    if best_params:
        model = LGBMClassifier(**best_params)
    else:
        model = LGBMClassifier()

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('lgbm', model)
    ])

    return pipeline
