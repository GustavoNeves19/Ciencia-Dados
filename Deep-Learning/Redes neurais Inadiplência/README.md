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

Após o treinamento e avaliação das três arquiteturas de redes neurais, obtivemos os seguintes resultados no conjunto de teste:

- **Modelo com 2 camadas ocultas** → **0.9632**  
- **Modelo com 3 camadas ocultas** → **0.9683**  
- **Modelo com 4 camadas ocultas** → **0.9667**

---

## 🔎 Análise Comparativa

- O **modelo de 3 camadas ocultas** apresentou a **maior acurácia** (**96,83%**), indicando um melhor equilíbrio entre **capacidade de aprendizado** e **generalização**.  
- O **modelo de 2 camadas ocultas** obteve **96,32%**, mostrando que mesmo uma rede relativamente simples já captura bem os padrões dos dados.  
- O **modelo de 4 camadas ocultas** alcançou **96,67%**, muito próximo ao de 3 camadas, mas sem ganhos significativos, o que sugere que o aumento de profundidade não trouxe vantagem relevante neste caso.  

---

### ✅ Conclusão


Com base na análise, o **modelo de 3 camadas ocultas** demonstrou ser a arquitetura mais eficiente para o problema. Embora os três modelos tenham apresentado alta performance, com acurácias acima de 96%, o modelo de 3 camadas alcançou o melhor desempenho, indicando que ele encontrou o ponto ideal entre complexidade e capacidade de generalização, superando as versões mais simples e as mais profundas.
