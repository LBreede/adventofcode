# --- Day 2: 1202 Program Alarm ---

def createIntcodeList(puzzle_input):
	intcode_list = open(puzzle_input, "r").read().split(",")
	intcode_list = list(map(int, intcode_list))
	return intcode_list

def modifyIncodeList(intcode_list):
	_intcode_list = intcode_list.copy()
	_intcode_list[1] = 12
	_intcode_list[2] = 2
	return _intcode_list

def intcodeProgramOne(intcode_list):
	idx = 0
	while True:
		operator = intcode_list[idx]

		if operator != 99:

			idx_in_1 = intcode_list[idx + 1]
			idx_in_2 = intcode_list[idx + 2]
			idx_out = intcode_list[idx + 3]
			in_1 = intcode_list[idx_in_1]
			in_2 = intcode_list[idx_in_2]

			if operator == 1:
				out = in_1 + in_2

			if operator == 2:
				out = in_1 * in_2
			
			intcode_list[idx_out] = out
			idx += 4

		else:
			break
	return intcode_list

if __name__ == "__main__":
	intcode_list = createIntcodeList("input.txt")
	mod_intcode_list = modifyIncodeList(intcode_list)
	# intcode_list = [1,1,1,4,99,5,6,0,99]
	post_intcode_list_one = intcodeProgramOne(mod_intcode_list)
	result_one = post_intcode_list_one[0]
	print(result_one)
	print("-------")
	instruction_list = makeInstructionList(intcode_list)
	result_two = intcodeProgramTwo(instruction_list)
	print(result_two)