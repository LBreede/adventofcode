# --- Day 2: Password Philosophy ---

import re

valid_one = valid_two = 0
with open("input.txt") as fp:
    for line in fp:
        a, b, letter, pw = re.search(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
        valid_one += 1 if int(a) <= pw.count(letter) <= int(b) else 0
        valid_two += 1 if (pw[int(a) - 1] == letter) ^ (pw[int(b) - 1] == letter) else 0
print("Part 1:", valid_one, "\nPart 2:", valid_two)
