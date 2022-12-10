# --- Day 13: Shuttle Search ---

from aoc_helper import load_input


def find_earliest_time(time, ids):
    while True:
        for i in ids:
            if time % i == 0:
                return time, i

        time += 1


subdir = "input"
day = 13
linelist = load_input(f"{subdir}/day_{day}.txt")
start = int(linelist[0])
bus_ids = [int(x) for x in linelist[1].split(",") if x != "x"]

earliest_time, bus_id = find_earliest_time(start, bus_ids)
minutes = earliest_time - start
result_1 = minutes * bus_id

print(f"Part 1: {result_1}")
