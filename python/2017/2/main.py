# --- Day 2: Corruption Checksum ---

with open("inputdata.txt", "r") as f:
	line_list = f.read().split("\n")

checksum_part_one = 0
checksum_part_two = 0
for line in line_list:
	vals = [int(val) for val in line.split()]
	vals.sort()
	checksum_part_one += vals[-1] - vals[0]

	for i in vals:
		for j in vals:
			if i != j and i % j == 0:
				checksum_part_two += int(i / j)
				break

print(checksum_part_one)
print(checksum_part_two)

