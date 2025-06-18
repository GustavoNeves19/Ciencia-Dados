# Classificação de Neoplasias com Machine Learning

## 🧬 Sobre o Problema

Neoplasias, conhecidas como tumores, são crescimentos anormais de tecido causados por divisão celular descontrolada. Elas podem ser:

* **Benignas**: não cancerígenas, crescem lentamente e não invadem tecidos vizinhos.
* **Malignas**: cancerígenas, crescem rapidamente, invadem tecidos e podem se espalhar (metástase).

Segundo o Instituto Nacional de Câncer (INCA), o Brasil terá mais de 700 mil novos casos de câncer por ano entre 2023 e 2025. O diagnóstico precoce é crucial para o sucesso do tratamento, e a Ciência de Dados pode apoiar significativamente essa tarefa.

## 🧠 Como a Ciência de Dados contribui?

Com o uso de algoritmos de Machine Learning, é possível:

* Construir modelos preditivos a partir de exames histopatológicos.
* Automatizar o diagnóstico de neoplasias com alta precisão.
* Reduzir tempo de análise e minimizar erros humanos em classificações clínicas.

## ⚙️ Sobre o Modelo LGBM

O modelo utilizado é o **LightGBM Classifier**, uma implementação eficiente de algoritmos de boosting (Gradient Boosting Machines).

### 🔬 Como funciona?

* Baseia-se em árvores de decisão.
* Cria modelos sequenciais, onde cada modelo novo corrige os erros dos anteriores.
* Utiliza **histogramas binários**, otimizando memória e velocidade.
* Suporta diretamente variáveis categóricas.
* Alta escalabilidade para grandes volumes de dados.

### 🎯 Por que usar o LGBM neste projeto?

* Eficiência no treinamento.
* Boa capacidade de generalização.
* Lida bem com desequilíbrio de classes.
* Permite visualização da importância dos atributos.
* É altamente eficaz para tarefas de classificação binária, como diferenciar neoplasias benignas de malignas.

## 📈 Resultados

* **Acurácia no conjunto de teste**: 98.83%
* **F1-Score** com GridSearchCV: 96.61%
* **Validação cruzada (CV=5)**: média de 94.55%
* Utilização de pipeline completo com:

  * Scaler (padronização dos dados)
  * Seleção de atributos (com base em importância)
  * Otimização de hiperparâmetros via GridSearch
  * Avaliação com curva ROC e área sob a curva (AUC > 0.99)

## 📂 Estrutura do Projeto

```
classification-neoplasias/
├── notebooks/
│   └── classification_neoplasias.ipynb     # Notebook principal com exploração e testes
├── data/
│   └── cancer.csv                          # Dataset original
├── models/                                 # Pasta reservada para salvamento de modelos treinados
├── reports/                                # Conclusões, resultados e insights extraídos
├── src/
│   ├── pipeline.py                         # Criação, treino e avaliação do pipeline com LGBM
│   ├── tuning.py                           # Otimização de hiperparâmetros com GridSearchCV
│   └── utils.py                            # Funções auxiliares de carregamento e métricas
├── README.md                               # Este documento
```

## 📊 Conclusão

Este projeto evidencia o poder da Inteligência Artificial aplicada à área da saúde, com foco na classificação automatizada de tumores. O uso do modelo LightGBM mostrou-se eficiente e robusto, com desempenho superior a 98% em acurácia e F1-score otimizado com validação cruzada.

Esse tipo de solução pode auxiliar profissionais da medicina na tomada de decisão e no diagnóstico precoce de neoplasias, contribuindo diretamente para salvar vidas e otimizar recursos clínicos.

---

Desenvolvido com propósito educacional e aplicado a um cenário realista de saúde pública com uso de Ciência de Dados.
