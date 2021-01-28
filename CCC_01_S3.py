import sys

# graph = {'A': set(['B', 'C']),
# 'B': set(['A', 'D', 'E']),
# 'C': set(['A', 'F']),
# 'D': set(['B']),
# 'E': set(['B', 'F']),
# 'F': set(['C', 'E'])}

graph = {}

inp = ""

while True:
    inp = sys.stdin.readline().replace('\n', '')
    if inp != "**":
        first = inp[0]
        second = inp[1]

        try:
            new_set = graph[first]
        except:
            new_set = set()
        new_set.add(second)
        graph[first] = new_set

        try:
            new_set = graph[second]
        except:
            new_set = set()
        new_set.add(first)
        graph[second] = new_set
    else:
        break

# bfs_paths() - lists all possible paths from start to end point, returns shortest path first

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

routes = list(bfs_paths(graph, 'A', 'B'))

print(routes) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

for i in range(len(routes)):
    temp = "".join(routes[i])
    print(temp)

