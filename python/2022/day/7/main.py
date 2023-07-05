# --- Day 7: No Space Left On Device ---

from anytree import Node, RenderTree
import re

curr_dir = None
with open("input.txt") as fp:
    for line in fp:
        match_cd = re.search(r"\$ cd (.+)", line)
        match_file = re.search(r"(\d+) (.+)", line)
        if match_cd:
            arg = match_cd.group(1)
            name = f"{arg} (dir)"
            curr_dir = Node(name, parent=curr_dir) if arg != ".." else curr_dir.parent
        elif match_file:
            size, name = match_file.groups()
            name = f"{name} (file, size={size})"
            Node(name, parent=curr_dir)

for pre, _, node in RenderTree(curr_dir.root):
    print(pre + node.name)

sizes = {}
for leaf in curr_dir.root.leaves:
    size = int(leaf.name.split("=")[-1][:-1])
    for a in leaf.ancestors:
        path = "/".join([x.name for x in a.path])
        sizes[path] = size if path not in sizes else sizes[path] + size

disk_space_used = 70_000_000 - sizes["/ (dir)"]
disk_space_to_clean = 30_000_000 - disk_space_used

part_one = sum([x for x in sizes.values() if x <= 100_000])
part_two = min([x for x in sizes.values() if x >= disk_space_to_clean])

print("\nPart 1:", part_one, "\nPart 2:", part_two)
