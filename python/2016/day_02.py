# --- Day 2: Bathroom Security ---


# fmt: off
KEYPAD_1 = (
    (None, None, None, None, None),
    (None, "1",  "2",  "3",  None),
    (None, "4",  "5",  "6",  None),
    (None, "7",  "8",  "9",  None),
    (None, None, None, None, None)
)
KEYPAD_2 = (
    (None, None, None, None, None, None, None),
    (None, None, None, "1",  None, None, None),
    (None, None, "2",  "3",  "4",  None, None),
    (None, "5",  "6",  "7",  "8",  "9",  None),
    (None, None, "A",  "B",  "C",  None, None),
    (None, None, None, "D",  None, None, None),
    (None, None, None, None, None, None, None)
)
# fmt: on


def solve_keypad(keypad, start, instructions):
    row, col = start
    code = ""
    for i in instructions:
        for j in i:
            row, col = traverse_keypad(j, (row, col), keypad)
        code += keypad[row][col]
    return code


def traverse_keypad(instruction, pos, keypad):
    row, col = pos
    if instruction in ("U", "D"):
        if instruction == "U":
            temp_row = row - 1
        elif instruction == "D":
            temp_row = row + 1

        if keypad[temp_row][col] is not None:
            row = temp_row

    elif instruction in ("L", "R"):
        if instruction == "L":
            temp_col = col - 1
        elif instruction == "R":
            temp_col = col + 1

        if keypad[row][temp_col] is not None:
            col = temp_col

    return (row, col)


def main():
    with open("input/day_02.txt") as f:
        data = [list(x) for x in f.read().split("\n")]

    code_1 = solve_keypad(KEYPAD_1, (2, 2), data)
    code_2 = solve_keypad(KEYPAD_2, (3, 1), data)

    print(code_1)
    print(code_2)


if __name__ == "__main__":
    main()
