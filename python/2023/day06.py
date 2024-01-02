import time


def get_result(race_times: list[int], record_distances: list[int]) -> int:
    result = 1
    for t, d in zip(race_times, record_distances):
        amount = 0
        for i in range(t + 1):
            dist = (t - i) * i
            amount += 1 if dist > d else 0
        result *= amount
    return result


def part1(data: str) -> int:
    race_times = [int(x) for x in data.splitlines()[0].split()[1:]]
    record_distances = [int(x) for x in data.splitlines()[1].split()[1:]]
    return get_result(race_times, record_distances)


def part2(data: str) -> int:
    race_times = [int("".join(data.splitlines()[0].split()[1:]))]
    record_distances = [int("".join(data.splitlines()[1].split()[1:]))]
    return get_result(race_times, record_distances)


def main() -> None:
    with open("./input_day06.txt", encoding="utf-8") as fp:
        data = fp.read()

    start = time.time()
    result = part1(data)
    duration = time.time() - start
    print(f"Part 1: {result} (took {duration:.3f} seconds)")

    start = time.time()
    result = part2(data)
    duration = time.time() - start
    print(f"Part 2: {result} (took {duration:.3f} seconds)")


if __name__ == "__main__":
    main()
