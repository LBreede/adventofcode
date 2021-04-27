# --- Day 2: I Was Told There Would Be No Math ---

def createLineList(input):
	lineList = [line.rstrip('\r\n') for line in open(input)]
	return lineList

def createDimList(lines):
	dimList = []
	for L in lines:
		dim = L.split("x")
		for i in range(0, len(dim)):
			dim[i] = int(dim[i])
		dimList.append(dim)
	return dimList

def createAreaList(dimensions):
	areaList = []
	for d in dimensions:
		lw = d[0] * d[1]
		wh = d[1] * d[2]
		hl = d[2] * d[0]
		slack = min(lw, wh, hl)
		area = 2 * lw + 2 * wh + 2 * hl + slack
		areaList.append(area)
	return areaList

def createRibbonList(dimensions):
	lenList = []
	for d in dimensions:
		l = d[0]
		w = d[1]
		h = d[2]
		ribbonLen = l * 2 + w * 2 + h * 2 - max(l, w, h) * 2
		bowLen = l * w * h
		totalLen = ribbonLen + bowLen
		lenList.append(totalLen)
	return lenList


line_list = createLineList("input.txt")
dim_list = createDimList(line_list)
area_list = createAreaList(dim_list)
ribbon_list = createRibbonList(dim_list)

print("The total amount of wrapping paper required is " + str(sum(area_list)) + " square feet.")
print("The total amount of ribbons required is " + str(sum(ribbon_list)) + " feet.")
