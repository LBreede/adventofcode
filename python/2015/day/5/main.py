# --- Day 5: Doesn't He Have Intern-Elves For This? ---
import re

REGEX = (r"([aeiou].*){3,}", r"(.)\1", r"ab|cd|pq|xy", r"(..).*\1", r"(.).\1")
answer_one = answer_two = 0
with open("input.txt") as fp:
    for string in fp:
        a, b, c, d, e = [re.search(r, string.rstrip()) for r in REGEX]
        answer_one += 1 if a and b and not c else 0
        answer_two += 1 if d and e else 0
print("Part 1:", answer_one, "\nPart 2:", answer_two)
