import re
import numpy as np


def isComplete(num,array):
    return len(array)-1 == num 
def equationToMatrix(array):
    equation = array.split()
    array = "".join(equation)
    z = re.findall(r'[\d\.\-\+]+', array)
    try:
      number_list = list(map(float,z))
      return number_list
    except:
      print('You should add "1" coeffecient')
      exit()
def matrix_parse(matrix):  
  for row in range(len(matrix)):    
    print("|",
    " ".join(str(i).ljust(20) for i in matrix[row][:-1]),"|",f"x{row}", "|",matrix[row][-1])    
    
list_matrix = []
number_variables = int(input("Enter number of variables: "))
print('''
It should be in format Ax + By = C 
Note: Kindly put "1" for coeffecient of a variable
For example:
1x + 2y = 7 (proper format)
not: x+2y = 7; 2y+x=7; 
''')
for i in range(number_variables):
    equation_input = input("Enter the equation: ")
    matrix_converted = equationToMatrix(equation_input)
    if (isComplete(number_variables,matrix_converted)):
        list_matrix.append(matrix_converted)
    else:
        print("Kindly check your input")
        exit()




matrix = array = np.arange(number_variables*(number_variables+1)*1.0).reshape(number_variables,number_variables+1)
solution = array = np.arange(number_variables).reshape(number_variables,1)

#reading data from matrix
for i in range(0,number_variables):
  for j in range(0,number_variables+1):
    matrix[i,j] = list_matrix[i][j]    
    
print("MATRIX: ",matrix)
print("=============")
#solution of equations
for i in range(0,number_variables):
  if (matrix[i,i]== 0):
    print("Math error kindly check your input",i)
    break
  for j in range(0,number_variables):
    if (i!=j):
      ratio = matrix[j,i] / matrix[i,i]
      print(f"ratio: {matrix[j,i]} /{matrix[i,i]} = {ratio}")

      for k in range(0,number_variables+1):
        solve_matrix = matrix[j,k] - ratio*matrix[i,k] 
        print(f"cell: {matrix[j,k]} - {ratio}*{matrix[i,k]} = {solve_matrix}")
        matrix[j,k]= solve_matrix      
        # printing of matrix how it was solved
        listMatrix = matrix.tolist()
        for row in range(len(listMatrix)):    
          print("|"," ".join(str(i).ljust(20) for i in listMatrix[row][:-1]),"|",f"x{row}", "|",listMatrix[row][-1]) 
        
        
solution_sets=[]
#show the solutions
print("Solution set: ")
for i in range(0,number_variables):
  solved = matrix[i,number_variables] / matrix[i,i]  
  print(f"Equation #{i+1} {matrix[i,number_variables]}/{ matrix[i,i] } = {solved}")
  solution[i]= solved
  solved_round = round(solved,4)
  solution_sets.append(solved_round)
  print(solved_round)

# checking
print("##### CHECKING OF EQUATIONS ####")
for sets in list_matrix:
    solve = sets[0:number_variables]    
    check = sets[-1]
    print("Equation",solve,check)
    distributed= [solution_sets[i] * sets[i] for i in range(len(solution_sets))]
    print("Subsitute the values: ",distributed, check)
    print("Get the sum: ",sum(distributed), check)
    print("Check if they are equal",sum(distributed) == check)

  
