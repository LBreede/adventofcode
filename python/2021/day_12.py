# --- Day 12: Passage Pathing ---

from aoc_helper import load_input
import re


def find_next(path, lst):
    paths = []
    last = path[-1]
    firsts = [x[0] for x in lst]
    for i in range(firsts.count(last)):
        for x in lst:
            if x[0] == path[-1]:
                path.append(x[1])
        paths.append(path)
    return paths


linelist = load_input("day12_example1.txt")
linelist = [x.split("-") for x in linelist]

a = [x[0] for x in linelist]
b = [x[1] for x in linelist]

path = ["start", "A"]
path = find_next(path, linelist)
path = find_next(path, linelist)
