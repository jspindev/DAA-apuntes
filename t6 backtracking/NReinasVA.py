
def imprimirSolucion(solucion):
    n = len(solucion)
    tablero = inicializarTablero(n)
    for fila in range(n):
        tablero[fila][solucion[fila]] = 1
        for columna in range(n):
            print(tablero[fila][columna], ' ', end='')
        print()




def inicializarTablero(N):
    fila = [0]*N
    tablero = []
    for i in range(N):
        tablero.append(fila[:])
    return tablero


def esFactible(solucion, fila, columna):
    factible = True
    i = 1
    while factible and i <= fila:
        factibleColumna = (solucion[fila-i] != columna)
        factibleDiag1 = (solucion[fila-i] != columna+i)
        factibleDiag2 = (solucion[fila-i] != columna -1)
        factible = factibleColumna and factibleDiag1 and factibleDiag2
        i +=1

    return factible


def inicializarSolucion(N):
    return [-1] * N

def esSolucion(sol, fila):
    return fila == len(sol)

def NReinasVA(solucion, fila):
    if esSolucion(solucion, fila):
        exito = True
    else:
        exito = False
        columna = 0
        while not exito and columna < len(solucion):
            if esFactible(solucion, fila, columna):
                solucion[fila] = columna
                (solucion, exito) = NReinasVA(solucion, fila + 1)
                if not exito:
                    solucion[fila]= -1
            columna += 1
    return (solucion, exito)


#prog principal
N=4
solucion = inicializarSolucion(N)
fila = 0
(solucion, exito) = NReinasVA(solucion, fila)

if exito:
    imprimirSolucion(solucion)
else:
    print('El problema no tiene solucion')
