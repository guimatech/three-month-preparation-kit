import unittest
from TimeConversion import timeConversion


class TestPlusMinus(unittest.TestCase):

    def test_case_0(self):
        s = '12:01:00PM'
        result = timeConversion(s)
        self.assertEqual(result, '12:01:00')

    def test_case_1(self):
        s = '12:01:00AM'
        result = timeConversion(s)
        self.assertEqual(result, '00:01:00')

    def test_case_2(self):
        s = '07:05:45PM'
        result = timeConversion(s)
        self.assertEqual(result, '19:05:45')


if __name__ == '__main__':
    unittest.main()
