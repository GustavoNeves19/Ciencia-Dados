import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json
from utils import process_validation_data
from genai_agente import generate_marketing_plan, IS_AGENT_READY # Importa o Agente Gemini

# --- CONFIGURAÇÃO DE CONSTANTES ---
# URL da sua API de Classificação (FastAPI).
API_ENDPOINT = "http://127.0.0.1:8000/predict/sentiment" 

# Cores para os sentimentos
COLOR_MAP = {
    "Positive": "green",
    "Negative": "red",
    "Neutral": "gray",
    "Irrelevant": "orange"
}

# --- Configuração da Página (Primeiro comando Streamlit) ---
st.set_page_config(page_title="Análise de Sentimentos - Holding (API)", layout="wide")


# --- FUNÇÃO DE CHAMADA DA API ---
def classify_via_api(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chama o endpoint da API de classificação de sentimentos com os dados brutos.
    
    Args:
        df (pd.DataFrame): DataFrame com as colunas 'content' e 'entity'.
        
    Returns:
        pd.DataFrame: DataFrame original com a coluna 'Sentimento' adicionada, ou None em caso de falha.
    """
    # Prepara os dados para o formato JSON esperado pela API (lista de objetos com content e entity)
    data_to_send = df[['content', 'entity']].to_dict('records')
    
    try:
        response = requests.post(API_ENDPOINT, json=data_to_send, timeout=30)
        
        # Verifica se a requisição foi bem-sucedida (código 200)
        if response.status_code == 200:
            results = response.json()
            
            # Adiciona os sentimentos de volta ao DataFrame original
            sentiments = [res['sentiment'] for res in results]
            df['Sentimento'] = sentiments
            
            return df
        else:
            st.error(f"Erro na API de Classificação (Status: {response.status_code}). Verifique se o 'api_server.py' está ativo.")
            st.json(response.json())
            return None
            
    except requests.exceptions.ConnectionError:
        st.error(f"Erro de Conexão: A API ({API_ENDPOINT}) não está respondendo. Certifique-se de que o uvicorn está rodando.")
        return None
    except Exception as e:
        st.error(f"Erro inesperado ao chamar a API: {e}")
        return None

# --- BARRA LATERAL E STATUS ---
if not IS_AGENT_READY:
    st.sidebar.warning("Agente de IA DESATIVADO: Verifique se a variável GEMINI_API_KEY está configurada no seu arquivo .env.")
else:
    st.sidebar.success("Agente de IA (Gemini) PRONTO.")
    
st.sidebar.info(f"API de Classificação alvo: {API_ENDPOINT}")


# --- INTERFACE PRINCIPAL ---
st.title("📊 Análise de Sentimentos sobre Empresas do Holding (API-Driven)")
st.markdown("Envie um arquivo `.csv` com as colunas `entity` e `content` para gerar insights estratégicos e planos de ação.")

# Upload do arquivo
uploaded_file = st.file_uploader("Envie o CSV com os comentários:", type="csv")

if uploaded_file is not None:
    
    # Leitura inicial do CSV (apenas colunas necessárias, sem pré-processamento local)
    try:
        df_raw = process_validation_data(uploaded_file)
        # Garante que temos as colunas necessárias para enviar à API
        if 'entity' not in df_raw.columns or 'content' not in df_raw.columns:
            st.error("O CSV deve conter as colunas 'entity' e 'content'.")
            st.stop()
            
    except Exception as e:
        st.error(f"Erro ao ler o CSV: {e}")
        st.stop()


    # 1. Chamada da API para Classificação
    with st.spinner(f"Enviando {len(df_raw)} comentários para a API de classificação..."):
        df = classify_via_api(df_raw.copy()) # Envia uma cópia para evitar warnings do Streamlit

    if df is None:
        st.stop() # Interrompe se a API falhou

    st.success("Classificação concluída pela API!")


    # 2. Filtragem de Dados
    empresas = ["Todas"] + sorted(df["entity"].unique().tolist())
    empresa_selecionada = st.selectbox("Filtrar por Empresa", empresas)
    df_filtrado = df if empresa_selecionada == "Todas" else df[df["entity"] == empresa_selecionada]

    
    # 3. PAINEL DE VISUALIZAÇÃO
    st.markdown("---")
    st.header("Análise de Sentimentos e Distribuição")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total de Comentários", len(df_filtrado))
    with col2:
        st.metric("Empresas Distintas", df_filtrado["entity"].nunique())

    st.subheader("🎯 Distribuição Geral dos Sentimentos")
    pie_fig = px.pie(df_filtrado, names="Sentimento", title="Distribuição Geral dos Sentimentos",
                      color="Sentimento", color_discrete_map=COLOR_MAP)
    st.plotly_chart(pie_fig, use_container_width=True)

    st.subheader("📌 Ranking de Sentimentos por Empresa")
    sentiment_counts = df_filtrado.groupby(["entity", "Sentimento"]).size().reset_index(name="Quantidade")
    bar_sent = px.bar(sentiment_counts, x="entity", y="Quantidade", color="Sentimento",
                      title="Sentimentos por Empresa", barmode="group", color_discrete_map=COLOR_MAP)
    st.plotly_chart(bar_sent, use_container_width=True)

    # Gráfico de Top Empresas (usando o DF completo para o ranking, se "Todas" estiver selecionado)
    st.subheader("🏆 Top 5 Empresas com Mais Comentários")
    df_ranking = df if empresa_selecionada == "Todas" else df_filtrado
    top_empresas = df_ranking["entity"].value_counts().nlargest(5).reset_index()
    top_empresas.columns = ["Empresa", "Quantidade"]
    bar_top = px.bar(top_empresas, x="Empresa", y="Quantidade", title="Top 5 Empresas com Mais Comentários", color_discrete_sequence=['#4CAF50'])
    st.plotly_chart(bar_top, use_container_width=True)

    
    # 4. GERAÇÃO DE PLANO DE AÇÃO (IA GENERATIVA)
    st.markdown("---")
    if empresa_selecionada != "Todas":
        st.header(f"✨ Plano de Ação Generativo para {empresa_selecionada}")
        
        if not IS_AGENT_READY:
            st.warning("O recurso de Plano de Ação generativo está desativado. Verifique a configuração da chave API do Gemini no seu arquivo .env.")
        else:
            # Filtrar Comentários Negativos e Neutros
            df_problemas = df_filtrado[df_filtrado["Sentimento"].isin(["Negative", "Neutral"])]
            
            if len(df_problemas) > 0:
                st.info(f"Analisando {len(df_problemas)} comentários (Negativos e Neutros) para gerar o plano de ação. Será utilizada uma amostra de até 100 comentários.")

                # Pega os textos dos comentários para enviar à LLM
                comentarios_a_analisar = df_problemas['content'].tolist()
                
                if st.button(f"🚀 Gerar Plano de Ação de Marketing com IA para {empresa_selecionada}", type="primary"):
                    with st.spinner("Gerando Plano de Ação. Isso pode levar alguns segundos..."):
                        # CHAMA A FUNÇÃO ENCAPSULADA NO genai_agent.py
                        plano_markdown = generate_marketing_plan(
                            company_name=empresa_selecionada, 
                            problem_comments=comentarios_a_analisar
                        )
                        
                        # Exibir o Resultado
                        st.subheader("Resultado Gerado pela IA")
                        st.markdown(plano_markdown)

            else:
                st.success(f"Não há comentários Negativos ou Neutros para {empresa_selecionada}. Não é necessário um plano de ação imediato.")
    
    else:
        st.info("Selecione uma empresa específica no filtro 'Filtrar por Empresa' para gerar um Plano de Ação de Marketing com IA Generativa.")


    # 5. Comentários Classificados e Download
    st.markdown("---")
    st.subheader("📋 Comentários Classificados")
    st.dataframe(df_filtrado[["entity", "content", "Sentimento"]])

    # Download do CSV rotulado
    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar CSV com Sentimentos",
        data=csv,
        file_name="comentarios_classificados.csv",
        mime="text/csv"
    )