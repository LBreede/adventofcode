# --- Day 3: Squares With Three Sides ---

f = open("input.txt", "r").read()

triangle_list = f.split("\n")

possible = []

for t in triangle_list:
	tri = t.split(" ")
	while len(tri)>3:
		tri.remove("")
	a, b, c = int(tri[0]), int(tri[1]), int(tri[2])
	if a + b > c and b + c > a and c + a > b:
		possible.append(a)

print len(possible)