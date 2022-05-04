def cutMatrix(matrix, actualCut):
    lenMatrix = len(matrix)
    mat1 = matrix[0:lenMatrix // 2]
    mat2 = matrix[lenMatrix // 2:lenMatrix]
    mat11 = [] # nos creamos tantas submatrices como divisiones hace el corte
    mat12 = []
    mat21 = []
    mat22 = []
    pieces = []
    for i1 in mat1: # analizamos los elementos de la LISTA, no una lista de listas como arriba que coje la mitad de la matriz
        lenLine1 = len(i1)
        mat11.append(i1[0:lenLine1 // 2])
        mat12.append(i1[lenLine1 // 2:lenLine1])
    for i2 in mat2:
        lenLine2 = len(i2)
        mat21.append(i2[0:lenLine2 // 2])
        mat22.append(i2[lenLine2 // 2:lenLine2])
    pieces.append(mat11) # añadimos los trozos cortados
    pieces.append(mat12)
    pieces.append(mat21)
    pieces.append(mat22)
    if actualCut == C:
        minSeed = float('inf')
        for p in pieces: # analizo los trozos de la matriz que quiero cortar
            sumSeed = 0
            for a in p:
                sumSeed += sum(a)
            if sumSeed < minSeed:
                minSeed = sumSeed
        minims.append(minSeed)
    else:
        cutMatrix(mat11, actualCut + 1)
        cutMatrix(mat12, actualCut + 1)
        cutMatrix(mat21, actualCut + 1)
        cutMatrix(mat22, actualCut + 1)


N, C = map(int, input().strip().split())
wm = []
for f in range(N):
    wm.append(list(map(int, input().strip().split())))
minims = []
totalPieces = 4 ** C # numero de submatrices ** es una potencia 4 ^c
maxPieces = N * N # numero de elementos en la matriz
minSeed1 = float('inf')
if maxPieces == totalPieces: # si el numero de elementos totales = numero de submatrices
    for f in range(N):
        minLine = min(wm[f]) # sacamos el min de cada fila y lo guardamos
        if minLine < minSeed1:
            minSeed1 = minLine #se guarda en minSeed1 el valor mas pequeño
    print(minSeed1)
else:
    cutMatrix(wm, 1)
    print(min(minims))