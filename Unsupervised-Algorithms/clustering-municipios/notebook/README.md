# 📊 Clusterização de Municípios do Pará - Desafio I2A2

Este notebook apresenta uma análise exploratória e modelagem baseada em **clusterização não supervisionada** dos municípios do estado do Pará, com base em dados ambientais, como precipitação, desmatamento, focos de calor e volume hídrico.

## 🧠 Contexto e Motivação

Este projeto foi desenvolvido como parte do **Desafio I2A2**, com o intuito de aplicar técnicas de ciência de dados para **agrupar municípios do Pará de acordo com similaridades ambientais**. A proposta busca fornecer suporte à gestão ambiental, ajudando a identificar padrões ou agrupamentos que possam embasar políticas públicas ou estratégias de monitoramento ambiental regional.

## 📁 Dataset

O dataset bruto encontra-se na pasta `/data/Raw`, contendo indicadores como:

- **Precipitação média**
- **Volume hídrico dos rios**
- **Número de focos de calor (queimadas)**
- **Taxa de desmatamento**

Após tratamento e normalização, esses dados foram usados para alimentar o algoritmo de clusterização.

---

## ⚙️ Metodologia

O pipeline de análise segue as seguintes etapas:

1. **Pré-processamento dos dados**
   - Tratamento de dados ausentes
   - Normalização com `MinMaxScaler`

2. **Análise Exploratória**
   - Correlação entre variáveis
   - Visualização de distribuição por município

3. **Determinação do número ideal de clusters**
   - **Gráfico de Elbow** para identificar o ponto de inflexão
   - Testes com diferentes valores de `k` para validação visual

4. **Clusterização**
   - Aplicação do algoritmo **K-Means**
   - Salvamento do modelo treinado na pasta `/models`

5. **Visualizações**
   - Visualização dos clusters em gráfico 2D (PCA)
   - Matriz colorida e centróides para interpretação dos grupos

---

## 🧾 Resultados

- A análise indicou que o número ótimo de clusters foi `k = 4`.
- Os municípios foram classificados em 4 grupos distintos, com base em semelhanças nos seus indicadores ambientais.
- O agrupamento permitiu identificar **municípios com maior pressão ambiental**, **municípios com alta cobertura hídrica**, entre outros padrões relevantes.

Os dados finais classificados foram salvos em `/data/Refined`, e o modelo K-Means foi armazenado em `/models`.

## ✅ Conclusão

Este estudo demonstrou o poder da análise de agrupamento para compreender melhor o comportamento ambiental dos municípios paraenses. A clusterização não só revelou **padrões escondidos nos dados**, como também pode servir de base para **decisões orientadas por dados no contexto ambiental**.

O projeto foi construído com modularidade e reprodutibilidade, facilitando adaptações futuras com novos indicadores ou regiões.