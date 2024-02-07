import unittest
from unittest.mock import patch
from io import StringIO
from MiniMaxSum import miniMaxSum


class TestMiniMaxSum(unittest.TestCase):

    def test_case_0(self):
        arr = [1, 3, 5, 7, 9]

        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            miniMaxSum(arr)

        console_output = fake_out.getvalue().split()

        self.assertEqual(console_output[0], '16')
        self.assertEqual(console_output[1], '24')

    def test_case_1(self):
        arr = [1, 2, 3, 4, 5]

        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            miniMaxSum(arr)

        console_output = fake_out.getvalue().split()

        self.assertEqual(console_output[0], '10')
        self.assertEqual(console_output[1], '14')

    def test_case_2(self):
        arr = [7, 69, 2, 221, 8974]

        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            miniMaxSum(arr)

        console_output = fake_out.getvalue().split()

        self.assertEqual(console_output[0], '299')
        self.assertEqual(console_output[1], '9271')


if __name__ == '__main__':
    unittest.main()
