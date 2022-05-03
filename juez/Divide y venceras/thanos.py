def rec_bs(e, low, high, elements):
    if low > high:
        return False

    mid = (low + high) // 2
    if elements[mid] == e:
        return True
    elif e < elements[mid]:
        return rec_bs(e, low, mid - 1, elements)
    else:
        return rec_bs(e, mid + 1, high, elements)


def rec_binarySearch(e, elements):
    return rec_bs(e, 0, len(elements) - 1, elements)


def chasquido(amoche,certificados):

    for i in range(len(certificados)):
        act = certificados[i]
        aux = rec_bs(act,0,len(amoche)-1,amoche)
        #print(aux)
        if not aux:
            print(":)")
        else:
            print(":_(")





n = int(input())
habitantes = []
for e in map(int,input().strip().split()):
    habitantes.append(e)

m = int(input())
amoches = []
for e in map(int, input().strip().split()):
    amoches.append(e)
amoches.sort()


p = int(input())
certificados = []
for e in map(int,input().strip().split()):
    certificados.append(e)
#certificados.sort()


chasquido(amoches,certificados)
