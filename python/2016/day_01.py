# --- Day 1: No Time for a Taxicab ---


DIR_TABLE = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
compass = 0


class Vector2:
    """Following the pygame conventions -y = up, therefore vector (0, -1) is north."""

    def __init__(self, x, y=None):
        if isinstance(x, (tuple, list)):
            self.x, self.y = x
        elif isinstance(x, (float, int)):
            self.x = x
            self.y = y

    def as_tuple(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vector2((self.x + other.x, self.y + other.y))

    def __str__(self):
        return f"[{self.x}, {self.y}]"


def turn_compass(turn):
    global compass
    if turn == "L":
        compass = (compass - 1) % 4
    elif turn == "R":
        compass = (compass + 1) % 4


def distance(sequence):
    return sum([abs(x) for x in sequence])


def main():
    with open("input/day_01.txt") as f:
        data = f.read().split(", ")

    data = [(x[0], int(x[1:])) for x in data]

    pos = Vector2(0, 0)
    pos_list = [pos.as_tuple()]
    append_to_list = True

    for d in data:
        turn, steps = d
        turn_compass(turn)

        for i in range(steps):
            direction = Vector2(DIR_TABLE[compass])
            pos += direction

            if append_to_list:
                if pos.as_tuple() in pos_list:
                    append_to_list = False
                pos_list.append(pos.as_tuple())

    answer_1 = distance(pos.as_tuple())
    answer_2 = distance(pos_list[-1])
    print(f"Part 1: {answer_1}\nPart 2: {answer_2}")


if __name__ == "__main__":
    main()
