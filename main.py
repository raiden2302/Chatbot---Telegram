
import telebot
import os
from dotenv import load_dotenv

load_dotenv()
import requests
import json

chave_api_telegram = os.getenv('TOKEN_TELEGRAM')
chave_api_openrouter = os.getenv('TOKEN_OPENROUTER')

if not chave_api_telegram:
    print('chave n encontrada')
    exit()
if not chave_api_openrouter:
    print('chave open n encontrada')
    exit()

bot = telebot.TeleBot(chave_api_telegram)


@bot.message_handler(commands=['start'])
def boasvindas(mensagem):
    bot.send_message(mensagem.chat.id, 'Olá! Como posso te ajudar?')


historico = {}


@bot.message_handler(func=lambda message: True)
def responder(mensagem):
    bot.send_chat_action(mensagem.chat.id, 'typing')

    usuario_id = mensagem.from_user.id

    if usuario_id not in historico:
        historico[usuario_id] = []

    historico[usuario_id].append({
        "role": "user",
        "content": mensagem.text
    })

    historico[usuario_id] = historico[usuario_id][-10:]

    mensagens = [
                    {
                        "role": "system",
                        "content": """
        Você é a Mia (Mentor.IA), uma assistente especializada em comunicação profissional (Não apresentar essa informação em cada resposta) 
        Pelos dados coletados em um formulário com 53 pessoas, 63% disse que não tem treinamento em suas empresas, principalmente na area de comunicação, vendas e contato com o público.
        Por isso, devido a falta de treinamento,você deve servir como uma mentora, para substituir esse treinamento.
        Seu diferencial: O diferencial da Mentor.IA é ser uma inteligência artificial especializada em comportamento organizacional, capaz de analisar problemas de comunicação dentro das empresas e gerar recomendações personalizadas para melhorar relações entre colaboradores, gestores e equipes. Diferente de IAs genéricas, ela possui um foco específico em gestão de pessoas, identificando dificuldades como falhas de comunicação, falta de clareza nas tarefas e necessidades de treinamento.

        Texto curto para a rotina corrida de trabalho.

        Responda:
        - Seja imparcial, seguinto questões éticas e morais.
        - curto (5 a 8 linhas)
        - direto
        - prático
        - pronto para uso no trabalho e dia a dia
        -Não utilize "*" nem formatação de texto como: negrito, itáligo, bold, sublinhado etc
        """
                    }
                ] + historico[usuario_id]

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + chave_api_openrouter,
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat-v3",
            "max_tokens": 300,
            "messages": mensagens
        },
        timeout=20
    )

    dados = response.json()

    if "choices" in dados:
        texto_da_ia = dados["choices"][0]["message"]["content"]
        bot.send_message(mensagem.chat.id, texto_da_ia)

    elif "error" in dados:
        print("Erro da OpenRouter:", dados["error"])
        bot.send_message(mensagem.chat.id, "Erro na IA.")

    else:
        print("Resposta inesperada:", dados)
        bot.send_message(mensagem.chat.id, "Erro inesperado.")


print('bot iniciado!')

bot.infinity_polling(timeout=10, long_polling_timeout=5)


