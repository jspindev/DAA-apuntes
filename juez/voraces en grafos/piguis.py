


def select_min(distances, visited):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index

def dijkstra(g, origin, destino):
    distances = [float('inf')] * len(g)
    visited = [False] * len(g)

    distances[origin] = 0
    visited[origin] = True

    final_weight = 0
    for start, end, weight in g[origin]:
        distances[end] = weight


    for i in range(2, len(g)):
        next_node = select_min(distances, visited)
        visited[next_node] = True
        for start, end, weight in g[next_node]:
            distances[end] = min(distances[end], distances[start]+weight) #distancia anterior o pasando a traves de mi
            final_weight += weight
    print(final_weight)
    return distances

n, m = map(int, input().strip().split())
g = []
for _ in range(m):
    g.append([])
for _ in range(m):
    start, end, weight = map(int,input().strip().split())
    g[start].append((start, end, weight))
origen, destino = map(int, input().strip().split())


sol = dijkstra(g, origen, destino)
print(sol)