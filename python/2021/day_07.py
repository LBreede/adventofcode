# --- Day 7: The Treachery of Whales ---

import aoc_helper


def align_submarines(data, constant_fuel=True):

    minpos = min(data)
    maxpos = max(data)

    minfuel = float("inf")

    for i in range(minpos, maxpos + 1):
        fuel = 0
        for pos in data:
            dist = abs(pos - i)

            if constant_fuel:
                fuel += dist

            else:
                for j in range(1, dist + 1):
                    fuel += j

        if fuel < minfuel:
            minfuel = fuel

    return minfuel


data = aoc_helper.load_input("day07_input.txt", separator=",")
data = [int(x) for x in data]

result1 = align_submarines(data)
result2 = align_submarines(data, constant_fuel=False)

print(f"Part 1: {result1}")
print(f"Part 2: {result2}")
