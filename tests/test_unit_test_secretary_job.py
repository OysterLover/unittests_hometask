import unittest
from parameterized import parameterized
from unittest.mock import patch
from main_hw_secretary_job import people, shelf, to_list, add


FIXTURE_people = [
            ("10006", "Аристарх Павлов"),
            ("dshfgg9", 'Invalid number')
        ]


FIXTURE_add = [
            ('passport', '376', 'Harry Potter', '2', 'Document added'),
            ('diploma', '5743', 'Draco Malfoy', '18', 'Invalid shelf number')
        ]

FIXTURE_shelf = [
            ("10006", '2'),
            ("dshfgg9", 'Invalid number')
        ]

class TestFunctions(unittest.TestCase):

    @parameterized.expand(FIXTURE_people)
    def test_people(self, a, result):
        self.assertEqual(people(a), result)

    @parameterized.expand(FIXTURE_shelf)
    def test_shelf(self, a, result):
        self.assertEqual(shelf(a), result)

    def test_to_list(self):
        #т.к. значения могут меняться пользователем, можно проверить, является ли возвращаемый объект списком
        result = to_list()
        self.assertIsInstance(result, list)

    @parameterized.expand(FIXTURE_add)
    def test_add(self, a, b, c, d, result):
        self.assertEqual(add(a, b, c, d), result)
