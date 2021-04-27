# --- Day 4: Repose Record ---

def createScheduleFromFile(input):
	return open(input, "r").read().split("\n")

def createTimesList(line_list):
	# del line_list[5:]
	times = []
	for L in line_list:
		time = int(L[6:8] + L[9:11] + L[12:14] + L[15:17])
		times.append(time)
	return times

def createSimplifiedSchedule(schedule):
	pass

def sortSchedule(schedule, times):
	sorted_schedule = [x for _,x in sorted(zip(times, schedule))]
	return sorted_schedule

if __name__ == "__main__":
	schedule = createScheduleFromFile("input.txt")
	times = createTimesList(schedule)
	sorted_schedule = sortSchedule(schedule, times)
	print(sorted_schedule)