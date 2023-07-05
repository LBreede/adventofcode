# --- Day 9: Rope Bridge ---
import time

WIDTH = 32
HEIGHT = 32
HWIDTH = WIDTH // 2
HHEIGHT = HEIGHT // 2


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def bold(string):
    return bcolors.BOLD + string + bcolors.ENDC


def move(pos, direction):
    if direction == "U":
        pos[1] += 1
    elif direction == "D":
        pos[1] -= 1
    elif direction == "L":
        pos[0] -= 1
    elif direction == "R":
        pos[0] += 1
    return pos


def follow(tail, head, direction):
    if all([tail[i] - 1 <= head[i] <= tail[i] + 1 for i in range(2)]):
        return tail
    (tail_x, tail_y), (head_x, head_y) = tail, head
    if tail_x == head_x:
        tail[1] += int(tail_y < head_y) * 2 - 1
    elif tail_y == head_y:
        tail[0] += int(tail_x < head_x) * 2 - 1
    else:
        tail[0] += int(tail_x < head_x) * 2 - 1
        tail[1] += int(tail_y < head_y) * 2 - 1
    return tail


def init_grid(visited={}):
    grid = []
    for i in range(-HHEIGHT, HHEIGHT):
        row = []
        for j in range(-HWIDTH, HWIDTH):
            if (j, i) not in visited:
                row.append(" .")
            else:
                row.append(bcolors.OKBLUE + bold(" #"))
        grid.append(row)
    return grid


def render_grid(grid):
    border = bcolors.WARNING + "=" * WIDTH * 2 + bcolors.ENDC
    print(border)
    print("\n".join(["".join(row) for row in grid[::-1]]))
    print(border + "\n")


head = [0, 0]
tail = head.copy()
one = head.copy()
two = head.copy()
three = head.copy()
four = head.copy()
five = head.copy()
six = head.copy()
seven = head.copy()
eight = head.copy()
nine = head.copy()

visited_one = {tuple(head)}
visited_two = {tuple(head)}

grid = init_grid()

with open("example2.txt") as fp:
    for motion in fp:
        direction, steps = motion.rstrip().split()
        for _ in range(int(steps)):

            head = move(head, direction)

            tail = follow(tail, head, direction)
            visited_one.add(tuple(tail))

            one = follow(one, head, direction)
            two = follow(two, one, direction)
            three = follow(three, two, direction)
            four = follow(four, three, direction)
            five = follow(five, four, direction)
            six = follow(six, five, direction)
            seven = follow(seven, six, direction)
            eight = follow(eight, seven, direction)
            nine = follow(nine, eight, direction)
            visited_two.add(tuple(nine))

            grid = init_grid(visited=visited_two)
            grid[HHEIGHT][HWIDTH] = bcolors.FAIL + bold(" s")
            grid[nine[1] + HHEIGHT][nine[0] + HWIDTH] = bcolors.OKCYAN + bold(" 9")
            grid[eight[1] + HHEIGHT][eight[0] + HWIDTH] = bcolors.OKCYAN + bold(" 8")
            grid[seven[1] + HHEIGHT][seven[0] + HWIDTH] = bcolors.OKCYAN + bold(" 7")
            grid[six[1] + HHEIGHT][six[0] + HWIDTH] = bcolors.OKCYAN + bold(" 6")
            grid[five[1] + HHEIGHT][five[0] + HWIDTH] = bcolors.OKCYAN + bold(" 5")
            grid[four[1] + HHEIGHT][four[0] + HWIDTH] = bcolors.OKCYAN + bold(" 4")
            grid[three[1] + HHEIGHT][three[0] + HWIDTH] = bcolors.OKCYAN + bold(" 3")
            grid[two[1] + HHEIGHT][two[0] + HWIDTH] = bcolors.OKCYAN + bold(" 2")
            grid[one[1] + HHEIGHT][one[0] + HWIDTH] = bcolors.OKCYAN + bold(" 1")
            grid[head[1] + HHEIGHT][head[0] + HWIDTH] = bcolors.OKGREEN + bold(" H")

            render_grid(grid)
            time.sleep(0.1)

# print("Part 1:", len(visited_one), "\nPart 2:", len(visited_two))
