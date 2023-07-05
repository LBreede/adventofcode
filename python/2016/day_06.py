# --- Day 6: Signals and Noise ---

from collections import Counter

with open("input/day_06.txt") as f:
    data = f.read().split("\n")

length = len(data[0])

lst = [""] * length

for x in data:
    for i, y in enumerate(x):
        lst[i] += y

msg_1 = ""
msg_2 = ""
for x in lst:
    msg_1 += Counter(x).most_common(1)[0][0]
    msg_2 += Counter(x).most_common()[-1][0]

print(msg_1)
print(msg_2)
