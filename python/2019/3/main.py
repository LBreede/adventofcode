# --- Day 3: Crossed Wires ---

with open("input.txt", "r") as fp:
	wirepath1, wirepath2 = fp.read().split("\n")

# wirepath1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
# wirepath2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

def create_coord_list(wirepath):

	wirepath_list = wirepath.split(",")

	coord_list = []

	x, y = 0, 0
	for wp in wirepath_list:
		d = wp[0]
		n = int(wp[1:])
		
		for i in range(n):
			if d == "U":
				y += 1
			elif d == "R":
				x += 1
			elif d == "D":
				y -= 1
			elif d == "L":
				x -= 1
			else:
				raise ValueError("Bad direction value!")

			coord_list.append( f"{x},{y}" )

	return coord_list

coord_list1 = create_coord_list(wirepath1)
coord_list2 = create_coord_list(wirepath2)

coord_set1 = set( coord_list1 )
coord_set2 = set( coord_list2 )
coord_intersection = coord_set1.intersection(coord_set2)

closest_dist = float("inf")

for i in coord_intersection:
	x, y = [int(x) for x in i.split(",")]
	dist = abs(x) + abs(y)
	if dist < closest_dist:
		closest_dist = dist

print(f"Closest intersection: {closest_dist}")

shortest_path = float("inf")

for i in coord_intersection:
	path1 = coord_list1.index(i) + 1
	path2 = coord_list2.index(i) + 1

	path = path1 + path2

	if path < shortest_path:
		shortest_path = path

print(f"Shortest path: {shortest_path}")
