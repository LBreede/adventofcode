# --- Day 3: Spiral Memory ---

inputdata = 368078

i = 1
while True:
    corner = i * i
    if corner >= inputdata:
        break
    i += 2

side = i - 1
corners = [corner - side * x for x in range(4)]
dist_to_corner = min([abs(x - inputdata) for x in corners])
dist_to_center = side - dist_to_corner
print("Part 1:", dist_to_center)
