# --- Day 2: Password Philosophy ---

lineList = [line.rstrip('\n') for line in open("input.txt")]

match_one = 0
match_two = 0

for line in lineList:
	parts = line.split(" ")

	password = parts[2]
	letter = parts[1][0]

	occurances = password.count(letter)

	ranges = parts[0].split("-")
	first = int(ranges[0])
	last = int(ranges[1])

	if occurances >= first and occurances <= last:
		match_one += 1

	if password[first-1] == letter and password[last-1] != letter or password[first-1] != letter and password[last-1] == letter:
		match_two += 1

print("In part one, " + str(match_one) + " passwords match!")
print("In part two, " + str(match_two) + " passwords match!")