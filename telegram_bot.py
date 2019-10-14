import telebot
from telebot import apihelper
import requests
import json

with open('config.json') as json_file:
    config = json.load(json_file)
token = config['telegram_api_token']
bot = telebot.TeleBot(token)

apihelper.proxy = {'https': 'https://167.71.59.12:80'}


@bot.message_handler(commands=['meme'])
def send_very_funny_meme(msg):
    response = requests.get("https://meme-api.herokuapp.com/gimme").json()
    meme_url = response['url']
    meme_pic = requests.get(meme_url)
    bot.send_photo(msg.chat.id, meme_pic.content)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Say hello if you want to talk with me! Write /help for more information")


@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    bot.reply_to(message, "Write /meme to get very funny picture")


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Hello":
        bot.send_message(message.from_user.id, "Hello! I am MEMEBOT! How can I help you?")
    elif message.text == "How low?":
        bot.send_message(message.from_user.id, "When the lights out it`s not dangerous! Here we are now! Entertain us!")
    else:
        bot.send_message(message.from_user.id, "Sorry, I can only send memes")


bot.polling(none_stop=True, timeout=123)
