# --- Day 3: Toboggan Trajectory ---

line_list = [line.rstrip("\n") for line in open("input.txt")]

def slopecheck(hori, vert):
	pos = 0
	found = 0
	i = 0
	for line in line_list:
		if i % vert == 0:
			if line[pos % len(line)] == "#":
				found += 1
			pos += hori
		i += 1
	return found

a = slopecheck(1, 1)
b = slopecheck(3, 1)
c = slopecheck(5, 1)
d = slopecheck(7, 1)
e = slopecheck(1, 2)

"""
print(a)
print(b)
print(c)
print(d)
print(e)
print(a*b*c*d*e)
"""