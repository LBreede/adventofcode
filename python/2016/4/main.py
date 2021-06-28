# --- Day 4: Security Through Obscurity ---

with open("inputdata.txt", "r") as f:
	line_list = f.read().split("\n")

# line_list = ["aaaaa-bbb-z-y-x-123[abxyz]"]

sectorid_sum = 0
for line in line_list:
	parts = line.split("-")
	name = "-".join(parts[:-1])
	sectorid = int(parts[-1].split("[")[0])
	checksum = parts[-1].split("[")[-1][:-1]
	print(name + " >>> [" + checksum + "]")
	current_max_count = 9999
	for i in range(5):
		count = name.count(checksum[i])
		if count <= current_max_count:
			current_max_count = count
			if i == 4:
				print("real")
				sectorid_sum += sectorid
		else:
			print("decoy")
			break
	

print(sectorid_sum)