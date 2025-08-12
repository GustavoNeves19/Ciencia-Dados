# Conclusão Geral do Projeto: Previsão de Preços de Ações da NVIDIA

## Objetivo do Projeto

Este projeto teve como objetivo a construção de um modelo de **Deep Learning** utilizando **LSTM (Long Short-Term Memory)** para prever os **preços de fechamento das ações da NVIDIA**. O modelo foi treinado com dados históricos da ação e utilizado para prever os preços futuros. A partir das previsões geradas, comparamos os resultados obtidos com os **valores reais** de fechamento da ação.

## Resultados Obtidos

### **Desempenho do Modelo**

A seguir, apresentamos as métricas que avaliam o desempenho do modelo, bem como a comparação entre as **previsões feitas** e os **valores reais**.

### **Métricas de Avaliação**:
- **MSE (Erro Quadrático Médio)**: 0.0117  
  O **MSE** mede a média dos erros quadráticos, sendo uma métrica importante para avaliar a magnitude do erro. O valor baixo de MSE sugere que o modelo foi capaz de prever os preços de maneira razoavelmente precisa.

- **MAE (Erro Absoluto Médio)**: 0.0749  
  O **MAE** indica o erro médio absoluto entre as previsões e os valores reais. O valor de **0.0749** sugere que o erro médio é relativamente pequeno, mas ainda existe uma margem de melhoria.

- **MAPE (Erro Absoluto Percentual Médio)**: 339.35%  
  O **MAPE** foi bastante elevado, indicando que o modelo tem dificuldades em prever com precisão para certos períodos, resultando em grandes desvios percentuais. Esse valor sugere que o modelo pode ter dificuldades em lidar com flutuações grandes nos preços.

- **R² (Coeficiente de Determinação)**: 0.9897  
  O **R²** é uma métrica que indica a proporção da variabilidade nos dados explicada pelo modelo. Um valor de **0.9897** indica que o modelo tem uma **excelente capacidade de explicação**, ou seja, **98.97%** da variabilidade dos preços de fechamento é explicada pelo modelo.

### **Comparação dos Resultados**

A comparação entre os valores **previstos** e **reais** revelou que o modelo **subestimou** consistentemente os preços de fechamento da ação da NVIDIA. Abaixo estão as diferenças:

- **Diferenças em Reais**:
  - 25/04/2024: Previsão R$906.16 vs Real R$846.71 → **Diferença de R$59.45**
  - 26/04/2024: Previsão R$881.86 vs Real R$762.00 → **Diferença de R$119.86**
  - 29/04/2024: Previsão R$860.01 vs Real R$795.18 → **Diferença de R$64.83**
  - 30/04/2024: Previsão R$874.15 vs Real R$824.23 → **Diferença de R$49.92**
  - 01/05/2024: Previsão R$840.35 vs Real R$796.77 → **Diferença de R$43.58**

### **Análise e Melhorias Futuras**

1. **Overfitting**: O modelo apresenta boas **métricas de ajuste** (R²), mas o **MAPE elevado** sugere que há problemas de **generalização**. Pode ser necessário ajustar a arquitetura do modelo e aplicar técnicas mais avançadas de regularização.

2. **Exploração de Hiperparâmetros**: O ajuste de hiperparâmetros como o número de **unidades LSTM**, a **taxa de dropout**, e a **função de ativação** pode melhorar a precisão do modelo, especialmente nas previsões de maior variação.

3. **Ajuste de Dados**: A qualidade dos dados de entrada pode ser aprimorada com a **normalização** e a **remoção de outliers** para reduzir o impacto de dados anômalos no desempenho do modelo.

4. **Incorporação de Variáveis Externas**: A adição de **variáveis econômicas**, como indicadores do mercado, pode ajudar o modelo a capturar melhor as flutuações no mercado de ações.

## Previsões Futuras

Com a melhoria contínua da arquitetura do modelo e a adição de dados adicionais, espera-se que o modelo se torne mais robusto e capaz de fornecer previsões mais precisas. A **técnica LSTM** mostrará uma boa capacidade de prever séries temporais, especialmente quando os ajustes necessários forem realizados.

## Conclusão Final

O modelo de **Deep Learning** baseado em **LSTM** para previsão de preços de fechamento da **NVIDIA** apresentou **um desempenho satisfatório**, com uma boa capacidade de explicar a variabilidade nos dados (R²) e um erro aceitável em relação aos preços de fechamento. No entanto, ajustes nas técnicas de **regularização** e **exploração de novos dados** são necessários para **melhorar a precisão** do modelo, especialmente em termos de **previsão de grandes flutuações de preços**.

O projeto fornece uma **base sólida para futuras melhorias** e pode ser expandido para incluir **mais variáveis** e **otimização contínua** do modelo para atender às necessidades do mercado financeiro.
