c=int(input())

pesca=list()

for i in range(0,c):
    pez=list(map(int, input().strip().split()))
    pesca.append(pez)

print(pesca)
#p=max(pesca);
puntos=pesca.index(0)
s=max(puntos)
print(s)
#for primero in enumerate(pesca):
 #   if primero == max(pesca):
  #      print(primero)
   # print(primero)