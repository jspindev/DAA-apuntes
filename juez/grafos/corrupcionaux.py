def eulerian_tour_directed(graph):
    P = [] # resulting tour
    Q = [0] # vertices to be explored, start at 0
    R = [] # path from start node
    next_ = [0] * len(graph) # initialize next_ to 0 for each node
    while Q:
        start = Q.pop() # explore a cycle from start node
        node = start # current node on cycle
        while next_[node] < len(graph[node]): # visit all allowable arcs
            neighbor = graph[node][next_[node]] # traverse an arc
            next_[node] += 1 # mark arc traversed

            R.append(neighbor) # append to path from start
            node = neighbor # move on
        while R:
            Q.append(R.pop()) # add to Q the discovered cycle R
        P.append(start) # resulting path P is extended
    return P
ciclo = []
g=[]
n,m = map(int, input().strip().split())
for _ in range (n):
    g.append([])

for _ in range (m):
    a,b =map(int, input().strip().split())
    g[a].append(b)

#corrupto = ciclos(g)
ciclo = eulerian_tour_directed(g)

print(ciclo)
print(len(ciclo))
if len(ciclo) < n:
    print("CORRUPTO")
else:
    print("INOCENTES")
#if not corrupto:
 #   print("INOCENTES")
#else:
 #   print("CORRUPTOS")