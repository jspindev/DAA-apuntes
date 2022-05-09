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

grafo = {}
grafo['n'] = 9
grafo['adyacenciaFila'] = []
grafo['adyacenciaColumna'] = []
for n in range(9):
    grafo['adyacenciaFila'].append((fila[n]))
    grafo['adyacenciaColumna'].append(columna[n])

#sol = inicializarSolucion(grafo)
sol = copy.deepcopy(fila)
nodo = 1
m=9
sudoku(grafo, m , sol,nodo)

#print(fila)
#print(columna)
