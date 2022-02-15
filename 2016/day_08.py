# --- Day 8: Two-Factor Authentication ---


def create_screen(x, y):
    global screen
    screen = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(0)
        screen.append(row)
    return screen


def create_rect(i):
    x, y = list(map(int, i[1].split("x")))
    for i in range(y):
        for j in range(x):
            screen[i][j] = 1 - screen[i][j]


def rotate(i):
    _, __, idx, ___, amt = i
    idx = int(idx.split("=")[1])
    amt = int(amt)
    if i[1] == "row":
        rotate_row(idx, amt)
    elif i[1] == "column":
        rotate_col(idx, amt)


def rotate_list(l, n):
    return l[-n:] + l[:-n]


def rotate_row(i, n):
    screen[i] = rotate_list(screen[i], n)


def rotate_col(idx, n):
    temp_col = []
    for x in screen:
        temp_col.append(x[idx])
    temp_col = rotate_list(temp_col, n)
    for i, x in enumerate(temp_col):
        screen[i][idx] = x


def solve(data):
    for x in data:
        if len(x) == 2:
            create_rect(x)
        elif len(x) == 5:
            rotate(x)


def draw_screen(on="#", off="."):
    pretty_screen = ""
    for row in screen:
        for col in row:
            if col:
                pretty_screen += on
            else:
                pretty_screen += off
        pretty_screen += "\n"
    print(pretty_screen)


def main():
    create_screen(50, 6)

    with open("input/day_08.txt") as f:
        data = [x.split() for x in f.read().split("\n")]

    solve(data)

    a = sum([sum(x) for x in screen])
    print(f"Part 1: {a}")

    print("Part 2:")
    draw_screen(on = "█", off = " ")


if __name__ == "__main__":
    main()
