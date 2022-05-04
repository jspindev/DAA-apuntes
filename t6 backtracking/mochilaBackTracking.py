import copy


def inicializarDatos():
    datos = {}
    datos['n'] = 4
    datos['w'] = 8
    datos['peso'] = [2,3,4,5]
    datos['valor'] = [3,5,6, 10]


def inicializarSolucion(datos):
    sol = {}
    sol['Objetos'] = [0] * datos['n']
    sol['Peso'] = 0
    sol['valor'] = 0

    return sol

def esSolucion(sol,datos):
    return sol['Peso'] + min(datos['Peso']) > datos['w']
#otra opcion peor
#def esSolucion(k,sol):
    #return k == len(sol['Objetos'] -1)
    #return k == datos['N']

def mejor(sol1, sol2):
    if sol1['valor'] > sol2['valor']:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor

def esFactible(sol, datos, i):
    return sol['peso'] + datos['peso'][i] <= datos['w']

def asignar(sol, i, datos):
    sol['objetos'][i] = 1
    sol['valor'] += datos['valor'][i]
    sol['peso'] += datos['peso'][i]

    return sol


def borrar(sol, i, datos):
    sol['objetos'][i] = 0
    sol['valor'] -= datos['valor'][i]
    sol['peso'] -= datos['peso'][i]

def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol,datos):
        mejorSol = mejor(mejorSol, sol)
    else:
        for i in range(k,datos['n']):
            if esFactible(sol,datos,i):
                sol = asignar(sol, i, datos)
                mejorSol = mochilaVA(sol, mejorSol, datos, i)
                sol = borrar(sol, i, datos)
    return mejorSol

#prog.principal
datos = inicializarDatos()
sol = inicializarSolucion(datos)
mejorsol = inicializarSolucion(datos)
k=0
mejorsol = mochilaVA(sol,mejorsol, datos, k)