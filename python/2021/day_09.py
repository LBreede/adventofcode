# --- Day 9: Smoke Basin ---

import aoc_helper


def gen_heightmap(filename):
    heightmap = aoc_helper.load_input(filename)
    return [list(map(int, x)) for x in heightmap]


def find_adjacent(pos, heightmap):
    xmax = len(heightmap[0]) - 1
    ymax = len(heightmap) - 1

    adj = []

    if pos[1] != 0:
        adj.append([pos[0], pos[1] - 1])
    if pos[1] != ymax:
        adj.append([pos[0], pos[1] + 1])
    if pos[0] != 0:
        adj.append([pos[0] - 1, pos[1]])
    if pos[0] != xmax:
        adj.append([pos[0] + 1, pos[1]])

    return adj


def read_value(pos, heightmap):
    return heightmap[pos[1]][pos[0]]


def batch_read_values(pos, heightmap):
    lst = []
    for p in pos:
        lst.append(read_value(p, heightmap))
    return lst


def find_valleys(heightmap):
    valleys = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            val = read_value([x, y], heightmap)

            adjacent = find_adjacent([x, y], heightmap)
            for adj in adjacent:
                adjval = read_value(adj, heightmap)
                if adjval <= val:
                    break
            else:
                valleys.append([x, y])
    return valleys


def risklevels(lst):
    return [x + 1 for x in lst]


def find_basins(valleys, heightmap):
    pass


heightmap = gen_heightmap("day09_example.txt")
valleys = find_valleys(heightmap)
valley_vals = batch_read_values(valleys, heightmap)
result1 = sum(risklevels(valley_vals))
print(f"Part 1: {result1}")
# find_basins(valleys, heightmap)
