import unittest

from solution import get_min_transfers as func

import os

cwd = os.getcwd()
files = os.listdir(cwd)
files = list(filter(lambda name: '.txt' in name, files))


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input_files = sorted(files, key=lambda name: int(name.split('_')[1].split('.')[0]))
        print(self.input_files)

    def test_1(self):
        result = func(self.input_files[0])
        self.assertEqual(result, 0)

    def test_2(self):
        result = func(self.input_files[1])
        self.assertEqual(result, 2)

    def test_3(self):
        result = func(self.input_files[2])
        self.assertEqual(result, 1)

    def test_17(self):
        result = func(self.input_files[3])
        self.assertEqual(result, 1)

    def test_24(self):
        result = func(self.input_files[4])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    pass
    unittest.main()
