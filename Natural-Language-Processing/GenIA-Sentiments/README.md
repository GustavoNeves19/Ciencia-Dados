# GenAI Sentiment: Análise Estratégica e Planos de Ação Generativos

O **GenAI Sentiment** é uma aplicação avançada que integra Processamento de Linguagem Natural (PLN) e Aprendizado de Máquina (ML) para classificação de sentimentos, com o poder da Inteligência Artificial Generativa (GenAI) para criar **estratégias de marketing acionáveis**.

O objetivo é transformar a classificação bruta de sentimentos em *insights acionáveis*. Ao identificar comentários negativos e neutros para uma empresa específica, a GenAI é acionada para gerar um plano de ação de marketing e comunicação em tempo real.

## 🌐 Tecnologias Utilizadas

* **Python 3**
* **Streamlit** (Interface do Usuário)
* **google-genai** (Integração com o modelo Gemini para geração de texto)
* **Scikit-learn / joblib** (Classificação de Sentimentos)
* **NLTK** (Pré-processamento de Linguagem)
* **Plotly** (Visualização de Dados)



## 🔍 Objetivo

O principal objetivo do **GenAI Sentiment** é permitir que um analista:

  * **Classifique** automaticamente o sentimento (Positivo, Negativo, Neutro) de comentários em massa.
  * **Visualize** os dados de sentimento e o ranking de empresas.
  * **Filtre** por uma empresa específica.
  * **Gere um Plano de Ação Estratégico** em tempo real usando IA Generativa, focado nos pontos de dor (comentários Negativos e Neutros) daquela empresa.

## 📋 Formato do Arquivo CSV de Entrada

O arquivo deve conter, no mínimo, as seguintes colunas:

  * `entity`: Nome da empresa mencionada (obrigatório para o filtro)
  * `content`: Texto do comentário (obrigatório para classificação)
  * *(Outras colunas, como `tweetid` e `target`, são opcionais e ignoradas ou utilizadas internamente.)*

## 🚀 Como Utilizar

### 1\. Pré-requisitos e Configuração da Chave Gemini

O projeto exige que você defina sua chave de API do Gemini (Google AI) na variável `CHAVE` dentro do arquivo `app.py`.

```python
# No arquivo app/app.py, edite esta linha:
CHAVE = "SUA_CHAVE_AQUI" 
```

### 2\. Instalação das Dependências

Crie e ative seu ambiente virtual, e depois instale os pacotes necessários:

```bash
# Ativar ambiente virtual (exemplo Linux/macOS)
source venv/bin/activate

# Instalação das bibliotecas
pip install joblib streamlit pandas plotly google-genai
```

### 3\. Execução da Aplicação

Certifique-se de que os arquivos `.pkl` dos modelos estejam em `models/` e execute o Streamlit:

```bash
cd app
streamlit run app.py
```

### 4\. Geração do Plano de Ação Generativo

Após carregar o CSV e visualizar os gráficos:

1.  Selecione uma empresa específica no filtro.
2.  Desça até a seção "✨ Plano de Ação Generativo".
3.  Clique no botão **"🚀 Gerar Plano de Ação de Marketing com IA para [Empresa]"** para obter um relatório estratégico baseado nos comentários Negativos/Neutros.

## 🌟 Funcionalidades Principais

  * **Classificação Automática:** Uso de modelo ML (ExtraTreesClassifier) com **96% de acurácia**.
  * **Filtragem por Empresa:** Permite focar a análise e a geração de IA em uma única entidade.
  * **Plano de Ação Generativo:** Analisa os comentários problemáticos e estrutura um plano de intervenção (pontos de dor, estratégias de comunicação e modelos de resposta).

## 🔬 Sobre os Modelo

### 🧠 1. Modelo de Classificação (ML/NLP)

| **Modelo** | **Detalhes** | **Performance** |
| :--- | :--- | :--- |
| **ExtraTreesClassifier** | Treinado com vetores **TF-IDF** gerados a partir do texto pré-processado. | **96% de acurácia** no conjunto de validação. |

🔹 Este modelo é responsável por **rotular automaticamente** cada comentário como:  
**Positivo**, **Negativo**, **Neutro** ou **Irrelevante**.  

Ele utiliza técnicas clássicas de **Processamento de Linguagem Natural (PLN)**, combinadas com aprendizado supervisionado, para obter resultados de alta precisão mesmo em textos curtos e informais (ex: tweets e comentários de redes sociais).

---

### 🤖 2. Inteligência Artificial Generativa (GenAI)

A etapa de **geração de estratégias** é conduzida por um **Large Language Model (LLM)**, responsável por transformar a análise de sentimentos em **planos de ação estratégicos de marketing e comunicação**.

| **LLM Utilizado** | **Função** | **Modelo** |
| :--- | :--- | :--- |
| **Gemini 2.5 Flash (Google AI)** | Atua como um **estrategista de marketing digital** e **especialista em satisfação do cliente**, convertendo dores identificadas nos comentários negativos e neutros em **soluções concretas e aplicáveis**. | LLM de última geração com capacidade de **contexto longo** e **resposta estruturada**. |

---

### 🧩 Engenharia de Prompt (System / User)

A aplicação utiliza **prompts estruturados** para orientar a IA generativa e garantir consistência e qualidade nos resultados.

#### **🧱 Instrução de Sistema (System Prompt)**
Define a **persona** do modelo:
> “Você é um estrategista de marketing digital e especialista em satisfação do cliente, responsável por criar planos de ação para melhorar a reputação de uma empresa com base em comentários de clientes.”

#### **💬 Prompt de Usuário (User Prompt)**
Envia o nome da empresa e uma **amostra dos comentários problemáticos**.  
O modelo deve retornar o resultado no seguinte formato estruturado:

1. **Identificação de Problemas** — Principais dores e falhas percebidas pelos clientes.  
2. **Plano de Ação** — Estratégias práticas de comunicação, marketing e melhoria de produto.  
3. **Modelo de Resposta** — Sugestão de mensagem institucional para resposta pública ou SAC.

---

💡 **Em resumo:**  
A combinação entre o **modelo de classificação (ExtraTreesClassifier)** e o **LLM (Gemini 2.5 Flash)** permite à aplicação ir além da simples análise de sentimentos — gerando **inteligência estratégica automatizada**, pronta para uso em contextos reais de **gestão de marca e relacionamento com o cliente**.


## 🔄 Possíveis Extensões Futuras

  * Deploy via Docker.
  * Disponibilização da classificação (ML) e geração (GenAI) como API REST com FastAPI.
  * Adicionar filtro de data e idioma aos comentários.

-----

## 🙏 Agradecimentos

Este projeto é uma extensão do estudo realizado com o dataset do Kaggle [Twitter Entity Sentiment Analysis](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis).

Desenvolvido para experiências realistas de negócios e dados, transformando dados em estratégia acionável.

---