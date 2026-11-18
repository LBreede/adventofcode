from collections import Counter
from itertools import combinations
from pathlib import Path


def part1(s: str) -> int:
    a = b = 0
    for x in s.splitlines():
        vals = Counter(x).values()
        a += int(2 in vals)
        b += int(3 in vals)
    return a * b


def part2(s: str) -> str:
    result = ""
    for a, b in combinations(s.splitlines(), 2):
        candidate = "".join(x for x, y in zip(a, b) if x == y)
        if len(candidate) > len(result):
            result = candidate
    return result


inputdata = Path(__file__).resolve().with_name("input.txt").read_text(encoding="utf-8")

example1 = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""

assert part1(example1) == 12
print(part1(inputdata))

example2 = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""
assert part2(example2) == "fgij"
print(part2(inputdata))
