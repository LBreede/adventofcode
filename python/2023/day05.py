import time

Map = list[tuple[range, range]]


def get_seeds(data: str) -> set[int]:
    return set(int(x) for x in data.splitlines()[0][7:].split())


def get_seed_ranges(data: str) -> set[int]:
    values = data.splitlines()[0][7:].split()
    seeds: set[int] = set()
    for i in range(0, len(values), 2):
        start = int(values[i])
        stop = start + int(values[i + 1])
        for x in range(start, stop):
            seeds.add(x)
    return seeds


def get_map(data: str, name: str) -> Map:
    values = [m for m in data.split("\n\n") if m.startswith(name)][0].splitlines()[1:]
    new_map: Map = []
    for line in values:
        dst_rng_start, src_rng_start, rng_length = [int(x) for x in line.split()]
        src_rng = range(src_rng_start, src_rng_start + rng_length)
        dst_rng = range(dst_rng_start, dst_rng_start + rng_length)
        new_map.append((src_rng, dst_rng))
    return new_map


def convert_value(number: int, conversion_map: Map) -> int:
    for src_rng, dst_rng in conversion_map:
        if number in src_rng:
            return dst_rng[src_rng.index(number)]
    return number


def get_min_location(data: str, numbers: set[int]) -> int:
    map_names = (
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    )
    for map_name in map_names:
        conversion_map = get_map(data, map_name)
        numbers = set(convert_value(num, conversion_map) for num in numbers)
    return min(numbers)


def part1(data: str) -> int:
    seeds = get_seeds(data)
    return get_min_location(data, seeds)


def part2(data: str) -> int:
    seeds = get_seed_ranges(data)
    return get_min_location(data, seeds)


def main() -> None:
    with open("./input_day05.txt", encoding="utf-8") as fp:
        data = fp.read()

    start = time.time()
    result = part1(data)
    duration = time.time() - start
    print(f"Part 1: {result} (took {duration:.3f} seconds)")

    # start = time.time()
    # result = part2(data)
    # duration = time.time() - start
    # print(f"Part 2: {result} (took {duration:.3f} seconds)")


if __name__ == "__main__":
    main()
