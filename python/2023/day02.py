def part1(data: str) -> int:
    result = 0
    for game in data.splitlines():
        game_number, game_data = game.split(": ")
        game_results: list[bool] = []
        for subset in game_data.split("; "):
            subset_results: list[bool] = []
            for cube in subset.split(", "):
                number, color = cube.split(" ")
                if color == "red":
                    subset_results.append(int(number) <= 12)
                elif color == "green":
                    subset_results.append(int(number) <= 13)
                elif color == "blue":
                    subset_results.append(int(number) <= 14)
            game_results.append(all(subset_results))
        if all(game_results):
            result += int(game_number.split(" ")[1])
    return result


def part2(data: str) -> int:
    result = 0
    for game in data.splitlines():
        game_data = game.split(": ")[1]
        red = green = blue = 0
        for subset in game_data.split("; "):
            for cube in subset.split(", "):
                number, color = cube.split(" ")
                if color == "red":
                    red = max(red, int(number))
                elif color == "green":
                    green = max(green, int(number))
                elif color == "blue":
                    blue = max(blue, int(number))
        result += red * blue * green
    return result


def main() -> None:
    with open("./input_day02.txt", encoding="utf-8") as fp:
        data = fp.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
