from sklearn.metrics import balanced_accuracy_score
from tqdm import tqdm

def train_and_evaluate(models, X_train, X_test, y_train, y_test):
    results = {}
    for name, model in tqdm(models.items()):
        model.fit(X_train, y_train)
        acc_train = balanced_accuracy_score(y_train, model.predict(X_train))
        acc_test = balanced_accuracy_score(y_test, model.predict(X_test))
        results[name] = {"Acc Train": acc_train, "Acc Test": acc_test}
    return results
