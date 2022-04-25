

def rec_bs(e, low, high, elements):
    if low > high:
        return -1
    mid = (low + high ) // 2

def rec_binarySearch(e, elements):
    return rec_bs(e, 0 , len(elements) -1, elements)


#divide y venceras se suele hacer de manera recursivo, en este caso tenemos  un array que vamos
# partiendo en mitades para ir descartando o hasta cuando se que ele lemneto no esta
#cuando se cruzan el low y el high quiere decir que el elemento no esta low>high
def rec_bs(e,low,high, elements):
    if low > high: #caso base, cuando no está el elemento y el low supera el high
        return -1 #decimosque no esta, luego para decir en que psoicion esta mañana lo pone
                  #si no entramos en el elemento recursivo
                  #si vemos que esta, nos posicionamos en el elemento mitad
    mid = (low+high)//2 #division entera
                #puede pasar que elem este en la mitad,o que elelemto este mas alla en la mitad,o que es mas pequeño que la mitad
    if elements[mid]==e:
        return mid
    elif e < elements[mid]:
        return rec_bs(e , low, mid-1 , elements)  #es -1 p orque se que mid no es porque no entro en el bucle del igual, asi que miramos ahora para estos datos
    else:
        return rec_bs(e , mid+1, high , elements)

def rec_binarySearch(e, elements):  #le pasamos lso argumentos fundamentales, inicializando una funcion recursiva
    rec_bs(e,0,len(elements)-1, elements)




v=[1,3,4,5,6,7,9]

index= rec_binarySearch(4,v)
# en el caso de que el elem no esta en el array devuelve un negativo,
# buscamos 4 en el array v, con boolean que me diga si esta o no,
# o puede devolver el indice donde esta el elemento a buscar, y si no esta devuelvo donde deberia estar
print(index)


v = [1, 3, 4, 5, 6, 7, 9]#no ordenar en busqueda binaria por que da igual

index = rec_binarySearch(4,v)#indice negativo para cuando no esta el elemento en inguna posicion y sino l posicion