# Deep Learning: Fundamentos e Aplicações 🧠💻

## O que é Deep Learning? 🧐

**Deep Learning** (ou Aprendizado Profundo) é uma subárea do **Machine Learning (Aprendizado de Máquina)** que se baseia em **redes neurais artificiais** com **múltiplas camadas** (por isso o termo "profundo"). 💡 Essas redes são projetadas para **imitar o funcionamento do cérebro humano** e são capazes de aprender representações de dados de forma hierárquica, extraindo **características complexas** a partir de dados brutos.

O Deep Learning se destaca em tarefas que envolvem **grandes volumes de dados e complexidade**, como **processamento de linguagem natural**, **reconhecimento de voz** e **previsões financeiras**.

-----

## 🎯 Principais Aplicações de Deep Learning

As redes neurais profundas são cruciais para avanços significativos em diversas áreas:

  * **Reconhecimento de Padrões e Imagens**: Utilizado em **detecção de objetos**, **segmentação de imagens** e **reconhecimento facial**. 🖼️
  * **Processamento de Linguagem Natural (PLN)**: Tarefas como **tradução automática**, **resumo de textos**, **análise de sentimentos** e **chatbots** usam Deep Learning para alcançar alta eficácia. 🗣️
  * **Previsão de Séries Temporais**: Em *Data Science*, é amplamente utilizado para **prever preços de ações** 📉, analisar dados econômicos e fazer **previsões de demanda de produtos**.
  * **Análise de Dados e Previsões de Mercado**: Aplicações como **análise de tendências de mercado** e **previsão de vendas**.

-----

## Tipos de Redes Neurais em Data Science 🕸️

Deep Learning utiliza diferentes tipos de **redes neurais** para resolver problemas específicos:

### 1\. **Redes Neurais Feedforward (FNN)**

  * Dados fluem **apenas em uma direção**, da entrada até a saída.
  * Usadas para tarefas **supervisionadas**, como classificação e regressão.

### 2\. **Redes Neurais Convolucionais (CNN)**

  * Ideais para **análise de dados estruturados** com padrões espaciais, como **imagens**.
  * Também relevantes em **textos** ou **séries temporais** quando aplicadas em técnicas de *embedding*.

### 3\. **Redes Neurais Recorrentes (RNN)**

  * Projetadas para lidar com **dados sequenciais** (texto ou séries temporais), com capacidade de **lembrar informações passadas**. 🔄
  * Variações como **LSTM (Long Short-Term Memory)** e **GRU (Gated Recurrent Unit)** melhoram o aprendizado de dependências de longo prazo.

### 4\. **Redes Neurais Multicamadas (MLP)**

  * Um tipo de rede neural profunda composta por **várias camadas densas** conectadas, usada para uma variedade de tarefas de classificação e regressão.

### 5\. **Autoencoders**

  * Redes projetadas para **redução de dimensionalidade** e **detecção de anomalias**. 🔍
  * Aprendem a **codificar dados de entrada** em uma representação compacta e depois reconstrui-los.

-----

## 🛠️ Tecnologias e Ferramentas Usadas

| Categoria | Tecnologia | Função Principal |
| :--- | :--- | :--- |
| **Bibliotecas DL** | **TensorFlow** / **Keras** | Construção e treinamento de modelos de *deep learning*, sendo Keras uma interface de alto nível. |
| **Bibliotecas DL** | **PyTorch** | Framework popular para **pesquisa** e **prototipagem rápida**, excelente para PLN. |
| **Plataformas de Treinamento** | **Google Colab / Kaggle** | Ambientes de **computação em nuvem** que oferecem **GPU gratuita** para treinamento de modelos complexos. 🚀 |
| **Pré-processamento** | **Pandas / NumPy** | Manipulação e análise eficiente de dados e *arrays* numéricos. |
| **Visualização** | **Matplotlib / Seaborn** | Criação de gráficos, **curvas de erro** e visualização de padrões. |
| **Monitoramento** | **TensorBoard** | Ferramenta para visualização de **métricas de treinamento** e **performance de modelos** no TensorFlow. |

-----

## Projetos de Deep Learning 📂

  * [Previsão de Preços de Ações da NVIDIA Utilizando Redes Neurais Profundas](./RNN-NVIDIA/) 💰

      * **Descrição**: Desenvolve um modelo de **Deep Learning** utilizando **Redes Neurais LSTM** (*Long Short-Term Memory*) para analisar dados históricos de preços e fazer **previsões de curto prazo** das ações da **NVIDIA**. O objetivo é aprender as **dependências temporais** para análises financeiras e estratégias de investimento.
      * **Tecnologias**: **Keras**, **Scikit-learn**, **TensorFlow**.

  * [Previsão de Inadimplência de Empréstimo](./MLP-Default/) 🏦

      * **Descrição**: Desenvolve um **modelo neural de classificação** para estimar a probabilidade de **DEFAULT** em empréstimos. O *pipeline* é robusto, incluindo **EDA**, tratamento de desbalanceamento (SMOTE/class weights), calibração de probabilidades, e **interpretabilidade com SHAP**. O foco é apoiar decisões de crédito com **métricas robustas** (`ROC-AUC`, `PR-AUC`, `Recall/F1 da classe DEFAULT`).
      * **Tecnologias**: **Python**, **Pandas**, **NumPy**, **Scikit-learn**, **PyTorch** (ou TensorFlow/Keras), **Optuna/keras-tuner**, **Imbalanced-Learn**.

-----

## Licença 📜

Este projeto está licenciado sob a **Licença MIT** (veja o arquivo `LICENSE` para detalhes).