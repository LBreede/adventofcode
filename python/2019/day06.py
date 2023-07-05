def map_dict(data):
    dic = {}
    while len(data) > 0:
        for x in list(data):
            a, b = x
            if a == "COM":
                dic[b] = [a]
                data.remove(x)
            elif a in dic:
                dic[b] = dic[a] + [a]
                data.remove(x)
    return dic


def load_map(file):
    with open(file) as fp:
        return [x.split(")") for x in fp.read().split("\n")]


def main():
    mapdata = load_map("day06_input.txt")
    mapdict = map_dict(mapdata)
    totalorbits = sum([len(x) for x in mapdict.values()])
    print("Total Orbits:", totalorbits)
    you_orbit = mapdict["YOU"]
    san_orbit = mapdict["SAN"]
    for x, y in zip(list(you_orbit), list(san_orbit)):
        if x == y:
            you_orbit.remove(x)
            san_orbit.remove(y)
    print("YOU to SAN:  ", len(you_orbit + san_orbit))


if __name__ == "__main__":
    main()
