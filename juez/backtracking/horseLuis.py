dirsX = [1, 0, -1, 0]
dirsY = [0, 1, 0, -1]


def bt(mat, cell, p, lastObject, actMin, actSteps, visited):
    if lastObject == p :
        actMin = min(actMin, actSteps)
    else:
        for a in range(len(dirsX)):
            updatedObject = False
            if isFeasible(cell, dirsX[a], dirsY[a], mat, lastObject, visited):
                nextX = cell[0] + dirsX[a]
                nextY = cell[1] + dirsY[a]
                visited.add((nextX, nextY))
                if mat[nextX][nextY] == lastObject + 1:
                    lastObject += 1
                    updatedObject = True
                actMin = min(bt(mat, (nextX, nextY), p, lastObject, actMin, actSteps + 1, visited), actMin)
                if updatedObject:
                    lastObject -= 1
                visited.remove((nextX, nextY))
    return actMin


def isFeasible(cell, dirX, dirY, mat, lastObject, visited):
    nextX = cell[0] + dirX
    nextY = cell[1] + dirY
    return 0 <= nextX < len(mat) and 0 <= nextY < len(mat[0]) and (mat[nextX][nextY] == lastObject + 1 or mat[nextX][nextY] == 0) and (nextX, nextY) not in visited


if __name__ == '__main__':
    n, m, p = map(int, input().strip().split())
    mat = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        mat.append(row)
    init_cell = (0, 0)
    visited = set()
    visited.add(init_cell)
    print(bt(mat, init_cell, p, 0, 0x3f3f3f, 1, visited))