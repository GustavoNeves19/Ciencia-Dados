# README - Notebook de Classificação de Qualidade de Frutas

Este notebook apresenta um estudo detalhado sobre a **classificação de frutas em boas (`good`) ou ruins (`bad`)** utilizando técnicas de Machine Learning. O objetivo principal foi prever a qualidade das frutas com base em atributos físicos e sensoriais, garantindo boa acurácia e generalização.

## 📊 Fluxo Geral do Notebook

1. **Leitura e Análise Exploratória dos Dados**

   * Dataset balanceado: ~2000 amostras de cada classe (`good` e `bad`).
   * Atributos utilizados: `Size`, `Weight`, `Sweetness`, `Crunchiness`, `Juiciness`, `Ripeness` e `Acidity`.
   * Visualizações incluíram:
     - **Boxplots**: evidenciaram diferenças de distribuição entre as classes.
     - **Pairplot**: mostrou sobreposição entre variáveis, reforçando a necessidade de modelos mais complexos.
     - **Matriz de correlação**: revelou fracas correlações (<0.3), indicando independência entre atributos.

2. **Pré-processamento**

   * Aplicação de `LabelEncoder` para transformar a variável-alvo (`Quality` → `0` = bad, `1` = good).
   * Padronização com `StandardScaler` (z-score) para normalizar os atributos numéricos.
   * Divisão em treino e teste preservando o balanceamento das classes.

3. **Construção do Pipeline Base**

   * Diferentes algoritmos foram testados: `DecisionTree`, `ExtraTree`, `RandomForest`, `ExtraTrees`, `XGBoost` e `LightGBM`.
   * Comparação inicial mostrou forte tendência de overfitting em árvores simples.
   * Modelos baseados em ensembles apresentaram melhor generalização.


4. **Avaliações e Interpretações dos Modelos**

| Modelo              | Acurácia | Precisão (0/1) | Recall (0/1) | F1-Score (0/1) | AUC    |
|---------------------|----------|----------------|--------------|----------------|--------|
| **Extra Trees**     | ~90.0%   | 0.89 / 0.91    | 0.91 / 0.89  | 0.90 / 0.90    | 0.9148 |
| **Random Forest**   | ~89.7%   | 0.89 / 0.90    | 0.90 / 0.90  | 0.90 / 0.90    | 0.9580 |
| **XGBoost**         | ~89.6%   | 0.90 / 0.89    | 0.89 / 0.91  | 0.89 / 0.90    | 0.9603 |


---

## 📈 Curva ROC e AUC

A **Curva ROC** (Receiver Operating Characteristic) foi utilizada para avaliar a capacidade discriminativa dos modelos:

- **Extra Trees**: AUC = 0.9148  
- **Random Forest**: AUC = 0.9580  
- **XGBoost**: AUC = 0.9603  

A curva ROC evidencia a **taxa de verdadeiros positivos (sensibilidade)** contra a **taxa de falsos positivos**.  
Os modelos **Random Forest e XGBoost** se destacaram com curvas mais próximas do canto superior esquerdo, indicando maior capacidade de distinção entre frutas boas e ruins.

---

## ✅ Conclusões Técnicas

* Modelos **baseados em ensembles** foram os mais eficazes.
* **Random Forest e XGBoost** apresentaram métricas superiores (AUC > 0.95, F1 ~0.90).
* O **Extra Trees** também mostrou bom desempenho, mas inferior aos dois anteriores.
* O uso de **validação cruzada** e **tuning de hiperparâmetros** foi crucial para evitar overfitting e garantir robustez.

### 📊 Comparativo Final: Extra Trees, Random Forest e XGBoost

| Métrica             | Extra Trees | Random Forest | XGBoost |
| ------------------- | ----------- | ------------- | ------- |
| Acurácia (teste)    | 90.25%      | 89.66%        | 89.58%  |
| F1-Score (média)    | 0.90        | 0.90          | 0.90    |
| ROC AUC             | 0.9148      | 0.9580        | 0.9603  |

**Conclusão**:  
O **XGBoost** apresentou o melhor equilíbrio geral entre métricas, sendo o modelo mais recomendado para produção. O **Random Forest** surge como uma ótima alternativa, oferecendo desempenho muito próximo ao XGBoost. Já o **Extra Trees**, apesar de competitivo, é menos robusto em termos de AUC.

---

Este notebook representa um exemplo sólido de aplicação de Machine Learning para classificação de frutas, com foco em análise exploratória, tuning de hiperparâmetros e comparativo de modelos de ensemble.
