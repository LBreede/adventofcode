# --- Day 5: Binary Boarding ---

with open("input.txt", "r") as f:
	line_list = [line.replace("\n", " ") for line in f.read().split("\n")]

# line_list = ["FBFBBFFRLR"]
# line_list = ["BFFFBBFRRR" , "FFFBBBFRRR", "BBFFBBFRLL"]

def findseat(code, amount):
	current_min = 0
	current_max = amount - 1
	for i in range(len(code)):
		amount *= 0.5
		if code[i] == "F" or code[i] == "L":
			current_max -= amount
		elif code[i] == "B" or code[i] == "R":
			current_min += amount
	return int(current_min)

all_seat_ids = []
for line in line_list:
	row_code = line[:-3]
	col_code = line[-3:]
	row = findseat(row_code, 128)
	col = findseat(col_code, 8)
	seat_id = row * 8 + col
	all_seat_ids.append(seat_id)

all_seat_ids.sort()
highest_seat_id = all_seat_ids[-1]

print("The seat with the highest seat ID is: {}".format(highest_seat_id))

for i in range(highest_seat_id):
	if (i - 1 in all_seat_ids and
		i not in all_seat_ids and
		i + 1 in all_seat_ids):
		my_seat_id = i
		break

print("My seat ID is: {}".format(my_seat_id))