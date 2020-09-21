import os

import telebot

# Application profile
PROFILE = os.environ.get('PROFILE', 'local')

# Botfather token
TOKEN = os.environ.get('BOT_TOKEN', '')

# Application url in heroku
APP_URL = 'https://school4-timetable-{}.herokuapp.com/'.format(PROFILE)

# Directory paths
TIMETABLES_DIR = os.path.join('..', 'school_classes')
IMG_DIR = os.path.join('..', 'imgs')

# S3 configurations
BUCKET_NAME = os.environ.get('BUCKET_NAME', '')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')

bot = telebot.TeleBot(TOKEN)
