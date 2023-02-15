import unittest
from beautiful_string_two_pointers import get_max_goodness as func


class TestGoodness(unittest.TestCase):
    def test_case1(self):
        my_str = 'abcaz'
        k = 2
        self.assertEqual(func(my_str, k), 4)

    def test_case2(self):
        my_str = 'helto'
        k = 2
        self.assertEqual(func(my_str, k), 3)

    def test_case_end_with_replacing(self):
        my_str = 'ablll'
        k = 2
        self.assertEqual(func(my_str, k), 5)

    def test_case_end_without_replacing(self):
        my_str = 'ablll'
        k = 0
        self.assertEqual(func(my_str, k), 3)

    def test_case_end_with_little_replacing(self):
        my_str = 'ablll'
        k = 1
        self.assertEqual(func(my_str, k), 4)

    def test_case_connect_end_to_start(self):
        my_str = 'lblll'
        k = 5
        self.assertEqual(func(my_str, k), 5)

    def test_case_start_with_replacing(self):
        my_str = 'lllab'
        k = 2
        self.assertEqual(func(my_str, k), 5)

    def test_case_start_without_replacing(self):
        my_str = 'lllaa'
        k = 0
        self.assertEqual(func(my_str, k), 3)

    def test_case_start_with_little_replacing(self):
        my_str = 'llladafsasf'
        k = 1
        self.assertEqual(func(my_str, k), 4)

    def test_case_connect_parts(self):
        my_str = 'aqweclvclzllfsl'
        k = 2
        self.assertEqual(func(my_str, k), 5)

    def test_case_all_different(self):
        my_str = 'aqwertyuiopzxcvbnm'
        k = 0
        self.assertEqual(func(my_str, k), 1)

    def test_case_4_from_contest(self):
        my_str = 'effdltvrpq'
        k = 7
        self.assertEqual(func(my_str, k), 9)

    def test_case_8_from_contest(self):
        with open('test_8_beautiful_string_input', encoding='utf-8') as file:
            my_str = file.read()
        k = 1258
        self.assertEqual(func(my_str, k), 1350)


if __name__ == '__main__':
    unittest.main()
