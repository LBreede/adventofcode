# --- Day 6: Lanternfish ---

def lanternfish(ages, days):
	for i in range(days):
		for j in range(len(ages)):
			if ages[j] == 0:
				ages[j] = 7
				ages.append(8)
			ages[j] -= 1
	return ages

def splitup_days(days):	
	day_list = []
	d = days
	while d > 1:
		d = d // 2
		day_list.append(d)

	rest = days - sum(day_list)
	[day_list.append(1) for i in range(rest)]

	return day_list

DAYS = 80
FILE = "example.txt"





day_list = splitup_days(80)
day_list = [40]
read_file = FILE

for day in day_list:

	with open(read_file, "r") as f:
		ages = [int(x) for x in f.read().split(",")]

	txt = ",".join( [str(x) for x in lanternfish(ages, day)] )
	
	with open(write_file, "w") as f:
		



# ages1 = lanternfish(ages, b1)

# with open("batch1.json", "w") as f:
# 	json.dump(ages1, f)

# with open("batch1.json", "r") as f:
# 	ages1 = json.load(f)

# ages2 = lanternfish(ages1, b2)
# DAYS = 80
# amount = len(lanternfish(ages, DAYS))


# print(f"\nAfter {DAYS} days, there were {amount} lanternfish in the sea.\
#  We're doomed!\n")

