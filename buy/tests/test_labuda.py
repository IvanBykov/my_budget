from django.test import TestCase

from buy.labuda import operations


class LabudaTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(6, 13, '-')
        self.assertEqual(-7, result)

    def test_multiply(self):
        result = operations(6, 13, '*')
        self.assertEqual(78, result)

    def test_divizion(self):
        result = operations(20, 5, '/')
        self.assertEqual(4, result)