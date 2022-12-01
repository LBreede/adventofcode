# --- Day 3: Perfectly Spherical Houses in a Vacuum ---


def move(x, y, direction):
    if direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    elif direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    return x, y


with open("input.txt") as fp:
    for i in range(2):  # reset file pointer, coordinates and position set
        fp.seek(0)
        x1 = y1 = x2 = y2 = 0
        pos = {(x1, y1), (x2, y2)}
        for j, direction in enumerate(fp.read()):
            if j % (i + 1) == 0:
                x1, y1 = move(x1, y1, direction)
                pos.add((x1, y1))
            else:
                x2, y2 = move(x2, y2, direction)
                pos.add((x2, y2))
        print(f"Part {i+1}: {len(pos)}")
