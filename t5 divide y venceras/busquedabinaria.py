

def rec_bs(e, low, high, elements):
    if low > high:
        return -1
    mid = (low + high ) // 2

def rec_binarySearch(e, elements):
    return rec_bs(e, 0 , len(elements) -1, elements)



v = [1, 3, 4, 5, 6, 7, 9]#no ordenar en busqueda binaria por que da igual

index = rec_binarySearch(4,v)#indice negativo para cuando no esta el elemento en inguna posicion y sino l posicion