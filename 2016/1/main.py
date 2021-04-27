# --- Day 1: No Time for a Taxicab ---

f = open("input.txt", "r").read()

directions = f.split(", ")

x = 0
y = 0

allpos = []
pos_two = []
trigger = 0

compass = 0 # N = 0, E = 1, S = 2, W = 3

for d in directions:
	turn = d[0]
	blocks = int(d[1:])
	
	if turn == "L":
		compass -= 1
	elif turn == "R":
		compass += 1
	else:
		print "ERROR! Bad turn direction!"

	compass = compass % 4
	
	for b in range (blocks):
		if compass == 0:
			y += 1
		elif compass == 1:
			x += 1
		elif compass == 2:
			y -= 1
		elif compass == 3:
			x -= 1
		else:
			print "ERROR! Bad compass value!"
		pos_one = [x, y]

		if pos_one in allpos and trigger == 0:
			pos_two = pos_one
			trigger = 1
		allpos.append(pos_one)

shortestpath_one = abs(sum(pos_one))
shortestpath_two = abs(sum(pos_two))

print "Part one leads us to a place " + str(shortestpath_one) + " blocks away."
print "Part two leads us to a place " + str(shortestpath_two) + " blocks away."