def load_input(subdir, day, separator="\n"):
    file = f"{subdir}/day_{str(day).zfill(2)}.txt"
    with open(file) as f:
        return f.read().split(separator)
