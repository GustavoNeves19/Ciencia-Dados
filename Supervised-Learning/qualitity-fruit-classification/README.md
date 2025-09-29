# 🍎 Classificação da Qualidade de Frutas com Machine Learning  

## 🧬 Sobre o Problema  

A qualidade de frutas é um fator determinante na aceitação pelo consumidor e no valor de mercado. Características como **tamanho, peso, doçura, crocância, suculência, maturação e acidez** influenciam diretamente na percepção de qualidade.  

O desafio é classificar automaticamente as frutas em duas categorias:  

* **Good (boa qualidade)**  
* **Bad (baixa qualidade)**  

Isso permite automatizar processos de seleção, reduzir custos e aumentar a eficiência na cadeia de produção e distribuição.  

## 🧠 Como a Ciência de Dados Contribui?  

Com o uso de algoritmos de Machine Learning, é possível:  

* **Classificar frutas automaticamente** a partir de atributos físicos e sensoriais.  
* **Reduzir a subjetividade** da avaliação manual feita por humanos.  
* **Otimizar processos industriais**, evitando que frutas de baixa qualidade cheguem ao consumidor final.  
* **Apoiar decisões estratégicas**, como ajustes no cultivo ou no controle de qualidade.  

## ⚙️ Sobre os Modelos  

Foram testados diversos modelos de classificação supervisionada:  

* **Decision Tree**  
* **Extra Tree**  
* **Random Forest**  
* **Extra Trees Classifier**  
* **XGBoost**  
* **LightGBM**  

Esses modelos são baseados em **árvores de decisão e ensemble methods**, adequados para lidar com variáveis contínuas e problemas de classificação binária.  

## 🔬 Como Funciona o Modelo  

* **Entrada**: Variáveis numéricas representando as características da fruta:  
  - `Size`, `Weight`, `Sweetness`, `Crunchiness`, `Juiciness`, `Ripeness`, `Acidity`  
* **Pré-processamento**:  
  - Padronização com **Z-score**.  
  - Transformação da variável alvo `Quality` em classes numéricas (`0 = bad`, `1 = good`).  
* **Treinamento**: Modelos supervisionados treinados com validação cruzada e ajuste de hiperparâmetros.  
* **Saída**: Classificação final da fruta em **Good** ou **Bad**.  

## 📈 Resultados  

### 6.1 Acurácia no Conjunto de Teste  
- **Extra Trees**: 90.0%  
- **Random Forest**: 89.6%  
- **XGBoost**: 89.5%  

### 6.2 Accuracy Geral  
- A média dos modelos ficou em torno de **90% de acurácia**, com **F1-Score = 0.90** para ambas as classes.  

### 6.3 Pipeline  
O pipeline de Machine Learning incluiu:  

1. **Pré-processamento**: limpeza, encoding da variável alvo e padronização.  
2. **Divisão dos dados**: treino (70%) e teste (30%), mantendo classes balanceadas.  
3. **Treinamento dos modelos**: ajuste de hiperparâmetros com validação cruzada.  
4. **Avaliação**: métricas de precisão, recall, f1-score, matrizes de confusão e curva ROC.  

## 📊 Conclusão  

* O modelo **Extra Trees Classifier** apresentou o melhor desempenho geral, atingindo **90% de acurácia** no teste e um **AUC de 0.9148**.  
* **Random Forest e XGBoost** também mostraram resultados sólidos (AUC ≈ 0.96), confirmando boa generalização.  
* Modelos mais simples como **Decision Tree e Extra Tree isolados** tiveram performance inferior, indicando overfitting ou baixa robustez.  

✅ **Conclusão final**: O uso de **métodos ensemble (Extra Trees, Random Forest, XGBoost)** garante maior robustez e precisão na tarefa de classificação da qualidade das frutas, tornando-os a melhor escolha para aplicações reais no setor agrícola e alimentício.  


