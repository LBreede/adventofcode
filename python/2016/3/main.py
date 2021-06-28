# --- Day 3: Squares With Three Sides ---

with open("inputdata.txt", "r") as f:
	text = f.read().replace("\n", " ")

dims = text.split()
dims = [int(dim) for dim in dims]

i = 0
hori_dims = []
while i < len(dims):
	hori_dims.append([dims[i], dims[i+1], dims[i+2]])
	i += 3

j = 0
vert_dims = []
while j < len(dims):
	vert_dims.append([dims[j], dims[j+3], dims[j+6]])
	vert_dims.append([dims[j+1], dims[j+4], dims[j+7]])
	vert_dims.append([dims[j+2], dims[j+5], dims[j+8]])
	j += 9

def countvalidtriangles(dimensions):
	count = 0
	for line in dimensions:
		if (line[0] + line[1] > line[2] and
			line[1] + line[2] > line[0] and
			line[2] + line[0] > line[1]):
			count += 1
	return count


print(countvalidtriangles(hori_dims))
print(countvalidtriangles(vert_dims))

# print(hori_dims)
# print(vert_dims)