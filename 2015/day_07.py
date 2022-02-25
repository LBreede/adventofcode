# --- Day 7: Some Assembly Required ---

MAX = 65535
LOGIC_LUT = {"AND": "&", "OR": "|", "LSHIFT": "<<", "RSHIFT": ">>", "NOT": "65535+1+~"}


def process(data):
    new_data = []
    for x in data:
        i, output = x.split(" -> ")
        i = (
            i.replace("AND", "&")
            .replace("OR", "|")
            .replace("LSHIFT", "<<")
            .replace("RSHIFT", ">>")
            .replace("NOT", "65535 + 1 + ~")
        )
        new_data.append(f"global {output}; {output} = {i}")
        # new_data.append(f"print({output})")
    return new_data


def main():
    with open("input/day_07.txt") as file:
        data = file.read().split("\n")

    data = process(data)

    valid = 0

    for iteration in range(16):
        for line in data:
            try:
                exec(line)
                print(line)
                valid += 1
                data.remove(line)
            except:
                pass  # do nothing

    print(valid)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# for i in range(1):
#     for x in a:
#         if x % 3 == 0:
#             a.remove(x)

# print(a)


if __name__ == "__main__":
    main()
