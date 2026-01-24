from operator import add, sub
import time

from aoc_helper import read_input_to_string, start_day

DAY = 1
EXAMPLE = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def part1(inputdata: str) -> int:
    password = 0
    dial = 50
    for line in inputdata.splitlines():
        op = add if line[0] == "R" else sub
        dial = op(dial, int(line[1:])) % 100
        password += int(dial == 0)
    return password


def part2(inputdata: str) -> int:
    password = 0
    dial = 50
    for line in inputdata.splitlines():
        op = add if line[0] == "R" else sub
        for _ in range(int(line[1:])):
            dial = op(dial, 1) % 100
            password += int(dial == 0)
    return password


def main():
    start_day(DAY)
    inputdata = read_input_to_string(DAY)

    assert part1(EXAMPLE) == 3
    start = time.time()
    result = part1(inputdata)
    elapsed = time.time() - start
    print(f"Part 1: {result}, took {elapsed:.3f}s")

    assert part2(EXAMPLE) == 6
    start = time.time()
    result = part2(inputdata)
    elapsed = time.time() - start
    print(f"Part 2: {result}, took {elapsed:.3f}s")


if __name__ == "__main__":
    main()
