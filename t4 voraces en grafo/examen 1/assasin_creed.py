#la mínima cantidad de monedas del juego que se debe utilizar para llegar de x a y

def select_min(distances, visited):
    min_dist = float('inf')
    index = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            min_dist = distances[i]
            index = i
    return index

def assasin(g, origin, cantidad):
    distances = [float('inf')] * len(g)
    visited = [False] * len(g)

    for i in cantidad:
        visited[i]=True

    distances[origin] = 0
    visited[origin] = True #nodo donde yo voy a medir la distancia lo marcamos visitado



    for start, end, weight in g[origin]: #dado grafo calculo los que estan al lado del uno
        distances[end] = weight

    for i in range(2, len(g)):  #del 2 a la longitud del grafo, como ya he calculado el 1 de posicion calculo el n-1, de los n nodos revisa n-1
        next_node = select_min(distances, visited)   #de todos sin visitar cual es el mas proximo, el menor
        visited[next_node] = True #el que elegimos los marcamos como viditado
        for start, end, weight in g[next_node]:  #para cada uno biscamos cual es menor la distancia previa o la siguiente
            distances[end] = min(distances[end], distances[start]+weight) #aqui te dice tamb lo de arriba, decimos cuesta menos ir directamente o cuesta menos ir a traves de otro

    return distances



n,m=map(int, input().strip().split())

list=[]
for i in range(n):
    list.append([])

for i in range(m):
    o,d,m = map(int, input().strip().split())
    list[o].append((o,d, m))
    list[d].append((d,o,m))

r=int(input())
cantidad=[]
for i in map(int, input().strip().split()):
    cantidad.append(i)

x, y = map(int, input().strip().split())

for j in cantidad:
    list[j] = []

camino=assasin(list, x, cantidad)

if camino[y] == float('inf'):
    print('IMPOSIBLE')
else:
    print(camino[y])