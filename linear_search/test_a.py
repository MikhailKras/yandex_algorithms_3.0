import unittest
from a import check_increasing as func


class TestA(unittest.TestCase):
    def test1(self):
        self.assertEqual(func([1, 7, 9]), 'YES')

    def test2(self):
        self.assertEqual(func([1, 9, 7]), 'NO')

    def test3(self):
        self.assertEqual(func([2, 2, 2]), 'NO')


if __name__ == '__main__':
    unittest.main()
