import re

with open("Advent of Code 2020.html", "r") as f:
	html = f.read()

main_list = html.split("Day")[:-1]

print(main_list)