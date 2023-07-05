# --- Day 6: Chronal Coordinates ---

from typing import Tuple, List

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

Coord = Tuple[int, int]


def read_coords(filepath: str) -> list:
    """Reads a text file on disk and converts each line from a string to a tuple with
    two integers, a coordinate. Every coordinate is then returned as a list.

    Args:
        filepath (str): The filepath on disk.

    Returns:
        list: A list of all coordinates extracted from a text file.

    """
    with open(filepath) as fp:
        line_list = fp.read().split("\n")

    c = [tuple(map(int, line.split(","))) for line in line_list]
    return c


def calc_distance(a: Coord, b: Coord) -> int:
    """Calculates the Manhatten distance between two coordinates.

    Args:
        a (Coord): The start coordinate.
        b (Coord): The end coordinate.

    Returns:
        int: The Manhatten distance from start to end.

    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def calc_minmax(coord_list: List[Coord]) -> Tuple[int, int, int, int]:
    """Calculates the minimum and maximum for both x and y for all coordinates.

    Args:
        coord_list (List[Coord]): A list of all coordinates.

    Returns:
        Tuple[int, int, int, int]: A ordered tuple holding the min for x, min for y, max
            for x and max for y in this order.

    """
    xl, yl = [], []

    for x, y in coords:
        xl.append(x)
        yl.append(y)

    return (min(xl), min(yl), max(xl), max(yl))


def get_coord_dict(coords, offset=0):
    xmin, ymin, xmax, ymax = calc_minmax(coords)
    coord_dict = {}
    for y in range(xmin - offset, xmax + 1 + offset):
        for x in range(ymin - offset, ymax + 1 + offset):
            dist_dict = {}

            for i, coord in enumerate(coords):
                dist = calc_distance((x, y), coord)
                dist_dict[i] = dist

            dist_dict = {
                k: v for k, v in sorted(dist_dict.items(), key=lambda item: item[1])
            }
            dist_vals = list(dist_dict.values())
            val_0, val_1 = dist_vals[:2]
            min_dist = val_0 if val_0 != val_1 else None
            closest_id = list(dist_dict.keys())[0] if min_dist is not None else None

            if closest_id is not None:
                if closest_id in coord_dict:
                    coord_dict[closest_id].append((x, y))
                else:
                    coord_dict[closest_id] = [(x, y)]

    return coord_dict


def find_largest_area(coords):
    coord_dict_a = get_coord_dict(coords)
    coord_dict_b = get_coord_dict(coords, offset=1)

    areas = []

    for k, v in coord_dict_a.items():
        if len(v) == len(coord_dict_b[k]):
            areas.append(len(v))

    return max(areas)


coords = read_coords("day06_input.txt")
largest_area = find_largest_area(coords)
print(largest_area)
