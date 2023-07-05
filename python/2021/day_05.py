# --- Day 5: Hydrothermal Venture ---

import aoc_helper


def process_data(data):
    better_data = []
    for line in data:
        start, ignore, end = line.split()
        pt1 = [int(val) for val in start.split(",")]
        pt2 = [int(val) for val in end.split(",")]
        better_data.append([pt1, pt2])
    return better_data


def is_vertical(pt1, pt2):
    return pt1[0] == pt2[0]


def is_horizontal(pt1, pt2):
    return pt1[1] == pt2[1]


def find_max_axis(data, axis=0):
    max_axis = 0
    for row in data:
        for pos in row:
            if pos[axis] > max_axis:
                max_axis = pos[axis]
    return max_axis


def draw_grid(data):
    grid = []

    max_x_axis = find_max_axis(data)
    max_y_axis = find_max_axis(data, 1)

    for i in range(max_y_axis + 1):
        row = []
        for j in range(max_x_axis + 1):
            row.append(0)
        grid.append(row)
    return grid


def draw_lines(grid, data, include_diagonal=0):

    for d in data:
        pt1, pt2 = d
        if is_horizontal(pt1, pt2):
            y = pt1[1]
            min_x = min(pt1[0], pt2[0])
            max_x = max(pt1[0], pt2[0])
            for i in range(min_x, max_x + 1):
                grid[y][i] += 1

        elif is_vertical(pt1, pt2):
            x = pt1[0]
            min_y = min(pt1[1], pt2[1])
            max_y = max(pt1[1], pt2[1])
            for i in range(min_y, max_y + 1):
                grid[i][x] += 1

        elif (
            not is_horizontal(pt1, pt2)
            and not is_vertical(pt1, pt2)
            and include_diagonal
        ):

            x1, y1 = pt1
            x2, y2 = pt2

            x_range = max(x1, x2) - min(x1, x2) + 1
            y_range = max(y1, y2) - min(y1, y2) + 1

            x_vals = []
            y_vals = []

            for i in range(x_range):
                if x1 < x2:
                    x_vals.append(min(x1, x2) + i)
                else:
                    x_vals.append(max(x1, x2) - i)

            for i in range(y_range):
                if y1 < y2:
                    y_vals.append(min(y1, y2) + i)
                else:
                    y_vals.append(max(y1, y2) - i)

            for i, x in enumerate(x_vals):
                y = y_vals[i]
                grid[y][x] += 1

    return grid


def count_overlap(grid):
    count = 0
    for row in grid:
        for val in row:
            if val > 1:
                count += 1
    return count


def print_grid(grid):
    for row in grid:
        print("".join([str(x) for x in row]).replace("0", "."))


def main():

    data = aoc_helper.load_input("day05_input.txt")
    data = process_data(data)

    grid1 = draw_grid(data)
    grid1 = draw_lines(grid1, data)
    overlaps1 = count_overlap(grid1)
    print(f"Part 1: {overlaps1}")

    grid2 = draw_grid(data)
    grid2 = draw_lines(grid2, data, 1)
    overlaps2 = count_overlap(grid2)
    print(f"Part 2: {overlaps2}")


if __name__ == "__main__":
    main()

# Part 1: 5442
# Part 2: 19571
# [Finished in 383ms]
