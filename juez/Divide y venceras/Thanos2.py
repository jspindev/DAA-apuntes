def rec_bs(e, low, high, elements):
    if low > high:
        #return -low - 1
        #return False
        print(":)")
    mid = (low + high) // 2
    if elements[mid] == e:
        print(":_(")
        return True
    elif e < elements[mid]:
        return rec_bs(e, low, mid - 1, elements)
    else:
        return rec_bs(e, mid + 1, high, elements)


def rec_binarySearch(e, elements):
    return rec_bs(e, 0, len(elements) - 1, elements)




#index = rec_binarySearch(2, v)


#if index < 0:
 #   index = - index - 1
  #  print("Should be at pos.:", index, "after the element" if index == len(v) else "and before element " + str(v[index]) )
#else:
 #   print("Element", v[index], "found at position", index)


def chasquido(habitantes,amoche,certificados):
    muerto = []
    for i in range(len(certificados)):
        act = certificados[i]
        rec_bs(act,0,len(amoche)-1,amoche)



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
certificados.sort()


chasquido(habitantes,amoches,certificados)
