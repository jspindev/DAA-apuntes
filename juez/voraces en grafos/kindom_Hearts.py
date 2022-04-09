
def update_components(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id


def kruskal(g):

    components = list(range(len(g)))
    count = len(g) - 1
    mst = 0
    list_edges = []

    for adjacents in g:
       for  start, end, weight in adjacents:
        if start < end:
            list_edges.append((weight, start, end))
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






g = []

n, m = map(int,input().strip().split())

for i in range(n+1):
    g.append([])
for _ in range(m):
    start, end, weight = map(int, input().strip().split())
    g[start].append((start, end, weight))


sol = kruskal(g)
print(sol)
