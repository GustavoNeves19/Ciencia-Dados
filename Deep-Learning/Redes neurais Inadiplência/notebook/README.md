### 🧠 Redes Neurais MLP para Previsão de Inadimplência

---

### 📌 Fluxo Geral do Projeto

O projeto foi desenvolvido em Python, utilizando as principais bibliotecas de ciência de dados e machine learning. O fluxo de trabalho seguiu as seguintes etapas:

1.  **Leitura e Análise Exploratória dos Dados**
    * Carregamento do *dataset*.
    * Análise da estrutura das variáveis (categóricas e numéricas).
    * Identificação de valores ausentes e possíveis inconsistências.
    * Visualização de distribuições, correlações e padrões de inadimplência.

2.  **Engenharia de Atributos**
    * Tratamento de valores nulos.
    * Normalização e padronização de variáveis numéricas.
    * Codificação de variáveis categóricas com `OneHotEncoder`.
    * Construção de um `ColumnTransformer` para um *pipeline* unificado.

3.  **Construção do Pipeline**
    * Implementação de três arquiteturas de **Multilayer Perceptron (MLP)** usando a API `Sequential` do Keras:
        * **Modelo de 2 camadas ocultas**: Estrutura simples, usada como *baseline*.
        * **Modelo de 3 camadas ocultas**: Melhor equilíbrio entre capacidade de aprendizado e generalização.
        * **Modelo de 4 camadas ocultas**: Rede mais profunda, sem ganhos significativos em relação ao modelo de 3 camadas.
    * Compilação com otimizador **Adam** e função de perda `binary_crossentropy`.
    * Treinamento com validação em dados de teste.

