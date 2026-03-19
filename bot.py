import telebot

TOKEN = "8434399652:AAFRWhgu_9kdjzYkAnsghMUz0AgC-v9zgK0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot aktif bro 🔥")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.polling()
