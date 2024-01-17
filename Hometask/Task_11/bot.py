import telebot
from Task1 import get_url_from_data as get_url_from_data
from Task1 import get_giphy_data as get_giphy_data
from keys import key_telegram as key


TOKEN = key()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
   bot.send_message(
       message.chat.id,'Please enter a word to search for Giphy.')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    search_text = message.text.lower()
    urls = get_url_from_data(get_giphy_data(search_text))
    bot.send_message(message.chat.id, f"{urls}")

bot.polling()

