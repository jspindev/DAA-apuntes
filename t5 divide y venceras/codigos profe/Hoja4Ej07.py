import numpy as np

def dibujar(A,ini,fin):
   for i in range(len(A)):
      if i == ini:
         print('[',end='')
      print(A[i],end=' ')
      if i == fin:
         print(']', end='')
   print()

def intercambiar(A, i, j):
   aux = A[i]
   A[i] = A[j]
   A[j] = aux
   return A


def pivote(A,ini,fin):
   ValorPivote = A[ini]
   i_crec = ini+1
   i_decrec = fin
   done = False
   while not done:
      while i_crec <= i_decrec and A[i_crec] <= ValorPivote:
         i_crec = i_crec + 1
      while A[i_decrec] >= ValorPivote and i_decrec >= i_crec:
         i_decrec = i_decrec -1
      if i_decrec < i_crec:
         done = True
      else:
         A = intercambiar(A, i_crec, i_decrec)
   A = intercambiar(A, ini, i_decrec)
   return A, i_decrec

def quicksort(A,i,j):
   dibujar(A, i, j)
   if i<j:
      [A,b] = pivote(A,i,j)
      A = quicksort(A, i, b-1)
      A = quicksort(A, b + 1,j)
   return A

coleccion = np.array([6,8,3,4,6,1,8,7,0,9])
coleccion = quicksort(coleccion,0, len(coleccion)-1)
print(coleccion)