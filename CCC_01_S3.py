import sys

graph = {}
keys = set()

inp = ""

while True:
    inp = sys.stdin.readline().replace('\n', '')
    if inp != "**":
        first = inp[0]
        second = inp[1]
        keys.add(first)
        keys.add(second)

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

stringed_routes = []

for i in range(len(routes)):
    stringed_routes.append("".join(routes[i]))

count = 0

for key_a in keys:
    for key_b in keys:
        for route in stringed_routes:
            if not str(key_a) + str(key_b) in route:
                break
        else:
            print(key_a + key_b)
            count += 1

print(f"There are {count} disconnecting roads.")