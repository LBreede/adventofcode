# --- Day 3: No Matter How You Slice It ---

def claimListFromInput(input):
	f = open(input, "r")
	raw_claim_list = f.read().split("\n")
	claim_list = []
	for raw_claim in raw_claim_list:
		parts = raw_claim.split(" ")
		parts.pop(1)
		
		claim_id = int(parts[0][1:])

		pos = parts[1].split(",")
		fromLeft = int(pos[0])
		fromTop = int(pos[1].split(":")[0])

		dim = parts[2].split("x")
		width = int(dim[0])
		height = int(dim[1])

		claim = [claim_id, fromLeft, fromTop, width, height]
		claim_list.append(claim)

	return claim_list

def createInitGrid(x, y):
	row = []
	grid = []
	for i in range(y):
		row = []
		for j in range(x):
			row.append(".")
		grid.append(row)
	return grid

def drawSingleSquare(grid, fromLeft, fromTop, width, height):
	for i in range(height):
		for j in range(width):
			grid[fromTop + i][fromLeft + j] = "#"
	return grid

def drawMultipleSquares(grid, claim_list):
	k = 1
	for claim in claim_list:
		height = claim[4]
		width = claim[3]
		fromTop = claim[2]
		fromLeft = claim[1]
		claim_id = claim[0]
		for i in range(height):
			for j in range(width):
				pos = grid[fromTop + i][fromLeft + j]
				if pos == ".":
					grid[fromTop + i][fromLeft + j] = str(claim_id)
				else:
					grid[fromTop + i][fromLeft + j] = "X"
		k += 1
	return grid

def countOverlaps(grid):
	found = 0
	for i in grid:
		for j in i:
			if j == "X":
				found += 1
	return found

def findFullClaim(grid, claimList):
	full_list = []
	for i in grid:
		for j in i:
			if j != "." and j != "X":
				full_list.append(j)

	full_claim_id = -1
	for c in claimList:
		claim_id = c[0]
		area = c[3] * c[4]
		count = full_list.count(str(claim_id))
		if count == area:
			full_claim_id = claim_id
			break

	return full_claim_id

if __name__ == "__main__":
	claim_list = claimListFromInput("input.txt")
	empty_grid = createInitGrid(1000,1000)

	# grid = drawSingleSquare(grid, 3, 1, 4, 4)
	# claim_list = [[1,3,4,4], [3,1,4,4], [5,5,2,2]]
	
	grid = drawMultipleSquares(empty_grid, claim_list)
	overlaps = countOverlaps(grid)
	full_claim_id = findFullClaim(grid, claim_list)

	print(overlaps)
	print(full_claim_id)