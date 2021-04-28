# --- Day 2: 1202 Program Alarm ---

with open("inputdata.txt", "r") as f:
	intcode_programm = f.read().split(",")

intcode_programm = [int(intcode) for intcode in intcode_programm]
intcode_programm[1] = 12
intcode_programm[2] = 2

"""
intcode_programm = [1,9,10,3,2,3,11,0,99,30,40,50]
intcode_programm = [1,0,0,0,99]
intcode_programm = [2,3,0,3,99]
intcode_programm = [2,4,4,5,99,0]
intcode_programm = [1,1,1,4,99,5,6,0,99]
"""

instruction_pointer = 0
while True:
	opcode = intcode_programm[instruction_pointer]
	if opcode != 99:
		idx_in_1 = intcode_programm[instruction_pointer + 1]
		idx_in_2 = intcode_programm[instruction_pointer + 2]
		idx_out = intcode_programm[instruction_pointer + 3]
		in_1 = intcode_programm[idx_in_1]
		in_2 = intcode_programm[idx_in_2]
		if opcode == 1:
			out = in_1 + in_2
		elif opcode == 2:
			out = in_1 * in_2

		intcode_programm[idx_out] = out

		instruction_pointer += 4
	else:
		break

answer = intcode_programm[0]
print(answer)



