# --- Day 5: Doesn't He Have Intern-Elves For This? ---

import re

def hasVowels(string, amount):
	c = len(re.findall("[aeiou]", string)) >= amount
	return c

def hasTwoConsecutiveLetters(string):
	regexp = re.compile(r"([a-z])\1")
	if re.search(regexp, string):
		c = True
	else:
		c = False
	return c

def hasForbiddenStrings(string, forbidden):
	regexp = "|".join(forbidden)
	c = len(re.findall(regexp, string)) == 0
	return c

def hasTwoConsecutiveLetterPairs(string):
	regexp = re.compile(r"([a-z][a-z])\1")
	if re.search(regexp, string):
		c = True
	else:
		c = False
	return c

def isNicePartOne(string):
	forbidden = ["ab", "cd", "pq", "xy"]

	nice = 0

	for L in string:
		cond1 = hasVowels(L, 3)
		cond2 = hasTwoConsecutiveLetters(L)
		cond3 = hasForbiddenStrings(L, forbidden)
		
		if cond1 and cond2 and cond3:
			nice += 1

	return nice

def isNicePartTwo(string):

	nice = 0

	for L in string:
		cond1 = hasTwoConsecutiveLetterPairs(string)
		cond2 = True

		if cond1 and cond2:
			nice += 1

		return nice

lines = [line.rstrip('\r\n') for line in open("input.txt")]
# lines = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
lines = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]


for L in lines:
	x = re.findall(r"(..){2}", L)
	print(x)

# print(isNicePartOne(lines))
# print(isNicePartTwo(lines))