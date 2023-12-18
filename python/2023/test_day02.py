import unittest

from day02 import part1, part2


class TestDay02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

        with open("./input_day02.txt", encoding="utf-8") as fp:
            cls.data = fp.read()

    def test_part1(self):
        self.assertEqual(part1(self.example_data), 8)
        self.assertEqual(part1(self.data), 2101)

    def test_part2(self):
        self.assertEqual(part2(self.example_data), 2286)
        self.assertEqual(part2(self.data), 58269)


if __name__ == "__main__":
    unittest.main()
