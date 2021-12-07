# --- Day 6: Lanternfish ---

import json

def lanternfish(ages, days):
	for i in range(days):
		for j in range(len(ages)):
			if ages[j] == 0:
				ages[j] = 7
				ages.append(8)
			ages[j] -= 1
		print(f"At day {i+1}, there were {len(ages)} fish...")
	return ages

with open("example.txt", "r") as f:
	ages = [int(x) for x in f.read().split(",")]

b1 = 256 // 2
b2 = b1 // 2
b3 = b2 // 2
b4 = b3 // 2
b5 = b4 // 2
b6 = b5 // 2
b7 = b6 // 2
b8 = b7 // 2
b9 = b8

# ages1 = lanternfish(ages, b1)

# with open("batch1.json", "w") as f:
# 	json.dump(ages1, f)

# with open("batch1.json", "r") as f:
# 	ages1 = json.load(f)

# ages2 = lanternfish(ages1, b2)
DAYS = 80
amount = len(lanternfish(ages, DAYS))


print(f"\nAfter {DAYS} days, there were {amount} lanternfish in the sea.\
 We're doomed!\n")

