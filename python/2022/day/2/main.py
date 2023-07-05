# --- Day 2: Rock Paper Scissors ---
# fmt: off
GAME_MAP = {
    "A X": 3, "A Y": 6, "A Z": 0,
    "B X": 0, "B Y": 3, "B Z": 6,
    "C X": 6, "C Y": 0, "C Z": 3,
}  # fmt: on
SHAPE_MAP = {
    "X": {"game_score": 0, "shape": {"A": "Z", "B": "X", "C": "Y"}},
    "Y": {"game_score": 3, "shape": {"A": "X", "B": "Y", "C": "Z"}},
    "Z": {"game_score": 6, "shape": {"A": "Y", "B": "Z", "C": "X"}},
}

shape_score = lambda shape: list(SHAPE_MAP.keys()).index(shape) + 1


def main():
    total_one = total_two = 0
    with open("input.txt", encoding="utf8") as fp:
        for game in fp.read().splitlines():
            left, right = game.split(" ")
            total_one += GAME_MAP[game] + shape_score(right)
            game_score = SHAPE_MAP[right]["game_score"]
            shape = SHAPE_MAP[right]["shape"][left]
            total_two += game_score + shape_score(shape)
    print("Part 1:", total_one, "\nPart 2:", total_two)


if __name__ == "__main__":
    main()
