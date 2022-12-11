# --- Day 4: Passport Processing ---
import re

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid_one = valid_two = 0
with open("input.txt") as fp:
    for pp in fp.read().split("\n\n"):
        pp = dict([x.split(":") for x in pp.split()])
        remaining_fields = REQUIRED_FIELDS.difference(set(pp.keys()))
        if not remaining_fields:
            valid_one += 1
            byr = 1920 <= int(pp["byr"]) <= 2002
            iyr = 2010 <= int(pp["iyr"]) <= 2020
            eyr = 2020 <= int(pp["eyr"]) <= 2030
            hgt_cm = pp["hgt"].endswith("cm") and 150 <= int(pp["hgt"][:-2]) <= 193
            hgt_in = pp["hgt"].endswith("in") and 59 <= int(pp["hgt"][:-2]) <= 76
            hgt = hgt_cm | hgt_in
            hcl = bool(re.search(r"^#[0-9a-f]{6}$", pp["hcl"]))
            ecl = pp["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            pid = bool(re.search(r"^\d{9}$", pp["pid"]))
            valid_two += 1 if all((byr, iyr, eyr, hgt, hcl, ecl, pid)) else 0

print("Part 1:", valid_one, "\rPart 2:", valid_two)
