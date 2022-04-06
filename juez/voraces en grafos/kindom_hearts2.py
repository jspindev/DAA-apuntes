from random import randint


def select_min(shortest_edges, visited):
    vertex = None
    weight = float('inf')

    #shortest_edges = [inf, inf, inf, 1, 2, inf, inf, 6]
    for i in range(1, len(shortest_edges)):
        if not visited[i] and shortest_edges[i] < weight:
            vertex = i
            weight = shortest_edges[i]
    return vertex, weight




def prim(g):
    initial = randint(1, len(g) -1)
    visited = [False] * len(g)

    mst = 0
    visited[initial] = True
    shortest_edges = [float('inf')] * len(g)
    #supongamos que intial = 1
    # shortest_edges =  [inf, inf, ..., inf]
    #g[initial] =  [(1,3,1), (1,4,2), (1,7,6)]
    #shortest_edges = [inf, inf, inf, 1, 2, inf, inf, 6]
    start, end, weight = g[initial]
    shortest_edges[end] = weight

    for i in range (2, len(g)):
        next_node, cost  = select_min(shortest_edges, visited)
        if cost < float('inf'):
            mst += cost
            visited[next_node] = True
            #para el nodo 3,  [(3,1,1), (3,4,3), (3,7,5)]
            edge = g[next_node]
            start, end, weight = edge
                # shortest_edges = [inf, inf, inf, 1, 2, inf, inf, 5]
            if not visited[end]:
                shortest_edges[end] = min(shortest_edges[end], weight)
    return mst




g = []

n, m = input().strip().split()
m = int(m)
for _ in range(m):
    start, end, weight = map(int, input().strip().split())
    g.append((start, end, weight))


sol = prim(g)

print(sol)