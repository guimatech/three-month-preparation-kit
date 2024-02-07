import unittest
from unittest.mock import patch
from io import StringIO
from PlusMinus import plusMinus


class TestPlusMinus(unittest.TestCase):

    def test_case_0(self):
        arr = [-4, 3, -9, 0, 4, 1]

        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            plusMinus(arr, 6)

        console_output = fake_out.getvalue().split()

        self.assertEqual(console_output[0], '0.500000')
        self.assertEqual(console_output[1], '0.333333')
        self.assertEqual(console_output[2], '0.166667')

    def test_case_1(self):
        arr = [1, 2, 3, -1, -2, -3, 0, 0]

        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            plusMinus(arr, 8)

        console_output = fake_out.getvalue().split()

        self.assertEqual(console_output[0], '0.375000')
        self.assertEqual(console_output[1], '0.375000')
        self.assertEqual(console_output[2], '0.250000')

    def test_case_2(self):
        arr = [1, 1, 0, -1, -1]

        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            plusMinus(arr, 5)

        console_output = fake_out.getvalue().split()

        self.assertEqual(console_output[0], '0.400000')
        self.assertEqual(console_output[1], '0.400000')
        self.assertEqual(console_output[2], '0.200000')


if __name__ == '__main__':
    unittest.main()
