
def dfsRec(g, visited, v):
    print(v, end=" ")
    visited[v] = True
    for adj in g[v]:
        if not visited[adj]:
            dfsRec(g, visited, adj)



def dfs(g):
    n = len(g)
    visited = [False] * n
    for v in range(1,n):
        if not visited[v]:
            dfsRec(g,visited,v)


#programa principal
g = [
    [], #en el cero se mete una lista vacia para igualar las posiciones 
    [2,4,8],
    [1,3,4],
    [2,4,5],
    [1,2,3,7],
    [3,6],
    [5,7],
    [4,6,9],
    [1,9],
    [7,8]
]
g1 = [
    [],
    [2,3],
    [1,3],
    [1,2],
    [5],
    [4]

]
dfs(g)
dfs(g1)
#complejidad en lista de nodos es o(n) y en matriz de adyacentes o(1)
#la complejidad depende de las aristas , nodos o las dos cosas