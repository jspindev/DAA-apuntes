

def partition(array, low, high):

    pivot = array[high] #elegimos el elmento mas alto de pivot

    i = low -1 #puntero para el elemento

    for j in range(low, high):
        if array[j] <= pivot: #si elemento pequeño que el pivot se cambia por el elemento apuntaod por i
            i +=1
            (array[i], array[j]) = (array[j], array[i]) #intercabiando los valores
    (array[i+1], array[high]) = (array[high], array[i+1]) #intercambiando el pivote con el elemento mas grande especificado por i

    return i+1 #devolvemos la posicion donde esta la particion

def quick_sort(array, low, high):

    if low < high:
        pi = partition(array,low, high) #buscamos el pivot

        quick_sort(array, low, pi -1) #recursivo para el lado izquierde

        quick_sort(array, pi+1, high) #recursivo para el lado derecho


array = [10,7,8,9,1,5]
quick_sort(array, 0 , len(array)-1)

print(f'Sorted array : {array}')


