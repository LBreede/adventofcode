# --- Day 10: Syntax Scoring ---

from aoc_helper import load_input
from math import floor

OPEN = "([{<"
CLOSE = ")]}>"
MATCH = {")": "(", "]": "[", "}": "{", ">": "<"}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}


def filter_lines(lst):
    legal = []
    illegal = []
    for line in lst:
        opened = []
        for char in line:
            if char in OPEN:
                opened.append(char)
            if char in CLOSE:
                if opened[-1] == MATCH[char]:
                    opened.pop()
                else:
                    illegal.append(char)
                    break
        else:
            legal.append(opened)

    return legal, illegal


def calc_syntax_error_score(lst):
    score = 0
    for char in CLOSE:
        score += lst.count(char) * POINTS[char]
    return score


def calc_score(lst):
    score = 0
    for char in lst:
        score *= 5
        score += POINTS[char]
    return score


def calc_middle_score(lst):
    scores = []
    for line in lst:
        line = line[::-1]
        score = calc_score(line)
        scores.append(score)
    scores = sorted(scores)
    return scores[floor(len(scores) / 2)]


linelist = load_input("day10_example.txt")
legal, illegal = filter_lines(linelist)
syntax_error_score = calc_syntax_error_score(illegal)
middle_score = calc_middle_score(legal)

print(f"Part 1: {syntax_error_score}")
print(f"Part 2: {middle_score}")
