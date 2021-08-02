import numpy as np


n = int(input("Number of variables: "))
matrix = array = np.arange(n*(n+1)*1.0).reshape(n,n+1)
solution = array = np.arange(n).reshape(n,1)

#reading data from matrix
for i in range(0,n):
  for j in range(0,n+1):
    matrix[i,j] = float (input("Cell: ["+ str(i) + "," + str(j) + "] "))
print(matrix)

#solution of equations
for i in range(0,n):
  if (matrix[i,i]== 0):
    print("Math error kindly check your input",i)
    break
  for j in range(0,n):
    if (i!=j):
      ratio = matrix[j,i] / matrix[i,i]
      for k in range(0,n+1):
        matrix[j,k]=matrix[j,k] - ratio*matrix[i,k]

#show the solutions

  try:
    for i in range(0,n):
      solution[i]= matrix[i,n] / matrix[i,i]
      print(matrix[i,n] / matrix[i,i])
  except:
    print("No solution or Infinite and many solution")
