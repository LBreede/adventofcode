# --- Day 4: Secure Container ---

import re


def criteria1(password):
    if len(str(password)) == 6:
        return True
    else:
        return False


def criteria2(password, puzzle_input):
    min_, max_ = [int(x) for x in puzzle_input.split("-")]
    if min_ <= password <= max_:
        return True
    return False


def criteria3(password):
    regex = re.compile(r"(\d)\1")
    if re.search(regex, str(password)):
        return True
    return False


def criteria4(password):
    a, b, c, d, e, f = [int(x) for x in str(password)]

    if a <= b <= c <= d <= e <= f:
        return True
    return False


def has_exact_double(password):
    """Find at least one exact double in password by iterating over every
    multiple and checking if at least one of them is of length 2

    Args:
        password (int): the password the match the criteria to

    Returns:
        The return value. True for an exact match, False otherwise

    """
    return any(
        len(match.group(0)) == 2 for match in re.finditer(r"(\d)\1+", str(password))
    )


puzzle_input = "137683-596253"
start, end = list(map(int, puzzle_input.split("-")))

match1 = 0
match2 = 0

for x in range(start, end + 1):
    c1 = criteria1(x)
    c3 = criteria3(x)
    c4 = criteria4(x)
    c5 = has_exact_double(x)
    if c1 and c3 and c4:
        match1 += 1
        if c5:
            match2 += 1

print(match1)
print(match2)
