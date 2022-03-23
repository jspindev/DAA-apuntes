

def update_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id

#despues de la primera iteracion 1-3
#components = [0, 3, 2, 3, 4, 5, 6, 7]
#despues de la segunda iteracion 4-5
#components = [0, 3, 2, 3, 5, 5, 6, 7]
#despues de la tercera iteracion
#components = [0,5, 2,



def kruskal(g):

    #components =  [0,1,2, ... 7]
    components =list(range(len(g)))
    count = len(g) - 1 #número de componentes conexas
    mst = 0

    list_edges = []
    for adjacents in g:
        for start, end, weight in adjacents:
            if start < end:
                list_edges.append((weight, start,end))
    list_edges.sort()

    i = 0
    while len(list_edges) > i and count > 1:
        weight, start, end = list_edges[i]
        if components[start] != components[end]:
            mst += weight
            count -= 1
            update_components(components, components[start], components[end])
        i +=1
    return mst

#g[1][1] -> (1,4,2)

g = [
    [],
    [(1,3,1), (1,4,2), (1,7,6)],
    [(2,5,2), (2,6,4), (2,7,7)],
    [(3,1,1), (3,4,3), (3,7,5)],
    [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
    [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
    [(6, 2, 4), (6, 4, 9)],
    [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)],
]

sol = kruskal(g)
print(sol)