from config import TIMETABLES_DIR

DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
LOWER_CLASSES_DAYS = DAYS[0:len(DAYS) - 1]

CLASS_NAMES = ['5 класс', '6 класс', '7 класс', '8 класс', '9 класс', '10 класс', '11 класс']
CLASS_NUMBERS = [class_name.split()[0] for class_name in CLASS_NAMES]

CLASS_LETTERS = ['А', 'Б', 'В', 'Г']

TIMETABLE_PATH_PATTERN = "^{}/".format(TIMETABLES_DIR) + "\\d{1,2}/\\d{1,2}-\\w.json$"

LESSONS_TIME = {
    1: '8:00-8:45',
    2: '8:55-9:40',
    3: '9:50-10:35',
    4: '10:50-11:35',
    5: '11:50-12:35',
    6: '12:40-13:25',
    7: '13:30-14:15'
}

LESSONS_TIME_SATURDAY = {
    1: '8:00-8:45',
    2: '8:50-9:35',
    3: '9:40-10:25',
    4: '10:30-11:15',
    5: '11:20-12:05'
}
