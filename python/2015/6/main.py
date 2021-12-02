# --- Day 6: Probably a Fire Hazard ---

with open("input.txt", "r") as fp:
	instruction_list = fp.read().split("\n")

def process_list(lst):
	new_list = []
	for i in lst:
		parts = i.split()
		if len(parts) == 4:
			op, start, ignore, end = parts
		elif len(parts) == 5:
			op1, op2, start, ignore, end = parts
			op = op1 + " " + op2
		else:
			raise ValueError(f"Bad amount of items in list: {parts}")

		s = [int(x) for x in start.split(",")]
		e = [int(x) for x in end.split(",")]
		new_list.append([op, s, e])
	return new_list

instruction_list = ["turn on 0,0 through 999,999"]

l = process_list(instruction_list)


grid = []

for i in range(10):
	row = []
	for j in range(10):
		row.append(0)
	grid.append(row)


# toggle
for i in range(4,5+1):
	for j in range(4,5+1):
		grid[i][j] = 1 - grid[i][j]


for i in range(3,4+1):
	for j in range(2,4+1):
		grid[i][j] = 1 - grid[i][j]

for row in grid:
	print(row)


