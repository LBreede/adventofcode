# --- Day 2: Password Philosophy ---

def processInput(puzzle_input, to_int=False):
	puzzle_input_list = open("input.txt", "r").read().split("\n")
	if to_int:
		puzzle_input_list = list(map(int, puzzle_input_list))
	return puzzle_input_list

def processPasswordList(password_list):
	processed_password_list = []
	for p in password_list:
		parts = p.split(" ")
		prange = parts[0].split("-")
		pmin = int(prange[0])
		pmax = int(prange[1])
		pattern = parts[1][:-1]
		password = parts[2]
		elem = [pmin, pmax, pattern, password]
		processed_password_list.append(elem)
	return processed_password_list

def countValidPasswordsOne(processed_password_list):
	valid = 0
	for p in processed_password_list:
		occur = p[3].count(p[2])
		if occur >= p[0] and occur <= p[1]:
			valid += 1
	return valid

def countValidPasswordsTwo(processed_password_list):
	valid = 0
	for p in processed_password_list:
		if p[3][p[0]-1] == p[2] and p[3][p[1]-1] != p[2] or p[3][p[0]-1] != p[2] and p[3][p[1]-1] == p[2]:
			valid += 1
	return valid

if __name__ == "__main__":
	password_list = processInput("input.txt")
	# password_list = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
	processed_password_list = processPasswordList(password_list)
	valid_password_count_one = countValidPasswordsOne(processed_password_list)
	valid_password_count_two = countValidPasswordsTwo(processed_password_list)
	print(valid_password_count_one)
	print(valid_password_count_two)