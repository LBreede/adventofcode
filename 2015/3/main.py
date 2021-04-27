# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

f = open("input.txt", "r").read()

def getSantasUniquePositions(file, numSantas):

	x = 0
	y = 0
	start = [x, y]

	santaPositions = [start]
	roboPositions = [start]

	i = 0

	santaX = roboX = x
	santaY = roboY = y

	for c in file:
		if i % numSantas == 0:
			santaPos = []
			if c == "^":
				santaY += 1
			elif c == "v":
				santaY -= 1
			elif c == ">":
				santaX += 1
			elif c == "<":
				santaX -= 1
			santaPos = [santaX, santaY]
			santaPositions.append(santaPos)
		else:
			roboPos = []
			if c == "^":
				roboY += 1
			elif c == "v":
				roboY -= 1
			elif c == ">":
				roboX += 1
			elif c == "<":
				roboX -= 1
			roboPos = [roboX, roboY]
			roboPositions.append(roboPos)
		i += 1

	accumPositions = santaPositions + roboPositions

	uniquePositions = set(tuple(i) for i in accumPositions)
	return len(uniquePositions)

partOne = getSantasUniquePositions(f, 1)
partTwo = getSantasUniquePositions(f, 2)

print(partOne)
print(partTwo)
