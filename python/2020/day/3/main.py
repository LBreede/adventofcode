# --- Day 3: Toboggan Trajectory ---


def slopecheck(right, down):
    found = i = j = 0
    while True:
        try:
            found += forest[i][j]
        except IndexError:
            return found
        i += down
        j = (j + right) % len(forest[0])


with open("input.txt") as fp:
    forest = tuple(tuple(1 if x == "#" else 0 for x in x.rstrip()) for x in fp)

a = slopecheck(1, 1)
b = slopecheck(3, 1)
c = slopecheck(5, 1)
d = slopecheck(7, 1)
e = slopecheck(1, 2)

print("Part 1:", b, "\nPart 2:", a * b * c * d * e)
