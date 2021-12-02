# --- Day 2: Dive! ---

with open("input.txt", "r") as fp:
	linelist = fp.read().split("\n")

better_linelist = []
for L in linelist:
	direction, amount = L.split(" ")
	amount = int(amount)
	better_linelist.append([direction, amount])


def drive(lst, use_aim=0):

	horizontal = 0
	depth = 0
	aim = 0

	for L in better_linelist:
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

part1 = drive(better_linelist)
part2 = drive(better_linelist, 1)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
