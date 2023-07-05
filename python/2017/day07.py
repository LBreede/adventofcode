# --- Day 7: Recursive Circus ---
from pprint import pprint

file = open("day07_example.txt")
data = []
for x in file:
    a, b, *c = x.rstrip().split()
    b = int(b[1:-1])
    c.pop(0) if c else None
    data.append([a, b, c])
file.close()
pprint(data)
