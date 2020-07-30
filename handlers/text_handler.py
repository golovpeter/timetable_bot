from telebot import types
from config import bot
from constants import class_letters, class_numbers
from utils import chunk


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text in class_numbers:
        keyboard_letters = types.ReplyKeyboardMarkup(resize_keyboard=True)

        divided_letters = chunk(class_letters, 2)

        for letters in divided_letters:
            keyboard_letters.row(*list(letters))

        bot.send_message(message.chat.id, 'Выберите букву', reply_markup=keyboard_letters)

    elif message.text == 'А':
        bot.send_message(message.chat.id, '123')

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')
