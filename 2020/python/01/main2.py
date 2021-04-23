# --- Day 1: Report Repair ---

def createExpenseReport(puzzle_input):
	expense_report = open(puzzle_input, "r").read().split("\n")
	expense_report = list(map(int, expense_report))
	return expense_report

def findPair(expense_report):
	a = -1
	b = -1
	for i in expense_report:
		for j in expense_report:
			if i + j == 2020:
				a = i
				b = j
				break
	return a * b

def findTriple(expense_report):
	a = -1
	b = -1
	c = -1
	for i in expense_report:
		for j in expense_report:
			for k in expense_report:
				if i + j + k == 2020:
					a = i
					b = j
					c = k
					break
	
	return a * b * c

if __name__ == "__main__":
	expense_report = createExpenseReport("input.txt")
	print(findPair(expense_report))
	print(findTriple(expense_report))