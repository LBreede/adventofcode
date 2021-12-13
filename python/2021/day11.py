# --- Day 11: Dumbo Octopus ---

from aoc_helper import load_input

def find_neighbours(pos, lst):
	x, y = pos
	xmax = len(lst[0])
	ymax = len(lst)
	neighbours = [
		[x, y+1],   [x+1, y+1], [x-1, y],   [x+1, y],
		[x-1, y-1], [x, y-1],   [x+1, y-1], [x-1, y+1]
	]

	for n in list(neighbours):
		if n[0] == -1 or n[0] == xmax:
			neighbours.remove(n)
		elif n[1] == -1 or n[1] == ymax:
			neighbours.remove(n)

	return neighbours

linelist = load_input("day11_example2.txt")
linelist = [list(map(int, list(x))) for x in linelist]

for i in range(2):
	for y, row in enumerate(linelist):
		print(row)
		for x, val in enumerate(row):
			val += 1
			if val > 9:
				val = 0
			linelist[y][x] = val
	print()

n = find_neighbours([0, 2], linelist)
print(n)
