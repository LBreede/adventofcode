# --- Day 6: Tuning Trouble ---

import re


def get_regex(n):
    regex = "([a-z])"
    for i in range(1, n):
        regex += "(?!"
        for j in range(1, i + 1):
            regex += f"\\{j}" if j == i else f"\\{j}|"
        regex += ")[a-z]" if i == n - 1 else ")([a-z])"
    return regex


with open("input.txt") as fp:
    data = fp.read()
part_one = re.search(get_regex(4), data).span()[1]
part_two = re.search(get_regex(14), data).span()[1]
print("Part 1:", part_one, "\nPart 2:", part_two)
