def select_min(distances, visited):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index


def piguis(g, ini, fin):
    parent = [-1] * len(g)
    distances = [float('inf')] * len(g)
    visited = [False] * len(g)
    explorar = []

    distances[ini] = 0
    visited[ini] = True
    for start, end, weight in g[ini]:
        distances[end] = weight

    for i in range(2, len(g)):
        next_node = select_min(distances, visited)
        visited[next_node] = True

        for start, end, weight in g[next_node]:
            distances[end] = min(distances[end], distances[start] + weight)
            parent[end] = next_node


    print(distances[fin])
    print(parent)
    print(explorar)



g = []
n, m = map(int, input().strip().split())
for r in range(n):
    g.append([])
for i in range(m):
    a, b, c = map(int, input().strip().split())
    g[a].append([a, b, c])
    g[b].append([b, a, c])
ini, fin = map(int, input().strip().split())

piguis(g, ini, fin)