import copy


def inicializarSolucion(grafo):
    sol = [0] * grafo['n']
    return sol

def esSolucion(nodo, grafo):
    return nodo not in grafo['adyacencia'][nodo][0] #and not in grafo['adyacencia'][nodo][1]

def esFactible(grafo, sol, nodo, color):
    factible = True
    adynodo = grafo['adyacencia'][nodo]
    i = 0
    #while factible and i < len(ady):
    return True

def sudoku(grafo, m,sol, nodo):
    if esSolucion(nodo, grafo):
        esSol = True
    else:
        esSol = False
        color = 1
        while not esSol and color <= m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                [sol, esSol] = sudoku(grafo, m, sol, nodo+1)
                if not esSol:
                    sol[nodo] = 0
            color += 1
    return sol, esSol


sudoku = []

fila = []
for f in range(9):
    fila.append(list(map(int, input().strip().split())))
columna = []
for i in range(9):
    columna.append([])
    for j in range(9):
        columna[i].append(fila[j][i])
cuadrante = []
for c in range(9):
    if c < 6:
        cuadrante[c].append(fila[c][c],fila[c][c+1],fila[c][c+2])


grafo = {}
grafo['n'] = 9
grafo['Fila'] = []
grafo['Columna'] = []
grafo['Cuadrante'] = cuadrante
for n in range(9):
    grafo['Fila'].append((fila[n]))
    grafo['Columna'].append(columna[n])

print(cuadrante)

#sol = inicializarSolucion(grafo)
sol = copy.deepcopy(fila)
nodo = 1
m=9
#sudoku(grafo, m , sol,nodo)

#print(fila)
#print(columna)
