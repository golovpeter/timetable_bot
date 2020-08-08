import telebot

from config import bot
from constants import CLASS_NAMES
from utils import create_buttons

logger = telebot.logger


@bot.message_handler(commands=['start'])
def start(message):
    logger.info("Start message received from user {}".format(message.from_user.username))
    buttons = create_buttons(CLASS_NAMES, 3, has_return=False)

    bot.send_message(message.chat.id,
                     "Привет, {0.first_name}! \nВыбери свой класс, чтобы получить "
                     "расписание.".format(
                         message.from_user),
                     parse_mode='html', reply_markup=buttons)
