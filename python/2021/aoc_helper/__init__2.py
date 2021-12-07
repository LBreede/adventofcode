import pathlib

import yaml
import requests

YEAR = 2021
URL = f"https://adventofcode.com/{YEAR}/day/{{day}}"

THIS_DIR = pathlib.Path(__file__).parent
INPUTS_FILE = THIS_DIR / "inputs.yaml"

TOKEN_FILE = THIS_DIR / ".token"

# TOKEN = {"session": TOKEN_FILE.read_text().strip()}


def day(d):
	""" DOC STRING

	"""
	d = str(d)

	inputs = yaml.full_load(INPUTS_FILE.read_text())

	# if d in inputs:
	# 	return inputs[d]

	response = requests.get(url=URL.format(day=d) + "/input" , cookies={"session": "lb"})
	# if not response.ok:
	# 	raise ValueError("Request failed.")
	print(response.status_code)

day(4)