matrix = [
    [1, 1, 1, -4],
    [-1, 2, 1, 4],
    [4, 3, -2, 16]
]

solution_set = [-2, 4, -6]

number_variables = 3

for sets in matrix:
    solve = sets[0:number_variables]
    
    check = sets[-1]
    print("Equation",solve,check)
    distributed= [solution_set[i] * sets[i] for i in range(len(solution_set))]
    print("Subsitute the values: ",distributed, check)
    print("Get the sum: ",sum(distributed), check)
    print("Check if they are equal",sum(distributed) == check)