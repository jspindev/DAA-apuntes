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