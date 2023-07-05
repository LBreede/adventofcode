# --- Day 6: Lanternfish ---

import aoc_helper


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
FILENAME = "example"
EXT = ".txt"

day_list = splitup_days(DAYS)
# day_list = [40]
read_file = "day06_" + FILENAME + EXT

for i, day in enumerate(day_list):

    ages = aoc_helper.load_input(read_file, separator=",")
    ages = [int(x) for x in ages]

    text = ",".join([str(x) for x in lanternfish(ages, day)])

    write_file = "_".join([FILENAME, str(DAYS) + "days", "batch" + str(i)])
    write_file += EXT

    print(write_file)

    with open(write_file, "w") as f:
        f.write(text)

    read_file = write_file

print(len(ages))
