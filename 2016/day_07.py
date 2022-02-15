# --- Day 7: Internet Protocol Version 7 ---


import re


def is_abba(sequence):
    half = len(sequence) // 2

    start = sequence[:half]
    end = sequence[half:]

    if start[0] != end[0] and start == end[::-1]:
        return True
    return False


data = ("abba[mnop]qrst", "abcd[bddb]xyyx", "aaaa[qwer]tyui", "ioxxoj[asdfgh]zxcvbn")

for ip in data:
    a, b = ip.split("[")
    b, c = b.split("]")

    if is_abba(a) or is_abba(c) and not is_abba(b):
        print("ABBA")
