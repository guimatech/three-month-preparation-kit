import unittest
from BreakingTheRecords import breakingRecords


class TestBreakingTheRecords(unittest.TestCase):

    def test_case_0(self):
        scores = [12, 24, 10, 24]
        result = breakingRecords(scores)
        self.assertEqual(result, [1, 1])

    def test_case_1(self):
        scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
        result = breakingRecords(scores)
        self.assertEqual(result, [2, 4])

    def test_case_2(self):
        scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
        result = breakingRecords(scores)
        self.assertEqual(result, [4, 0])


if __name__ == '__main__':
    unittest.main()
