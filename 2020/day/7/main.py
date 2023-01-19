# --- Day 7: Handy Haversacks ---

VAULT = "/Users/lennartbreede/Library/CloudStorage/Dropbox/Obsidian/HandyHaversacks/"


def md_dump(title, content, safety=False):
    path = VAULT + title + ".md"
    text = f"# {title}\n"
    for x in content:
        if not x:
            break
        for i in range(x[0]):
            text += f"- [[{x[1]}]]\n"

    if safety:
        with open(path, "w") as fp:
            fp.write(text)


all_bags = {}
with open("input.txt") as fp:
    for b in fp:
        parent, child = b.rstrip().split(" bags contain ")
        if child != "no other bags.":
            children = [" ".join(c.split(" ")[:3]) for c in child.split(", ")]
            advanced_children = []
            for child in children:
                n, *color = [int(x) if x.isnumeric() else x for x in child.split(" ")]
                color = " ".join(color)
                advanced_children.append([n, color])
        else:
            advanced_children = [[]]
        all_bags[parent] = advanced_children

for k, v in all_bags.items():
    md_dump(k, v)

# count = 0
# for k, v in all_bags.items():
#     queue = v.copy()
#     print(k, v)
#     temp_count = 0
#     for bag in queue:
#         if len(bag):
#             if bag[1] == "shiny gold":
#                 count += 1
#                 break
#             else:
#                 for sub_bag in all_bags[bag[1]]:
#                     queue.append(sub_bag)
# print(count)
