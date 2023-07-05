# --- Day 6: Memory Reallocation ---

with open("day06_input.txt") as fp:
    data = [int(x) for x in fp.read().split()]

toString = lambda lst: "".join([str(x) for x in lst])
configs = []
while toString(data) not in configs:
    configs.append(toString(data))
    maximum = max(data)
    length = len(data)
    idx = data.index(maximum)
    data[idx] = 0
    for i in range(maximum):
        data[(idx + i + 1) % length] += 1
configs.append(toString(data))

nconfigs = len(configs) - 1  # subtract one to account for the duplicate at the end
print("Part 1:", nconfigs)

last = configs[-1]  # finds the "last item" in the list
idx_a = configs.index(last)  # finds the index of the first mention of the "last item"
idx_b = nconfigs  # the index of the second mention of the "last item"
print("Part 2:", idx_b - idx_a)  # finds the distance between mention one and two
