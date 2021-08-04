matrix = [[ 1,          0,          0.33333333, -4.       ],
 [ 0 ,        3 ,         2   ,       0 ,       ],
 [ 0   ,       0   ,      -5.33333333 ,32]]
variables= ["x","y","z"]
for row in range(len(matrix)):
    
    print("|",
    " ".join(str(i).ljust(20) for i in matrix[row][:-1]),"|",variables[row], "|",matrix[row][-1])
