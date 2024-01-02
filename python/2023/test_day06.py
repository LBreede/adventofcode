import unittest

from day06 import part1, part2


class TestDay06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_data = """Time:      7  15   30
Distance:  9  40  200"""

        with open("./input_day06.txt", encoding="utf-8") as fp:
            cls.input_data = fp.read()

    def test_part1(self):
        self.assertEqual(part1(self.example_data), 288)
        self.assertEqual(part1(self.input_data), 449820)

    def test_part2(self):
        self.assertEqual(part2(self.example_data), 71503)

    # self.assertEqual(part2(self.input_data), 11827296)


if __name__ == "__main__":
    unittest.main()
