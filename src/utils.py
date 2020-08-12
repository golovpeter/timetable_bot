import os
import json
import plotly.graph_objects as go

from itertools import islice
from telebot import types
from constants import *
from config import IMGS_DIR


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def create_buttons(array, chunk_length, has_return=True):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    divided_objects = chunk(array, chunk_length)

    for objects in divided_objects:
        keyboard.row(*list(objects))

    if has_return:
        keyboard.row('Назад')

    return keyboard


def create_timetable_image(file_path, message):
    with open(file_path, encoding='utf-8') as json_file:
        timetable = json.load(json_file)
        i = DAYS.index(message.text)
        lessons = timetable[i]['lessons']
        lesson_numbers, name_of_lessons, rooms = get_table_data(lessons)
        layout = go.Layout(margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
                           height=(TABLE_HEADER_HEIGHT + TABLE_ROW_HEIGHT * (len(lessons))))
        fig = go.Figure(data=[go.Table(header=dict(values=['№', 'Урок', 'Кабинет', 'Время']),
                                       cells=dict(values=[lesson_numbers, name_of_lessons, rooms,
                                                          get_lesson_time(message.text)[0:len(lesson_numbers)]]))],
                        layout=layout)

        fig.write_image(os.path.join(IMGS_DIR, str(message.from_user.id) + '.png'), scale=5)


def get_lesson_time(day_of_the_week):
    if day_of_the_week != 'Суббота':
        return LESSONS_TIME
    else:
        return LESSONS_TIME_SATURDAY


def get_table_data(lessons):
    lesson_numbers = []
    name_of_lessons = []
    rooms = []
    counter = 1
    for lesson in lessons:
        if lesson['lessonNumber'] != counter:
            lesson_numbers.append(counter)
            name_of_lessons.append('-')
            rooms.append('-')
            counter += 1

        lesson_numbers.append(lesson['lessonNumber'])
        name_of_lessons.append(lesson['lessonName'])
        rooms.append(lesson['roomNumber'])
        counter += 1

    return lesson_numbers, name_of_lessons, rooms
