DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
LOWER_CLASSES_DAYS = DAYS[0:len(DAYS) - 1]

CLASS_NAMES = ['5 класс', '6 класс', '7 класс', '8 класс', '9 класс', '10 класс', '11 класс']
CLASS_NUMBERS = [class_name.split()[0] for class_name in CLASS_NAMES]

CLASS_LETTERS = ['А', 'Б', 'В', 'Г']

LESSONS_TIME = ['8:00-8:45', '8:55-9:40', '9:50-10:35', '10:50-11:35', '11:50-12:35', '12:40-13:25', '13:30-14:15']
LESSONS_TIME_SATURDAY = ['8:00-8:45', '8:50-9:35', '9:40-10:25', '10:30-11:15', '11:20-12:05']

TABLE_HEADER_HEIGHT = 29
TABLE_ROW_HEIGHT = 20.5