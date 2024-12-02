import io
from typing import IO


def split_columns(file: IO) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in file:
        # a, b = (int(x) for x in line.rstrip().split())
        a, b = map(int, line.rstrip().split())
        left.append(a)
        right.append(b)
    file.close()
    return (left, right)


def part_one(file: IO) -> int:
    left, right = split_columns(file)
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def part_two(file: IO) -> int:
    left, right = split_columns(file)
    return sum(x * right.count(x) for x in left)


def main() -> None:
    example = """3   4
4   3
2   5
1   3
3   9
3   3"""
    answer = part_one(io.StringIO(example))
    assert answer == 11

    file = open("input_day01.txt", "r", encoding="utf-8")
    print(file)
    answer = part_one(file)
    print(f"Part 1: {answer}")

    answer = part_two(io.StringIO(example))
    assert answer == 31

    file = open("input_day01.txt", "r", encoding="utf-8")
    answer = part_two(file)
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
