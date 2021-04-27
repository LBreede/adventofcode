# --- Day 5: Doesn"t He Have Intern-Elves For This? ---

import re

with open("inputdata.txt", "r") as f:
    string_list = f.read().split("\n")

# most regular expression are inspired or copied in it"s entirety from 
# u/technojamin on the adventofcode subreddit.

count_part_1 = count_part_2 = 0
for string in string_list:
	if (re.search(r"([aeiou].*){3,}", string) and
		re.search(r"(.)\1", string) and
		not re.search(r"ab|cd|pq|xy", string)):
		count_part_1 += 1
	if (re.search(r"(..).*\1", string) and
		re.search(r"(.).\1", string)):
		count_part_2 += 1

print(count_part_1)
print(count_part_2)


# - REGEX USED FOR FUTURE REFERENCE -

"([aeiou].*){3,}"	# AT LEAST 3 VOWELS e.g.: xazegov
"(.)\1"				# ANY DOUBLE CHARACTER e.g.: abcdde
"ab|cd|pq|xq"		# ANY OF THESE PAIRS

"(..).*\1"			# ANY DOUBLES THAT APPEAR AT LEAST TWICE e.g.: aabcdefgaa
"(.).\1"			# ANY CHARACTER TWICE WITH ANOTHER CHARACTER IN BETWEEN e.g.: abcdefeghi (efe)
