# --- Day 12: Hill Climbing Algorithm ---
from string import ascii_lowercase as lowercase


def check_elevation(old_val, new_val):
    return old_val - 1 <= new_val <= old_val + 1


def move(pos):
    global heightfield
    x, y = pos

    old_val = heightfield[y][x]

    # up
    if y > 0:
        new_y = y - 1
        new_val = heightfield[new_y][x]
        new_pos = (x, new_y)
        if check_elevation(old_val, new_val) and new_pos not in visited:
            visited.append(new_pos)
            return new_pos

    # down
    if y < len(heightfield) - 1:
        new_y = y + 1
        new_val = heightfield[new_y][x]
        new_pos = (x, new_y)
        if check_elevation(old_val, new_val) and new_pos not in visited:
            visited.append(new_pos)
            return new_pos

    # left
    if x > 0:
        new_x = x - 1
        new_val = heightfield[y][new_x]
        new_pos = (new_x, y)
        if check_elevation(old_val, new_val) and new_pos not in visited:
            visited.append(new_pos)
            return new_pos

    if x < len(heightfield[0]) - 1:
        new_x = x + 1
        new_val = heightfield[y][new_x]
        new_pos = (new_x, y)
        if check_elevation(old_val, new_val) and new_pos not in visited:
            visited.append(new_pos)
            return new_pos


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
pos = (0, 1)  # start
visited = [(0, 0), pos]

for i in range()
while True:
    pos = move(pos)
    if pos is None or pos == end:
        break
    print(pos)
    print(visited)
    print()
print(len(visited))
