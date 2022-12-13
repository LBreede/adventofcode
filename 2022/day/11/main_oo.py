# --- Day 11: Monkey in the Middle ---
from pprint import pprint
from numpy import prod
from tqdm import trange
from copy import deepcopy


class Monkey:
    def __init__(self, index, items, operation, divisor, true, false):
        self.index = index
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.true = true
        self.false = false
        self.inspections = 0

    def solve(self, val):
        a = int(self.operation[0]) if self.operation[0].isnumeric() else val
        b = int(self.operation[2]) if self.operation[2].isnumeric() else val
        return a * b if self.operation[1] == "*" else a + b

    def throw(self, val):
        return self.true if val % self.divisor == 0 else self.false

    def __repr__(self):
        return f"<Monkey(index={self.index}, ... )>"

    def __str__(self):
        return f"Monkey {self.index} - Inspections: {self.inspections}"


def load_monkeys(file):
    monkeys = []
    with open(file) as fp:
        for monkey in fp.read().split("\n\n"):
            a, b, c, d, e, f = monkey.splitlines()
            i = int(a[-2])
            items = [int(x) for x in b[18:].split(", ")]
            op = c[19:].split()
            div = int(d.split()[-1])
            true = int(e.split()[-1])
            false = int(f.split()[-1])
            m = Monkey(i, items, op, div, true, false)
            monkeys.append(m)
    return monkeys


def play_keep_away(monkeys, n, desc, is_boring=True):
    for _ in trange(n, desc=desc):
        for i, monkey in enumerate(monkeys):
            monkey.inspections += len(monkey.items)
            for old in monkey.items.copy():
                new = monkey.solve(old)
                new = new // 3 if is_boring else new
                monkeys[monkey.throw(new)].items.append(new)
                monkey.items.remove(old)
    return monkeys


monkeys = load_monkeys("example.txt")
monkeys_one = play_keep_away(deepcopy(monkeys), 20, "Part 1")
monkeys_two = play_keep_away(deepcopy(monkeys), 20, "Part 2", is_boring=False)

for m in monkeys_two:
    print(m)

part_one = prod(sorted([monkey.inspections for monkey in monkeys_one])[-2:])
print(part_one)
#
