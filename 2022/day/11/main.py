# --- Day 11: Monkey in the Middle ---
from pprint import pprint
from numpy import prod
from tqdm import trange
from copy import deepcopy

monkeys = {}
with open("example.txt") as fp:
    for monkey in fp.read().split("\n\n"):
        a, b, c, d, e, f = monkey.splitlines()
        i = int(a[-2])
        items = [int(x) for x in b[18:].split(", ")]
        op = c[13:]
        divisor = int(d.split()[-1])
        true = int(e.split()[-1])
        false = int(f.split()[-1])
        monkeys[i] = {
            "items": items,
            "op": op,
            "divisor": divisor,
            True: true,
            False: false,
            "inspections": 0,
        }


monkeys_one = deepcopy(monkeys)
for _ in trange(20):
    for monkey in monkeys_one.values():
        monkey["inspections"] += len(monkey["items"])
        for old in monkey["items"].copy():
            exec(monkey["op"])
            new //= 3
            monkeys_one[monkey[new % monkey["divisor"] == 0]]["items"].append(new)
            monkey["items"].remove(old)

monkeys_two = deepcopy(monkeys)
for _ in trange(20):
    for monkey in monkeys_two.values():
        monkey["inspections"] += len(monkey["items"])
        for old in monkey["items"].copy():
            exec(monkey["op"])
            monkeys_two[monkey[new % monkey["divisor"] == 0]]["items"].append(new)
            monkey["items"].remove(old)


for k, v in monkeys_one.items():
    print("Monkey", k, ":", v["inspections"])

part_one = prod(sorted([val["inspections"] for val in monkeys_one.values()])[-2:])
print(part_one)
