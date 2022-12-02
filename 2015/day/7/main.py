# --- Day 7: Some Assembly Required ---
def get_val(val, dic):
    if val.isnumeric():
        return int(val)
    else:
        try:
            return dic[val]
        except KeyError:
            return None


def solve(lines):

    signals = {}

    while True:

        lines_removed = 0

        for i, line in enumerate(lines.copy()):

            z, _, *xy = line.split(" ")[::-1]
            xy.reverse()

            if len(xy) == 3:
                x, op, y = xy
                x = get_val(x, signals)
                y = get_val(y, signals)
                if x is None or y is None:
                    continue

                if op == "AND":
                    val = x & y

                elif op == "OR":
                    val = x | y

                elif op == "LSHIFT":
                    val = x << y

                elif op == "RSHIFT":
                    val = x >> y

            elif len(xy) == 2:
                x = xy[1]
                x = get_val(x, signals)
                if x is None:
                    continue

                val = ~x & 65535

            elif len(xy) == 1:
                x = xy[0]
                x = get_val(x, signals)
                if x is None:
                    continue
                val = x

            signals[z] = val
            lines.remove(line)
            lines_removed += 1

        if not lines_removed:
            break

    return signals


with open("input.txt") as fp:
    lines = fp.read().splitlines()

signals_one = solve(lines.copy())
part_one = signals_one["a"]

lines_two = lines.copy()
to_replace = [x for x in lines_two if x.endswith(" -> b")][0]
idx = lines_two.index(to_replace)
lines_two[idx] = f"{part_one} -> b"
part_two = solve(lines_two)["a"]
print("Part 1:", part_one, "\nPart 2:", part_two)