4.  **Avaliação e Interpretação dos Modelos**
    * Métricas extraídas: Acurácia, *Precision*, *Recall*, F1-Score e **AUC**.
    * Análise da matriz de confusão.
    * Curva **ROC** e **AUC** para avaliar o poder discriminatório.
    * Importância relativa das variáveis (via SHAP/*permutation importance*).

## Análise de Dados    

### Objetivos e Perguntas da Análise de Dados

A etapa de Análise de Dados tem como objetivo principal entender a fundo o *dataset* de empréstimos, preparando-o para a modelagem preditiva. Para isso, as colunas foram organizadas em variáveis numéricas contínuas e categóricas, o que permite uma abordagem de análise e pré-processamento mais direcionada e eficaz.

As principais perguntas que esta análise busca responder são:

#### Perguntas sobre Variáveis Categóricas:
* Qual é a relação entre a situação de moradia do cliente (**RENT**, **MORTGAGE**, **OWN**) e a taxa de inadimplência (**DEFAULT**)?
* A finalidade do empréstimo (**EDUCATION**, **DEBTCONSOLIDATION**, **VENTURE**, etc.) tem alguma correlação com o risco de *default*?
* Existe uma relação monotônica entre a nota de crédito (**A** a **E**) e a inadimplência? Em quais faixas a taxa de *default* acelera?
* O histórico de crédito prévio (**Y/N**) impacta a chance de inadimplência? O comportamento do grupo com dados faltantes é atípico?

#### Perguntas sobre Variáveis Numéricas:
* **Clientes mais jovens** apresentam uma maior taxa de *default*?
* **Rendas mais baixas** concentram uma maior probabilidade de inadimplência?
* **Menor tempo de emprego** do cliente aumenta a chance de *default*?
* **Valores de empréstimo mais altos** implicam maior probabilidade de inadimplência?
* **Taxas de juros mais altas** aumentam o risco de o cliente se tornar inadimplente?

Ao responder a essas perguntas, a análise de dados irá fornecer *insights* valiosos que guiarão as próximas etapas, como o pré-processamento de dados e a seleção das melhores características para os modelos de *machine learning*.

## Resultados

### 📊 Resultados Comparativos

| Métrica | Modelo 2 Camadas | Modelo 3 Camadas | Modelo 4 Camadas |
| :--- | :---: | :---: | :---: |
| **Acurácia** | 0.9624 | 0.9652 | 0.9661 |
| **Precisão NO DEFAULT** | 0.95 | 0.94 | 0.95 |
| **Precisão DEFAULT** | 0.97 | 0.97 | 0.97 |
| **Recall NO DEFAULT** | 0.88 | 0.90 | 0.90 |
| **Recall DEFAULT** | 0.99 | 0.98 | 0.99 |
| **AUC** | 0.99 | 0.99 | 0.99 |

* Todos os modelos apresentaram **AUC = 0.99**, indicando excelente capacidade de discriminação.
* O modelo de **2 camadas** é simples e eficaz, mas sacrifica *recall* em bons pagadores.
* O modelo de **4 camadas** é mais complexo, mas não apresentou ganhos relevantes em relação ao de 3 camadas.
* O modelo de **3 camadas ocultas** é o mais equilibrado, oferecendo ótima detecção de inadimplentes e redução de falsos positivos sem um custo excessivo de complexidade.

 A **ROC (Receiver Operating Characteristic)** é um gráfico que mostra a performance de um classificador binário.  
- O eixo **X** representa a **taxa de falsos positivos (False Positive Rate — FPR)**.  
- O eixo **Y** representa a **taxa de verdadeiros positivos (True Positive Rate — TPR ou Recall)**.  
- Quanto mais a curva se aproxima do **canto superior esquerdo**, melhor é o desempenho do modelo (alta taxa de acertos e baixa taxa de erros).  

---

### 🔎 O que é o AUC?
- O **AUC (Area Under the Curve)** é a **área sob a curva ROC**.  
- Valores de AUC variam entre **0 e 1**:  
  - **0.5** → Modelo aleatório (sem poder de classificação).  
  - **>0.8** → Bom modelo.  
  - **>0.9** → Excelente modelo.  
- Em termos práticos, o AUC mede a **capacidade do modelo de distinguir entre as classes** (NO DEFAULT e DEFAULT).  

 📌 Resultados Obtidos
- **Modelo com 2 camadas** → AUC = **0.99**  
- **Modelo com 3 camadas** → AUC = **0.99**  
- **Modelo com 4 camadas** → AUC = **0.99**  

- Todos os três modelos apresentam **AUC = 0.99**, o que indica **desempenho quase perfeito** em distinguir inadimplentes (DEFAULT) de bons pagadores (NO DEFAULT).  
- A proximidade das curvas mostra que **não há diferença relevante** entre os modelos em termos de AUC.  
- Isso reforça que, mesmo aumentando a complexidade (de 2 para 4 camadas), **não houve ganho significativo na capacidade discriminatória** — confirmando a conclusão anterior de que o modelo de 3 camadas é o mais equilibrado.  

### Multilayer Perceptron (MLP): 3 Layers

### Análise Detalhada do Modelo de 3 Camadas Ocultas

O modelo de 3 camadas ocultas se destacou como a arquitetura ideal, atingindo o equilíbrio perfeito entre complexidade e desempenho. Com uma **acurácia de 96,83%**, ele demonstrou a maior precisão na classificação de clientes adimplentes e inadimplentes, superando as outras duas arquiteturas.

Sua capacidade superior de aprendizado permitiu capturar padrões mais complexos nos dados sem sofrer de *overfitting* significativo. As métricas de desempenho revelam sua eficácia:

* **Recall para DEFAULT (inadimplentes): 0.98** — O modelo conseguiu identificar corretamente 98% dos clientes que de fato se tornaram inadimplentes.
* **Recall para NO DEFAULT (adimplentes): 0.90** — Houve uma redução nos falsos positivos, minimizando a classificação incorreta de clientes que pagaram suas dívidas.
* **F1-Score para DEFAULT: 0.98** — Essa métrica confirma a robustez do modelo na detecção de inadimplentes, equilibrando de forma eficaz a precisão e o *recall*.

![matriz-confusão]

| Classe real \\ Predita | **NO DEFAULT (0)** | **DEFAULT (1)** |
|-------------------------|--------------------|-----------------|
| **NO DEFAULT (0)**     | **1298** (Verdadeiros Negativos) | **147** (Falsos Positivos) |
| **DEFAULT (1)**        | **84** (Falsos Negativos)        | **5260** (Verdadeiros Positivos) |

### Interpretação
- O modelo identificou corretamente **5260 inadimplentes**.  
- Apenas **84 inadimplentes** foram classificados incorretamente como bons pagadores.  
- **147 bons pagadores** foram classificados incorretamente como inadimplentes.  
- O equilíbrio entre recall e precisão confirma o modelo de 3 camadas como o mais robusto.  


#### 📊 Importância das Variáveis no Modelo Neural

![features-importances]
 🔎 Principais variáveis

1. **historical_default** → A variável mais relevante, com impacto muito superior às demais. Clientes com histórico de inadimplência são fortemente associados a novos casos de default.  
2. **cred_hist_length** → Quanto maior o histórico de crédito, maior a confiança na avaliação. Um histórico curto aumenta a incerteza e o risco.  
3. **loan_int_rate** → Taxa de juros aparece como fator determinante, indicando que empréstimos mais caros estão relacionados a maior probabilidade de inadimplência.  

---

 📌 Variáveis intermediárias

- **customer_age** e **customer_income** → Mostram importância relevante, refletindo que idade e renda impactam a probabilidade de pagamento.  
- **loan_amnt** e **term_years** → O valor e o prazo do empréstimo também são influentes, sugerindo que montantes altos e prazos longos aumentam risco.  

 ⚠️ Variáveis com menor impacto

- **employment_duration**, **loan_intent**, **home_ownership** e **loan_grade** têm importância mais baixa, mas ainda contribuem para a decisão do modelo.  
- Isso indica que, embora relevantes, seu peso no resultado final é bem menor que variáveis financeiras e históricas.  



---

### 📊 Conclusões Técnicas

* Todos os modelos apresentaram **AUC = 0.99**, demonstrando alta capacidade de distinguir entre clientes inadimplentes e adimplentes.
* O modelo de **2 camadas** obteve um bom desempenho, mas classificou mais falsos positivos.
* O modelo de **4 camadas** não trouxe melhorias significativas, apesar da maior complexidade.
* O modelo de **3 camadas ocultas** foi o mais equilibrado, alcançando:
    * **Recall DEFAULT = 0.98** (captura quase todos os inadimplentes).
    * **Recall NO DEFAULT = 0.90** (reduz falsos positivos em relação ao de 2 camadas).
    * **F1-Score DEFAULT = 0.98** (robustez no equilíbrio entre precisão e *recall*).

---

### ✅ Conclusão Final

O modelo de **3 camadas ocultas (MLP)** é o mais adequado para a previsão de inadimplência neste *dataset*, pois combina alto desempenho preditivo com um menor custo de complexidade.




