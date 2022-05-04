

def cutMatrix(matriz, actualcut):
    lenMatriz = len(matriz)
    mat1 = matriz[0:lenMatriz // 2]
    mat2 = matriz[lenMatriz // 2:lenMatriz]
    mat11 = []
    mat12 = []
    mat21 = []
    mat22 = []
    pieces = []
    for i1 in mat1:
        lenline1 = len(i1)
        mat11.append(i1[0:lenline1 // 2])
        mat12.append(i1[lenline1// 2:lenline1])
    for i2 in mat2:
        lenline2 = len(i2)
        mat21.append(i2[0:lenline2 // 2])
        mat22.append(i2[lenline2 // 2:lenline2])

    pieces.append(mat11)
    pieces.append(mat12)
    pieces.append(mat21)
    pieces.append(mat22)
    if actualcut == c:
        minSeed = float('inf')
        for p in pieces:
            sumseed = 0
            for a in p:
                sumseed += sum(a)
            if sumseed < minSeed:
                minSeed = sumseed
        minimos.append(minSeed)
    else:
        cutMatrix(mat11,actualcut+1)
        cutMatrix(mat12, actualcut+1)
        cutMatrix(mat21, actualcut+1)
        cutMatrix(mat22, actualcut +1)


#n = longitud c = cortes
n, c = map(int, input().strip().split())
matriz = []
for f in range(n):
    matriz.append(list(map(int, input().strip().split())))
minimos = []
totalPieces = 4 ** c #numero de submatrices
maxPieces = n * n #numero de elementos
minSeed1 = float('inf')
if maxPieces == totalPieces:
    for f in range(n):
        minLine = min(matriz[f])
        if minLine < minSeed1:
            minSeed1 = minLine
    print(minSeed1)
else:
    cutMatrix(matriz,1)
    print(min(minimos))