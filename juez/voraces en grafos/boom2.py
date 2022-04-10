def select_min(distance, visited):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distance)):
        if not visited[i] and distance[i] < min_dist:
            min_dist = distance[i]
            index = i

    return index


def dijkstra(g, origin):
    distance = [float('inf')] * len(g)
    visited = [False] * len(g)

    distance[origin] = 0
    visited[origin] = True

    for star, end, weight in g[origin]:
        distance[end] = weight

    for i in range(2, len(g)):
        next_node = select_min(distance, visited)
        visited[next_node] = True
        for start, end, weight in g[next_node]:
            distance[end] = min(distance[end], distance[start] + weight)

    return distance


g = []
n, m = map(int, input().strip().split())
for y in range(n):
    g.append([])

s = []
c = (input().strip().split())
b = [int(x) for x in c]
for x in range(max(b) + 1):
    s.append([])
for d in range(len(b)):
    s[b[d]].append(d)

for y in range(m):
    i, j, w = map(int, input().strip().split())
    g[i].append([i, j, w])
    g[j].append([j, i, w])

a1 = []
for y in range(len(s)):
    for f in s[y]:
        r = dijkstra(g, f)
        for p in s[y]:
            if r[p] != 0:
                a1.append(r[p])
    sol = min(a1)
    print(sol, end=" ")
    a1.clear()
