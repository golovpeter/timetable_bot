import os
import json
import plotly.graph_objects as go

from itertools import islice
from telebot import types
from constants import DAYS, LESSONS_TIME, LESSONS_TIME_SATURDAY


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


def get_timetable(file_path, message):
    if os.path.isfile(str(message.from_user.id) + '.png'):
        return

    with open(file_path, encoding='utf-8') as json_file:
        timetable = json.load(json_file)
        i = DAYS.index(message.text)
        lessons = timetable[i]['lessons']
        lessosn_numbers = list(map(lambda x: x['lessonNumber'], lessons))
        name_of_lessons = list(map(lambda x: x['lessonName'], lessons))
        rooms = list(map(lambda x: x['roomNumber'], lessons))
        layout = go.Layout(margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
                           height=(29 + 20.5 * (len(lessons))))
        fig = go.Figure(data=[go.Table(header=dict(values=['№', 'Урок', 'Кабинет', 'Время']),
                                       cells=dict(values=[lessosn_numbers, name_of_lessons, rooms,
                                                          get_lesson_time(message.text)[0:len(lessosn_numbers)]]))],
                        layout=layout)

        fig.write_image(os.path.join('..', 'imgs', 'out' + '.png'), scale=5)


def get_lesson_time(day_of_the_week):
    if day_of_the_week != 'Суббота':
        return LESSONS_TIME
    else:
        return LESSONS_TIME_SATURDAY
