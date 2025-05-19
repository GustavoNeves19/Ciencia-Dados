
# 🧠 Análise de Sentimentos no Twitter com PLN

Este projeto aplica técnicas de **Processamento de Linguagem Natural (PLN)** e **Machine Learning Supervisionado** para classificar sentimentos em tweets mencionando empresas. Os dados foram retirados do Kaggle e foram tratados para treinar modelos que conseguem prever se um tweet é **positivo**, **negativo**, **neutro** ou **irrelevante**.

---

## ❓ O problema

Empresas precisam monitorar a opinião pública em redes sociais como o Twitter. Mas analisar isso manualmente é inviável em larga escala. Este projeto usa IA para automatizar essa tarefa e detectar rapidamente menções críticas, elogiosas ou neutras.

---

## 🧠 O que é Processamento de Linguagem Natural (PLN)?

O PLN é uma área da inteligência artificial que ensina os computadores a entenderem a linguagem humana (como textos e falas). Neste projeto, ele é usado para transformar tweets (textos) em **números** que os modelos de machine learning conseguem entender e analisar.

---

## 🛠 Tecnologias usadas

- **Python** (Pandas, Scikit-learn, NLTK)
- **TF-IDF** para transformar texto em números
- **Modelos supervisionados**: Random Forest e Extra Trees
- **Avaliação com métricas**: Acurácia, F1-score, Matriz de Confusão
- **Deploy com Streamlit** (aplicação web interativa)

---

## 🧪 Resultados

| Modelo        | Acurácia | F1-score |
|---------------|----------|----------|
| Random Forest | 95.6%    | 95.6%    |
| Extra Trees   | 96.2%    | 96.2%    |

> Veja os relatórios detalhados na pasta `/reports`

## Conclusões do Projeto 📍

- [Conclusão do `Random Forest`](./reports/conclusao_random_forest.md)

- [Conclusão do `Extra Tress`](./reports/conclusao_extra_trees.md)

- [Conclusão Geral](./reports/conclusao_geral_final.md)

---

## ▶️ Como rodar a aplicação (Streamlit)

1. Instale as dependências:
```bash
pip install -r app/requirements.txt
```

2. Execute a aplicação:
```bash
streamlit run app/app.py
```

---

## 📁 Estrutura do Projeto

| Pasta         | Conteúdo                                      |
|---------------|-----------------------------------------------|
| `app/`        | Código da aplicação Streamlit para o deploy   |
| `models/`     | Modelos treinados e vetorizador TF-IDF        |
| `data/`       | Dataset de validação                          |
| `reports/`    | Relatórios de avaliação dos modelos           |
| `images/`     | Matrizes de confusão e gráficos               |
| `utils/`      | Funções auxiliares para preprocessamento      |

---

## 📊 Conclusão

Este projeto demonstrou como é possível aplicar PLN e machine learning para classificar sentimentos em redes sociais com alta precisão. Os resultados obtidos mostraram que os modelos Random Forest e Extra Trees são confiáveis e prontos para serem utilizados em produção com uma interface web (Streamlit).

A estrutura do projeto também está preparada para futuras melhorias, como agrupamento binário de sentimentos (Negativo x Não Negativo) e deploy com Docker.

---

## 👤 Autor

Gustavo Neves da Paz Rafael
