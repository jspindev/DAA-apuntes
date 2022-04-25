def BinaryIterative(lista, x):
    f = False
    while len(lista)>0 and f == False:
        mitad = len(lista) // 2
        if lista[mitad] == x:
            f = True
        else:
            if x > lista[mitad]:
                lista = lista[mitad + 1:]
            else:
                lista = lista[:mitad]
    return f

coleccion = [3, 5, 6, 9, 10]
found = BinaryIterative(coleccion, 3)
print(found)