def eulerian_tour_undirected(graph):
    P = [] # resulting tour
    Q = [0] # vertices to be explored, start at 0
    R = [] # path from start node
    next_ = [0] * len(graph) # initialize next_ to 0 for each node
    seen = [set() for _ in graph] # mark backward arcs
    while Q:
        start = Q.pop() # explore a cycle from start node
        node = start # current node on cycle
        while next_[node] < len(graph[node]): # visit all allowable arcs
            neighbor = graph[node][next_[node]] # traverse an arc
            next_[node] += 1 # mark arc traversed
            if neighbor not in seen[node]: # not yet traversed
                seen[neighbor].add(node) # mark backward arc
                R.append(neighbor) # append to path from start
                node = neighbor # move on
        while R:
            Q.append(R.pop()) # add to Q the discovered cycle R
        P.append(start) # resulting path P is extended
    return P

npersonas, nrelaciones =map(int, input().strip().split())


relaciones = {}
keys = []
for _ in range(npersonas):
    keys.append([])
for _ in range(nrelaciones):
    a, b = map(int, input().strip().split())
    keys.append(a)
    relaciones[keys[a]].append(b)

sol = eulerian_tour_undirected(relaciones)

if len(sol)> 0:
    print("CORRUPTOS")
else:
    print("INOCENTES")