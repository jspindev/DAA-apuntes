def isSolution(f, c, numObjects):
    return f == N - 1 and c == M - 1 and numObjects == P


def isPossible(lab, f, c, step):
    return (f >= 0) and (f < len(lab)) and (c >= 0) and (c < len(lab[0])) and (lab[f][c] == 0 or lab[f][c] == 1) and step < minSolution


def labyrinthVA(lab, f, c, step, numObjects, minSolution):
    if isSolution(f, c, numObjects):
        if step < minSolution:
            minSolution = step
        suc = False
    else:
        suc = False
        mov = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        if f == N - 1 and c == M - 1:
            i = 4
        else:
            i = 0
        while not suc and i < len(mov):
            if isPossible(lab, f + mov[i][0], c + mov[i][1], step):
                if lab[f + mov[i][0]][c + mov[i][1]] != 1:
                    lab[f + mov[i][0]][c + mov[i][1]] = 2
                else:
                    lab[f + mov[i][0]][c + mov[i][1]] = 3
                    numObjects += 1
                step += 1
                [lab, suc, minSolution] = labyrinthVA(lab, f + mov[i][0], c + mov[i][1], step, numObjects, minSolution)
                if not suc:
                    if lab[f + mov[i][0]][c + mov[i][1]] == 3:
                        lab[f + mov[i][0]][c + mov[i][1]] = 1
                        numObjects -= 1
                    else:
                        lab[f + mov[i][0]][c + mov[i][1]] = 0
                    step -= 1
            i += 1
    return lab, suc, minSolution


N, M, P = map(int, input().strip().split())
lab = []
for f in range(N):
    lab.append(list(map(int, input().strip().split())))
Xini = 0
Yini = 0
step = 0
minSolution = float('inf')
numObjects = 0
lab[Xini][Yini] = 2
[lab, suc, minSolution] = labyrinthVA(lab, Xini, Yini, step + 1, numObjects, minSolution)
if minSolution != float('inf'):
    print(minSolution)
else:
    print('No hay solucion')