# 📊 Repositório de Projetos de Ciência de Dados

Este repositório, criado por mim, **Gustavo Neves** centraliza e organiza diversas aplicações práticas de **Ciência de Dados**. O objetivo é apresentar um portfólio abrangente, reunindo técnicas estatísticas, algoritmos de *Machine Learning* (ML), processamento de dados e implementação de modelos.

A intenção é que este espaço funcione como uma base de aprendizado contínuo, sendo constantemente atualizado com novos estudos, experimentos e implementações. Sinta-se à vontade para explorar e contribuir!

---

## 🏗️ Estrutura e Conteúdo do Repositório

O repositório está organizado em diretórios, cada um focado em uma área fundamental de *Data Science*. Cada projeto individual inclui explicação do problema, *dataset*, abordagem técnica, avaliação de resultados e código modularizado.

| Categoria Principal | Tópicos e Algoritmos Abordados | Destaques dos Projetos |
| :--- | :--- | :--- |
| [**Aprendizado Supervisionado (Classificação)**](./Supervised-Learning/) 🏷️ | Previsão, Categorização, K-NN, LightGBM, Random Forest, XGBoost. | **Diagnóstico de Neoplasias** (Classificação Binária com 98.83% de acurácia) e **Classificação da Qualidade de Frutas** (Controle de Qualidade Automatizado). |
| [**Aprendizado Não Supervisionado (Clustering)**](./Unsupervised-Algorithms/) 🔍 | Segmentação, K-Means, PCA, Análise Exploratória de Padrões. | **Clusterização de Municípios do Pará** com base em dados ambientais (desmatamento, focos de calor) para apoiar políticas públicas. |
| [**Processamento de Linguagem Natural (PLN)**](./Natural-Language-Processing/) 🗣️ | Análise de Sentimentos, Classificação de Texto, Tradução Automática, Tokenização. | **Análise de Sentimentos do Twitter** para monitoramento corporativo e **GenAI Sentiment** (integração de Classificação ML com **Gemini 2.5 Flash** para gerar Planos de Ação Estratégica). |
| [**Deep Learning (Redes Neurais)**](./Deep-Learning/) 🧠 | RNN, LSTM, FNN, Previsão de Séries Temporais, Classificação. | **Previsão de Preços de Ações da NVIDIA** (utilizando **Redes Neurais LSTM**) e **Previsão de Inadimplência de Empréstimos** (utilizando modelos neurais robustos). |
| **Implementação & Deploy** 🚀 | APIs (FastAPI), Interfaces Interativas (Streamlit), Servidores de Modelo. | Uso de **FastAPI** para servir modelos de classificação via API, desacoplando o *back-end* do *front-end* **Streamlit**. |

---

## 🛠️ Tecnologias Principais Utilizadas

Os projetos foram desenvolvidos utilizando um ecossistema robusto de ferramentas e bibliotecas de *Data Science* em Python:

* **Linguagem**: Python 3
* **Machine Learning (Clássico)**: **Scikit-learn**, Pandas, NumPy
* **Deep Learning**: **TensorFlow/Keras**, **PyTorch**
* **PLN/GenAI**: **NLTK**, **Hugging Face Transformers**, **Google GenAI (Gemini 2.5 Flash)**
* **Visualização**: Matplotlib, Seaborn, Plotly
* **Deploy**: **Streamlit** (Interfaces), **FastAPI** (APIs/Servidor de Modelos), Uvicorn

---

## 🌐 Como Explorar

1.  **Navegue pelos Diretórios**: Clique nas pastas correspondentes a cada categoria para acessar os projetos individuais.
2.  **Leia os READMEs**: Cada projeto contém um `README.md` detalhado com:
    * Explicação do problema.
    * Abordagem e técnicas aplicadas.
    * Avaliação dos resultados (métricas).
    * Instruções de uso (`Como Utilizar`).
3.  **Código**: O código está modularizado e pronto para ser executado (seguindo as instruções de dependências e *deploy* local).

---

## 🤝 Contato e Licença

Sinta-se à vontade para me contatar em caso de dúvidas, sugestões ou oportunidades de colaboração!

Este projeto está licenciado sob a **Licença MIT** (veja o arquivo `LICENSE` para detalhes), permitindo a reutilização e modificação do código.