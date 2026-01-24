import time
from aoc_helper import read_input_to_string, start_day

DAY = 0
EXAMPLE = ""


def part1(inputdata: str) -> int:
    return len(inputdata.splitlines())


def part2(inputdata: str) -> int:
    return len(inputdata.splitlines())


def main():
    start_day(DAY)
    inputdata = read_input_to_string(DAY)

    assert part1(EXAMPLE) == 42
    start = time.time()
    result = part1(inputdata)
    elapsed = time.time() - start
    print(f"Part 1: {result}, took {elapsed:.3f}s")

    assert part2(EXAMPLE) == 27
    start = time.time()
    result = part2(inputdata)
    elapsed = time.time() - start
    print(f"Part 2: {result}, took {elapsed:.3f}s")


if __name__ == "__main__":
    main()
