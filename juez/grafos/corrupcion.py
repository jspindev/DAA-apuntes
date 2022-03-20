from collections import deque


def bfsAux(g,visited,v):
    inicial=v
    q = deque()
    ciclo = False
    visited[v]=True
    q.append(v)
    while q:
        aux=q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True
                if inicial == adj:
                    ciclo=True
            elif visited[adj]:
                ciclo = True
    return ciclo

def ciclos(g):
    sc=False
    n=len(g)
    visited=[False]*n
    solci=[False] * n
    for v in range (n):
        if not visited[v]:
            sc =bfsAux(g,visited,v)
        solci[v] = sc
    return solci



g=[]
n,m = map(int, input().strip().split())
for _ in range (n):
    g.append([])

for _ in range (m):
    a,b =map(int, input().strip().split())
    g[a].append(b)

corrupto=False
sol = ciclos(g)

for i in sol:
    if sol[i]:
        corrupto=True

if not corrupto:
    print("INOCENTES")
else:
    print("CORRUPTOS")