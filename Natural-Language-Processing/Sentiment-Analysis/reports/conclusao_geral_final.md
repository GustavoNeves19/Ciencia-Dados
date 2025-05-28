
# 📌 Conclusão Final

Percebe-se que esse dataframe possui quatro classes de sentimentos: *Neutro*, *Irrelevante*, *Positivo* e *Negativo*. Determinados modelos conseguiram prever essas quatro classes com excelentes resultados, como mostrado nas avaliações do Random Forest e do Extra Trees.

O modelo **Random Forest** alcançou uma acurácia de **95.6%**, enquanto o **Extra Trees** obteve **96.2%**, com métricas de F1-score, precisão e recall consistentemente acima de 0.95 para todas as classes. Isso indica que ambos os modelos são altamente confiáveis para classificar sentimentos em textos do Twitter, com destaque para o Extra Trees em termos de precisão nas classes *Positive* e *Neutral*.

A análise da matriz de confusão revelou que as maiores confusões ocorrem entre as classes *Neutral* e *Positive*, o que é esperado em tarefas de PLN, dado o conteúdo subjetivo e o tom ambíguo de muitos comentários. Apesar disso, os erros são relativamente baixos e não comprometem a performance geral do modelo.

### 🎯 Observações Estratégicas

Para fins de negócio, é viável considerar a **redução das quatro classes para duas**, agrupando *Neutral* e *Irrelevante* como *Não-Negativas*, e mantendo apenas *Positivo* e *Negativo*. Isso porque:
- Comentários neutros, em muitos contextos, não indicam insatisfação e podem ser tratados como *comentários aceitáveis*.
- Comentários irrelevantes podem conter ruídos que não agregam valor à análise estratégica.

Essa **redefinição de classes** deve ser guiada pelos objetivos do projeto: se o foco for monitoramento de crise, priorizar *Negativo* vs *Não-Negativo* pode ser mais eficaz. Se o objetivo for análise de satisfação, manter as quatro classes pode enriquecer a granularidade.

---

Este projeto demonstra a aplicação de **aprendizado de máquina** em um problema real de **processamento de linguagem natural (PLN)**, utilizando dados da plataforma Kaggle: [Análise de sentimento do Twitter](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis/code). Os modelos foram validados com rigor e estão prontos para serem integrados em pipelines de análise automatizada de sentimentos com potencial para dashboard, APIs ou interfaces interativas com Streamlit.

