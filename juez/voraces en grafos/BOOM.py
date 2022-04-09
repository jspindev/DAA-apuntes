
def select_min(distances, visited):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index

def dijkstra(g,t ,origin):
    distances = [float('inf')] * len(g)
    visited = [False] * len(g)

    distances[origin] = 0
    visited[origin] = True

    #si origin es el nodo 1
    #[(1,2,5), (1,4,3)]

    for start, end, weight in g[origin]: #añade los nodos que estan al lado su peso
        distances[end] = weight

    #distances = [inf, 0, 5, inf, 3, inf]
    for i in range(2, len(g)):
        next_node = select_min(distances, visited)
        visited[next_node] = True
        for start, end, weight in g[next_node]:
            distances[end] = min(distances[end], distances[start]+weight) #distancia anterior o pasando a traves de mi

    return distances



g = []
t = []
n,m = map(int,input().strip().split())
for _ in range(n):
    g.append([])
for tipo in map(int, input().strip().split()):
    t.append(tipo)

for _ in range(m):
    start, end, weight = map(int, input().strip().split())
    g[start].append((start, end, weight))
l = []

i = 0
taux = [] #tipos
for a in t:
    if a == i:
        taux.append(a)
        i+=1

for a in taux:
    solve = dijkstra(g,t,a)
    if a == t[a]:
        cm = min(solve)
    l.append(cm)
print(l)
#print(solve)