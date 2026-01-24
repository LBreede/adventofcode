def start_day(day: int) -> None:
    print(f"Advent of Code 2025 - Day {day:02}\n")


def read_input_to_string(day: int) -> str:
    file = f"input/{day:02}.txt"
    with open(file, "r", encoding="utf-8") as fp:
        return fp.read()
