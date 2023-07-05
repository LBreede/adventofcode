# --- Day 6: Probably a Fire Hazard ---
state = [0] * 1_000_000
brightness = state.copy()
with open("input.txt") as fp:
    for line in fp.read().splitlines():
        b, _, a, *c = line.split(" ")[::-1]
        ax, ay = [int(x) for x in a.split(",")]
        bx, by = [int(x) for x in b.split(",")]
        c = " ".join(c[::-1])
        for i in range(ax, bx + 1):
            for j in range(ay, by + 1):
                idx = j * 1000 + i
                if c == "turn on":
                    state[idx] = 1
                    brightness[idx] += 1
                elif c == "turn off":
                    state[idx] = 0
                    brightness[idx] = max(brightness[idx] - 1, 0)
                elif c == "toggle":
                    state[idx] = 1 - state[idx]
                    brightness[idx] += 2
print("Part 1:", sum(state), "\nPart 2:", sum(brightness))
