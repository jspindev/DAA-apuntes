import copy
from math import inf

def inicializarLaberinto(n):
    F = 10
    C = 10
    fila = [0]*n
    laberinto = []
    for i in range(F):
        laberinto.append(fila[:])
    paredes = [[0, 2], [0, 7], [1, 0], [1, 2], [1, 5], [1, 6], [1, 8], [2, 6], [2, 8], [3, 1], [3, 4], [3, 5], [3, 6], [4,2],[4,3],[4,7],[5,5],[5,7],[6,0],[6,3],[6,4],[6,7],[6,9],[7,1],[7,2],[7,8],[7,9],[8,2],[8,4],[8,5]]
    for i in range(len(paredes)):
        laberinto[paredes[i][0]] [paredes[i][1]] = inf

    return laberinto

def inicializarMejorSol(lab):
    mejorSol = copy.deepcopy(lab)
    mejorSol[len(lab)-1][len(lab[0]) -1] = inf
    return mejorSol

def esSolucion(lab, f, c):
    return (f == len(lab)-1) and (c == len(lab[0])-1)

def esMejor(sol1,sol2):
    n = len(sol1) -1
    m = len(sol1[[0]])-1

    return sol1[n][m] < sol2[n][m]

def esFactible(lab,f,c):
    if f >= 0 and f < len(lab) and c>=0 and c <len(lab[0]):
        return lab[f][c] == 0
    else:
        return False

def laberintoVA(lab, mejorSol, f, c, k):

    if esSolucion(lab, f, c):
        if esMejor(lab,mejorSol):
            mejorSol = copy.deepcopy(lab)
            fin = True
    else:
        fin = False
        desp = [[1,0], [1,0], [-1,0], [0, -1]]
        i=0
        while i < len(desp):
            newF= f +desp[i][0]
            newC = c +desp[i][1]
            if esFactible(lab,f+desp[i][0], c+ desp[i][1]):
                lab[f+desp[i][0]][c+desp[i][1]] = k
                #mejorSol = laberintoVA(lab, mejorSol, f+desp[i][0], c+ desp[i][1], k+1)
                mejorSol = laberintoVA(lab, mejorSol, newF,newC, k + 1)
                #lab[f+desp[i][0]][c+ desp[i][1]]
                lab[newF][newC] = 0
            i+=1

    return fin

def imprimir(laberinto):
    for f in range(len(laberinto)):
        for c in range(len(laberinto[0])):
            if laberinto[f][c] == inf:
                print('*', end='\t')
            else:
                if laberinto[f][c] == 0:
                    print(' ', end='\t')
                else:
                    print(laberinto[f][c], end='\t')
        print()
    print()


#prog principal



n = int(input())
laberinto = []
for i in range(n):
    laberinto.append(list(map(int, input().strip().split())))
paredes = []

cx = 0
cy = 0
for x in laberinto:
    for y in x:
        if x[y] == -1:
            paredes.append((cx,cy))
        cy += 1
    cx += 1
    cy =0

msol = inicializarMejorSol(laberinto)
f = 0
c = 0
k = 1
sol = laberintoVA(laberinto,msol,f,c,k+1)

#print(sol)
#imprimir(sol)
if sol:
    print("SI")
else:
    print("NO")
#print(laberinto)
#print(paredes)