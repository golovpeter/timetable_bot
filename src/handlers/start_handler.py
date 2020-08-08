from config import bot
from utils import create_buttons
from constants import CLASS_NAMES


@bot.message_handler(commands=['start'])
def start(message):
    buttons = create_buttons(CLASS_NAMES, 3, has_return=False)

    bot.send_message(message.chat.id,
                     "Привет, {0.first_name}! \nВыбери свой класс, чтобы получить "
                     "расписание.".format(
                         message.from_user),
                     parse_mode='html', reply_markup=buttons)
