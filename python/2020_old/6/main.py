# --- Day 6: Custom Customs ---

with open("input.txt", "r") as f:
	line_list = [line.split("\n") for line in f.read().split("\n\n")]

counts_pt_one = counts_pt_two = 0
for line in line_list:
	groupsize = len(line)
	answer = ""
	for L in line:
		answer += L
	unique_answers = "".join(set(answer))
	counts_pt_one += len(unique_answers)
	for letter in unique_answers:
		if answer.count(letter) == groupsize:
			counts_pt_two += 1
	
print(counts_pt_one)
print(counts_pt_two)