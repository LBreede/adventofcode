# --- Day 5: How About a Nice Game of Chess? ---
import hashlib


def main():
    DOOR_ID = "uqwqemis"
    password_1 = ""
    password_2 = [None] * 8
    i = 3231929
    while True:
        string = f"{DOOR_ID}{i}"
        hexadecimal = hashlib.md5(string.encode()).hexdigest()
        if hexadecimal[:5] == "00000":
            sixth, seventh = hexadecimal[5:7]
            if len(password_1) < 8:
                password_1 += str(sixth)
            if sixth in ("0", "1", "2", "3", "4", "5", "6", "7"):
                if password_2[int(sixth)] is None:
                    password_2[int(sixth)] = seventh
        if None not in password_2:
            break
        i += 1
    password_2 = "".join(password_2)
    print(f"Part 1: {password_1}.")
    print(f"Part 2: {password_2},")
    print(f"After {i+1} iterations.")


if __name__ == "__main__":
    main()
