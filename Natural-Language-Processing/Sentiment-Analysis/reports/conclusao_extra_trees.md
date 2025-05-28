
## ✅ Conclusão sobre o Modelo Extra Trees - Classificação de Sentimentos

### 📊 Distribuição Real das Classes

| Sentimento  | Ocorrências | Porcentagem |
|-------------|-------------|-------------|
| Neutral     | 285         | 28.5%       |
| Positive    | 277         | 27.7%       |
| Negative    | 266         | 26.6%       |
| Irrelevant  | 172         | 17.2%       |
| **Total**   | **1000**    | **100%**    |

---

### 🧠 Desempenho Geral (Extra Trees)

| Métrica              | Valor    |
|----------------------|----------|
| Accuracy             | **96.2%** |
| Precision (weighted) | 96.3%    |
| Recall (weighted)    | 96.2%    |
| F1-score (weighted)  | 96.2%    |

O modelo Extra Trees superou ligeiramente o Random Forest, mantendo equilíbrio entre precisão e recall e demonstrando robustez na classificação das 4 categorias.

---

### 📌 Desempenho por Classe

| Classe      | Precision | Recall | F1-score | Suporte | Observação |
|-------------|-----------|--------|----------|---------|------------|
| Irrelevant  | **0.99**  | 0.94   | 0.96     | 172     | Excelência em precisão, mas com leve perda em recall (alguns falsos negativos) |
| Negative    | 0.95      | **0.97**| 0.96     | 266     | Desempenho muito sólido, com altíssima cobertura |
| Neutral     | 0.95      | **0.97**| 0.96     | 285     | Modelo captura muito bem essa classe |
| Positive    | **0.98**  | 0.95   | 0.97     | 277     | Ótimo equilíbrio e destaque em precisão |

---

### 🧮 Análise da Matriz de Confusão

| Tipo de erro                         | Qtde | Impacto                                  |
|--------------------------------------|------|-------------------------------------------|
| Irrelevant → outras classes           | 10   | 5.8% dos "Irrelevant" foram confundidos   |
| Positive → outras                     | 13   | 4.7% de erro entre Positive e Negative    |
| Neutral → outras                      | 8    | 2.8% confundidos com outras               |
| Negative → outras                     | 7    | 2.6% de erro                              |

📉 Erros ligeiramente menores que o Random Forest, com melhor separação das classes **Positive** e **Neutral**.

---

## 🔍 Pontos Fortes do Modelo
- Métrica F1 consistentemente alta (≥ 0.96) para todas as classes.
- Melhor separação entre classes semelhantes (Neutral e Positive).
- Excelente desempenho geral, sendo um dos melhores modelos da avaliação.

---

## ⚠️ Elos Fracos / Oportunidades de Melhoria
- Pequena confusão ainda entre classes subjetivamente próximas.
- Como é um modelo ensemble, pode ser mais pesado computacionalmente.
- Potencial de reforço com embeddings ou modelos semânticos mais profundos (BERT, RoBERTa).

---

## 🧪 Conclusão Final

> O modelo Extra Trees demonstrou performance excepcional em classificação de sentimentos com PLN. Com métricas superiores a 96% em todas as dimensões e erros muito controlados, ele se apresenta como uma das melhores opções para deploy imediato, mantendo precisão, robustez e generalização.

> A função gera uma **matriz de confusão** como esta:

![Matriz de Confusão Extra Tress](../images/matriz_of_confusion_extra_tress.png)

