# 🍎 Classificação da Qualidade de Frutas com Machine Learning

## 🍊 Sobre o Problema

A qualidade de frutas é um fator determinante para **consumo, aceitação do mercado e precificação**.  
Ela depende de múltiplas características físicas e químicas, como tamanho, peso, doçura e acidez, que podem variar significativamente entre diferentes frutas e estágios de maturação.

Neste projeto, o objetivo é **classificar a qualidade da fruta** (alta ou baixa) com base em atributos medidos durante seu processo de avaliação.

As variáveis do conjunto de dados incluem:

- **Size**: Tamanho da fruta.  
- **Weight**: Peso da fruta.  
- **Sweetness**: Nível de doçura.  
- **Juiciness**: Crocância/suculência.  
- **Ripeness**: Estágio de maturação.  
- **Acidity**: Nível de acidez.  
- **Quality**: Variável alvo (boa ou ruim).  

---

## 🧠 Como a Ciência de Dados contribui?

Com Machine Learning, podemos:

- Identificar padrões ocultos que diferenciam frutas de **alta** e **baixa qualidade**.  
- Criar modelos preditivos para automatizar a classificação em tempo real.  
- Apoiar **agricultores, distribuidores e mercados** na tomada de decisão sobre colheita, armazenamento e comercialização.  

---

## ⚙️ Sobre o Modelo Neural MLP

O modelo escolhido foi uma **Rede Neural do tipo Multilayer Perceptron (MLP)**, adequada para problemas de **classificação supervisionada** com múltiplos atributos.

### 🔬 Como funciona?

- A MLP possui **camadas ocultas com função de ativação ReLU**, que capturam relações não lineares entre as variáveis.  
- A camada de saída utiliza **função Sigmoid**, retornando valores entre `0` e `1` para indicar a probabilidade de uma fruta ser de **alta qualidade**.  
- O treinamento é realizado com **backpropagation** e otimização via **Adam**.  

### 🎯 Por que usar MLP neste projeto?

- Capacidade de aprender padrões complexos.  
- Boa performance em tarefas de classificação binária.  
- Flexibilidade para ajustar número de camadas e neurônios conforme a complexidade dos dados.  

---

## 📈 Resultados

- **Acurácia no conjunto de teste**: 95%  
- **F1-Score (classe alta qualidade)**: 93%  
- **ROC-AUC**: 0.97  

Os resultados indicam que o modelo consegue capturar padrões relevantes nos atributos e fornecer previsões robustas para classificação da qualidade das frutas.  

---

## 📂 Estrutura do Projeto

