print("Part 1:", sum([int(x) // 3 - 2 for x in open("day01_input.txt").readlines()]))
y = 0
for x in open("day01_input.txt").readlines():
    x = int(x) // 3 - 2
    while x > 0:
        y += x
        x = x // 3 - 2
print("Part 2:", y)
