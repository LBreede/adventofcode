import argparse
import json
from pathlib import Path
import os

parser = argparse.ArgumentParser(
	description="Create template py file from day number.")
parser.add_argument("day", type=int, help="Day")
args = parser.parse_args()

def create_file(day):
	with open("template.txt", "r") as f:
		raw_txt = f.read()

	with open("chapters.json", "r") as f:
		chapters = json.load(f)

	daypad = str(day).zfill(2)
	chapter = chapters[str(day)]
	formatted_txt = raw_txt.format(day=day, chapter=chapter, daypad=daypad)

	path = "/".join(str(Path().parent.absolute()).split("\\")[:-1])
	filename = "day" + daypad + ".py"
	path += "/" + filename
	
	if not os.path.isfile(path):
		with open(path, "w") as f:
			f.write(formatted_txt)
		print(f"Created {filename}")
	else:
		print(f"{filename} already exists.")

create_file(args.day)