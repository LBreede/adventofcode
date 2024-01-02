import unittest

from day05 import part1, part2


class TestDay05(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("./example_day05.txt", encoding="utf-8") as fp:
            cls.example_data = fp.read()

        with open("./input_day05.txt", encoding="utf-8") as fp:
            cls.input_data = fp.read()

    def test_part1(self):
        self.assertEqual(part1(self.example_data), 35)
        # self.assertEqual(part1(self.input_data), 388071289)

    def test_part2(self):
        self.assertEqual(part2(self.example_data), 46)
        # self.assertEqual(part2(self.input_data), 11827296)


if __name__ == "__main__":
    unittest.main()
