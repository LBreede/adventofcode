# --- Day 4: Passport Processing ---

import re

with open("input/day_04.txt", "r") as f:
    line_list = [line.replace("\n", " ") for line in f.read().split("\n\n")]

passport_list = []
for line in line_list:
    fields = line.split(" ")
    passport = {}
    for f in fields:
        k, v = f.split(":")
        passport[k] = v
    passport_list.append(passport)

valid_passport_list_one = []
for p in passport_list:
    if len(p) == 8 or len(p) == 7 and "cid" not in p:
        valid_passport_list_one.append(p)

print("Part one has {} valid passports.".format(len(valid_passport_list_one)))

valid_passport_list_two = []
for p in valid_passport_list_one:
    rules = 0
    for k, v in p.items():
        if k == "byr":
            if int(v) >= 1920 and int(v) <= 2002:
                rules += 1
        elif k == "iyr":
            if int(v) >= 2010 and int(v) <= 2020:
                rules += 1
        elif k == "eyr":
            if int(v) >= 2020 and int(v) <= 2030:
                rules += 1
        elif k == "hgt":
            if v[-2:] == "cm":
                if int(v[:-2]) >= 150 and int(v[:-2]) <= 193:
                    rules += 1
            elif v[-2:] == "in":
                if int(v[:-2]) >= 59 and int(v[:-2]) <= 76:
                    rules += 1
        elif k == "hcl":
            if v[0] == "#":
                if len(re.findall("[a-z0-9]", v[1:])) == 6:
                    rules += 1
        elif k == "ecl":
            colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
            if v in colors:
                rules += 1
        elif k == "pid":
            if len(re.findall("[0-9]", v)) == 9:
                rules += 1
    if rules == 7:
        valid_passport_list_two.append(p)

print("Part two has {} valid passports.".format(len(valid_passport_list_two)))
