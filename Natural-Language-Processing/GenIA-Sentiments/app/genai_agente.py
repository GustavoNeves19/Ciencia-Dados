import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# --- Carregar variáveis de ambiente do arquivo .env ---
load_dotenv()
api_key = os.getenv("API_KEY") 

try:
    # Passa a chave API, que agora é carregada do .env
    client = genai.Client(api_key=api_key) 
    IS_AGENT_READY = True
except Exception as e:
    print(f"ERRO: Não foi possível inicializar o cliente Gemini. Verifique a configuração da GEMINI_API_KEY no arquivo .env. Detalhes: {e}")
    client = None
    IS_AGENT_READY = False

def generate_marketing_plan(company_name: str, problem_comments: list) -> str:
    """
    Gera um plano de ação de marketing usando a LLM Gemini com base em comentários negativos/neutros.
    
    Args:
        company_name (str): O nome da empresa selecionada.
        problem_comments (list): Lista de comentários classificados como Negativo ou Neutro.
        
    Returns:
        str: O plano de ação formatado em Markdown ou uma mensagem de erro.
    """
    if not IS_AGENT_READY or client is None:
        return "Erro: O Agente de IA não está pronto. Verifique a configuração da GEMINI_API_KEY no seu ambiente."

    # Limitar a quantidade de comentários a enviar para a IA para evitar excesso de tokens
    limite_comentarios = 100
    comentarios_amostra = problem_comments[:limite_comentarios]
    
    # Converte a lista para uma string única
    comentarios_str = "\n".join([f"- {c}" for c in comentarios_amostra])

    # 1. Definindo a Instrução de Sistema (Persona do Agente) como uma STRING
    # A instrução de sistema agora é passada diretamente como uma string.
    system_instruction_text = "Você é um estrategista de marketing digital e especialista em satisfação do cliente. Sua resposta deve ser formatada estritamente em Markdown e ser clara e concisa."
    
    # 2. Criar o Prompt do Usuário (Tarefa)
    user_query = f"""
    Sua tarefa é analisar os seguintes comentários de clientes para a empresa '{company_name}' e gerar um plano de ação de marketing focado em converter as percepções negativas e neutras em positivas.

    Comentários a serem analisados (Negativos/Neutros):
    {comentarios_str}

    Gere o plano de ação seguindo EXATAMENTE este formato:
    
    ## 1. Identificação dos Principais Problemas
    * Problema 1: (Descrição baseada nos comentários)
    * Problema 2: (Descrição baseada nos comentários)
    * Problema 3: (Descrição baseada nos comentários)

    ## 2. Plano de Ação Tático para Marketing e Atendimento
    1. Ação 1: (Foco em comunicação e melhoria de imagem)
    2. Ação 2: (Foco em comunicação e melhoria de imagem)
    3. Ação 3: (Foco em comunicação e melhoria de imagem)

    ## 3. Mensagem de Conversão (Modelo de Resposta)
    [Sugestão de resposta genérica e profissional para interagir com esses comentários.]
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[user_query],
            config=types.GenerateContentConfig(
                system_instruction=system_instruction_text
            )
        )
        return response.text

    except Exception as e:
        return f"Erro ao gerar o plano de ação da IA: {e}"