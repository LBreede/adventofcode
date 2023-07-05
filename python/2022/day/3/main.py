# --- Day 3: Rucksack Reorganization ---
from string import ascii_letters


def get_priorities(items: list, n: int) -> int:
    priorities = 0
    for i in range(len(items) // n):
        if n == 1:
            item = items[i]
            nchars_halved = len(item) // 2
            a, b = set(item[:nchars_halved]), set(item[nchars_halved:])
            intersection = a.intersection(b)
        else:
            intersection = set(ascii_letters)
            for item in items[i * n : i * n + n]:
                intersection = intersection.intersection(set(item))
        priorities += ascii_letters.index(next(iter(intersection))) + 1
    return priorities


with open("input.txt") as fp:
    items = fp.read().splitlines()
part_one = get_priorities(items, 1)
part_two = get_priorities(items, 3)
print("Part 1:", part_one, "\nPart 2:", part_two)
