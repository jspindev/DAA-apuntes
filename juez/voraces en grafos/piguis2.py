def select_min(distances, visited):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index


def dijkstra(g, ini, fin):

    distances = [float('inf')] * len(g)
    visited = [False] * len(g)
    ruta = []
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
            explorar.append(end)
    cont = 0
    for  a in explorar:
        if a != fin and cont <1:
            ruta.append(a)
        else:
            cont+=1
    ruta.append(fin)

    print(distances[fin])
    print(ruta)



g = []
n, m = map(int, input().strip().split())
for _ in range(n):
    g.append([])
for _ in range(m):
    start, end, weight = map(int, input().strip().split())
    g[start].append([start, end, weight])
    g[end].append([end, start, weight])
ini, fin = map(int, input().strip().split())

dijkstra(g, ini, fin)