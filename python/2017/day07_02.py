import networkx as nx
import collections

with open("day07_example.txt") as fp:
    lines = fp.read().split("\n")

graph = nx.DiGraph()

# Build the graph of programs
for line in lines:
    name = line.split()[0]

    graph.add_node(name, weight=int(line.split()[1].strip("()")))

    if "->" in line:
        children = [n.strip() for n in line.split("->")[1].split(",")]

        for child in children:
            graph.add_edge(name, child)

# Topological sort to find the root of the tree
ordered = list(nx.topological_sort(graph))

print("PART 1:", ordered[0])

# Keep track of each node's total weight (itself + its children)
weights = {}

# Going backwards (starting from the leaves)
for node in reversed(ordered):
    # Start with this nodes own weight
    total = graph.nodes[node]["weight"]

    counts = collections.Counter(weights[child] for child in graph[node])
    unbalanced = None

    for child in graph[node]:
        # If this child's weight is different than others, we've found it
        if len(counts) > 1 and counts[weights[child]] == 1:
            unbalanced = child
            break

        # Otherwise add to the total weight
        val = weights[child]
        total += weights[child]

    if unbalanced:
        # Find the weight adjustment and the new weight of this node
        diff = weights[unbalanced] - val
        print("PART 2:", graph.nodes[unbalanced]["weight"] - diff)
        break

    # Store the total weight of the node
    weights[node] = total
