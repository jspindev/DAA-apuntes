def esFactible(tablero, nueva_x, nueva_y):
    if (nueva_x>=len(tablero)) or (nueva_x<0) or (nueva_y>=len(tablero) or nueva_y<0):
        return False
    if (tablero[nueva_x][nueva_y]==-1) or (tablero[nueva_x][nueva_y]=='E'):
        return False
    return True

def estacompleto(tablero):
    relleno= True
    i=0
    while relleno and i<len(tablero):
        if tablero[i].__contains__(0):
            return False
        i +=1
    return True


def BT(tablero, pos_actual_x, pos_actual_y, mov_rel_x, mov_rel_y):
    exito=False
    intento=0
    while intento<=3 and not exito:
        nueva_x=pos_actual_x + mov_rel_x[intento]
        nueva_y=pos_actual_y + mov_rel_y[intento]
        if esFactible(tablero,nueva_x,nueva_y):
            if(tablero[nueva_x][nueva_y]=='S')and(estacompleto(tablero)): # es solucion
                exito=True
            else:
                tablero[nueva_x][nueva_y]=-1
                exito=BT(tablero,nueva_x,nueva_y,mov_rel_x,mov_rel_y)

                if not exito:
                    tablero[nueva_x][nueva_y]=0
        intento=intento+1
    return exito


N= int(input()) #numero de filas y de columnas
tablero=[]
for i in range(N):
    fila = list(map(int,input().strip().split()))
    tablero.append(fila)

mov_rel_x = [1,-1,0, 0]
mov_rel_y = [0,0,1, -1]
tablero[0][0]='E'
tablero[N-1][N-1]='S'

exito=BT(tablero,0,0,mov_rel_x,mov_rel_y)
if (exito):
    print('SI')
else:
    print('NO')