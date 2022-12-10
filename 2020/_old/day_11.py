# --- Day 11: Seating System ---

from aoc_helper import load_input
import copy


def find_adjacent(pos, lst):
    x, y = pos
    xmax = len(lst[0])
    ymax = len(lst)
    adj = [
        [x, y + 1],
        [x + 1, y + 1],
        [x - 1, y],
        [x + 1, y],
        [x - 1, y - 1],
        [x, y - 1],
        [x + 1, y - 1],
        [x - 1, y + 1],
    ]

    for n in list(adj):
        if n[0] == -1 or n[0] == xmax:
            adj.remove(n)
        elif n[1] == -1 or n[1] == ymax:
            adj.remove(n)

    return adj


def collect_adjacent_states(pos, lst):
    adj_states = []
    for x, y in find_adjacent([pos[0], pos[1]], lst):
        adj_states.append(lst[y][x])
    return adj_states


def print_layout(layout):
    width = len(layout[0]) + 4
    print("-" * width)
    for row in layout:
        print("| " + "".join(row) + " |")
    print("-" * width)


def occupy_seats(lst):
    new_lst = copy.deepcopy(lst)
    for y, row in enumerate(lst):
        for x, val in enumerate(row):
            if val == "L":
                adj_states = collect_adjacent_states([x, y], lst)
                if "#" not in adj_states:
                    new_lst[y][x] = "#"
    return new_lst


def empty_seats(lst):
    new_lst = copy.deepcopy(lst)
    for y, row in enumerate(lst):
        for x, val in enumerate(row):
            if val == "#":
                adj_states = collect_adjacent_states([x, y], lst)
                if adj_states.count("#") >= 4:
                    new_lst[y][x] = "L"
    return new_lst


def convert_to_string(lst):
    s = ""
    for row in lst:
        s += "".join(row)
    return s


def stablilize_chaos(lst):
    i = 0
    while True:
        if i % 2 == 0:
            new_lst = occupy_seats(lst)

        else:
            new_lst = empty_seats(lst)

        string = convert_to_string(lst)
        new_string = convert_to_string(new_lst)

        if string == new_string:
            return string.count("#")
        else:
            lst = copy.deepcopy(new_lst)
        i += 1


dir_ = "input"
layout = load_input(f"{dir_}/day_11.txt")
layout = [list(x) for x in layout]
print(stablilize_chaos(layout))
