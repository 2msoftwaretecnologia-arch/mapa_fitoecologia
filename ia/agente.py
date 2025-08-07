import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("api_grok")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"
TEMPERATURE = 0.7
max_tokens = 200


def Ask_AI(pergunta):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    mensagem_sistema = (
        """
        Você é um especialista em solos, biomas e regiões fitoecológicas, 
        com amplo conhecimento em classificação pedológica não me entregue com 
        paragrafos nen topicos quero tudo em um texto so.
        """
    )
    
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": mensagem_sistema},
            {"role": "user", "content": pergunta}
        ],
        "temperature": TEMPERATURE,
        "max_tokens": max_tokens  # Adicionando o controle de tokens
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        resposta = response.json()
        
        # Opcional: Mostrar informações de uso de tokens
        usage = resposta.get("usage", {})
        print(f"Tokens usados: {usage.get('total_tokens', 'N/A')}")
        print(f"Tokens na resposta: {usage.get('completion_tokens', 'N/A')}")
        
        return resposta["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {e}"
    except KeyError:
        return "Erro: Resposta da API em formato inesperado."
    



