import os

from config import bot, user_cache
from constants import class_letters, class_numbers, days, lower_classes_days
from utils import create_buttons, get_timetable


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

    buttons = create_buttons(class_letters, 2)

    bot.send_message(message.chat.id, 'Выберите букву', reply_markup=buttons)


def handle_class_letter(message):
    user_id = message.from_user.id
    class_index = user_cache[user_id]
    class_letter = message.text
    file_path = os.path.join("school_classes", class_index, "{}-{}.json".format(class_index, class_letter))
    user_cache[user_id] = file_path

    if int(class_index) >= 8:
        buttons = create_buttons(days, 3)
    else:
        buttons = create_buttons(lower_classes_days, 2)

    bot.send_message(message.chat.id, "Выберите день недели", reply_markup=buttons)


def handel_day_of_the_week(message):
    file_path = user_cache[message.from_user.id]

    if os.path.isfile(file_path):
        timetable = get_timetable(file_path, message.text)
        bot.send_message(message.chat.id, timetable)
    else:
        bot.send_message(message.chat.id, "Расписание для выбранного класса не найдено")
