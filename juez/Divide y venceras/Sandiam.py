n, c = map(int, input().strip().split())

watermelon = []

for i in range(n):
    watermelon.append([])
    for cut in map(int, input().strip().split()):
        watermelon[i].append(cut)


def cutWM(wm, y, x, n, c):
    if c == 0:
        return sum(
            wm[i][j]
            for i in range(y, y + n)
            for j in range(x, x + n)

        )
    w = n // 2
    minHeight = min(
        cutWM(wm, y, x, w, c - 1),
        cutWM(wm, y + w, x, w, c - 1),
        cutWM(wm, y, x + w, w, c - 1),
        cutWM(wm, y + w, x + w, w, c - 1),
    )
    return minHeight


print(cutWM(watermelon, 0, 0, n, c))
