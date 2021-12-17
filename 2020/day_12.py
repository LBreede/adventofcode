# --- Day 12: Rain Risk ---

from aoc_helper import load_input

def part_1(lst):

	north = 0
	east = 0
	curr_dir = 1

	for x in lst:
		action, value = x

		if   action == "N": north += value
		elif action == "E": east  += value
		elif action == "S": north -= value
		elif action == "W": east  -= value

		elif action == "F":
			if   curr_dir == 0: north += value
			elif curr_dir == 1: east  += value
			elif curr_dir == 2: north -= value
			elif curr_dir == 3: east  -= value

		elif action == "R": curr_dir = (curr_dir + int(value / 90)) % 4
		elif action == "L": curr_dir = (curr_dir - int(value / 90)) % 4

	return abs(east) + abs(north)

def part_2(lst, print_log=False):

	north = 0
	east = 0
	north_waypoint = 1
	east_waypoint = 10

	for x in lst:
		if print_log:
			print("="*35)
			print(f"Current Position: [ {north} | {east} ]")
			print(f"Current Waypoint: [ {north_waypoint} | {east_waypoint} ]\n")
		action, value = x

		if   action == "N":	north_waypoint += value
		elif action == "E": east_waypoint  += value
		elif action == "S": north_waypoint -= value
		elif action == "W": east_waypoint  -= value

		elif action == "F":
			north += north_waypoint * value
			east  += east_waypoint  * value

		elif action == "R" or action == "L":
			rot = int(value / 90)
			if action == "L":
				rot = -rot
			rot = rot % 4
			if rot == 1:
				north_waypoint, east_waypoint = -east_waypoint, north_waypoint
			elif rot == 2:
				north_waypoint, east_waypoint = -north_waypoint, -east_waypoint
			elif rot == 3:
				north_waypoint, east_waypoint = east_waypoint, -north_waypoint

		if print_log:
			print(f"Action: {action}, Value: {value}\n")
			print(f"Current Position: [ {north} | {east} ]")
			print(f"Current Waypoint: [ {north_waypoint} | {east_waypoint} ]")
			print("="*35 + "\n")

	return abs(east) + abs(north)

subdir = "input"
day = 12
linelist = load_input(f"{subdir}/day_{day}.txt")
linelist = [[x[0], int(x[1:])] for x in linelist]

print(f"Part 1: {part_1(linelist)}")
print(f"Part 2: {part_2(linelist)}")