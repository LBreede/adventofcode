# --- Day 4: The Ideal Stocking Stuffer ---
from hashlib import md5


def solve(key: str, zeroes: int) -> int:
    i = 0
    while True:
        hash_ = md5((key + str(i)).encode()).hexdigest()
        if hash_.startswith("0" * zeroes):
            return i
        i += 1


key = "yzbqklnj"
print("Part 1:", solve(key, 5), "\nPart 2:", solve(key, 6))
