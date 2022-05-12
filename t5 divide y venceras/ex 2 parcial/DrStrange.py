def rec_bs(e, low, high, elements):
    if low > high:
        return -low - 1
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid
    elif e < elements[mid]:
        return rec_bs(e, low, mid - 1, elements)
    else:
        return rec_bs(e, mid + 1, high, elements)


def rec_binarySearch(e, elements):
    return rec_bs(e, 0, len(elements) - 1, elements)


def Niveles (l, a):
    for i in range(len(l)):
        minMax = rec_binarySearch(l[i], a)
        if minMax < 0:
            minMax = -minMax - 1
        if l[i] == a[0] or minMax <= 0:
            print('VACIO', a[minMax+1])
        elif l[i] == a[len(a) - 1] or minMax >= len(a):
            print(a[minMax - 1], 'VACIO')
        elif a[minMax] == l[i]:
            print(a[minMax - 1], a[minMax + 1])
        else:
            print(a[minMax - 1], a[minMax])





universos = []
for i in list(input().strip().split()):
    universos.append(i)

universos.sort()
N = int(input())  #numero de universos
indicado = []
for i in range(N):
    for a in list(input().strip().split()):
      indicado.append(a)

Niveles(indicado, universos)