
def select_min(distances, visited):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index

def dijkstra(g,origin):
    distances = [float('inf')] * len(g)
    visited = [False] * len(g)

    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight

    for i in range(2, len(g)):
        next_node = select_min(distances, visited)
        visited[next_node] = True
        for start, end, weight in g[next_node]:
            distances[end] = min(distances[end], distances[start]+weight) #distancia anterior o pasando a traves de mi

    return distances



g = []
n,m = map(int,input().strip().split())
for _ in range(n):
    g.append([])

ctipo =(input().strip().split())
tipo=[int(x) for x in ctipo]
t = []
for nt in range(max(tipo)+1):
    t.append([])
for c in range(len(ctipo)):
    t[tipo[c]].append(c)


for _ in range(m):
    start, end, weight = map(int, input().strip().split())
    g[start].append((start,end,weight))
    g[end].append((end,start,weight))

aux = []
lsol = []
for i in range(len(t)):
    for e in t[i]:
        solve = dijkstra(g,e)
        for s in t[i]:
            if solve[s] != 0:
                aux.append(solve[s])
    sol = min(aux)
    lsol.append(sol)
    aux.clear()

print(*lsol)