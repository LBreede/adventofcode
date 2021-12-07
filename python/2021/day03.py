# --- Day 3: Binary Diagnostic ---

import aoc_helper
from collections import Counter

def most_common_v1(lst):
	"""Great way to find return the most common item in a list. Unfortunately, 
	the result is unpredictable in case of a tie. This can be avoided by using
	the Counter function in the collections module.

	Args:
		lst (list): The list to seach in for the most common item.

	Returns:
		The most common item in the list.
	"""
	return max(set(lst), key=lst.count)

def most_common(lst):
	data = Counter(lst)
	return max(lst, key=data.get)

def least_common(lst):
	data = Counter(lst)
	return min(lst, key=data.get)

def calc_gamma(lst, reverse, most):
	g = ""
	for i in range(len(lst[0])):
		bits = []
		for x in lst:
			bits.append(x[i])

		bits.sort(reverse=reverse)
		if most:
			g += most_common(bits)
		else:
			g += least_common(bits)
	return g

def bitwise_complement(a):
	return "".join([str(1-int(x)) for x in a])

def mult_binary(a, b):
	return int(a, 2) * int(b, 2)

def calc_rating(lst, typ):
	if typ.lower() == "oxy":
		reverse = True
		most = True
	elif typ.lower() == "co2":
		reverse = False
		most = False
	else:
		raise ValueError(f"Unsupported type {typ}.")

	tmp_lst = []

	for i in range(len(lst[0])):
		
		if i > 0:
			lst = tmp_lst[:]
			tmp_lst = []

		gamma = calc_gamma(lst, reverse, most)
		for x in lst:
			if x[i] == gamma[i]:
				tmp_lst.append(x)

	return tmp_lst[0]

linelist = aoc_helper.load_input("day03_input.txt")

gamma = calc_gamma(linelist, True, True)
epsilon = bitwise_complement(gamma)

print(f"Part 1: {mult_binary(gamma, epsilon)}")

oxygen = calc_rating(linelist, "oxy")
cotwo = calc_rating(linelist, "co2")

print(f"Part 2: {mult_binary(oxygen, cotwo)}")