from collections import deque


def bfsAux(g,visitados,v):
    q = deque()
    visitados[v] = True
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visitados[adj]:
                q.append(adj)
                visitados[adj] = True

def ciclos(g,visitados):
    for v in range(n):
        visitados[v]=True
        for adj in g[v]:
            if not visitados[adj]:
                bfsAux(g,visitados,v)
            if not False in visitados:
                conexo[v]=True


corrupto=False
g=[]
n,m = map(int, input().strip().split())
visitados=[False]*n
conexo=[False]*n
for _ in range (n):
    g.append([])

for _ in range (m):
    a,b =map(int, input().strip().split())
    g[a].append(b)

ciclos(g,visitados)

for i in conexo:
    if conexo[i]:
        corrupto=True

if not corrupto:
    print("INOCENTES")
else:
    print("CORRUPCION")