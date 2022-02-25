# --- Day 2: 1202 Program Alarm ---


from intcode import computer


def main():
    with open("input/day_02.txt", "r") as f:
        program = list(map(int, f.read().split(",")))

    result_1 = computer.run(program, 12, 2)

    for i in range(100):
        for j in range(100):
            result = computer.run(program, i, j)
            if result == 19690720:
                result_2 = 100 * i + j
                break

    print(f"Part 1: {result_1}")
    print(f"Part 2: {result_2}")


if __name__ == "__main__":
    main()
