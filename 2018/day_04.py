# --- Day 4: Repose Record ---

from aoc_helper import load_input

DAY = 4


def process_data(subdir):
    linelist = load_input(subdir, DAY)
    linelist.sort()

    dic = {}
    key = ""

    for line in linelist:
        a = line.split()
        year, month, day = a[0][1:].split("-")
        hour, minute = list(map(int, a[1][:-1].split(":")))

        if hour == 23:
            day = str(int(day) + 1).zfill(2)
            minute = minute - 60

        if a[2:][0] == "Guard":
            key = f"{month}-{day}#{a[2:][1][1:]}"
            # hour = 0
            # minute = 0
            lst = []

        lst.append(minute)
        dic[key] = lst

    return dic


data = process_data("example")

print(data)

for k, v in data.items():
    v.pop(0)
    minutes_asleep = 0
    for i, minute in enumerate(v):
        if i % 2 == 0:
            minutes_asleep -= minute
        else:
            minutes_asleep += minute
    data[k] = [v, minutes_asleep]

ids = set()
for k, v in data.items():
    id_ = int(k.split("#")[1])
    ids.add(id_)

dic = {}
for i in ids:
    dic[i] = []

for k, v in data.items():
    id_ = int(k.split("#")[1])
    dic[id_].append(v[1])

for k, v in dic.items():
    dic[k] = sum(v)

{k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}

first_key = list(dic)[0]
first_val = list(dic.values())[0]
print(first_key * first_val)
