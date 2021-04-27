import re

with open("Advent of Code 2020.html", "r") as f:
	line_list = f.read().split("\n")

line_list = line_list[107:132]

f = open("README.md", "w")
for line in line_list:
	line = re.split(r'class="calendar-day [0-9]">|class="calendar-day[0-9][0-9]">', line)
	start = ""
	if len(line) > 1:
		line = re.split(r'<span class="calendar-day"> [0-9]</span>|<span class="calendar-day">[0-9][0-9]</span>', line[1])
		start = line[0]
	f.write(start + "\n")	
f.close()