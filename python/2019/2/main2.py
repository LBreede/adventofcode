# --- Day 2: 1202 Program Alarm ---
import time

with open("inputdata.txt", "r") as f:
	intcode_programm = f.read().split(",")

intcode_programm = [int(intcode) for intcode in intcode_programm]
intcode_programm[1] = 12
intcode_programm[2] = 2

instruction_pointer = 0
while True:
	opcode = intcode_programm[instruction_pointer]
	if opcode == 1 or opcode == 2:
		noun = intcode_programm[instruction_pointer + 1]
		verb = intcode_programm[instruction_pointer + 2]
		if 100 * noun + verb == 19690720:
			print("100 * {} + {} = 1960720".format(noun, verb))
		instruction_pointer += 4
		print("Valid opcode!")
	elif opcode == 99:
		instruction_pointer += 1
		print("Halt and catch fire!")
		break
	else:
		print("ERROR! Illegal opcode detected!")



