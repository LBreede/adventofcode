def get_layers(encoded, w, h):
    pixelcount = w * h
    layercount = len(encoded) // pixelcount
    layers = []
    for i in range(layercount):
        layer = encoded[pixelcount * i : pixelcount * (i + 1)]
        layers.append(layer)
    return layers


def get_layer_by_count(lst, val):
    val = str(val)
    lowest_count = float("inf")
    layer = -1
    for i, x in enumerate(lst):
        count = x.count(val)
        if count < lowest_count:
            lowest_count = count
            layer = i
    return layer


def decode(encoded, w, h):
    layers = get_layers(encoded, w, h)
    pixelcount = w * h
    decoded = ["2"] * pixelcount
    decoded = list(decoded)
    for layer in layers:
        for i, pixel in enumerate(layer):
            if pixel != "2" and decoded[i] == "2":
                decoded[i] = pixel
    message = ""
    for i, pixel in enumerate(decoded):
        if pixel == "1":
            message += "#"
        else:
            message += " "
        if i % w == w - 1 and i < len(decoded) - 1:
            message += "\n"
    return message


def main():
    with open("day08_input.txt") as fp:
        encoded = fp.read()
    width, height = 25, 6

    # encoded = "123456789012"
    # width, height = 3, 2

    # encoded = "0222112222120000"
    # width, height = 2, 2

    layers = get_layers(encoded, width, height)
    i = get_layer_by_count(layers, 0)
    a, b = layers[i].count("1"), layers[i].count("2")

    print("Part 1:", a * b)

    message = decode(encoded, width, height)

    print(f"Part 2:\n{message}")


if __name__ == "__main__":
    main()
