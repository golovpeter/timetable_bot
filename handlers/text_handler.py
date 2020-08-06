import os

from telebot import types

from config import bot, user_cache
from constants import class_letters, class_numbers, days
from utils import chunk


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text in class_numbers:
        handle_class_number(message)
    elif message.text in class_letters:
        handle_class_letter(message)
    elif message.text in days:
        handel_day_of_the_week(message)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')


def handle_class_number(message):
    class_index = message.text.split()[0]
    user_cache[message.from_user.id] = class_index

    keyboard_letters = types.ReplyKeyboardMarkup(resize_keyboard=True)
    divided_letters = chunk(class_letters, 2)

    for letters in divided_letters:
        keyboard_letters.row(*list(letters))

    bot.send_message(message.chat.id, 'Выберите букву', reply_markup=keyboard_letters)


def handle_class_letter(message):
    user_id = message.from_user.id
    class_index = user_cache[user_id]
    class_letter = message.text
    file_path = os.path.join("school_classes", class_index, "{}-{}.json".format(class_index, class_letter))
    user_cache[user_id] = file_path

    keyboard_days_week = types.ReplyKeyboardMarkup(resize_keyboard=True)
    divided_days = chunk(days, 3)

    for day in divided_days:
        keyboard_days_week.row(*list(day))

    bot.send_message(message.chat.id, "Выберите день недели", reply_markup=keyboard_days_week)


def handel_day_of_the_week(message):
    day_of_the_week = message.text
    file_path = user_cache[message.from_user.id]

    if os.path.isfile(file_path):
        # TODO
        # Вывести расписание, отобразить снова дни недели и кнопку возврата
        pass
    else:
        bot.send_message(message.chat.id, "Расписание для выбранного класса не найдено≥")