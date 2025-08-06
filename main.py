import os
import openai
import telebot

openai.api_key = os.environ["OPENAI_API_KEY"]
bot = telebot.TeleBot(os.environ["TELEGRAM_BOT_TOKEN"])

@bot.message_handler(func=lambda message: True)
def responder_com_ia(message):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, resposta.choices[0].message.content)
    except Exception as e:
        bot.reply_to(message, f"Erro: {e}")

bot.polling()
