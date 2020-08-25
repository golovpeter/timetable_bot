import os

from config import bot, user_cache, TIMETABLES_DIR, file_util, PROFILE
from constants import *
from utils import create_buttons, create_timetable_image


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
    cache_dict = {'class_index': class_index}
    user_cache.put(message.from_user.id, cache_dict)

    buttons = create_buttons(CLASS_LETTERS, 2)

    bot.send_message(message.chat.id, 'Выбери букву', reply_markup=buttons)


def handle_class_letter(message):
    user_id = message.from_user.id

    if not user_cache.containsKey(user_id) or not (user_cache.get(user_id)).get('class_index') in CLASS_NUMBERS:
        buttons = create_buttons(CLASS_NAMES, 3, has_return=False)
        bot.send_message(message.chat.id, 'Ошибка. Давай попробуем сначала. Выбери класс', reply_markup=buttons)
        return

    class_index = user_cache.get(user_id).get('class_index')
    class_letter = message.text
    file_path = os.path.join(TIMETABLES_DIR, class_index, "{}-{}.json".format(class_index, class_letter))

    if not os.path.isfile(file_path):
        buttons = create_buttons(CLASS_NAMES, 3, has_return=False)
        bot.send_message(message.chat.id, "Расписание для выбранного класса не найдено", reply_markup=buttons)

    cache_dict = {'class_index': class_index, 'class_letter': class_letter, 'file_path': file_path}
    user_cache.put(user_id, cache_dict)

    if int(class_index) >= 8:
        buttons = create_buttons(DAYS, 3)
    else:
        buttons = create_buttons(LOWER_CLASSES_DAYS, 2)

    bot.send_message(message.chat.id, "Выбери день недели", reply_markup=buttons)


def handle_day_of_the_week(message):
    if PROFILE == 'prod':
        bot.send_message(message.chat.id, "Каникулы! Приходи 1-ого сентября :)")
        return

    user_id = message.from_user.id

    if not user_cache.containsKey(user_id) or not os.path.isfile(user_cache.get(user_id).get('file_path')):
        buttons = create_buttons(CLASS_NAMES, 3, has_return=False)
        bot.send_message(message.chat.id, 'Ошибка. Давай попробуем сначала. Выбери класс', reply_markup=buttons)
        return

    timetable_path = user_cache.get(user_id).get('file_path')
    create_timetable_image(timetable_path, message)
    img_path = file_util.getTimetableImagePath(timetable_path, message.text)
    img_data = file_util.getFileDescriptor(img_path)
    bot.send_photo(message.chat.id, img_data)


def handle_return(message):
    user_id = message.from_user.id

    if user_cache.containsKey(user_id):
        user_cache.delete(user_id)

    buttons = create_buttons(CLASS_NAMES, 3, has_return=False)
    bot.send_message(message.chat.id, 'Выбери свой класс, чтобы получить расписание', reply_markup=buttons)
