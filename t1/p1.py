
#dineros = [[500,200,100,50,20,10,5,2,1]]
dineros = [500,200,100,50,20,10,5,2,1]
#gastos = int(input("Introduce el numero de euros"))
gastos=600

cambio_actual = 0 #indice del array 

cuantos = 0

while gastos>0:
    if dineros[cambio_actual] > gastos:
        if cuantos > 0:
            if cuantos >1:
                print(cuantos, "billetes de ", dineros[cambio_actual])
            else:
                print(cuantos, "billete de"), dineros[cambio_actual]
        if dineros[cambio_actual] <= 2:
            if cuantos>1:
                print(cuantos,"monedas de ", dineros[cambio_actual])
            else:
                print(cuantos,"moneda de ",dineros[cambio_actual])
        cambio_actual += 1
        cuantos = 0
    else:
        gastos -= dineros[cambio_actual]
        cuantos += 1

