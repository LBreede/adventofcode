# --- Day 9: Stream Processing ---


def process_stream(stream: str) -> tuple[int, int]:
    opened = 0
    group_score = 0
    is_garbage = False
    num_garbage = 0
    i = 0
    while i < len(stream):
        char = stream[i]
        if char == "!":
            i += 1
        elif char == ">":
            is_garbage = False
        elif is_garbage:
            num_garbage += 1
        elif char == "{":
            opened += 1
        elif char == "}":
            group_score += opened
            opened -= 1
        elif char == "<":
            is_garbage = True
        else:
            pass
        i += 1

    return group_score, num_garbage


def main() -> None:
    assert process_stream("{}")[0] == 1
    assert process_stream("{{{}}}")[0] == 6
    assert process_stream("{{},{}}")[0] == 5
    assert process_stream("{{{},{},{{}}}}")[0] == 16
    assert process_stream("{<a>,<a>,<a>,<a>}")[0] == 1
    assert process_stream("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
    assert process_stream("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
    assert process_stream("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3

    assert process_stream("<>")[1] == 0
    assert process_stream("<random characters>")[1] == 17
    assert process_stream("<<<<>")[1] == 3
    assert process_stream("<{!>}>")[1] == 2
    assert process_stream("<!!>")[1] == 0
    assert process_stream("<!!!>>")[1] == 0
    assert process_stream('<{o"i!a,<{i<a>')[1] == 10

    with open("day09_input.txt", encoding="utf-8") as fp:
        group_score, num_garbage = process_stream(fp.read())

    print(f"Part one: {group_score}")
    print(f"Part two: {num_garbage}")


if __name__ == "__main__":
    main()
