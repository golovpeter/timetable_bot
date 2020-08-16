import os

import telebot

from cache import UserCacheFactory

# Token from BotFather
TOKEN = os.environ.get('BOT_TOKEN', '')
# Heroku app url
APP_URL = 'https://school4-timetable-dev.herokuapp.com/'
# Directory with timetables
TIMETABLES_DIR = os.path.join('..', 'school_classes')

IMGS_DIR = os.path.join('..', 'imgs')

# S3 Bucket name
BUCKET_NAME = "school4-timetable"
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')

user_cache = UserCacheFactory.getCache()

from fileutil import FileUtilFactory

file_util = FileUtilFactory.getFileUtil()

bot = telebot.TeleBot(TOKEN)
