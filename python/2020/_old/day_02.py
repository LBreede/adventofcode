# --- Day 2: Password Philosophy ---

from aoc_helper import load_input


def process_data(filename):
    lst = load_input(filename)
    lst = [x.split() for x in lst]
    data = []
    for x in lst:
        count = list(map(int, x[0].split("-")))
        char = x[1].replace(":", "")
        data.append([count, char, x[2]])
    return data


def count_valid(data):
    valid_one = 0
    valid_two = 0
    for x in data:
        range_, char, pw = x
        a, b = range_
        if pw.count(char) >= a and pw.count(char) <= b:
            valid_one += 1
        if (
            pw[a - 1] == char
            and pw[b - 1] != char
            or pw[a - 1] != char
            and pw[b - 1] == char
        ):
            valid_two += 1

    return valid_one, valid_two


data = process_data("day02_input.txt")
valid_one, valid_two = count_valid(data)
print(f"Part 1: {valid_one}")
print(f"Part 2: {valid_two}")
