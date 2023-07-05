# --- Day 1: Inverse Captcha ---

with open("input/day_01.txt") as f:
    data = list(map(int, f.read()))

ndigits = len(data)
answer_1 = answer_2 = 0
for i, a in enumerate(data):
    b = data[(i + 1) % ndigits]
    c = data[(i + ndigits // 2) % ndigits]
    if a == b:
        answer_1 += a
    if a == c:
        answer_2 += a

print(f"Part 1: {answer_1}\nPart 2: {answer_2}")
