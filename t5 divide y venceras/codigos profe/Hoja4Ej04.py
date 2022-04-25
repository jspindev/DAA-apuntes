def representar(vector, ini, fin):
    for i in range(len(vector)):
        if i == ini:
            print('[',end=' ')
        print(vector[i], end=' ')
        if i == fin:
            print(']', end=' ')
    print()

def busquedaTernaria(vector, ini, fin, x):
    representar(vector, ini, fin)
    if ini > fin:
        resultado = False
    else:
        corte1 = ini + (fin - ini) // 3
        if vector[corte1] == x:
            resultado = True
        else:
            if x < vector[corte1]:
                resultado = busquedaTernaria(vector, ini, corte1-1,x)
            else:
                corte2 = ini + 2 * (fin - ini) // 3
                if vector[corte2] == x:
                    resultado = True
                else:
                    if x < vector[corte2]:
                        resultado = busquedaTernaria(vector,corte1+1,corte2-1,x)
                    else:
                        resultado = busquedaTernaria(vector,corte2+1,fin,x)
    return resultado

# Prog Ppal:
vector = [1, 2, 4, 5, 6, 8, 9, 10, 11, 15, 18]
x = 3
if busquedaTernaria(vector,0,len(vector)-1,x):
    print(x,'está en la colección')
else:
    print(x, 'no está en la colección')