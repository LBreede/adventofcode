# --- Day 3: Spiral Memory ---

inputdata = 368078

right, up, left, down = (1,0), (0,1), (-1,0), (0,-1)
turn_left = {right: up, up: left, left: down, down: right}

x, y = 0, 0
dx, dy = down

been_there = [[0,0]]

for i in range(inputdata):
	if i > 0:
		temp_dx, temp_dy = turn_left[dx, dy]
		if [x + temp_dx, y + temp_dy] not in been_there:
			dx, dy = temp_dx, temp_dy
		x += dx
		y += dy
		been_there.append([x,y])
	print("Data from square {} is at location ({}|{}) and {} steps away from the origin.".format(i+1, x, y, abs(x)+abs(y)))


k = 0
for i in range(650):
	print("i: {}".format(i))
	if i % 2 == 1:
		j = i * i
		if j > inputdata:
			break
		k += 1
		print("Bottom right corner of loop {} is {}".format(k, j))
		
	print("----")
	