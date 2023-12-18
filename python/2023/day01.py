def part1(data: str) -> int:
    result = 0
    for line in data.splitlines():
        digits = [x for x in line if x.isdigit()]
        first, last = digits[0], digits[-1]
        result += int(first + last)
    return result


def part2(data: str) -> int:
    data = (
        data.replace("one", "o1ne")
        .replace("two", "t2wo")
        .replace("three", "th3ree")
        .replace("four", "f4our")
        .replace("five", "f5ive")
        .replace("six", "s6ix")
        .replace("seven", "s7even")
        .replace("eight", "e8ight")
        .replace("nine", "n9ine")
    )
    return part1(data)


def main() -> None:
    with open("./input_day01.txt", encoding="utf-8") as fp:
        data = fp.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
