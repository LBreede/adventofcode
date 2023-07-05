# --- Day 10: Elves Look, Elves Say ---
def look_and_say(puzzle, iterations):
    for i in range(iterations):
        curr_char = temp_puzzle_input = ""
        for j, char in enumerate(puzzle):
            if char not in curr_char and j > 0:
                temp_puzzle_input += str(len(curr_char)) + curr_char[0]
                curr_char = char
            else:
                curr_char += char
        puzzle = temp_puzzle_input + str(len(curr_char)) + curr_char[0]
    return puzzle


puzzle_input = "1321131112"
part_one = look_and_say(puzzle_input, 40)
part_two = look_and_say(part_one, 10)
print(len(part_one), len(part_two))
