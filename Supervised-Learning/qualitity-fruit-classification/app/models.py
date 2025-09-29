from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

def get_models(seed=42):
    return {
        "DecisionTree": DecisionTreeClassifier(random_state=seed),
        "ExtraTree": ExtraTreeClassifier(random_state=seed),
        "RandomForest": RandomForestClassifier(random_state=seed, n_jobs=-1),
        "ExtraTrees": ExtraTreesClassifier(random_state=seed, bootstrap=True, n_jobs=-1),
        "XGBoost": XGBClassifier(random_state=seed, n_jobs=-1),
        "LightGBM": LGBMClassifier(random_state=seed, n_jobs=-1, verbosity=-1),
    }
