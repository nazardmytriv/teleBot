import os
import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привіт! Я працюю на AWS 🚀")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()