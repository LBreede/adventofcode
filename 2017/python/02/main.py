# --- Day 2: Corruption Checksum ---

def createCellList(input):
	f = open(input, "r").read()
	cell_list = []
	line_list = f.split("\n")
	for L in line_list:
		cells = L.split("\t")
		for c in cells:
			cell_list.append(c)
	return cell_list

def createSortedCellList(cell_list):
	sorted_cell_list = []
	for cell in cell_list:
		sorted_cell = []
		for digit in cell:
			sorted_cell.append(int(digit))

		sorted_cell.sort()
		sorted_cell_list.append(sorted_cell)
	return sorted_cell_list

def calcChecksum(sorted_cell_list):
	differences = []
	for cell in sorted_cell_list:
		differences.append(cell[-1] - cell[0])
	return sum(differences)

cell_list = createCellList("input.txt")

cell_list = ["666"]

sorted_list = createSortedCellList(cell_list)
checksum = calcChecksum(sorted_list)
print(checksum)