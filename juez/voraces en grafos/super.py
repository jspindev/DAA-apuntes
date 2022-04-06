def updateComponents(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(g):
    components = list(range(len(g))) # Guarda las componentes conexas
    count = len(g)
    mst = 0 # Valor de la funcion objetivo

    candidates = []
    for edgeList in g:
        for start, end, weight in edgeList:
            candidates.append((weight, end, start)) # Ponemos primero weight porque sort ordena el primero y empata los otros dos
    candidates.sort()

    while len(candidates) and count > 1:
        (weight, start, end) = candidates.pop(0)
        if components[start] != components[end]:
            count -= 1
            mst += weight
            updateComponents(components, components[start], components[end])
    return mst
#GRAFO
n, m = list(map(int, input().strip().split()))
g = []
for _ in range(n):
    g.append([])

for _ in range(m):
    origen, destino, peso = map(int, input().strip().split())
    g[origen].append((origen, destino, peso))

sol = kruskal(g)
print(sol)