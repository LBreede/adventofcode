# --- Day 4: Camp Cleanup ---
part_one = part_two = 0
with open("input.txt") as fp:
    for line in fp.read().splitlines():
        a, b = [[int(y) for y in x.split("-")] for x in line.split(",")]
        a, b = {x for x in range(a[0], a[1] + 1)}, {x for x in range(b[0], b[1] + 1)}
        aminusb, bminusa = a.difference(b), b.difference(a)
        part_one += 1 if not aminusb or not bminusa else 0
        part_two += 1 if a != aminusb or b != bminusa else 0

print("Part 1:", part_one, "\nPart 2:", part_two)
