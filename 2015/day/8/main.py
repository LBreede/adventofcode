# --- Day 8: Matchsticks ---
def njailed(string):
    i = 0
    for line in string.splitlines():
        exec(f"global x; x = {line}")
        i += len(x)
    return i


def escape(string):
    escaped = ""
    for line in string.splitlines():
        escaped += '"' + line.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return escaped


with open("example.txt") as fp:
    txt = fp.read()
literal = len([x for x in txt if x != "\n"])
part_one = literal - njailed(txt)
nescaped = len([x for x in escape(txt) if x != "\n"])
part_two = nescaped - literal
print("Part 1:", part_one, "\nPart 2:", part_two)
