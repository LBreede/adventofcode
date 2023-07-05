# --- Day 4: High-Entropy Passphrases ---

from aoc_helper import load_input

passphrase_list = load_input("input", 4)
passphrase_list = [x.split() for x in passphrase_list]


def count_valid(lst, include_anagrams=0):
    valid = 0
    for x in lst:
        if include_anagrams:
            x = ["".join(sorted(y)) for y in x]
        if len(x) == len(set(x)):
            valid += 1
    return valid


result1 = count_valid(passphrase_list)
result2 = count_valid(passphrase_list, include_anagrams=1)

print(f"Part 1: {result1}")
print(f"Part 2: {result2}")
