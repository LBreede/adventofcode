import itertools
from pathlib import Path


def part1(s: str, sep: str | None = None) -> int:
    return sum(int(x) for x in s.split(sep))


def part2(s: str, sep: str | None = None) -> int:
    last = 0
    results = {last}
    for x in itertools.cycle(s.split(sep)):
        last += int(x)
        if last in results:
            return last
        results.add(last)
    raise RuntimeError("Unreachable")


inputdata = Path(__file__).resolve().with_name("input.txt").read_text(encoding="utf-8")

assert part1("+1, -2, +3, +1", sep=", ") == 3
assert part1("+1, +1, +1", sep=", ") == 3
assert part1("+1, +1, -2", sep=", ") == 0
assert part1("-1, -2, -3", sep=", ") == -6
print(part1(inputdata))

assert part2("+1, -2, +3, +1", sep=", ") == 2
assert part2("+1, -1", sep=", ") == 0
assert part2("+3, +3, +4, -2, -4", sep=", ") == 10
assert part2("-6, +3, +8, +5, -6", sep=", ") == 5
assert part2("+7, +7, -2, -7, -4", sep=", ") == 14
print(part2(inputdata))
