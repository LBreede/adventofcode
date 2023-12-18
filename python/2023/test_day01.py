import unittest

from day01 import part1, part2


class TestDay01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_data_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

        cls.example_data_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
        with open("./input_day01.txt", encoding="utf-8") as fp:
            cls.data = fp.read()

    def test_part1(self):
        self.assertEqual(part1(self.example_data_1), 142)
        self.assertEqual(part1(self.data), 54708)

    def test_part2(self):
        self.assertEqual(part2(self.example_data_2), 281)
        self.assertEqual(part2(self.data), 54087)


if __name__ == "__main__":
    unittest.main()
