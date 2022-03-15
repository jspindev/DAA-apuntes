from collections import deque


def bfsAux(g, visited, v, lista):
    q = deque()
    visited[v] = True
    lista.append(v)
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj]:
                visited[adj] = True
                lista.append(adj)
                q.append(adj)


def esConexo(g, numNodos):
    for v in range(0, len(g)):
        l = []
        visited = [False] * len(g)
        if len(g[v]) != 0:
            bfsAux(g, visited, v, l)
            return numNodos == len(l)
    return False


def copiarGrafo(gOrigen, gDestino):
    for v in range(0, len(gOrigen)):
        lista = []
        for adj in gOrigen[v]:
            lista.append(adj)
        gDestino.append(lista)


def borrarNodo(grafo, nodo):
    grafo[nodo] = []  # Ojo, borramos adyacentes, no hagais pop que destrozais la politica de indices
    for v in range(0, len(grafo)):
        if nodo in grafo[v]:
            grafo[v].remove(nodo)


def puntosArticulados(g, listaPuntosArticulados):
    for v in range(0, len(g)):
        gCopia = []
        copiarGrafo(g, gCopia)
        borrarNodo(gCopia, v)
        if not esConexo(gCopia, len(g) - 1):
            listaPuntosArticulados.append(v)


linea = input()
numNodos = int(linea.split(" ")[0])
numArcos = int(linea.split(" ")[1])
grafo = []
coste = []

for i in range(0, numNodos):
    grafo.append([])
    linea = input()
    coste.append(int(linea))

for i in range(0, numArcos):
    linea = input()
    origen = int(linea.split(" ")[0])
    destino = int(linea.split(" ")[1])
    grafo[origen].append(destino)
    grafo[destino].append(origen)

puntos = []
puntosArticulados(grafo, puntos)
costeTotal = 0
for punto in puntos:
    costeTotal += coste[punto]
print(costeTotal)
