from unittest import TestCase
from parameterized import parameterized

from main import get_courses_list, mentors, courses, durations, max_duration, min_duration


expected_list = [{'title': 'Python-разработчик с нуля',
             'mentors': ['Евгений Шмаргунов', 'Олег Булыгин', 'Дмитрий Демидов',
                         'Кирилл Табельский', 'Александр Ульянцев', 'Александр Бардин',
                         'Александр Иванов', 'Антон Солонилин', 'Максим Филипенко',
                         'Елена Никитина', 'Азамат Искаков', 'Роман Гордиенко'],
             'duration': 14}, {'title': 'Java-разработчик с нуля',
                               'mentors': ['Филипп Воронов', 'Анна Юшина', 'Иван Бочаров',
                                           'Анатолий Корсаков', 'Юрий Пеньков',
                                           'Илья Сухачев', 'Иван Маркитан', 'Ринат Бибиков',
                                           'Вадим Ерошевичев', 'Тимур Сейсембаев',
                                           'Максим Батырев', 'Никита Шумский',
                                           'Алексей Степанов', 'Денис Коротков',
                                           'Антон Глушков', 'Сергей Индюков',
                                           'Максим Воронцов', 'Евгений Грязнов',
                                           'Константин Виролайнен', 'Сергей Сердюк',
                                           'Павел Дерендяев'], 'duration': 20},
            {'title': 'Fullstack-разработчик на Python',
             'mentors': ['Евгений Шмаргунов', 'Олег Булыгин', 'Александр Бардин',
                         'Александр Иванов', 'Кирилл Табельский', 'Александр Ульянцев',
                         'Роман Гордиенко', 'Адилет Асканжоев', 'Александр Шлейко',
                         'Алена Батицкая', 'Денис Ежков', 'Владимир Чебукин',
                         'Эдгар Нуруллин', 'Евгений Шек', 'Максим Филипенко',
                         'Елена Никитина'], 'duration': 12},
            {'title': 'Frontend-разработчик с нуля',
             'mentors': ['Владимир Чебукин', 'Эдгар Нуруллин', 'Евгений Шек',
                         'Валерий Хаслер', 'Татьяна Тен', 'Александр Фитискин',
                         'Александр Шлейко', 'Алена Батицкая', 'Александр Беспоясов',
                         'Денис Ежков', 'Николай Лопин', 'Михаил Ларченко'],
             'duration': 20}]
expected_min =['Fullstack-разработчик на Python']
expected_max =['Java-разработчик с нуля', 'Frontend-разработчик с нуля']

FIXTURES = [(courses, mentors, durations, expected_list)]
FIXTURES_min = [(courses, mentors, durations, expected_min)]
FIXTURES_max = [(courses, mentors, durations, expected_max)]


class TestFunction(TestCase):
    @parameterized.expand(FIXTURES)
    def test_my_function(self, courses, mentors, durations, expected_list):
        self.maxDiff = None
        result = get_courses_list(courses, mentors, durations)
        self.assertEqual(result, expected_list)

    @parameterized.expand(FIXTURES_min)
    def test_min(self, courses, mentors, durations,expected_min):
        self.maxDiff = None
        courses_list = get_courses_list(courses, mentors, durations)
        result = min_duration(courses_list)
        self.assertEqual(result, expected_min)

    @parameterized.expand(FIXTURES_max)
    def test_max(self, courses, mentors, durations, expected_max):
        self.maxDiff = None
        courses_list = get_courses_list(courses, mentors, durations)
        result = max_duration(courses_list)
        self.assertEqual(result, expected_max)


