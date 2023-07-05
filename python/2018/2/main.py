# --- Day 2: Inventory Management System ---

line_list = open("input.txt", "r").read().split("\n")
# line_list = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
alphabet = "abcdefghijklmnopqrstuvwxyz"

count_two = 0
count_three = 0

for line in line_list:
    for letter in alphabet:
        count = line.count(letter)
        if count == 2:
            count_two += 1
            break
    for letter in alphabet:
        count = line.count(letter)
        if count == 3:
            count_three += 1
            break

print(count_two * count_three)

found = 0
for i in range(len(line_list)):
    for j in range(len(line_list)):
        matches = [
            k for k in range(len(line_list[i])) if line_list[i][k] != line_list[j][k]
        ]
        if len(matches) == 1 and found == 0:
            oldstr = line_list[i]
            newstr = oldstr[: matches[0]] + oldstr[(matches[0]) + 1 :]
            print(newstr)
            found = 1
