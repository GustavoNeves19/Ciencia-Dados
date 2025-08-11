# Deep Learning: Fundamentos e Aplicações

## O que é Deep Learning?

**Deep Learning** (ou Aprendizado Profundo) é uma subárea do **Machine Learning (Aprendizado de Máquina)** que se baseia em **redes neurais artificiais** com múltiplas camadas (daí o termo "profundo"). Essas redes são projetadas para **imitar o funcionamento do cérebro humano** e são capazes de aprender representações de dados de forma hierárquica, extraindo características complexas a partir de dados brutos.

O **Deep Learning** se destaca especialmente em tarefas que envolvem grandes volumes de dados e complexidade, como **processamento de linguagem natural**, **reconhecimento de voz**, **previsões financeiras**, entre outras.

### Principais Aplicações de Deep Learning

As redes neurais profundas têm sido fundamentais para avanços significativos em diversas áreas. Algumas das principais aplicações incluem:

- **Reconhecimento de Padrões e Imagens**: Embora a visão computacional não seja abordada neste README, o Deep Learning tem sido amplamente utilizado em **detecção de objetos**, **segmentação de imagens** e **reconhecimento facial**.
- **Processamento de Linguagem Natural (PLN)**: Tarefas como **tradução automática**, **resumo de textos**, **análise de sentimentos** e **chatbots** são exemplos em que o Deep Learning tem se mostrado muito eficaz.
- **Previsão de Séries Temporais**: Em **Data Science**, o Deep Learning é amplamente utilizado para **prever preços de ações**, **analisar dados econômicos** e fazer **previsões de demanda de produtos**.
- **Análise de Dados e Previsões de Mercado**: Aplicações como **análise de tendências de mercado** e **previsão de vendas** são realizadas com redes neurais profundas para lidar com grandes volumes de dados.

### Tipos de Redes Neurais em Data Science

Deep Learning utiliza diferentes tipos de **redes neurais** para resolver problemas específicos. Em **Data Science**, as mais comuns incluem:

#### 1. **Redes Neurais Feedforward (FNN - Feedforward Neural Networks)**
- As redes **Feedforward** são compostas por camadas de neurônios onde os dados fluem **apenas em uma direção**, da entrada até a saída. 
- Usadas para tarefas **supervisionadas**, como classificação e regressão.
  
#### 2. **Redes Neurais Convolucionais (CNN - Convolutional Neural Networks)**
- **CNNs** são ideais para **análise de dados estruturados** com padrões espaciais, como **imagens**. Porém, sua utilização também é relevante em **textos** ou **séries temporais** quando aplicadas em técnicas de **embedding**.

#### 3. **Redes Neurais Recorrentes (RNN - Recurrent Neural Networks)**
- As **RNNs** são redes projetadas para lidar com **dados sequenciais**, como texto ou séries temporais. Elas têm a capacidade de **lembrar informações passadas**.
- **LSTM (Long Short-Term Memory)** e **GRU (Gated Recurrent Unit)** são variações que melhoram a memória e o aprendizado de **dependências de longo prazo**.

#### 4. **Redes Neurais Multicamadas (MLP - Multi-layer Perceptron)**
- Um tipo de **rede neural profunda** composta por várias camadas densas conectadas entre si, usada para uma variedade de tarefas de **classificação** e **regressão**.

#### 5. **Autoencoders**
- **Autoencoders** são redes projetadas para **redução de dimensionalidade** e **detecção de anomalias**. Elas aprendem a **codificar dados de entrada** em uma representação compacta e depois reconstrui-los.

### Tecnologias e Ferramentas Usadas em Deep Learning

Para implementar soluções de **Deep Learning**, diversas tecnologias e ferramentas podem ser utilizadas. Abaixo estão algumas das mais populares no campo de **Data Science**:

#### 1. **Bibliotecas de Deep Learning**

- **TensorFlow**: Biblioteca de código aberto amplamente usada para construção e treinamento de modelos de **deep learning**. Suporta redes neurais profundas e é utilizada em ambientes de **produção** e **pesquisa**.
- **Keras**: Biblioteca de alto nível que facilita a criação de redes neurais. Keras é usada como interface para o TensorFlow.
- **PyTorch**: Framework de deep learning com **forte suporte à comunidade** e excelente para **pesquisa** e **prototipagem rápida**. É muito popular em tarefas de **processamento de linguagem natural**.
- **Theano**: Embora menos utilizado atualmente, Theano foi um dos primeiros frameworks a permitir cálculos de redes neurais de maneira eficiente e paralelizada.
  
#### 2. **Plataformas de Treinamento**

- **Google Colab**: Plataforma de **computação em nuvem** que oferece **GPU gratuita** para treinamento de modelos, facilitando o desenvolvimento de projetos em **Deep Learning**.
- **Kaggle**: Além de ser uma plataforma de competição, **Kaggle** oferece ambientes para **treinamento de modelos de machine learning** e **deep learning**, com datasets e kernels prontos para uso.

#### 3. **Ambientes de Desenvolvimento**

- **Jupyter Notebook**: Ferramenta interativa que facilita a prototipagem, experimentação e documentação do código. Ideal para projetos de **Data Science** e **Deep Learning**.
- **VS Code / PyCharm**: IDEs robustas que oferecem excelente suporte ao desenvolvimento de projetos em Python, incluindo depuração e integração com **TensorFlow** e **PyTorch**.

#### 4. **Ferramentas para Pré-processamento de Dados**

- **Pandas**: Biblioteca fundamental para manipulação e análise de dados em Python, oferecendo ferramentas para trabalhar com **DataFrames** e realizar operações em larga escala.
- **NumPy**: Biblioteca para manipulação eficiente de arrays e cálculos numéricos. Fundamental para operações com dados em **Deep Learning**.
- **Scikit-learn**: Embora não seja específico de Deep Learning, **Scikit-learn** é frequentemente usado para tarefas de pré-processamento, como **normalização de dados**, **seleção de características** e **treinamento de modelos básicos**.

#### 5. **Ferramentas de Visualização**

- **Matplotlib / Seaborn**: Bibliotecas populares para visualização de dados em Python, usadas para criar gráficos e **curvas de erro**, além de visualizações de **tendências e padrões**.
- **TensorBoard**: Ferramenta para visualização de **métricas de treinamento** e **performance de modelos** no TensorFlow.

---

## Projetos
Aqui está uma lista dos projetos contidos neste repositório. Clique no link de cada projeto para ver seu README.md específico e obter mais detalhes.

- [Previsão de Preços de Ações da NVIDIA Utilizando Redes Neurais Profundas](./RNN-NVIDIA/)
    - **Descrição**: O projeto "Previsão de Preços de Ações da NVIDIA Utilizando Redes Neurais Profundas" tem como objetivo desenvolver um modelo de **Deep Learning** para prever os preços futuros das ações da **NVIDIA**. O modelo utiliza redes neurais **LSTM** (Long Short-Term Memory) para analisar dados históricos de preços e fazer previsões de curto prazo. O modelo é capaz de aprender as **dependências temporais** nos dados de séries temporais e gerar previsões precisas, permitindo **análises financeiras** e **estratégias de investimento** com base nas tendências do mercado.

    - **Tecnologias**: Keras, Scikit-learn, TensorFlow


## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
