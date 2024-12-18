# Write a python program to added two matrices.

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimansions.")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

matrix1 = [
    [2,4,3],
    [9,7,6],
    [4,5,9]
]
matrix2 = [
    [9,8,7,],
    [4,7,4,],
    [2,2,7,]
]
try:
    result_matrix = add_matrices(matrix1, matrix2)
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)
except ValueError as e:
    print(e)


