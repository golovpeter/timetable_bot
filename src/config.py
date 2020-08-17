import os

import telebot

from cache import UserCacheFactory

PROFILE = os.environ.get('PROFILE', 'local')
TOKEN = os.environ.get('BOT_TOKEN', '')
APP_URL = 'https://school4-timetable-{}.herokuapp.com/'.format(PROFILE)
TIMETABLES_DIR = os.path.join('..', 'school_classes')

IMGS_DIR = os.path.join('..', 'imgs')

# S3 Bucket name
BUCKET_NAME = os.environ.get('BUCKET_NAME', '')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')

user_cache = UserCacheFactory.getCache()

from fileutil import FileUtilFactory

file_util = FileUtilFactory.getFileUtil()

bot = telebot.TeleBot(TOKEN)
