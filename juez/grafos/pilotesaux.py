
from collections import deque


npilotes=list(map(int, input().strip().split()))
#npilotes.append(in_put)

for i in range(0,npilotes[1]):
    pilotes=list(map(int,input().strip().split()))
    npilotes.append(pilotes)

def bfsAux(npilotes,visited,v):
    q = deque()
    #print(v, end=" ")
    visited[v]=True
    q.append(v)
    while q:
        aux=q.popleft()
        for adj in npilotes[aux]:
            if not visited[adj]:
                q.append(adj)
                visited[adj]=True
                #print(adj,end="")
        print(visited)


def bfs(npilotes):
    n=len(npilotes)
    visited=[False]*n
    for v in range(0,n):
        if not visited[v]:
            bfsAux(npilotes,visited,v)

