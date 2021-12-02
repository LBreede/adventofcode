# --- Day 6: Probably a Fire Hazard ---

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

def init_grid(x, y):
	grid = []
	for i in range(y):
		row = []
		for j in range(x):
			row.append(0)
		grid.append(row)

	return grid

def switch_lights(grid, lst, part):

	for instruction in lst:

		startx = min(instruction[1][0], instruction[2][0])
		starty = max(instruction[1][0], instruction[2][0])

		endx = min(instruction[1][1], instruction[2][1])
		endy = max(instruction[1][1], instruction[2][1])

		for i in range(startx, starty+1):
			for j in range(endx, endy+1):
				if instruction[0] == "turn on":
					if part == 1:
						grid[i][j] = 1
					elif part == 2:
						grid[i][j] += 1
				elif instruction[0] == "turn off":
					if part == 1:
						grid[i][j] = 0
					elif part == 2:
						grid[i][j] = max(grid[i][j] - 1, 0)
				elif instruction[0] == "toggle":
					if part == 1: 
						grid[i][j] = 1 - grid[i][j]
					elif part == 2:
						grid[i][j] += 2
				else:
					raise ValueError(f"Bad opcode in instruction: {i}")

	return grid

with open("input.txt", "r") as fp:
	instruction_list = fp.read().split("\n")

xsize = 1000
ysize = 1000

# instruction_list = ["toggle 0,0 through 999,999"]

lst = process_list(instruction_list)

grid = init_grid(xsize, ysize)
grid1 = switch_lights(grid, lst, 1)

lights_on = 0
for row in grid1:
	lights_on += row.count(1)

print(f"Part 1: {lights_on}")

grid = init_grid(xsize, ysize)
grid2 = switch_lights(grid, lst, 2)

total_intensity = 0
for row in grid2:
	total_intensity += sum(row)

print(f"Part 2: {total_intensity}")


