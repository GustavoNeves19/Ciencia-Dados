# tuning.py
from sklearn.model_selection import GridSearchCV
from lightgbm import LGBMClassifier

def tune_hyperparameters(X_train, y_train, pipeline):
    """
    Realiza o ajuste de hiperparâmetros com GridSearchCV.

    Parâmetros:
        X_train (DataFrame): Dados de entrada de treino
        y_train (Series): Rótulos do treino
        pipeline (Pipeline): Pipeline contendo o modelo

    Retorna:
        dict: Melhores hiperparâmetros encontrados
    """
    param_grid = {
        'lgbm__n_estimators': [100, 200],
        'lgbm__learning_rate': [0.01, 0.1],
        'lgbm__max_depth': [3, 5, 7],
        'lgbm__num_leaves': [15, 31],
        'lgbm__min_child_samples': [10, 20]
    }

    grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1', n_jobs=-1)
    grid.fit(X_train, y_train)

    print("Melhor F1 Score:", grid.best_score_)
    print("Melhores parâmetros:", grid.best_params_)
    return grid.best_params_
