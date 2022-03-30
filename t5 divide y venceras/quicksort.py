from random import Random

def partition(start,end,elements):
    #mid = (start + end ) // 2
    mid = start

    for i in range(start,end):
        if elements[i] < elements[end]:
            elements[i], elements[mid] = elements[mid], elements[i]
            mid +=1
    elements[mid], elements[end] = elements[end], elements[i]
    return mid


def qs_rec(start, end, elements):
    pivot = partition(start,end, elements)

def quickSort(elements):
    qs_rec(0, len(elements)-1, elements)




#Prog princ


print("testing ... ", end="")
for i in range(1000):
    input = []
    rng = Random(0) # la semilla
    n = rng.randint(1,1000) #genero mil array de tamaño n
    for j in range(n):
        input.append(rng.randint(1, 100)) #rellenado de 1 a 100

    copy = input[:] #copia el array pero el contenido no los punteros

    quickSort(input)
    copy.sort()
    assert copy == input #si no es cierta la igualdad hace exit

print("Done ...")