from random import randint

def randomBusquedaBinaria(A, ini, fin, x):
    if ini > fin:
        return False
    else:
        print(A[ini:fin+1])
        corte = randint(ini,fin)
        if x == A[corte]:
            return True
        else:
            if x > A[corte]:
                return randomBusquedaBinaria(A, corte+1, fin, x)
            else:
                return randomBusquedaBinaria(A, ini, corte-1, x)
# -- Main --
#A = list(map(int, input("Items in A:").strip().split()))
A = [1, 3, 4, 5, 7, 8, 10, 12, 13, 15, 17, 20]
#X = int(input("Item to serach (X):"))
X = 11
#A.sort()
print(randomBusquedaBinaria(A, 0, len(A)-1, X))