DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
LOWER_CLASSES_DAYS = DAYS[0:len(DAYS) - 1]

CLASS_NAMES = ['5 класс', '6 класс', '7 класс', '8 класс', '9 класс', '10 класс', '11 класс']
CLASS_NUMBERS = [class_name.split()[0] for class_name in CLASS_NAMES]

CLASS_LETTERS = ['А', 'Б', 'В']

CLASS_PROFILES = ['Технический профиль', 'Естественно-научный профиль', 'Гуманитарный профиль', '']

LESSONS_TIME = ['8:00-8:45', '9:05-9:50', '10:05-10:50', '11:05-11:50', '12:05-12:50', '13:05-13:50', '14:00-14:45',
                '14:50 - 15:35']
LESSONS_TIME_SATURDAY = ['8:00-8:45', '8:50-9:35', '9:40-10:25', '10:30-11:15', '11:20-12:05']

TABLE_HEADER_HEIGHT = 33
TABLE_ROW_HEIGHT = 20.3
TABLE_WIDTH = 460