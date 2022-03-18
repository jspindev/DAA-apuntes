def topsort(g):
    search = []
    edges = []
    nodes = []
    n = len(g)
    for i in range(n):
        edges.append(0)
    for i in range(n):
        for j in g[i]:
            edges[j] = edges[j] + 1
    for i in range(n):
        if edges[i] == 0:
            nodes.append(i)
    while len(nodes) != 0:
        if len(nodes) == 1:
            source = nodes.pop(0)
        else:
            source = min(nodes)
            nodes.remove(source)

        search.append(source)
        for adj in g[source]:
            edges[adj] = edges[adj] - 1
            if edges[adj] == 0:
                nodes.append(adj)
    return search


n,m = map(int,input().strip().split())
g = []
for _ in range (n):
    g.append([])


for _ in range(m):
    a , b = map(int, input().strip().split())
    g[a].append(b)

sol =topsort(g)
sol.sort()
print(sol)