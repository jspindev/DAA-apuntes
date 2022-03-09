

emp=list(map(int,input().strip().split()))

employees = [0]*10

for e in emp:
    if e >=0:
        employees[e] += 1

for i in range(len(employees)):
    if employees[i] >= 3:
        print(i, end= " ")


