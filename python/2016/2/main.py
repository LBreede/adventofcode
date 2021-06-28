# --- Day 2: Bathroom Security ---

def codelist_from_input(input):
	f = open(input, "r").read()
	dirlist = f.split("\n")
	return dirlist

def find_3x3_positions(dirlist):
	x = 1
	y = 1
	positions = []
	for code in dirlist:
		for c in code:
			if c == "U":
				y = max(min(y + 1, 2), 0)
			elif c == "D":
				y = max(min(y - 1, 2), 0)
			elif c == "L":
				x = max(min(x - 1, 2), 0)
			elif c == "R":
				x = max(min(x + 1, 2), 0)
		positions.append([x, y])
	return positions

def find_5x5_positions(dirlist):
	x = 0
	y = 2
	positions = []
	for code in dirlist:
		for c in code:
			minposx = minposy = 1
			maxposx = maxposy = 3

			if x == 2:
				minposy = 0
				maxposy = 4
				if y == 0 or y == 4:
					minposx = 2
					maxposx = 2
			if y == 2:
				minposx = 0
				maxposx = 4
				if x == 0 or x == 4:
					minposy = 2
					maxposy = 2

			if c == "U":
				y = max(min(y + 1, maxposy), minposy)
			elif c == "D":
				y = max(min(y - 1, maxposy), minposy)
			elif c == "L":
				x = max(min(x - 1, maxposx), minposx)
			elif c == "R":
				x = max(min(x + 1, maxposx), minposx)
		positions.append([x, y])
	return positions

def vec2_to_keypad(positions):
	code = ""
	for p in positions:
		x = p[0]
		y = p[1]
		digit = (x + 1) + ((2 - y) * 3)
		code += str(digit)
	return code

# Second approach more akin to vec2 to diamond
def vec2_to_keypad2(positions):
	code = ""
	pattern = "123\n456\n789"
	for p in positions:
		x = p[0]
		y = p[1]
		digit = pattern.split("\n")[2-y][x]
		code += str(digit)
	return code

def vec2_to_diamond(positions):
	code = ""
	pattern = "  1  \n 234 \n56789\n ABC \n  D  "
	for p in positions:
		x = p[0]
		y = p[1]
		digit = pattern.split("\n")[4-y][x]
		code += str(digit)
	return code


dirlist = codelist_from_input("input.txt")
# dirlist = ["ULL", "RRDDD", "LURDL", "UUUUD"]

positions_3x3 = find_3x3_positions(dirlist)
code_3x3 = vec2_to_keypad2(positions_3x3)

positions_5x5 = find_5x5_positions(dirlist)
code_5x5 = vec2_to_diamond(positions_5x5)

print code_3x3
print code_5x5