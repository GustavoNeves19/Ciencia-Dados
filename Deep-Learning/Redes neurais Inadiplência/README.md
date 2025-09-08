### 📌 Previsão de Inadimplência com Redes Neurais

---

### 🔎 Sobre o Problema

A **inadimplência em empréstimos** é um dos principais desafios do setor financeiro. Identificar quais clientes têm maior risco de não pagar suas dívidas é essencial para reduzir prejuízos e criar políticas de crédito mais seguras. Com a evolução da **Inteligência Artificial**, modelos de **redes neurais artificiais (RNA)** têm sido aplicados com sucesso para prever o status de um cliente (adimplente ou inadimplente).

### ⚙️ Implementações dos Modelos Neurais

Neste projeto, foram implementadas três arquiteturas de redes neurais do tipo **Multilayer Perceptron (MLP)** para a tarefa de classificação binária do status do empréstimo (**DEFAULT** ou **NO DEFAULT**). As redes foram criadas usando a API `Sequential` do Keras.

#### 🔹 Modelo com 2 Camadas Ocultas
* **Arquitetura**: Entrada → 14 neurônios (ReLU) → 14 neurônios (ReLU) → 1 neurônio (Sigmoid)
* **Características**: Estrutura mais simples, ideal como baseline para comparação, e com menor risco de *overfitting*.

#### 🔹 Modelo com 3 Camadas Ocultas
* **Arquitetura**: Entrada → 14 neurônios (ReLU) → 14 neurônios (ReLU) → 14 neurônios (ReLU) → 1 neurônio (Sigmoid)
* **Características**: Captura relações não lineares mais complexas, com maior capacidade de representação e um leve aumento do risco de *overfitting*.

#### 🔹 Modelo com 4 Camadas Ocultas
* **Arquitetura**: Entrada → 32 neurônios (ReLU) → 16 neurônios (ReLU) → 16 neurônios (ReLU) → 8 neurônios (ReLU) → 1 neurônio (Sigmoid)
* **Características**: Rede mais profunda e variada em número de neurônios, adequada para padrões complexos. Demanda mais regularização (*Dropout*, *EarlyStopping*).

---

### 🧮 Função Sigmoid

Usada na camada de saída para classificação binária, a função **Sigmoid** retorna valores entre 0 e 1, que são interpretados como probabilidade:
* Valores próximos de 0 → **NO DEFAULT**
* Valores próximos de 1 → **DEFAULT**

Essa função é compatível com a função de perda `binary_crossentropy`.

---

### ❓ Por que usar Redes Neurais neste problema?

* **Alta capacidade** de aprender padrões complexos em dados históricos de clientes.
* **Melhor desempenho** em relação a classificadores lineares em datasets grandes.
* **Possibilidade de generalizar** melhor e reduzir perdas financeiras.

---

### 📊 Resultados Comparativos

| Métrica | Modelo 2 Camadas | Modelo 3 Camadas | Modelo 4 Camadas |
| :--- | :---: | :---: | :---: |
| **Acurácia** | 0.9624 | 0.9652 | 0.9661 |
| **Precisão NO DEFAULT** | 0.95 | 0.94 | 0.95 |
| **Precisão DEFAULT** | 0.97 | 0.97 | 0.97 |
| **Recall NO DEFAULT** | 0.88 | 0.90 | 0.90 |
| **Recall DEFAULT** | 0.99 | 0.98 | 0.99 |
| **AUC** | 0.99 | 0.99 | 0.99 |

---

### ✅ Conclusão

* Todos os modelos apresentaram **AUC = 0.99**, indicando excelente capacidade de discriminação.
* O modelo de **2 camadas** é simples e eficaz, mas sacrifica *recall* em bons pagadores.
* O modelo de **4 camadas** é mais complexo, mas não apresentou ganhos relevantes em relação ao de 3 camadas.
* O modelo de **3 camadas ocultas** é o mais equilibrado, oferecendo ótima detecção de inadimplentes e redução de falsos positivos sem um custo excessivo de complexidade.