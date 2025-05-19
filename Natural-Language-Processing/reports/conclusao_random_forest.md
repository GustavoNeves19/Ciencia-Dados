
## ✅ Conclusão sobre o Modelo Random Forest - Classificação de Sentimentos

### 📊 Distribuição Real das Classes

Antes de avaliar o modelo, vale lembrar a distribuição original no conjunto de validação:

| Sentimento  | Ocorrências | Porcentagem |
|-------------|-------------|-------------|
| Neutral     | 285         | 28.5%       |
| Positive    | 277         | 27.7%       |
| Negative    | 266         | 26.6%       |
| Irrelevant  | 172         | 17.2%       |
| **Total**   | **1000**    | **100%**    |

---

### 🧠 Desempenho Geral (Random Forest)

| Métrica              | Valor    |
|----------------------|----------|
| Accuracy             | **95.6%** |
| Precision (weighted) | 95.6%    |
| Recall (weighted)    | 95.6%    |
| F1-score (weighted)  | 95.6%    |

O modelo apresenta **alta acurácia geral**, com excelente equilíbrio entre precisão e recall nas classes.

---

### 📌 Desempenho por Classe

| Classe      | Precision | Recall | F1-score | Suporte | Observação |
|-------------|-----------|--------|----------|---------|------------|
| Irrelevant  | **0.99**  | 0.94   | 0.96     | 172     | Alta precisão, recall levemente menor – há falsos negativos |
| Negative    | 0.95      | **0.97**| 0.96     | 266     | Classificações muito corretas, poucos falsos positivos |
| Neutral     | 0.94      | **0.96**| 0.95     | 285     | Alta sensibilidade, boa cobertura da classe |
| Positive    | 0.96      | 0.95   | 0.96     | 277     | Equilíbrio ideal entre precisão e recall |

---

### 🧮 Análise da Matriz de Confusão

| Tipo de erro                         | Qtde | Impacto                                  |
|--------------------------------------|------|-------------------------------------------|
| Irrelevant → Negative/Neutral/Positive | 11   | 6.4% dos casos de "Irrelevant" foram confundidos |
| Neutral → Negative/Positive            | 12   | 4.2% dos "Neutral" foram confundidos       |
| Positive → Neutral/Negative            | 14   | 5.1% dos "Positive" foram mal classificados |
| Negative → Positive/Neutral            | 7    | 2.6% de erro                              |

📉 Classes **Neutral e Positive** tendem a se confundir mais entre si.

---

## 🔍 Pontos Fortes do Modelo
- Excelente desempenho nas 4 classes principais com F1 acima de 0.95.
- Poucos erros graves de confusão cruzada.
- Modelo escalável e eficiente para textos vetorizados.

---

## ⚠️ Elos Fracos / Oportunidades de Melhoria
- O modelo ainda comete cerca de 4 a 6% de erros por classe.
- Pode ser mais robusto com **lematização** ou modelos como **BERT**.
- Sugestões de incremento:
  - Ajuste de hiperparâmetros com GridSearch
  - Word Embeddings (GloVe, FastText)
  - Balanceamento com oversampling

---

## 🧪 Conclusão Final

> O modelo Random Forest apresentou desempenho excelente na tarefa de classificação de sentimentos, com métricas consistentes e erros baixos. Apesar de pequenas confusões entre classes subjetivamente próximas, ele está pronto para uso real e pode ser facilmente integrado a um sistema de análise de sentimentos, com potencial de melhora por meio de vetores semânticos e técnicas modernas de PLN.

> A função gera uma **matriz de confusão** como esta:

![Matriz de Confusão Random Forest](../images/matriz_of_confusion_random_forest.png)

