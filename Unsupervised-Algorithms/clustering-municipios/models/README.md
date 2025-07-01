# 🤖 Modelos - K-Means & PCA

Esta pasta contém os arquivos relacionados aos modelos gerados durante a análise de clusterização dos municípios paraenses, desenvolvida no projeto **Desafio I2A2**.

## 📌 Modelos Salvos

- `kmeans_model.pkl`: Modelo de agrupamento K-Means treinado com o número ótimo de clusters.
- `pca_components.pkl`: Objeto PCA utilizado para redução de dimensionalidade (caso necessário).

---

## 📊 Modelo K-Means

O algoritmo **K-Means** foi escolhido por sua simplicidade, eficiência e aplicabilidade em cenários com dados contínuos e normalizados. Após testes e análise com o **Gráfico de Elbow**, determinou-se que o número ideal de clusters seria **k = 4**.

### Parâmetros usados:

- `n_clusters=4`
- `init="k-means++"`
- `random_state=42`

O modelo foi salvo usando a biblioteca `joblib` para posterior reutilização, seja em análises futuras ou para produção.

---

## 🔍 PCA - Análise de Componentes Principais

Embora o K-Means trabalhe com os dados multidimensionais originais, utilizamos a **PCA** como técnica de visualização, projetando os dados em **2 dimensões**.

A PCA permitiu:

- Visualizar claramente a separação entre os clusters.
- Reduzir a dimensionalidade mantendo a maior variância possível.
- Ajudar a interpretar os eixos mais importantes do agrupamento.

### Resultados:

- Os dois primeiros componentes principais explicaram **mais de 70% da variância total**.
- O gráfico 2D com as cores dos clusters reforçou a boa separação das classes.

---

## 🧠 Uso futuro

Esses modelos podem ser carregados da seguinte forma:

```python
from joblib import load

# Carregando o modelo K-Means
kmeans = load("models/kmeans_model.pkl")

# (Opcional) Carregando o PCA para transformar novos dados
pca = load("models/pca_components.pkl")

# Prevendo novos dados
new_labels = kmeans.predict(novos_dados_normalizados)

```
## Conclusão ✅

O armazenamento modular dos modelos permite reusabilidade, comparações futuras e eventual deploy em uma aplicação com novos dados ambientais. Tanto o K-Means quanto a PCA demonstraram forte valor analítico no contexto deste projeto.