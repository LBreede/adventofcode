from pprint import pprint

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("day07_example.txt") as fp:
    data = fp.read()

instructions = {}

for x in data.splitlines():
    a, b = x.split()[1], x.split()[7]
    if b not in instructions:
        instructions[b] = [a]
    else:
        instructions[b].append(a)


pprint(instructions)

done = []

for letter in "ABCABDE":

    if letter in instructions:
        lst = instructions[letter]
        for y in lst:
            if y in done:
                done.append(letter)
    else:
        done.append(letter)

    pprint(done)
    # pprint(data)
