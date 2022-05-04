

def binary_search(enemigos, q, ini, fin):
    if enemigos[0] > q:
        return -1
    elif ini == fin:
        return ini
    else:
        medio = (ini + fin )// 2
        if q >= enemigos[medio + 1]:
            return binary_search(enemigos, q, medio+1, fin)
        else:
            return binary_search(enemigos, q, ini, medio)


#busqueda binaria+

if __name__ == '__main__':
    n = int(input().strip())
    enemigos = list(map(int, input().strip().split()))
    suma_puntos = []
    suma_puntos.append(enemigos[0])
    for i in range(1, n):
        suma_puntos.append(suma_puntos[i-1] + enemigos[i])
    m = int(input().strip())
    for _ in range(m):
        q = int(input().strip())
        pos = binary_search(enemigos, q, 0, n-1) #n-1 es len enemigos-1
        suma=0
        if (pos < 0):
            print(0,0)
        else:
            print(str(pos+1) + " " + str(suma_puntos[pos]))

