# --- Day 9: All in a Single Night ---
from itertools import permutations

ROUTE = "{start} -> {end}"
locations = set()
distances = {}

with open("input.txt") as fp:
    for line in fp:
        start, _, end, _, dist = line.rstrip().split(" ")
        locations.add(start)
        locations.add(end)
        distances[ROUTE.format(start=start, end=end)] = int(dist)
        distances[ROUTE.format(start=end, end=start)] = int(dist)

shortest_distance = float("inf")
longest_distance = 0

for route in list(permutations(locations, r=len(locations))):
    distance = 0
    for i in range(len(route) - 1):
        distance += distances[ROUTE.format(start=route[i], end=route[i + 1])]
    if distance < shortest_distance:
        shortest_distance = distance
    if distance > longest_distance:
        longest_distance = distance

print(shortest_distance)
print(longest_distance)
