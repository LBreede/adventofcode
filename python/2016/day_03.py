# --- Day 3: Squares With Three Sides ---


def count_triangles(data):
    ntris = 0
    for x in data:
        if x[0] + x[1] > x[2] and x[1] + x[2] > x[0] and x[2] + x[0] > x[1]:
            ntris += 1
    return ntris


def rows_to_cols(data):
    new_data = []
    for i in range(len(data) // 3):
        a = data[i * 3]
        b = data[i * 3 + 1]
        c = data[i * 3 + 2]
        x = [a[0], b[0], c[0]]
        y = [a[1], b[1], c[1]]
        z = [a[2], b[2], c[2]]
        new_data.append(x)
        new_data.append(y)
        new_data.append(z)
    return new_data


def main():
    with open("input/day_03.txt") as f:
        data = [list(map(int, x.split())) for x in f.read().split("\n")]

    answer_1 = count_triangles(data)

    data = rows_to_cols(data)
    answer_2 = count_triangles(data)

    print(f"Part 1: {answer_1}")
    print(f"Part 2: {answer_2}")


if __name__ == "__main__":
    main()
