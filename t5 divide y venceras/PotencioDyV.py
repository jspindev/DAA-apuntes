

def potDyV(x,a):
    if a == 0:
        result = 1
    else:
        if a == 1:
            result = x
        else:
            if a % 2 == 0:
                aux = potDyV(x,a // 2)
                result = aux * aux
            else:
                 result = x * potDyV(x,a-1)


    return result

print("Calculo de x^a con un enfoque Divide y venceras")
x = float(input("valor de la x:"))
a = float(input("valor de la a:"))
print("x^a = ", potDyV(x,a))