# --- Day 9: Rope Bridge ---


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

with open("input.txt") as fp:
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

print("Part 1:", len(visited_one), "\nPart 2:", len(visited_two))
