import time
import re
from aoc_helper import read_input_to_string, start_day

DAY = 2
EXAMPLE = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
824824821-824824827,2121212118-2121212124"


def is_repeated_twice(n: int) -> bool:
    s = str(n)
    width = len(s)
    return s[: width // 2] == s[width // 2 :]


def is_repeated_multiple(n: int) -> bool:
    s = str(n)
    width = len(s)
    for k in range(1, width // 2 + 1):
        if width % k == 0:
            block = s[:k]
            if block * (width // k) == s:
                return True
    return False


def part1(inputdata: str) -> int:
    result = 0
    for a, b in ((int(y) for y in x.split("-")) for x in inputdata.split(",")):
        result += sum(n for n in range(a, b + 1) if is_repeated_twice(n))
    return result


def part1_re(inputdata: str) -> int:
    result = 0
    pattern = re.compile(r"^(\d+)\1$")
    for a, b in ((int(y) for y in x.split("-")) for x in inputdata.split(",")):
        result += sum(n for n in range(a, b + 1) if re.match(pattern, str(n)))
    return result


def part2(inputdata: str) -> int:
    result = 0
    for a, b in ((int(y) for y in x.split("-")) for x in inputdata.split(",")):
        result += sum(n for n in range(a, b + 1) if is_repeated_multiple(n))
    return result


def part2_re(inputdata: str) -> int:
    result = 0
    pattern = re.compile(r"^(\d+)\1+$")
    for a, b in ((int(y) for y in x.split("-")) for x in inputdata.split(",")):
        result += sum(n for n in range(a, b + 1) if re.match(pattern, str(n)))
    return result


def main():
    start_day(DAY)
    inputdata = read_input_to_string(DAY)

    assert part1(EXAMPLE) == 1227775554
    start = time.time()
    result = part1(inputdata)
    elapsed = time.time() - start
    print(f"Part 1: {result}, took {elapsed:.3f}s")

    assert part2(EXAMPLE) == 4174379265
    start = time.time()
    result = part2(inputdata)
    elapsed = time.time() - start
    print(f"Part 2: {result}, took {elapsed:.3f}s")

    start = time.time()
    result = part1_re(inputdata)
    elapsed = time.time() - start
    print(f"\nPart 1: {result}, took {elapsed:.3f}s (with regex)")

    start = time.time()
    result = part2_re(inputdata)
    elapsed = time.time() - start
    print(f"Part 2: {result}, took {elapsed:.3f}s (with regex)")


if __name__ == "__main__":
    main()
