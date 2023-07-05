# --- Day 1: Calorie Counting ---
with open("input.txt", encoding="utf8") as fp:
    c = sorted([sum([int(y) for y in x.split("\n")]) for x in fp.read().split("\n\n")])
print("Part 1:", c[-1], "\nPart 2:", sum(c[-3:]))
