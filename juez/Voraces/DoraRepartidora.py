
n = int(input())
paquetes = []

for i in range(n):
    id, timepaquete = map(int,input().strip().split())
    paquetes.append(timepaquete)

paquetes.sort()

sumWaitingTime = 0
for j in range(len(paquetes)):
    i = 0
    acum = 0
    while i <= j:
        acum += paquetes[i]
        i += 1
    sumWaitingTime += acum

print(sumWaitingTime)