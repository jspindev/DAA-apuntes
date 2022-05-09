def isSolution(lab, f, c):
    return p == lab[f][c]


def isPossible(lab, f, c, cont):
    return (f >= 0) and (f < len(lab)) and (c >= 0) and (c < len(lab[0])) and (
            lab[f][c] == 0 or lab[f][c] == cont) and (lab[f][c] != p + 1)


def laberintoVA(lab, f, c, step, cont, mejorSol):
    if isSolution(lab, f, c):
        mejorSol.append(step - 1)
        suc = False
    else:
        suc = False
        mov = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 0
        while not suc and i < len(mov):
            if isPossible(lab, f + mov[i][0], c + mov[i][1], cont):
                if lab[f + mov[i][0]][c + mov[i][1]] == cont:
                    cont += 1
                else:
                    lab[f + mov[i][0]][c + mov[i][1]] = -2
                [lab, suc, mejorSol] = laberintoVA(lab, f + mov[i][0], c + mov[i][1], step + 1, cont, mejorSol)
                if not suc and (lab[f + mov[i][0]][c + mov[i][1]] == cont - 1):
                    lab[f + mov[i][0]][c + mov[i][1]] = cont - 1
                    cont -= 1
                else:
                    lab[f + mov[i][0]][c + mov[i][1]] = 0
            i += 1
    return [lab, suc, mejorSol]


terreno = []

n, m, p = map(int, input().strip().split())
for x in range(n):
    terreno.append(list(map(int, input().strip().split())))

cont = 0
Xini = 0
Yini = 0
step = 1
terreno[Xini][Yini] = -1
mejorSol = []
[lab, suc, mejorSol] = laberintoVA(terreno, Xini, Yini, step + 1, cont + 1, mejorSol)
if mejorSol:
    print(min(mejorSol))