import numpy as np

def dibujar(A,ini,fin):
   for i in range(len(A)):
      if i == ini:
         print('[',end='')
      print(A[i],end=' ')
      if i == fin:
         print(']', end='')
   print()


def merge(A, p, q, r):
   n1 = q - p + 1
   R = np.empty(n2+1)
   for i in range(n1):
      L[i] = A[p + i]
   for j in range(n2):
      R[j] = A[q + 1 + j]
   L[n1] = np.inf
   R[n2] = np.inf
   i = 0
   j = 0
   for k in range(p,r + 1):
      if L[i] <= R[j]:
         A[k] = L[i]
         i += 1
      else:
         A[k] = R[j]
         j += 1
   return A

def mergesort(A,p,r):
   dibujar(A, p, r)
   if p < r:
      q = (p+r) // 2
      mergesort(A, p, q)
      mergesort(A, q + 1, r)
      merge(A, p, q, r)
   return A

coleccion = np.array([6,8,3,4,6,1,8,7,0,9])
coleccion = mergesort(coleccion,0, len(coleccion)-1)
print(coleccion)