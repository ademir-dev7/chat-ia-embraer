
# CHAT IA - EMBRAER


# Importa as bibliotecas necessárias
# "from X import Y" = pegar Y de dentro de X
from groq import Groq
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
# É aqui que ele lê sua chave de API
load_dotenv()

# Cria o cliente Groq usando a chave do .env
# os.getenv busca a variável GROQ_API_KEY do arquivo .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Lista que guarda o histórico da conversa
# Igual ArrayList do Java
historico = []

# Instrução secreta que define o comportamento da IA
system_prompt = """
Você é um assistente técnico especializado em aviação e aeronáutica, com foco em aeronaves da Embraer e do setor aeroespacial brasileiro.

Suas responsabilidades:
- Responder perguntas sobre aeronaves, manutenção, componentes e terminologia técnica
- Usar linguagem técnica precisa, com siglas e normas do setor quando aplicável
- Ser direto e objetivo nas respostas
- Quando relevante, mencionar normas como RBAC, AMM, IPC ou documentação ANAC/FAA

Regras importantes:
- Responda SEMPRE em português brasileiro
- Se não souber algo, diga claramente — nunca invente dados técnicos ou especificações
- Em dúvidas de segurança operacional, sempre recomende consultar documentação oficial
- Após responder qualquer pergunta, finalize com: "Posso te ajudar com mais alguma coisa?"
"""
# Cabeçalho do chat
print("=" * 50)
print("   ASSISTENTE TÉCNICO - EMBRAER IA")
print("=" * 50)
print("Digite 'sair' para encerrar.\n")

# Loop infinito — igual while(true) do Java
while True:

    # Lê o que o usuário digitou — igual Scanner do Java
    pergunta = input("Você: ")

    # Se digitar 'sair', encerra
    if pergunta.lower() == "sair":
        print("Encerrando. Até logo!")
        break

    # Adiciona pergunta no histórico
    historico.append({
        "role": "user",
        "content": pergunta
    })

    # Chama a IA com o histórico completo
    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            *historico,
        ]
    )

    # Extrai o texto da resposta
    texto_resposta = resposta.choices[0].message.content

    # Salva resposta no histórico
    historico.append({
        "role": "assistant",
        "content": texto_resposta
    })

    # Mostra a resposta
    print(f"\nIA: {texto_resposta}\n")