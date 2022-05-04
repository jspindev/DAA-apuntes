def inicializarGrafo():
    # Lo vamos a representar como lista de adyacencia:
    grafo = {}
    grafo['n'] = 4
    grafo['adyacencia'] = [[1, 2, 3], [0], [0, 3], [0, 2]]
    return grafo


def inicializarSolucion(grafo):
    sol = [0] * grafo['n']
    return sol


def inicializarSolMejor(grafo):
    sol = list(range(1, grafo['n'] + 1))
    return sol


def esFactible(grafo, sol, nodo, color):
    factible = True
    adyacenciaNodo = grafo['adyacencia'][nodo][:]
    i = 0
    while factible and i < len(adyacenciaNodo):
        if adyacenciaNodo[i] < nodo:
            factible = color != sol[adyacenciaNodo[i]]
        i += 1
    return factible


def esMejor(sol1, sol2):
    return max(sol1) - min(sol1) < max(sol2) - min(sol2)


def esSolucion(sol, nodo):
    return nodo >= len(sol)


def coloreadoVA(grafo, m, sol, solMejor, nodo, sols):
    if esSolucion(sol, nodo):
        if esMejor(sol, solMejor):
            solMejor = sol[:]
        sols.append(sol[:])
    else:
        color = 1
        while color <= m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                solMejor = coloreadoVA(grafo, m, sol, solMejor, nodo + 1, sols)
            color += 1
            sol[nodo] = 0
    return solMejor


# Prog Ppal:
grafo = inicializarGrafo()
sol = inicializarSolucion(grafo)
solMejor = inicializarSolMejor(grafo)
m = 5  # Num de colores disponibles
nodo = 0  # Emepzamos coloreando el nodo 0
sols = []
solMejor = coloreadoVA(grafo, m, sol, solMejor, nodo, sols)
print('La mejor solución encontrada es:', solMejor)
print('Todas las soluciones encontradas son: ', sols)
