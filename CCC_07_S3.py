from sys import stdin

num_pairs = int(stdin.readline().replace('\n', ''))
graph = {}
inp = ""

for i in range(num_pairs):
    inp = stdin.readline().replace('\n', '').split()
    first = int(inp[0])
    second = int(inp[1])

    try:
        new_set = graph[first]
    except:
        new_set = set()
    new_set.add(second)
    graph[first] = new_set


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


while True:
    inp = stdin.readline().replace('\n', '').split()
    first = int(inp[0])
    second = int(inp[1])

    if first == 0 and second == 0:
        break

    first_paths_all = list(bfs_paths(graph, first, second))
    second_paths_all = list(bfs_paths(graph, second, first))

    print(first_paths_all, second_paths_all, bool(first_paths_all), bool(second_paths_all))

    if bool(first_paths_all):
        if bool(second_paths_all):
            first_path = shortest_path(graph, first, second)
            second_path = shortest_path(graph, second, first)
            if len(first_path) <= len(second_path):
                print(f'Yes {len(first_path)-2}')
            else:
                print(f'Yes {len(second_path)-2}')
        else:
            print('No')
    else:
        print('No')