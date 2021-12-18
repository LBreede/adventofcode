# --- Day 4: Repose Record ---

from aoc_helper import load_input

DAY = 4

def process_data(subdir):
	linelist = load_input(subdir, DAY)
	linelist.sort()
	lst = []
	for line in linelist:
		a = line.split()
		year, month, day = list(map(int, a[0][1:].split("-")))
		hour, minute = list(map(int, a[1][:-1].split(":")))

		if a[2:][0] == "Guard":
			id_ = int(a[2:][1][1:])
			shift = 0

		if a[2:][0] == "falls":
			shift = 1

		if a[2:][0] == "wakes":
			shift = 2

		dic = {
			"year": year, "month": month, "day": day,
			"hour": hour, "minute": minute,
			"id": id_, "shift": shift
		}
		lst.append(dic)
		# print(info)
	return lst

data = process_data("example")
for a in data:
	print(a)