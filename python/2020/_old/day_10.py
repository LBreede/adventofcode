# --- Day 10: Adapter Array ---

from aoc_helper import load_input

# from tqdm import tqdm

numbers = list(map(int, load_input("examples/day_10.txt")))
highest = max(numbers)
# bar = tqdm(desc="2020 Day 10", total=highest)
j = 0
ojd = 0  #   One Jolt Difference
tjd = 0  # Three Jolt Difference

while j < highest:
    match = sorted([x for x in numbers if x >= j + 1 and x <= j + 3])[0]
    diff = match - j
    if diff == 1:
        ojd += 1
    if diff == 3:
        tjd += 1
    # bar.update(diff)
    j += diff

tjd += 1

print(f"Part 1: {ojd * tjd} = {ojd} * {tjd}")
