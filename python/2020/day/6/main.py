# --- Day 6: Custom Customs ---

def main():
    part_one = part_two = 0

    with open("./example.txt", encoding="utf-8") as fp:
        for line in [line.split("\n") for line in fp.read().split("\n\n")]:
            groupsize = len(line)
            answer = "".join(line)
            unique_answers = "".join(set(answer))
            part_one += len(unique_answers)
            for letter in unique_answers:
                if answer.count(letter) == groupsize:
                    part_two += 1

    print("Part 1:", part_one, "\nPart 2:", part_two)

if __name__ == "__main__":
    main()
