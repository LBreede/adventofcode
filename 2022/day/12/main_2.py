# --- Day 12: Hill Climbing Algorithm ---
from string import ascii_lowercase as lowercase
import random
from itertools import combinations, permutations


def can_move(curr_val, next_val):
    return curr_val - 1 <= next_val <= curr_val + 1


def can_move_up(pos, heightfield, curr_val):
    x, y = pos
    if y == 0:
        return False
    y -= 1
    next_val = heightfield[y][x]
    return can_move(curr_val, next_val)


def can_move_down(pos, heightfield, curr_val):
    x, y = pos
    if y == len(heightfield) - 1:
        return False
    y += 1
    next_val = heightfield[y][x]
    return can_move(curr_val, next_val)


def can_move_left(pos, heightfield, curr_val):
    x, y = pos
    if x == 0:
        return False
    x -= 1
    next_val = heightfield[y][x]
    return can_move(curr_val, next_val)


def can_move_right(pos, heightfield, curr_val):
    x, y = pos
    if x == len(heightfield[0]) - 1:
        return False
    x += 1
    next_val = heightfield[y][x]
    return can_move(curr_val, next_val)


def move_up(pos):
    x, y = pos
    return (x, y - 1)


def move_down(pos):
    x, y = pos
    return (x, y + 1)


def move_left(pos):
    x, y = pos
    return (x - 1, y)


def move_right(pos):
    x, y = pos
    return (x + 1, y)


def move(pos, heightfield, direction: str):
    x, y = pos
    curr_val = heightfield[y][x]

    up = can_move_up(pos, heightfield, curr_val)
    down = can_move_down(pos, heightfield, curr_val)
    left = can_move_left(pos, heightfield, curr_val)
    right = can_move_right(pos, heightfield, curr_val)

    if direction == "U" and up:
        return move_up(pos)
    if direction == "D" and down:
        return move_down(pos)
    if direction == "L" and left:
        return move_left(pos)
    if direction == "R" and right:
        return move_right(pos)
    return None


with open("example.txt") as fp:
    heightfield = [[y for y in x.rstrip()] for x in fp]
for y, row in enumerate(heightfield):
    for x, col in enumerate(row):
        if col == "S":
            start = (x, y)
            heightfield[y][x] = "a"
        if col == "E":
            end = (x, y)
            heightfield[y][x] = "z"
heightfield = tuple(tuple(lowercase.index(y) for y in x) for x in heightfield)
# print(start, end)
pos = start
# print(pos)
# for i in range(1000):
#     pos = move_random(pos, heightfield)
#     print(pos)
#     if pos == end:
#         print("SUCCESS")
#         brea
lst = "UDLR"

print(list(permutations(lst, r=4)))
# for c in combinations(lst, r=5):
#     pos = start
#     for d in c:
#         pos = move(pos, heightfield, d)
#         if pos is None:
#             print("Can't move this way!")
#             break
#         elif pos == end:
#             print("SUCCESS")
#             break
#         print(pos)
