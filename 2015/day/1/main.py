# --- Day 1: Not Quite Lisp ---

f = open("input.txt", "r").read()

floor = 0
i = 1
basement_trigger = -1

for c in f:
	if c == "(":
		floor += 1
	elif c == ")":
		floor -= 1

	if floor < 0 and basement_trigger == -1:
		basement_trigger = i
	else:
		i += 1

print("The instructions take Santa to floor " + str(floor) + ".")
print("Position " + str(basement_trigger) + " causes Santa to first enter the basement.")