# GenAI Sentiment: Análise Estratégica e Planos de Ação Generativos

O **GenAI Sentiment** é uma aplicação avançada que integra Processamento de Linguagem Natural (PLN) e Aprendizado de Máquina (ML) para classificação de sentimentos, com o poder da Inteligência Artificial Generativa (GenAI) para criar **estratégias de marketing acionáveis**.

O objetivo é transformar a classificação bruta de sentimentos em *insights acionáveis*. Ao identificar comentários negativos e neutros para uma empresa específica, a GenAI é acionada para gerar um plano de ação de marketing e comunicação em tempo real.

## 🧱 Arquitetura e Tecnologias

Este projeto utiliza uma **Arquitetura Desacoplada** para garantir flexibilidade e escalabilidade:

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| **Front-end (Cliente)** | **Streamlit** | Interface do Usuário. Envia dados brutos para a API e consome a resposta. |
| **Back-end (Classificação)** | **FastAPI** | Servidor API para hospedar o modelo de ML. Recebe dados, processa, classifica e retorna o sentimento. |
| **Modelagem (ML/PLN)** | **Scikit-learn / joblib** | Modelos de classificação de sentimentos. |
| **Geração (LLM)** | **Google GenAI** (Gemini 2.5 Flash) | Agente LLM para geração de planos de ação estratégicos. |

### 🌐 Tecnologias Utilizadas

  * **Python 3**
  * **FastAPI / Uvicorn** (Servidor API)
  * **Streamlit** (Interface do Usuário)
  * **google-genai** (Integração com o modelo Gemini)
  * **Scikit-learn / joblib** (Classificação de Sentimentos)
  * **NLTK** (Pré-processamento de Linguagem)
  * **Plotly** (Visualização de Dados)

-----

## 🔍 Objetivo e Funcionalidades

O principal objetivo do **GenAI Sentiment** é permitir que um analista:

  * **Classifique** automaticamente o sentimento (via API) de comentários em massa.
  * **Visualize** os dados de sentimento e o ranking de empresas.
  * **Filtre** por uma empresa específica.
  * **Gere um Plano de Ação Estratégico** em tempo real usando IA Generativa.

### 🌟 Funcionalidades Principais

  * **Classificação via API:** O Streamlit não carrega modelos pesados; ele consome o resultado do FastAPI, garantindo eficiência.
  * **Filtragem por Empresa:** Permite focar a análise e a geração de IA em uma única entidade.
  * **Plano de Ação Generativo:** Analisa os comentários problemáticos e estrutura um plano de intervenção.

-----

## 📋 Formato do Arquivo CSV de Entrada

O arquivo deve conter, no mínimo, as seguintes colunas de dados brutos para que a API possa processar:

  * `entity`: Nome da empresa mencionada (obrigatório para o filtro)
  * `content`: Texto do comentário (obrigatório para classificação)
  * *(Outras colunas são opcionais e são ignoradas pelo processo de classificação.)*

-----

## 🚀 Como Utilizar (Execução e *Deploy* Local)

Para rodar esta aplicação, você precisa ativar **dois serviços** separadamente: a API (Back-end) e o Streamlit (Front-end).

### 1\. Pré-requisitos e Configuração da Chave Gemini

O projeto usa a biblioteca `python-dotenv` para carregar a chave Gemini (LLM) de um arquivo `.env` na raiz do projeto:

```bash
# Crie o arquivo .env na raiz do projeto e adicione sua chave:
GEMINI_API_KEY="SUA_CHAVE_AQUI"
```

### 2\. Instalação das Dependências

Crie e ative seu ambiente virtual e instale todas as bibliotecas necessárias para o cliente e o servidor:

```bash
# Ativar ambiente virtual (exemplo Linux/macOS)
source venv/bin/activate

# Instalação das bibliotecas
pip install fastapi uvicorn requests python-dotenv joblib streamlit pandas plotly google-genai nltk
```

### 3\. Inicialização do Serviço de Classificação (FastAPI - Back-end)

Você deve iniciar o servidor que hospeda os modelos de Machine Learning.

```bash
# 💡 Execute este comando no terminal DENTRO da pasta 'app/'
cd app
uvicorn api_server:app --reload
```

> **IMPORTANTE:** Este terminal deve permanecer aberto e rodando para que o Streamlit consiga se conectar e classificar os dados.

### 4\. Inicialização da Aplicação (Streamlit - Front-end)

Em um **segundo terminal** (com o ambiente virtual ativo), inicie o aplicativo Streamlit:

```bash
# 💡 Execute este comando no segundo terminal DENTRO da pasta 'app/'
cd app
streamlit run app.py
```

### 5\. Fluxo de Geração

1.  Envie o arquivo CSV na interface.
2.  O `app.py` faz uma requisição HTTP para o servidor **FastAPI** (`http://127.0.0.1:8000/predict/sentiment`).
3.  O FastAPI classifica e retorna os rótulos.
4.  Selecione a empresa e clique em **"🚀 Gerar Plano de Ação de Marketing com IA"**.
5.  O `app.py` usa o SDK do **Gemini** (LLM) para gerar o plano estratégico.

-----

## 🔬 Modelos e Inteligência Artificial

### 🧠 1. Modelo de Classificação (ML/NLP)

O modelo é carregado pelo **FastAPI** e serve a classificação via API.

| **Modelo** | **Detalhes** | **Performance** |
| :--- | :--- | :--- |
| **ExtraTreesClassifier** | Treinado com vetores **TF-IDF** gerados a partir do texto pré-processado. | **96% de acurácia** no conjunto de validação. |

🔹 Este modelo utiliza técnicas clássicas de **Processamento de Linguagem Natural (PLN)** para rotular automaticamente cada comentário.

### 🤖 2. Inteligência Artificial Generativa (GenAI)

A etapa de **geração de estratégias** é conduzida por um **Large Language Model (LLM)**.

| **LLM Utilizado** | **Função** | **Modelo** |
| :--- | :--- | :--- |
| **Gemini 2.5 Flash (Google AI)** | Atua como um **estrategista de marketing digital** e **especialista em satisfação do cliente**, convertendo dores identificadas nos comentários negativos e neutros em **soluções concretas e aplicáveis**. | LLM de última geração com capacidade de **contexto longo** e **resposta estruturada**. |

### 🧩 Engenharia de Prompt (System / User)

A aplicação utiliza **prompts estruturados** para orientar a IA generativa e garantir consistência e qualidade nos resultados.

#### **🧱 Instrução de Sistema (System Prompt)**

Define a **persona** do modelo:

> “Você é um estrategista de marketing digital e especialista em satisfação do cliente, responsável por criar planos de ação para melhorar a reputação de uma empresa com base em comentários de clientes.”

#### **💬 Prompt de Usuário (User Prompt)**

Envia o nome da empresa e uma **amostra dos comentários problemáticos**, exigindo a resposta em um formato estruturado (Identificação de Problemas, Plano de Ação, Modelo de Resposta).

-----

## 🔄 Possíveis Extensões Futuras

  * *Deploy* da API de classificação para um serviço de nuvem (AWS/GCP/Azure) para acesso público 24/7.
  * *Deploy* da aplicação Streamlit via Docker.
  * Adicionar filtro de data e idioma aos comentários.

## 🙏 Agradecimentos

Este projeto é uma extensão do estudo realizado com o dataset do Kaggle [Twitter Entity Sentiment Analysis](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis).

Desenvolvido para experiências realistas de negócios e dados, transformando dados em estratégia acionável.