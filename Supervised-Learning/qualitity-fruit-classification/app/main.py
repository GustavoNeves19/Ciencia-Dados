from preprocessing import load_data, preprocess_data
from models import get_models
from training import train_and_evaluate
from evaluation import evaluate_model, plot_confusion_matrix

def run_pipeline(path="data/apple_quality.csv"):
    # Carregar e preprocessar
    df = load_data(path)
    X_train, X_test, y_train, y_test, le = preprocess_data(df)

    # Inicializar modelos
    models = get_models()

    # Treinar e avaliar
    results = train_and_evaluate(models, X_train, X_test, y_train, y_test)

    print("\nResultados comparativos:")
    for name, res in results.items():
        print(f"{name} -> Train: {res['Acc Train']:.4f} | Test: {res['Acc Test']:.4f}")

    # Exemplo: avaliar modelo final
    final_model = models["ExtraTrees"]
    acc, report, y_pred = evaluate_model(final_model, X_test, y_test)
    print("\nAcurácia Final:", acc)
    print("\nRelatório de Classificação:")
    for label, metrics in report.items():
        print(label, metrics)

    plot_confusion_matrix(y_test, y_pred, title="Extra Trees Confusion Matrix")

if __name__ == "__main__":
    run_pipeline()
