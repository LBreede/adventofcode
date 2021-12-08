# --- Day 8: Seven Segment Search ---

import aoc_helper

SEGMENTCOUNT = {
	"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, 
	"5": 5, "6": 6, "7": 3, "8": 7, "9": 6
}

SEVEN_SEGMENT_DISPLAY = {
	"abcdef": 0, "bc": 1, "abdeg": 2, "abcdg": 3, "bcfg": 4,
	"acdfg": 5, "acdefg": 6, "abc": 7, "abcdefg": 8, "abcdfg": 9
}

def process_data(lst):
	new_lst = []
	for line in lst:
		entry_list = line.split(" ")
		del entry_list[10]
		# ["".join(sorted(x)) for x in entry_list]
		new_lst.append(entry_list)
	return new_lst

def segments(val):
	return SEGMENTCOUNT[str(val)]

def count_output_by_segment_num(data):
	count = 0
	for line in data:
		for val in line[-4:]:
			segs = len(val)
			if (segs == segments(1) or segs == segments(4) or
					segs == segments(7) or segs == segments(8)):
				count += 1
	return count

linelist = aoc_helper.load_input("day08_input.txt")
data = process_data(linelist)
result1 = count_output_by_segment_num(data)

print(f"Part 1: {result1}")

result2 = 0

for entry in data:

	one = ""
	four = ""
	seven = ""
	nine = ""
	eight = ""
	six = ""
	five = ""
	three = ""

	a = ""
	d = ""
	e = ""
	fg = ""
	c = ""
	b = ""
	g = ""
	f = ""

	i = 0

	while len(a+b+c+d+e+f) < 6:

		p = entry[i%14]

		# FIND THE EASY ONES
		if len(p) == 2: one = p
		if len(p) == 3: seven = p
		if len(p) == 4: four = p
		if len(p) == 7: eight = p

		# FIND SEGMENT A (TOP)
		if one != "" and seven != "" and a == "":
			a = seven
			for x in one:
				a = a.replace(x, "")

		# FIND NINE AND SEGMENT D (BOTTOM)
		if four != "" and a != "" and len(p) == 6 and nine == "" and d == "":
			temp_d = p
			for x in four + a:
				temp_d = temp_d.replace(x, "")
				if len(temp_d) == 1:
					d = temp_d
					nine = p
					break

		# FIND SEGMENT E (LOWER LEFT)
		if eight != "" and nine != "" and e == "":
			e = eight
			for x in nine:
				e = e.replace(x, "")

		# FIND SEGMENT FG (4 - 1)
		if four != "" and one != "" and fg == "":
			fg = four
			for x in one:
				fg = fg.replace(x, "")
			# fg = "".join(sorted(fg))

		# FIND 6 AND SEGMENT C
		if (a != "" and d != "" and e != "" and fg != "" and len(p) == 6 and
				six == "" and c == ""):
			temp_c = p
			for x in a + d + e + fg:
				temp_c = temp_c.replace(x, "")
				if len(temp_c) == 1:
					c = temp_c
					six = p
					break

		# FIND SEGMENT B
		if one != "" and c != "" and b == "":
			b = one.replace(c, "")

		# FIND 3 AND SEGMENT G
		reverse_c = a + b + c + d
		if len(reverse_c) == 4 and len(p) == 5 and three == "" and g == "":
			temp_g = p
			for x in reverse_c:
				temp_g = temp_g.replace(x, "")
				if len(temp_g) == 1:
					g = temp_g
					three = p

		# FIND SEGMENT F
		reverse_six = a + b + c + d + e + g
		if len(reverse_six) == 6 and eight != "" and f == "":
			f = eight
			for x in reverse_six:
				f = f.replace(x, "")

		i += 1

	dic = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g}
	number = ""

	for bad_pattern in entry[-4:]:
		good_pattern = ""
		for p in bad_pattern:
			good_pattern += list(dic.keys())[list(dic.values()).index(p)]
		good_pattern = "".join(sorted(good_pattern))
		
		number += str(SEVEN_SEGMENT_DISPLAY[good_pattern])

	number = int(number)
	result2 += number

print(f"Part 2: {result2}")

