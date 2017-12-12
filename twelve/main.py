from inn import inn
data = inn("input")

from collections import defaultdict
from collections import deque
dd = defaultdict(list)

for line in data:
    line = line.strip()
    cells = line.split(" ")
    name = cells[0]
    print(line, "name:", name)
    neighbs = " ".join(cells[2:]).split(", ")
    dd[name] = neighbs

def exhaust_group(first):
    visited = defaultdict(lambda: False)
    q = deque()
    q.append(first)
    while len(q) > 0:
        name = q.popleft()
        visited[name] = True
        for node in dd[name]:
            if not visited[node]:
                q.append(node)
    print(first, "had", len(visited))
    return set(visited.keys())

all_nodes = set(dd.keys())
remaining_nodes = all_nodes
groups = 0
while len(remaining_nodes) > 0:
    groups += 1
    node = remaining_nodes.pop()
    visited = exhaust_group(node)
    print("REMAINING:", len(remaining_nodes), remaining_nodes)
    remaining_nodes = remaining_nodes.difference(visited)
print("GROUPS:", groups)

#visited_nodes = set(visited.keys())
#unvisited = all_nodes.difference(visited_nodes)
#print("ALL:", len(all_nodes))
#print("VISITED:", len(visited_nodes))
#print("UNVISITED", len(unvisited))
