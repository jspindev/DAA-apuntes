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
    for _ in range(len(g)):
        ruta.append([ini])#inciamos todos los caminos desde origen


    distances[ini] = 0
    visited[ini] = True
    for start, end, weight in g[ini]:
        distances[end] = weight
        ruta[end].append(end)

    for i in range(len(g)):
        next_node = select_min(distances, visited)
        visited[next_node] = True
        for start, end, weight in g[next_node]:
            #distances[end] = min(distances[end], distances[start] + weight)
           if distances[end] > distances[start] + weight: #cuando se actualice copiamos la ruta que llevamos a donde se termina y añadimos el fin
                distances[end] = distances[start] + weight
                ruta[end] = ruta[start].copy()
                ruta[end].append(end)
            #end1=distances[end] lo mismo de otra forma
            #distances[end] = min(distances[end], distances[start] + weight)
            #if end1 != distances[end]:
             #   ruta[end]=ruta[start].copy()
              #  ruta[end].append(end)


    print(distances[fin])
    print(*ruta[fin])



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