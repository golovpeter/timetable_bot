from itertools import islice
from telebot import types
from constants import days
import json


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def create_buttons(array, chunk_length):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    divided_objects = chunk(array, chunk_length)

    for objects in divided_objects:
        keyboard.row(*list(objects))

    return keyboard


def get_timetable(file_path, day_of_the_week):
    with open(file_path, encoding='utf-8') as json_file:
        timetable = json.load(json_file)
        i = days.index(day_of_the_week)
        lessons = timetable[i]['lessons']
        result = ''
        for lesson in lessons:
            result += '{}. {} | {}:{} \n'.format(str(lesson['lessonNumber']), lesson['lessonName'],
                                                 'Кабинет ', lesson['roomNumber'])
        return result
