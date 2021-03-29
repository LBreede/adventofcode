# --- Day 1: Inverse Captcha ---

f = open("input.txt", "r").read()
# f = "91212129"

def solveCapcha(input, part):
	digit_amount = len(f)
	value = []

	for x in range(digit_amount):
		curr_digit = f[x]

		if part == 1:
			offset = x + 1
		elif part == 2:
			offset = x + digit_amount / 2

		next_digit = f[offset % digit_amount]

		if curr_digit == next_digit:
			value.append(int(curr_digit))

	return sum(value)


print solveCapcha("input.txt", 1)
print solveCapcha("input.txt", 2)