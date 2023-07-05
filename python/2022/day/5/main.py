# --- Day 5: Supply Stacks ---
from copy import deepcopy


def move_crates(lst: list, n: int, src: int, dst: int, reverse: bool = False) -> list:
    crates_to_move = lst[src][:n][::-1] if reverse else lst[src][:n]

    for crate in crates_to_move:
        lst[dst].insert(0, crate)
        lst[src].remove(crate)

    return lst


with open("input.txt") as fp:
    crates_ascii, commands = fp.read().split("\n\n")

ncrates = int(crates_ascii[-2])
crates_ascii = "\n".join(crates_ascii.split("\n")[:-1])
crate_list = [[] for _ in range(ncrates)]

for line in crates_ascii.split("\n"):
    for i in range(ncrates):
        crate_letter = line[i * 4 + 1]
        if crate_letter != " ":
            crate_list[i].append(crate_letter)

commands = [[int(y) for y in x.split() if y.isnumeric()] for x in commands.split("\n")]
commands = [[y - 1 if i != 0 else y for i, y in enumerate(x)] for x in commands]

crate_list_one = deepcopy(crate_list)
crate_list_two = deepcopy(crate_list)

for cmd in commands:
    n, src, dst = cmd
    move_crates(crate_list_one, n, src, dst)
    move_crates(crate_list_two, n, src, dst, reverse=True)

part_one = "".join([x[0] for x in crate_list_one])
part_two = "".join([x[0] for x in crate_list_two])

print("Part 1:", part_one, "\nPart 2:", part_two)
