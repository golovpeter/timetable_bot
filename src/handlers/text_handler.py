import os
import re

from config import bot, user_cache
from constants import *
from utils import create_buttons, get_timetable


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text in CLASS_NAMES:
        handle_class_number(message)
    elif message.text in CLASS_LETTERS:
        handle_class_letter(message)
    elif message.text in DAYS:
        handle_day_of_the_week(message)
    elif message.text == 'Назад':
        handle_return(message)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')


def handle_class_number(message):
    class_index = message.text.split()[0]
    user_cache.put(message.from_user.id, class_index)

    buttons = create_buttons(CLASS_LETTERS, 2)

    bot.send_message(message.chat.id, 'Выбери букву', reply_markup=buttons)


def handle_class_letter(message):
    user_id = message.from_user.id

    if not user_cache.containsKey(user_id) or not user_cache.get(user_id) in CLASS_NUMBERS:
        buttons = create_buttons(CLASS_NAMES, 3, has_return=False)
        bot.send_message(message.chat.id, 'Ошибка. Давай попробуем сначала. Выбери класс', reply_markup=buttons)
        return

    class_index = user_cache.get(user_id)
    class_letter = message.text
    file_path = os.path.join(TIMETABLES_DIR, class_index, "{}-{}.json".format(class_index, class_letter))

    if not os.path.isfile(file_path):
        buttons = create_buttons(CLASS_NAMES, 3, has_return=False)
        bot.send_message(message.chat.id, "Расписание для выбранного класса не найдено", reply_markup=buttons)

    user_cache.put(user_id, file_path)

    if int(class_index) >= 8:
        buttons = create_buttons(DAYS, 3)
    else:
        buttons = create_buttons(LOWER_CLASSES_DAYS, 2)

    bot.send_message(message.chat.id, "Выбери день недели", reply_markup=buttons)


def handle_day_of_the_week(message):
    user_id = message.from_user.id

    if not user_cache.containsKey(user_id) \
            or not bool(re.match(TIMETABLE_PATH_PATTERN, user_cache.get(user_id))):
        buttons = create_buttons(CLASS_NAMES, 3, has_return=False)
        bot.send_message(message.chat.id, 'Ошибка. Давай попробуем сначала. Выбери класс', reply_markup=buttons)
        return

    file_path = user_cache.get(user_id)
    timetable = get_timetable(file_path, message.text)
    bot.send_message(message.chat.id, timetable)


def handle_return(message):
    user_id = message.from_user.id

    if user_cache.containsKey(user_id):
        user_cache.delete(user_id)

    buttons = create_buttons(CLASS_NAMES, 3, has_return=False)
    bot.send_message(message.chat.id, 'Выбери свой класс, чтобы получить расписание', reply_markup=buttons)
