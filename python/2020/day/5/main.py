# --- Day 5: Binary Boarding ---


def findseat(code: str, amount: int) -> int:
    current_min = 0
    current_max = amount - 1  # What is this even used for?
    for i in range(len(code)):
        amount //= 2
        if code[i] == "F" or code[i] == "L":  # and this?
            current_max -= amount  # or this? Don't even know what I was thinking..
        elif code[i] == "B" or code[i] == "R":
            current_min += amount
    return current_min


all_seat_ids = set()

with open("input.txt") as fp:
    for line in fp:
        row_code = line[:-3]
        col_code = line.rstrip()[-3:]
        row = findseat(row_code, 128)
        col = findseat(col_code, 8)
        all_seat_ids.add(row * 8 + col)

highest_seat_id = sorted(all_seat_ids)[-1]
for i in range(highest_seat_id):
    if i - 1 in all_seat_ids and i not in all_seat_ids and i + 1 in all_seat_ids:
        break
print("Part 1:", highest_seat_id, "\nPart 2:", i)
