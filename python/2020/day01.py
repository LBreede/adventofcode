# --- Day 1: Report Repair ---

from aoc_helper import load_input

def find_two(lst):
	for a in lst:
		for b in lst:
			if a != b and a + b == 2020:
				return a * b

def find_three(lst):
	for a in lst:
		for b in lst:
			for c in lst:
				if a != b and b != c and c != a and a + b + c == 2020:
					return a * b * c

linelist = load_input("day01_input.txt")
linelist = list(map(int, linelist))

print(find_two(linelist))
print(find_three(linelist))