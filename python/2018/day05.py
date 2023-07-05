# --- Day 5: Alchemical Reduction ---
import re
import os
from tqdm import trange


ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def create_regex():
    regex = ""
    for char in ALPHABET:
        regex += f"{char}{char.upper()}|{char.upper()}{char}|"
    return re.compile(regex[:-1])


def initial_reduction(s, letter):
    regex = re.compile(f"[{letter}{letter.upper()}]")
    s = re.sub(regex, "", s)
    return s


def recursive_reduction(s):
    regex = create_regex()
    result = re.search(regex, s)
    while result:
        s = re.sub(regex, "", s, 1)
        result = re.search(regex, s)
    return s


def main():
    with open("day05_input.txt") as fp:
        string = fp.read()
    # string = "dabAcCaCBAcCcaDA"

    reduced_string = recursive_reduction(string)
    print(f"Part 1: {len(reduced_string)}")

    smallest = float("inf")

    for i in trange(len(ALPHABET)):
        letter = ALPHABET[i]
        reduced_string = initial_reduction(string, letter)
        reduced_string = recursive_reduction(reduced_string)

        if len(reduced_string) < smallest:
            smallest = len(reduced_string)

    print(f"Part 2: {smallest}")


if __name__ == "__main__":
    main()
