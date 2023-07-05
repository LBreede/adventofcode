def load_input(inputfile, separator="\n"):
    with open(inputfile, "r") as f:
        return f.read().split(separator)
