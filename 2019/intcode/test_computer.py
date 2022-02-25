import unittest
import computer


class TestComputer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example_day_02(self):
        with open("../example/day_02.txt") as f:
            data = list(map(int, f.read().split(",")))
        a = computer.run(data)
        self.assertEqual(a, 3500)

    def test_input_day_02(self):
        with open("../input/day_02.txt") as f:
            data = list(map(int, f.read().split(",")))
        a = computer.run(data, 12, 2)
        self.assertEqual(a, 3058646)

    def test_more_examples_day_02(self):
        pass


if __name__ == "__main__":
    unittest.main()


def main():

    with open("../input/day_02.txt") as f:
        input_day_02 = list(map(int, f.read().split(",")))

    # a = run(example_day_02)
    b = computer.run((1, 0, 0, 0, 99))
    c = computer.run([2, 3, 0, 3, 99], result_idx=3)
    d = computer.run([2, 4, 4, 5, 99, 0], result_idx=5)
    e = computer.run([1, 1, 1, 4, 99, 5, 6, 0, 99])
    f = computer.run(input_day_02, first_noun=12, first_verb=2)
    print(b, c, d, e, f)


# if __name__ == "__main__":
#     main()
