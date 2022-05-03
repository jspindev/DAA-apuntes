def inicializarDatos():
    datos = {}
    datos['n'] = 4
    datos['w'] = 8
    datos['peso'] = [2,3,4,5]
    datos['valor'] = [3,5,6, 10]


def inicializarSolucion(datos):
    sol = {}
    sol['Objetos'] = [0] * datos['N']
    sol['Peso'] = 0
    sol['valor'] = 0

    return sol

def esSolucion(sol,datos):
    return sol['Peso'] + min(datos['Peso']) > datos['w']
#otra opcion peor
#def esSolucion(k,sol):
    #return k == len(sol['Objetos'] -1)
    #return k == datos['N']
def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol,datos):
        pass

#prog.principal
datos = inicializarDatos()
sol = inicializarSolucion(datos)
mejorsol = inicializarSolucion(datos)
k=0
mejorsol = mochilaVA(sol,mejorsol, datos, k)