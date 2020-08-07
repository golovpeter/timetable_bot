import os

import telebot

# Token from BotFather
TOKEN = os.environ.get('BOT_TOKEN', '')
# Heroku app url
APP_URL = 'https://school4-timetable-dev.herokuapp.com/'

user_cache = {}

bot = telebot.TeleBot(TOKEN)
