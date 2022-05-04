

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2

        L = array[:mid]

        R = array[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R): #copiamos los datos a array temporales de L y R
            if L[i] < R[j]:
                array[k] =L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L): #comprobando los elementos de la izquierda
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R): #comprobando los elementos de la derecha
            array[k] = R[j]
            j += 1
            k =+ 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
    print()

if __name__ == '__ main__':
    array = [12, 11, 13, 5, 6, 7]
    print("array inicial es", end="\n")
    printList(array)
    mergeSort(array)
    print("array ordenado es ", end="\n")
    printList(array)