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


def mostrarnivel(l, e):
    for i in range(len(l)):
        minMax = rec_binarySearch(l[i], e)
        if minMax < 0:
            minMax = -minMax - 1
        if l[i] <= e[0]:
            print('X', e[minMax])
        elif l[i] >= e[len(e) - 1]:
            print(e[minMax - 1], 'X')
        elif e[minMax] == l[i]:
            print(e[minMax - 1], e[minMax + 1])
        else:
            print(e[minMax - 1], e[minMax])


n = int(input())
tniveles= []
for e in map(int, input().strip().split()):
    tniveles.append(e)

Q = int(input())
niveles = []
for l in map(int, input().strip().split()):
    niveles.append(l)
mostrarnivel(niveles, tniveles)