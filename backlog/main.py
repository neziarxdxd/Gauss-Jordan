import numpy as np


number_of_variables = int(input("Number of variables: "))
matrix = array = np.arange(number_of_variables*(number_of_variables+1)*1.0).reshape(number_of_variables,number_of_variables+1)
solution = array = np.arange(number_of_variables).reshape(number_of_variables,1)

#reading data from matrix
for i in range(0,number_of_variables):
  for j in range(0,number_of_variables+1):
    matrix[i,j] = float (input("Cell: ["+ str(i) + "," + str(j) + "] "))
print(matrix)

#solution of equations
for i in range(0,number_of_variables):
  if (matrix[i,i]== 0):
    print("Math error kindly check your input",i)
    break
  for j in range(0,number_of_variables):
    if (i!=j):
      ratio = matrix[j,i] / matrix[i,i]
      for k in range(0,number_of_variables+1):
        matrix[j,k]=matrix[j,k] - ratio*matrix[i,k]

#show the solutions

for i in range(0,number_of_variables):
  solution[i]= matrix[i,number_of_variables] / matrix[i,i]
  print(matrix[i,number_of_variables] / matrix[i,i])
  
