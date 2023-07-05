# --- Day 5: A Maze of Twisty Trampolines, All Alike ---

from aoc_helper import load_input

linelist = load_input("input", 5)
linelist = list(map(int, linelist))


def find_exit(list_, strange_offset=False):
    lst = list_.copy()
    idx = 0
    i = 0
    while True:
        try:
            new_idx = idx + lst[idx]
        except:
            break
        if strange_offset:
            if lst[idx] >= 3:
                lst[idx] -= 1
            else:
                lst[idx] += 1
        else:
            lst[idx] += 1
        idx = new_idx
        i += 1
    return i


result1 = find_exit(linelist)
result2 = find_exit(linelist, strange_offset=True)

print(f"Part 1: {result1}")
print(f"Part 2: {result2}")
