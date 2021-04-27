# --- Day 7: Handy Haversacks ---

with open("inputdata.txt", "r") as text:
    bags = text.read().split("\n")

all_bags = {}
for b in bags:
	parent, child = b.split(" bags contain ")
	if child != "no other bags.":
		children = child.split(", ")
		children = [" ".join(child.split(" ")[:3]) for child in children]
		advanced_children = []
		for c in children:
			cc = c.split(" ")
			amt = int(cc[0])
			clr = " ".join(cc[1:3])
			advanced_children.append([amt, clr])
	else:
		children = []
		advanced_children = [[]]
	all_bags[parent] = advanced_children



count = 0
for k, v in all_bags.items():
	queue = v.copy()

	temp_count = 0
	for bag in queue:
		if len(bag) > 0:
			if bag[1] == "shiny gold":
				count += 1
				break
			else:
				for sub_bag in all_bags[bag[1]]:
					queue.append(sub_bag)
print(count)
"""
super_count = 1
for b in all_bags["shiny gold"]:
	if len(b) > 0:
		super_count += b[0]
print(super_count)
"""
"""
for k, v in all_bags.items():
	print("{} -> {}".format(k, v))
"""
