import os

import telebot

from cache import UserCacheFactory

# Token from BotFather
TOKEN = os.environ.get('BOT_TOKEN', '')
# Heroku app url
APP_URL = 'https://school4-timetable-dev.herokuapp.com/'

user_cache = UserCacheFactory.getCache()

bot = telebot.TeleBot(TOKEN)
