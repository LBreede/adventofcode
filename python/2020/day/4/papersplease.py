from random import randint
from random import choice
import time

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
SEP = "=" * 30

passport_fmt = (
    f"{SEP}\n"
    "{name}\n"
    f"{SEP}\n"
    "DOB. {dob}\n"
    "SEX  {sex}\n"
    "ISS. {iyr}\n"
    "EXP. {eyr}\n"
    f"{SEP}\n"
    "{pid}\n"
    f"{SEP}\n\n\n"
)

with open("names.txt") as fp:
    names = fp.read().splitlines()

with open("input.txt") as fp:
    for pp in fp.read().split("\n\n"):
        pp = dict([x.split(":") for x in pp.split()])
        remaining_fields = REQUIRED_FIELDS.difference(set(pp.keys()))
        if not remaining_fields:
            name = choice(names) + " " + choice(names)
            dob = pp["byr"]
            sex = choice(("M", "F"))
            print(
                passport_fmt.format(
                    name=name,
                    dob=dob,
                    sex=sex,
                    iyr=pp["iyr"],
                    eyr=pp["eyr"],
                    pid=pp["pid"],
                )
            )
            time.sleep(0.01)
