def rec_bs(e, low, high, elements,M,oport):
    if low > high:
        print('¿Donde esta Penny?')
    mid = (low + high) // 2
    if elements[mid] == e:
        oport=oport+1
        return oport, mid
    elif e < elements[mid]:
        oport=oport+1
        return rec_bs(e, low, mid - 1, elements,M,oport)
    else:
        oport=oport+1
        return rec_bs(e, mid + 1, high, elements,M,oport)


N,M,P = map(int, input().strip().split())

hab=[]

for i in map(int, input().strip().split()):
    hab.append(i)
hab.sort
oport= 0
result, habitacion = rec_bs(P, 0, len(hab) - 1, hab,M,oport)

if result <= M:
    print('Penny esta en la habitacion ' + str(habitacion) + ', se han requerido ' + str(result) + ' saltos')
else:
    print('¿Donde esta Penny?')