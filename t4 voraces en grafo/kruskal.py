#{1},{2},{3},{4},{5},{6},{7}
#components[1]=1
#components[3] = 3

#{1},{2},{3},{4},{5},{6},{7}
#components[1] = 3
#components[3] = 3

def updateComponents(components, old_id, new_id):
    for i in range(components):
        if components[i] == old_id:
            components[i] = new_id
    return
def kruskal(graph):
    components = list (range(len(graph)))
    count = len(graph) - 1
    mst = 0 #minimum no se que

    #inicio de algoritmo voraz
    candidates = [] #lista vacia
    for edgeList in graph: #ahora lo añadimos con weight primero para ordenarlo ahora con el sort
        for start, end , weight in edgeList:
            if start < end:
                candidates.append((weight, start , end))

    #ordenar los elementos
    candidates.sort()

    i=0
    while len(candidates) > i and count > 1:
        (weight, start, end) = candidates[i]
        if components[start] != components[end]:
            count -= 1
            mst += weight
            updateComponents(components, components[start], components[end])
        i+=1
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


print("minimun spanning tree", kruskal(g))