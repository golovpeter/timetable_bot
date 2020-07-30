from telebot import types
from config import bot
from utils import chunk
from constants import class_numbers


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    divided_classes = list(chunk(class_numbers, 3))

    for classes in divided_classes:
        markup.row(*list(classes))

    bot.send_message(message.chat.id,
                     "Привет, {0.first_name}! \nВыбери день недели, чтобы получить "
                     "расписание.".format(
                         message.from_user),
                     parse_mode='html', reply_markup=markup)
