from random import randint

def select_min(shortest_edge,visited):
    vertex = None
    weight = float('inf')
    for i in range(1, len(shortest_edge)): #meter al nodo de menor peso que no hace un ciclo
        if not visited[i] and shortest_edge[i] < weight:
            vertex = i
            weight = shortest_edge[i]

    return vertex, weight

def prim(g):

    initial = randint(1, len(g)-1)
    visited = [False] * len(g)
    visited[initial] = True
    mst = 0

    shortest_edge = [float('inf')] * len(g)
    for strat, end, weight in g[initial]:
        shortest_edge[end] = weight

    for i in range (2, len(g)):
        (next_nodo, cost) = select_min(shortest_edge, visited)
        visited[next_nodo] = True
        mst += cost
        for strat , end , weight in g[next_nodo]:
            if not visited[end]:
                shortest_edge[end] = min (shortest_edge[end], weight)
    return mst


#grafo
g = [
    [], #copiar el de la traspa esta incompleto
    [(1,3,1), (1,4,2), (1,7,6)],
    [(2,5,2),(2,6,4),(2,7,7)],
    [(3,1,1),(3,4,3),(3,7,5)],
    [(4,1,2), (4,3,3), (4,5,1), (4,6,9)],
    [(5,2,2),(5,4,1),(5,7,8)],
    [(6,2,4),(6,4,9)],
    [(7,1,6),(7,2,7),(7,3,5),(7,5,8)],
]


print("minimun spanning tree", prim(g))