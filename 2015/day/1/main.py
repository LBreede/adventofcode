# --- Day 1: Not Quite Lisp ---
floor = 0
j = None
with open("input.txt") as fp:
    for i, x in enumerate(fp.read()):
        floor += 1 if x == "(" else -1
        if floor < 0 and j is None:
            j = i + 1
print("Part 1:", floor, "\nPart 2:", j)
