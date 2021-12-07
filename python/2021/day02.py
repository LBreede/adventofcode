# --- Day 2: Dive! ---

import aoc_helper

def drive(lst, use_aim=0):

	horizontal = 0
	depth = 0
	aim = 0

	for L in lst:
		d, x = L

		if d == "forward":
			horizontal += x

		if not use_aim:
			if d == "up":
				depth -= x
			elif d == "down":
				depth += x
		else:
			if d == "forward":
				depth += aim * x
			elif d == "up":
				aim -= x
			elif d == "down":
				aim += x

	return horizontal * depth

raw_cmd_list = aoc_helper.load_input("day02_input.txt")

cmd_list = []
for L in raw_cmd_list:
	direction, amount = L.split(" ")
	amount = int(amount)
	cmd_list.append([direction, amount])

part1 = drive(cmd_list)
part2 = drive(cmd_list, 1)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
