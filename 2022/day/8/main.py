# --- Day 8: Treetop Tree House ---


def is_visible_at_dir(lst, val):
    return not any([True if x >= val else False for x in lst])


def distance_at_dir(lst, val):
    for i, x in enumerate(lst):
        if x >= val:
            return i + 1
    return len(lst)


with open("input.txt") as fp:
    trees = tuple(tuple(int(y) for y in x.rstrip()) for x in fp.readlines())

nvisible = maxdist = 0
for i, row in enumerate(trees):
    for j, tree in enumerate(row):

        up, dn = [], []
        for k, x in enumerate(trees):
            if k < i:
                up.insert(0, x[j])
            elif k > i:
                dn.append(x[j])

        lf = row[:j][::-1]
        rg = row[j + 1 :]

        is_visible_up = is_visible_at_dir(up, tree)
        is_visible_dn = is_visible_at_dir(dn, tree)
        is_visible_rg = is_visible_at_dir(rg, tree)
        is_visible_lf = is_visible_at_dir(lf, tree)
        is_visible = any((is_visible_up, is_visible_dn, is_visible_rg, is_visible_lf))
        nvisible += 1 if is_visible else 0

        dist_up = distance_at_dir(up, tree)
        dist_lf = distance_at_dir(lf, tree)
        dist_rg = distance_at_dir(rg, tree)
        dist_dn = distance_at_dir(dn, tree)
        dist = dist_up * dist_lf * dist_rg * dist_dn
        maxdist = dist if dist > maxdist else maxdist

print("Part 1:", nvisible, "\nPart 2:", maxdist)
