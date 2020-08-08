import os

import telebot

from cache import UserCacheFactory

# Token from BotFather
TOKEN = os.environ.get('BOT_TOKEN', '')
# Heroku app url
APP_URL = 'https://school4-timetable-dev.herokuapp.com/'
# Directory with timetables
TIMETABLES_DIR = os.path.join('..', 'school_classes')

user_cache = UserCacheFactory.getCache()

bot = telebot.TeleBot(TOKEN)
