# --- Day 2: I Was Told There Would Be No Math ---


paper = ribbons = 0
with open("input.txt") as fp:
    for line in fp:
        l, w, h = [int(dim) for dim in line.rstrip().split("x")]
        paper += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
        ribbons += sum(sorted((l, w, h))[:2]) * 2 + l * h * w
print("Part 1:", paper, "\nPart 2:", ribbons)
