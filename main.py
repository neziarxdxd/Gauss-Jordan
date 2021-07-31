import numpy as np

#ingresamos tamaño de la matriz
n = int(input("ingrese n: "))
matriz = array = np.arange(n*(n+1)*1.0).reshape(n,n+1)
solucion = array = np.arange(n).reshape(n,1)

#lectura de datos de la matriz
for i in range(0,n):
  for j in range(0,n+1):
    matriz[i,j] = float (input("ingrese matriz["+str(i)+","+str(j)+"]"))
print(matriz)

#solucion de las ecuaciones
for i in range(0,n):
  if (matriz[i,i]== 0):
    print("Error matemático",i)
    break
  for j in range(0,n):
    if (i!=j):
      ratio = matriz[j,i] / matriz[i,i]
      for k in range(0,n+1):
        matriz[j,k]=matriz[j,k] - ratio*matriz[i,k]

#mostramos las soluciones
for i in range(0,n):
  solucion[i]= matriz[i,n] / matriz[i,i]
  print(matriz[i,n] / matriz[i,i])