from django.test import TestCase

from buy.labuda import operations


class LabudaTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_plus(self):
        #print('test_plus')
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        #print('test_minus')
        result = operations(6, 13, '-')
        self.assertEqual(-7, result)

    def test_multiply(self):
        #print('test_multiply')
        result = operations(6, 13, '*')
        self.assertEqual(78, result)

    def test_divizion(self):
        #print('test_divizion')
        result = operations(20, 5, '/')
        self.assertEqual(4, result)
