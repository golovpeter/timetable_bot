from config import TIMETABLES_DIR

DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
LOWER_CLASSES_DAYS = DAYS[0:len(DAYS) - 1]

CLASS_NAMES = ['5 класс', '6 класс', '7 класс', '8 класс', '9 класс', '10 класс', '11 класс']
CLASS_NUMBERS = [class_name.split()[0] for class_name in CLASS_NAMES]

CLASS_LETTERS = ['А', 'Б', 'В', 'Г']

TIMETABLE_PATH_PATTERN = "^{}/".format(TIMETABLES_DIR) + "\\d{1,2}/\\d{1,2}-\\w.json$"
