def list_from_file(filename):
	with open (filename, "r") as fp:
		return [int(x) for x in fp.read().split("\n")]

def count_increased(lst):
	increased = 0
	for i in range(len(lst)):
		j = max(i - 1, 0)
		if lst[i] > lst[j]:
			increased += 1
	return increased

def combine_data(lst, window):
	new_lst = []
	for i in range(len(lst)-window+1):
		val = 0
		for j in range(window):
			val += lst[i+j]
		new_lst.append(val)
	return new_lst

def main():
	depthlist = list_from_file("input.txt")
	print("Part 1: {}".format(count_increased(depthlist)))
	new_depthlist = combine_data(depthlist, 3)
	print("Part 2: {}".format(count_increased(new_depthlist)))

if __name__ == '__main__':
	main()