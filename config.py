import os

import telebot

# Token from BotFather
TOKEN = os.environ.get('BOT_TOKEN', '')
# Heroku app url
APP_URL = 'https://test-school4-bot.herokuapp.com/'

user_cache = {}

bot = telebot.TeleBot(TOKEN)
