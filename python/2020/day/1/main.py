# --- Day 1: Report Repair ---


def part_one(numbers):
    for a in numbers:
        for b in numbers:
            if a + b == 2020 and a != b:
                return a * b


def part_two(numbers):
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == 2020 and a != b != c:
                    return a * b * c


with open("input.txt") as fp:
    numbers = [int(x) for x in fp.readlines()]
print("Part 1:", part_one(numbers), "\nPart 2:", part_two(numbers))
