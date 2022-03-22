

def dfsRec(g, visited, v,padre):
    visited[v] = True
    for adj in g[v]:
        if not visited[adj]:
           if  dfsRec(g, visited, adj,padre):
               return True
        elif padre != adj:
            return True

    return False


def dfs(g):
    n = len(g)
    visited = [False] * n
    for v in range(n):
        if not visited[v]:
           if  dfsRec(g,visited,v,-1):
               return True
    return False


g=[]
n,m = map(int, input().strip().split())
for _ in range (n):
    g.append([])

for _ in range (m):
    a,b =map(int, input().strip().split())
    g[a].append(b)

corruptos=dfs(g)

if not corruptos:
    print("INOCENTES")
else:
    print("CORRUPCION")

