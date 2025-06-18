# Pasta: models/

Esta pasta é reservada para o armazenamento de modelos treinados, em especial os arquivos `.pkl` resultantes do processo de treinamento e tuning do modelo.

## 📁 Conteúdo Esperado

* `lgbm_best_model.pkl`: modelo LightGBM treinado com os melhores hiperparâmetros encontrados via GridSearchCV.
* Outros modelos intermediários ou alternativos também podem ser salvos aqui para comparação futura.

## ⚠️ Importante

Esta pasta está incluída no `.gitignore` por dois motivos:

1. **Evitar versionamento de arquivos grandes** (GitHub possui limite de 100 MB por arquivo).
2. **Boa prática de segurança e organização**, mantendo o repositório leve e portável.

## 🛠️ Recomendação

Caso deseje disponibilizar o modelo treinado:

* Utilize um link externo (ex: Google Drive, Hugging Face, Weights & Biases, etc.)
* Ou forneça um script para reentreinamento, como já implementado neste repositório.

---

> Esta README garante que mesmo que a pasta `models/` não esteja visível no GitHub, sua existência e função fiquem documentadas.
