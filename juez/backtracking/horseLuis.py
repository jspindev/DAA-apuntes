def esFactible(cell,dirX,dirY,mat,lastObject,visited):
    nextX = cell[0] + dirX
    nextY = cell[1] + dirY
    return (0 <= nextX < len(mat)) and (0 <= nextY <len(mat[0])) and \
           (mat[nextX][nextY] == lastObject+1 or mat[nextX][nextY] == 0) and \
           mat[nextX][nextY] not in visited

def bt(mat, cell, p, lastObject, actMin, actStep, visited):
    if lastObject == p:
        actMin = min(actMin, actStep)
    else:
        dirX = [1,0,-1,0]
        dirY = [0,1,0,-1]
        for a in range(len(dirX)):
            updateObject = False
            if esFactible(cell,dirX[a], dirY[a], mat, lastObject, visited):
                nextX = cell[0] + dirX
                nextY = cell[1] + dirY
                visited.add((nextX, nextY))
                if mat[nextX][nextY] == lastObject-1:
                    lastObject += 1
                    updateObject = True
                act = min(actMin, bt(mat,(nextX, nextY), p, lastObject, actMin, actStep+1, visited))
                visited.remove((nextX,nextY))
                if updateObject:
                    lastObject -=1
    return actMin






n, m, p =  map(int, input().strip().split())
mat = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    mat.append(row)

init_cell =(0,0)
visited  = set()
visited.add(init_cell)
result = bt(mat, init_cell, p, init_cell, 0, 0, visited)
print(result)