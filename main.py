import telebot
import json
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

with open('timetable.json', encoding='utf-8') as json_file:
    timetable = json.load(json_file)

photo = open('imgs/zvonki.png', 'rb').read()
days = list(map(lambda x: x['day_of_the_week'], timetable))


@bot.message_handler(commands=['start'])
def start(message):
    sti = open('imgs/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(days[0])
    item2 = types.KeyboardButton(days[1])
    item3 = types.KeyboardButton(days[2])
    item4 = types.KeyboardButton(days[3])
    item5 = types.KeyboardButton(days[4])
    item6 = types.KeyboardButton(days[5])
    item7 = types.KeyboardButton('Расписание звонков')
    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id,
                     "Привет, {0.first_name}! \nВыбери день недели, чтобы получить "
                     "расписание.".format(
                         message.from_user),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == days[0]:
        lessons = timetable[0]['lessons']
        result = ''
        for lesson in lessons:
            result += str(lesson['lessonNumber']) + "." + " " + " " + \
                      lesson['lessonName'] + " |" + " " + lesson['teacherName'] + " |" \
                      + ' Кабинет: ' + str(lesson['roomNumber']) + '\n'
        bot.send_message(message.chat.id, result)

    elif message.text == days[1]:
        lessons = timetable[1]['lessons']
        result = ''
        for lesson in lessons:
            result += str(lesson['lessonNumber']) + "." + " " + " " + \
                      lesson['lessonName'] + " |" + " " + lesson['teacherName'] + " |" \
                      + ' Кабинет: ' + str(lesson['roomNumber']) + '\n'
        bot.send_message(message.chat.id, result)

    elif message.text == days[2]:
        lessons = timetable[2]['lessons']
        result = ''
        for lesson in lessons:
            result += str(lesson['lessonNumber']) + "." + " " + " " + \
                      lesson['lessonName'] + " |" + " " + lesson['teacherName'] + " |" \
                      + ' Кабинет: ' + str(lesson['roomNumber']) + '\n'
        bot.send_message(message.chat.id, result)

    elif message.text == days[3]:
        lessons = timetable[3]['lessons']
        result = ''
        for lesson in lessons:
            result += str(lesson['lessonNumber']) + "." + " " + " " + \
                      lesson['lessonName'] + " |" + " " + lesson['teacherName'] + " |" \
                      + ' Кабинет: ' + str(lesson['roomNumber']) + '\n'
        bot.send_message(message.chat.id, result)

    elif message.text == days[4]:
        lessons = timetable[4]['lessons']
        result = ''
        for lesson in lessons:
            result += str(lesson['lessonNumber']) + "." + " " + " " + \
                      lesson['lessonName'] + " |" + " " + lesson['teacherName'] + " |" \
                      + ' Кабинет: ' + str(lesson['roomNumber']) + '\n'
        bot.send_message(message.chat.id, result)

    elif message.text == days[5]:
        lessons = timetable[5]['lessons']
        result = ''
        for lesson in lessons:
            result += str(lesson['lessonNumber']) + "." + " " + " " + \
                      lesson['lessonName'] + " |" + " " + lesson['teacherName'] + " |" \
                      + ' Кабинет: ' + str(lesson['roomNumber']) + '\n'
        bot.send_message(message.chat.id, result)

    elif message.text == 'Расписание звонков':
        bot.send_photo(message.chat.id, photo)

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!')


bot.polling(none_stop=True, interval=0)
