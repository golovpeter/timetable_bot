import io
import json
from itertools import islice

import plotly.graph_objects as go
from telebot import types

from constants import *
from fileutil import FileUtilFactory

file_util = FileUtilFactory.getFileUtil()


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


def create_timetable_image(file_path, message, class_profile):
    day_of_the_week = message.text
    img_path = file_util.getTimetableImagePath(file_path, class_profile, day_of_the_week)

    if file_util.exists(img_path):
        return

    with open(file_path, encoding='utf-8') as json_file:
        timetable = json.load(json_file)
        class_profiles = get_classes_profiles(file_path)
        day_index = DAYS.index(day_of_the_week)
        profile_index = class_profiles.index(class_profile)
        lessons = timetable[profile_index]['timetable'][day_index]['lessons']
        lesson_numbers, name_of_lessons, rooms = get_table_data(lessons)
        layout = go.Layout(margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
                           height=(TABLE_HEADER_HEIGHT + TABLE_ROW_HEIGHT * (len(lessons))),
                           width=TABLE_WIDTH)
        fig = go.Figure(data=[go.Table(columnwidth=[10, 40, 15, 20],
                                       header=dict(
                                           values=['<b>№</b>', '<b>Урок</b>', '<b>Кабинет</b>', '<b>Время</b>']),
                                       cells=dict(values=[lesson_numbers, name_of_lessons, rooms,
                                                          get_lesson_time(day_of_the_week)[0:len(lesson_numbers)]]))],
                        layout=layout)

        img_data = io.BytesIO()
        fig.write_image(img_data, scale=5)
        img_data.seek(0)
        file_util.saveImage(img_path, img_data)


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


def get_classes_profiles(file_path):
    class_profiles = []
    with open(file_path, encoding='utf-8') as json_file:
        timetable = json.load(json_file)
        for i in range(len(timetable)):
            class_profiles.append(timetable[i]['profile'])
    return class_profiles
